# 한밭대학교 컴퓨터공학과 HSORT 팀

## 팀 구성 및 담당 역할
- 20172608 이동진 (팀장) </br>
  RFID 출입 시스템 개발 </br>
  YOLO detector와 StrongSORT tracker를 활용하여 학생 위치 파악 시스템 개발
- 20172598 김규진 </br>
  반응형 웹서버 front/back-end 개발
- 20172615 최우석 </br>
  안드로이드 어플리케이션 개발
- 20172616 한수호 </br>
  YOLO detector와 StrongSORT tracker를 활용하여 학생 위치 파악 시스템 개발

- - -

## 프로젝트 소개
### RFID와 카메라를 활용한 학생 인식 및 위치 추적 시스템
- RFID 출입 게이트와 카메라를 활용하여 학생의 출입과 위치를 확인할 수 있는 시스템.
- RFID는 비접촉식으로 태그가 직접 리더기에 닿지 않아도 인식 범위 내에서 자동으로 인식함.
- RFID 태그의 ID를 카메라 영상 속 객체에게 부여하여 추적한 뒤, 객체의 위치를 파악함.
- 교수자는 스마트폰 또는 PC로 웹서버에 접속하여 교실의 정보를 한 눈에 파악할 수 있음.

- - -

## 프로젝트 배경

### 1. 비접촉식 RFID 출입 시스템
<img src="https://user-images.githubusercontent.com/101806955/195024426-383a2351-fdd3-458b-b540-9408ee203523.png" width="600px" height="350px"></img>  
<br><br>
신뢰성있는 비접촉식 RFID 출입 시스템을 개발하여 출입 시 태그를 소지하고 지나가기만 하면 되는 </br>
편리한 출입 시스템을 통해 접촉식 RFID 출입 시스템의 제약과 불편함을 해소하고자 함.

- - -

### 2. 교수자와 학생 간의 소통 문제
<img src="https://user-images.githubusercontent.com/101806955/195013863-3e963c05-d372-4bee-bfac-11f783b680e6.png" width="600px" height="552px"></img>
###### 출처: [충청뉴스 <한밭대, ‘MZ세대 학습자 이해와 공감’ 교수법 세미나 개최>](https://www.ccnnews.co.kr/news/articleView.html?idxno=258946)
</br>
코로나19 팬데믹 이후 비대면 수업으로 인해 교수자-학생 소통이 원활하지 않았고 대면 수업 전환 이후에도 </br>
1학년부터 혹은 복학 후 비대면 수업을 경험한 상황 등에 의해 소통에 어려움을 겪고 있는 상황임. </br>
학생의 위치와 정보를 한 눈에 파악할 수 있는 시스템을 통해 교수자가 학생에 맞는 적절한 피드백을 줄 수 있고 </br>
학생은 자신의 정보를 알고 있는 교수자와 더욱 적극적으로 소통할 수 있는 효과를 기대함.

- - -

