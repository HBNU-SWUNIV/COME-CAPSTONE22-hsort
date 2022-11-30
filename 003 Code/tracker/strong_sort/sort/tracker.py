# vim: expandtab:ts=4:sw=4
from __future__ import absolute_import
import numpy as np
from . import kalman_filter
from . import linear_assignment
from . import iou_matching
from .track import Track

from location import Location

class Tracker:
    """
    This is the multi-target tracker.
    Parameters
    ----------
    metric : nn_matching.NearestNeighborDistanceMetric
        A distance metric for measurement-to-track association.
    max_age : int
        Maximum number of missed misses before a track is deleted.
    n_init : int
        Number of consecutive detections before the track is confirmed. The
        track state is set to `Deleted` if a miss occurs within the first
        `n_init` frames.
    Attributes
    ----------
    metric : nn_matching.NearestNeighborDistanceMetric
        The distance metric used for measurement to track association.
    max_age : int
        Maximum number of missed misses before a track is deleted.
    n_init : int
        Number of frames that a track remains in initialization phase.
    kf : kalman_filter.KalmanFilter
        A Kalman filter to filter target trajectories in image space.
    tracks : List[Track]
        The list of active tracks at the current time step.
    """
    GATING_THRESHOLD = np.sqrt(kalman_filter.chi2inv95[4])

    def __init__(self, metric, max_iou_distance=0.9, max_age=1000, n_init=3, _lambda=0, ema_alpha=0.9, mc_lambda=0.995, max_id=100, db=None):
        self.metric = metric
        self.max_iou_distance = max_iou_distance
        self.max_age = max_age
        self.n_init = n_init
        self._lambda = _lambda
        self.ema_alpha = ema_alpha
        self.mc_lambda = mc_lambda

        self.kf = kalman_filter.KalmanFilter()
        self.tracks = []
        ###
        self.ids = []
        self.max_id = max_id
        self.db = db
        self.id = 999
        self.id_list = ['20172616', '20172615', '20172598']
        self.i = 0
        self.deleted_tracks = []
        ###

    def predict(self):
        """Propagate track state distributions one time step forward.

        This function should be called once every time step, before `update`.
        """
        for track in self.tracks:
            track.predict(self.kf)

    def increment_ages(self):
        for track in self.tracks:
            track.increment_age()
            track.mark_missed()

    def camera_update(self, previous_img, current_img):
        for track in self.tracks:
            track.camera_update(previous_img, current_img)

    def update(self, detections, classes, confidences):
        """Perform measurement update and track management.

        Parameters
        ----------
        detections : List[deep_sort.detection.Detection]
            A list of detections at the current time step.

        """
        # Run matching cascade.
        matches, unmatched_tracks, unmatched_detections = \
            self._match(detections)

        ###
        # match()로 track과 detection이 가장 유사한 것을 tuple로 매치하여 업데이트
        # 위치 반고정 처리
        # 업데이트 전에 matches 리스트를 db에 저장된 위치 정보를 바탕으로 전부 수정 후 업데이트하는 방법
        # detection의 bbox를 구하고 detection의 위치와 db의 해당 위치값을 갖는 id를 가져옴
        # 해당 id를 가진 matches 리스트의 track 인덱스를 구해서 서로의 튜플 위치를 교환
        # 2중 반복문 처리 시간으로 인해 시스템이 지연되는 문제 예상 -> i3 랩탑 기준 이상치 1개당 0.4초 소요
        i = 0
        while (True):
            if (i == len(matches)):
                break
            track_idx, detection_idx  = matches[i][0], matches[i][1]
            cx, cy, _, _ = detections[detection_idx].to_xyah()
            loc = Location(cx, cy)
            location= loc.get_location()
            
            if (location != 0):
                id = int(self.db.get_id(location))
                if (id != self.tracks[track_idx].track_id):
                    for j in range(len(matches)):
                        if (self.tracks[matches[j][0]].track_id == id):
                            temp_detect_idx = matches[j][1]
                            matches[j] = (j, detection_idx)
                            matches[i] = (track_idx, temp_detect_idx)
                            break
            i += 1
        ###
        self.match_list = []
        for i, _ in matches:
            self.match_list.append(self.tracks[i].track_id)

        # Update track set.
        for track_idx, detection_idx in matches:
            self.tracks[track_idx].update(
                detections[detection_idx], classes[detection_idx], confidences[detection_idx])
        for track_idx in unmatched_tracks:
            self.tracks[track_idx].mark_missed()
        for detection_idx in unmatched_detections:
            self._initiate_track(detections[detection_idx], classes[detection_idx].item(), confidences[detection_idx].item())
        ###
        for t in self.tracks:
            if t.is_deleted():
                self.deleted_tracks.append(t)
        ###
        self.tracks = [t for t in self.tracks if not t.is_deleted()]

        # Update distance metric.
        active_targets = [t.track_id for t in self.tracks if t.is_confirmed()]
        features, targets = [], []
        for track in self.tracks:
            if not track.is_confirmed():
                continue
            features += track.features
            targets += [track.track_id for _ in track.features]
        self.metric.partial_fit(np.asarray(features), np.asarray(targets), active_targets)

    def _full_cost_metric(self, tracks, dets, track_indices, detection_indices):
        """
        This implements the full lambda-based cost-metric. However, in doing so, it disregards
        the possibility to gate the position only which is provided by
        linear_assignment.gate_cost_matrix(). Instead, I gate by everything.
        Note that the Mahalanobis distance is itself an unnormalised metric. Given the cosine
        distance being normalised, we employ a quick and dirty normalisation based on the
        threshold: that is, we divide the positional-cost by the gating threshold, thus ensuring
        that the valid values range 0-1.
        Note also that the authors work with the squared distance. I also sqrt this, so that it
        is more intuitive in terms of values.
        """
        # Compute First the Position-based Cost Matrix
        pos_cost = np.empty([len(track_indices), len(detection_indices)])
        msrs = np.asarray([dets[i].to_xyah() for i in detection_indices])
        for row, track_idx in enumerate(track_indices):
            pos_cost[row, :] = np.sqrt(
                self.kf.gating_distance(
                    tracks[track_idx].mean, tracks[track_idx].covariance, msrs, False
                )
            ) / self.GATING_THRESHOLD
        pos_gate = pos_cost > 1.0
        # Now Compute the Appearance-based Cost Matrix
        app_cost = self.metric.distance(
            np.array([dets[i].feature for i in detection_indices]),
            np.array([tracks[i].track_id for i in track_indices]),
        )
        app_gate = app_cost > self.metric.matching_threshold
        # Now combine and threshold
        cost_matrix = self._lambda * pos_cost + (1 - self._lambda) * app_cost
        cost_matrix[np.logical_or(pos_gate, app_gate)] = linear_assignment.INFTY_COST
        # Return Matrix
        return cost_matrix

    def _match(self, detections):

        def gated_metric(tracks, dets, track_indices, detection_indices):
            features = np.array([dets[i].feature for i in detection_indices])
            targets = np.array([tracks[i].track_id for i in track_indices])
            cost_matrix = self.metric.distance(features, targets)
            cost_matrix = linear_assignment.gate_cost_matrix(cost_matrix, tracks, dets, track_indices, detection_indices)

            return cost_matrix

        # Split track set into confirmed and unconfirmed tracks.
        confirmed_tracks = [
            i for i, t in enumerate(self.tracks) if t.is_confirmed()]
        unconfirmed_tracks = [
            i for i, t in enumerate(self.tracks) if not t.is_confirmed()]

        # Associate confirmed tracks using appearance features.
        matches_a, unmatched_tracks_a, unmatched_detections = \
            linear_assignment.matching_cascade(
                gated_metric, self.metric.matching_threshold, self.max_age,
                self.tracks, detections, confirmed_tracks)

        # Associate remaining tracks together with unconfirmed tracks using IOU.
        iou_track_candidates = unconfirmed_tracks + [
            k for k in unmatched_tracks_a if
            self.tracks[k].time_since_update == 1]
        unmatched_tracks_a = [
            k for k in unmatched_tracks_a if
            self.tracks[k].time_since_update != 1]
        matches_b, unmatched_tracks_b, unmatched_detections = \
            linear_assignment.min_cost_matching(
                iou_matching.iou_cost, self.max_iou_distance, self.tracks,
                detections, iou_track_candidates, unmatched_detections)

        matches = matches_a + matches_b
        unmatched_tracks = list(set(unmatched_tracks_a + unmatched_tracks_b))
        return matches, unmatched_tracks, unmatched_detections

    def _initiate_track(self, detection, class_id, conf):
        ###
        # id의 개수가 max_id 이상인데 새로운 추적 객체가 생성될 경우
        # 새로 id를 부여하는 것이 아닌 기존에 생성됐던 id지만
        # 현재 추적 상태가 아닌(deleted_tracks(state==3)) 객체들 중
        # 가장 유사한 객체의 id를 부여하고 deleted_track 상태 해제
        # 만약 state==3인 객체가 없을 경우, 최근에 사라지거나
        # 탐지에 실패하는 등의 이유로 아직 deleted 상태가 되지 않은 객체
        # 추적이 확실히 진행 중인 match list에 없는 id를 가져와서
        # 다시 탐지된, 또는 다시 등장한 객체에 부여함
        if ((len(self.ids) >= self.max_id)):
            max_feature_distance = 9999
            if ((len(self.deleted_tracks) > 0)):
                for i in self.deleted_tracks:
                    i_feature = np.array(i.features)
                    i_feature_distance = np.mean(np.abs(detection.feature-i_feature))
                    if (max_feature_distance > i_feature_distance):
                        max_feature_distance = i_feature_distance
                        self.id = i.track_id
                        i.state = 2
                        self.deleted_tracks.remove(i)
                        print(i.track_id)
                        break
            else:
                for i in self.tracks:
                    if (i.track_id not in self.match_list):
                        i_feature = np.array(i.features)
                        i_feature_distance = np.mean(np.abs(detection.feature-i_feature))
                        if (max_feature_distance > i_feature_distance):
                            max_feature_distance = i_feature_distance
                            self.id = i.track_id
                            self.match_list.append(i.track_id)
                            print(i.track_id)
                            break
        else:
            # self.id = self.get_id()
            # self.id += 1
            self.id = self.id_list[self.i]
            self.i += 1
            self.ids.append(self.id)
            print(self.id)
        ###
        self.tracks.append(Track(   
            detection.to_xyah(), self.id, class_id, conf, self.n_init, self.max_age, self.ema_alpha,
            detection.feature)) 
###
    def get_id(self):
        self.client_socket.send(b'request id')
        id = self.client_socket.recv(32).decode()
        print(id)
        if (len(id) > 0):
            self.client_socket.send(b'receive id')

        return id

def set_client_socket(client_socket):
    Tracker.client_socket = client_socket
    client_socket.sendall(b'track')
    data = client_socket.recv(32).decode()
    print(data)
    if (data == 'check'):
        client_socket.sendall(b'check')
###