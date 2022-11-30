import json
import os
import pandas as pd
from read_pic import read_pic

def get_json(room_no):
    global df

    path = os.getcwd()
    file = os.path.join(path, "room_data", room_no)
    file += ".json"

    if (os.path.isfile(file)):
        with open(file, "r") as sample_json:
            sample = json.load(sample_json)
        df = pd.DataFrame(sample)
        return df
    else:
        read_pic(room_no)
        df = get_json(room_no)

def num_seats():
    return len(df)

class Location:
    def __init__(self, center_x, center_y):
        self.cx = center_x
        self.cy = center_y
        self.location = 0

    def get_location(self):
        for x in range(len(df)):
            if df.loc[x]['start_location_y'] < self.cy < df.loc[x]['end_location_y']: 
                if df.loc[x]['start_location_x'] < self.cx < df.loc[x]['end_location_x']:   
                    self.location = x + 1
        return self.location