### 3. 신뢰성 있는 영상 기반 객체추적 시스템 개발
영상 기반으로 객체를 추적하는 시스템은 결과물이 일반 사용자가 이해하기 쉽고 </br>
활용방법이 다양하기 때문에 국내외로 연구가 활발히 진행 중에 있음. </br>
</br>
- 박종혁, 박도현, 현동환, 나유민 and 이수홍. (2022). 객체 추적 알고리즘을 활용한 딥러닝 기반 실시간 화재 탐지 시스템. 한국컴퓨터정보학회논문지, 27(1), 1-8. [LINK](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART002807623)
- 김경훈, 강석주, Junho Heo. (2019). 딥러닝 기반 실시간 다중 객체 추적 시스템. 한국방송미디어공학회 학술발표대회 논문집, (), 246-246. [LINK](https://scienceon.kisti.re.kr/srch/selectPORSrchArticle.do?cn=NPAP13342247)
- Wojke, N., Bewley, A., & Paulus, D. (2017, September). Simple online and realtime tracking with a deep association metric. In 2017 IEEE international conference on image processing (ICIP) (pp. 3645-3649). IEEE. [LINK](https://arxiv.org/abs/1703.07402)
- Du, Y., Song, Y., Yang, B., & Zhao, Y. (2022). Strongsort: Make deepsort great again. arXiv preprint arXiv:2202.13514. [LINK](https://arxiv.org/abs/2202.13514)

</br>
하지만 객체추적 AI는 고질적인 단점으로 </br>
사물에 의한 차폐와 객체 간의 겹침으로 인한 ID switching 문제를 가지고 있음. </br>
이를 해결하기 위한 방안을 고려하고 실제로 적용하여 기술적인 성과를 얻고자 함.

- - -

## 시스템 구조
![개요도](https://user-images.githubusercontent.com/101806955/195017256-fce55de8-b5cc-4e4a-bef0-7676db793d5d.png)

- - -

### 객체추적 프로그램
  * YOLOv5와 StrongSORT를 활용하여 객체를 탐지, 추적함.</br>
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195027182-bc15b870-0788-415c-8702-d792254fbc8c.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195032202-5b2e1c61-118a-4c73-9e3e-288ff1cdba62.png" width="300px" height="100px"></img>
  </br></br>
  
  YOLOv5 by Glenn Jocher [[github]](https://github.com/ultralytics/yolov5)</br>
  YOLOv5+StrongSORT with OSNet by Mikel Brostrom [[github]](https://github.com/mikel-brostrom/Yolov5_StrongSORT_OSNet)
</div>
</br>

* YOLOv5</br>
  (YOLOv1 논문) - [You Only Look Once: Unified, Real-Time Object Detection](https://arxiv.org/abs/1506.02640) </br>
  기존 R-CNN 모델은 이미지 1장을 여러 장으로 쪼갠 후 </br>
  Bounding Box Regression, Detection Score를 찾는 2가지의 task를 수행했지만 </br>
  YOLO는 R-CNN에 비해 성능은 조금 하락했지만 'You Only Look Once'라는 논문의 제목에 어울리게 </br>
  이미지 전체를 Regression Task 1가지의 task로 처리하여 detection 속도를 상승시킨 1-stage detector. </br>
  때문에 Real-time object detection에 적합한 특성을 가짐. </br></br>
  YOLOv5는 여러 버전을 거쳐 성능을 개선하고 pytorch 프레임워크를 도입하여 개발됨. </br></br>

* StrongSORT</br>
  ![image](https://user-images.githubusercontent.com/101806955/197722166-0dcdcf18-3215-4dcc-a116-0887eebb66a9.png) </br>
  ![image](https://user-images.githubusercontent.com/101806955/197728345-d2611d70-0d40-4032-a7c1-138ecf7b4f8b.png) </br>
  ![image](https://user-images.githubusercontent.com/101806955/197724671-a0a55b14-795a-4e04-865e-cc77e59110e2.png) </br>
  ![image](https://user-images.githubusercontent.com/101806955/197724278-c605b1b8-a1a3-484b-9b0a-0cce6c450489.png) </br>

  * BOT와 ResNeSt50을 backbone으로 객체의 appearance feature 정보를 획득. </br>
  * EMA 방식으로 객체들의 appearance state를 업데이트. </br>
  * 움직임 보정을 위해 ECC를 사용하고 low-quality detection과 noise에 취약한 </br>
    기존의 kalman filter 대신 NSA kalman algorithm을 사용.
  * cost는 appearance cost와 motion cost의 weight sum.
</br></br>

* 차폐 및 ID switching 문제
  * 차폐 문제</br>
    객체가 사물에 가려지거나 영상 밖으로 나가는 등 탐지 및 추적이 불가능한 상태가 된 후에 </br>
    다시 등장했을 때 발생하는 문제. 사라졌던 객체의 ID가 유지되지 않고 새로운 ID가 부여되는 현상 발생. </br>
  * ID switching 문제 </br>
    객체 간의 겹침이 발생했을 때 서로의 ID가 바뀌는 현상. </br></br>
  * 해결방안
    * Occlusion 문제 </br>
      강의 정원에 맞춰 추적 개체의 최대치를 설정하여 차폐로 인한 새로운 ID 부여 현상을 감소시킴.
    * ID switching 문제 </br>
      학생이 앉은 자리를 잘 변경하지 않는다는 것을 고려하여 학생의 위치 정보 </br>
      반고정처리 과정을 거침으로써 ID switching 발생률을 감소시킴. </br>
    * 성능 비교
      * 기본 </br>
      <img src="https://user-images.githubusercontent.com/101806955/198521709-2a3c3074-9103-431e-9f11-1126750c6085.png" width="586px" height="438px"> </br>
      CPU </br>
      ![default](https://user-images.githubusercontent.com/101806955/203014801-1701ea35-501b-48c6-9d0c-e8bda006c840.png) </br>
      GPU </br>
      ![default](https://user-images.githubusercontent.com/101806955/198514303-9b77ecbb-290f-4227-b29a-5d5d7fcb7705.png) </br>
      ID 수 : 20 </br>
      ID switching 횟수 : 8회 </br>
      * 적용 결과 </br>
      ![all_capture](https://user-images.githubusercontent.com/101806955/198521171-3a877fc7-25f5-4ce0-912e-11530e21001d.png) </br>
      CPU </br>
      ![all](https://user-images.githubusercontent.com/101806955/203012957-c8f549cf-3d3f-42e7-8e5f-9bfa5bab315a.png) </br>
      GPU </br>
      ![all](https://user-images.githubusercontent.com/101806955/198514351-82d77078-830f-4d2c-82e1-911b2bf41bbc.png) </br>
      ID 수 : 17 (max-id 옵션으로 17 제한) </br>
      ID switching 횟수 : 5회 </br></br>
      
      > 실험 결과 ID 수의 최대치를 제한하고 객체 추적 테이블 업데이트에 학생의 위치 정보를 넣음으로써 </br>
      > 차폐 및 객체 간 겹침으로 인한 새로운 ID 부여 현상과 ID switching 현상을 줄일 수 있었음. </br>
      > 하지만 객체 간의 겹침이 활발할 경우에 그렇지 않은 경우보다 처리 과정이 오래 걸렸고 </br>
      > 실험 데이터 기준으로 기본 상태의 tracker에 비해 프레임마다 아래와 같이 처리 시간이 증가함.
      * CPU (Intel i3-10110U) </br>
        추적 업데이트(StrongSORT update)에 평균 약 1.03배의 시간(+185.6ms)이 소요됨.
      * GPU (Geforce RTX 2060) </br>
        추적 업데이트(StrongSORT update)에 평균 약 2.2배의 시간(+76.4ms)이 소요됨.

- - -

### 서버
  * Nuxt.js, Node.js로 프론트/백엔드 개발.
  * Google Firebase Hosting로 배포.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195033693-0ee9c805-42b8-452a-87f9-52b98d6b59e4.png" width="400px" height="100px"></img>    
  <img src="https://user-images.githubusercontent.com/101806955/195035144-54556f33-231b-48bd-9c2e-456f54ae50f5.png"></img>
  </br></br>
  <img src="https://user-images.githubusercontent.com/101806955/195034694-7128cf8d-aeb8-476a-917e-a8ab67f8f362.png" width="300px" height="100px"></img>
</div>

- - -

### DB
  * Google Firebase Realtime DB를 활용.
<div align="center">
  <img src="https://user-images.githubusercontent.com/101806955/195035930-aa134308-2dff-48ef-94f4-b9dd948fc380.png"></img>
</div>

- - -

### 어플리케이션
  * 웹서버 및 스마트폰 어플리케이션 개발.

- - -

## 결과물

- - -

## 결론
> 비접촉식 RFID 출입 시스템 통해 학생 출입을 관리, 영상 속 학생에게 부여할 ID를 획득하고, </br>
> YOLOv5 탐지 모델과 StrongSORT 탐지 모델을 활용하여 영상 속 학생에게 ID를 부여하여 추적한 후 </br>
> 학생이 지정된 좌표의 자리에 위치할 경우 자리에 있는 학생에 대한 정보를 얻을 수 있는 시스템을 개발함. </br>
> 
> 객체추적의 Occlusion 문제를 해결하기 위해 ID의 최대값을 지정하고 ID의 수가 그 이상일 경우</br>
> 추적이 끝난 ID 중 가장 feature가 유사한 것의 ID를 새로 등장한 객체에 부여했고, </br>
> 
> ID switching 문제를 해결하기 위해 학생의 위치 정보를 반고정으로 처리하는 방법으로 </br>
> 지정한 자리 좌표에 위치한 객체끼리의 겹침이 발생했을 때 ID switching이 발생하면, </br>
> DB에 저장된 ID를 겹침이 끝난 후에도 계속 그 자리에 위치한 객체에 부여하는 방법을 사용함. </br>
> 
> 위 방법들을 시도하여 문제를 완벽하게 해결하지는 못했지만 상기 서술했던 것처럼 완화하는 것에 성공함. </br>
</br>

* 보완해야할 점 </br>
Occlusion, ID switching 문제를 해결하기 위해서는 카메라의 설치 위치와 각도, 높이 등을 최적화 하는 방법 </br>
또는 여러 대의 카메라 영상을 stitching 하는 방법을 통해 영상 속 객체의 겹침과 차폐를 최소화하는 방법이 </br>
필요하다고 생각함. 또한 출입 게이트의 통신 안정화가 필요함. </br>


