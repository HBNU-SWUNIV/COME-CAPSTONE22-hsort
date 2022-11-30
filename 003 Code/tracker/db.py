# pip install firebase_admin
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from location import num_seats

class DB:
    def __init__(self, room_no, max_id):
        # Fetch the service account key JSON file contents
        cred = credentials.Certificate('./key/Firebase_Realtime_DB_key.json')

        # Initialize the app with a service account, granting admin privileges
        firebase_admin.initialize_app(cred, {
            'databaseURL': 'Firebase_Realtime_DB_url'
        })

        # As an admin, the app has access to read and write all data, regradless of Security Rules
        self.ref = db.reference(str(room_no))
        self.max_id = max_id

    def init_room(self):
        init_dict = dict()
        for i in range(num_seats()):
            init_dict['seat'+str(i+1)] = {
                'id': '0'
            }
        self.ref.set(init_dict)

    def get_data(self):
        return self.ref.get()

    def update_db(self, data):
        if (self.get_data() == None):
            self.init_room()
        else:
            if (len(data) > 0):
                self.ref.update(data)

    def get_id(self, location):
        data = self.get_data()
        if (data != None):
            return data['seat'+str(location)]['id']
        else:
            return 0
