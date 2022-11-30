import tkinter
from matplotlib import image
from matplotlib.font_manager import json_load
import numpy as np
import cv2 
import tkinter as tk
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
import os

from collections import OrderedDict
import json

def read_pic(room_no):
    file_data = OrderedDict()

    path = os.getcwd()
    file_path = os.path.join(path, "room_data", room_no)
    file_path += ".json"

    if os.path.exists(file_path):
        os.remove(file_path)

    with open(file_path, 'w', encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")

    number = []
    start_location_x = []
    start_location_y = []
    end_location_x = []
    end_location_y = []

    global a
    global b

    a = 1
    b = 1
    root = Tk()
    root.title('location')

    with open(file_path, 'r') as fp:
        after = json.load(fp)
        
    for i in range(len(after)):
        after.pop(i)
        break

    #시작지점이 마지막 지점보다 크면 뒤집기

    textExample= tk.Text(root, height=10)

    lbl = tk.Label(root, text="Tkinter와 OpenCV를 이용한 GUI 프로그래밍")
    lbl.grid(row=0, column=0) # 라벨 행, 열 배치

    frm = tk.Frame(root, bg="white", width=720, height=480) # 프레임 너비, 높이 설정
    frm.grid(row=1, column=0) # 격자 행, 열 배치

    lbl1 = tk.Label(frm)
    lbl1.grid()

    #btnRead.pack()
    def open2():
        global my_image # 함수에서 이미지를 기억하도록 전역변수 선언 (안하면 사진이 안보임)
        
        root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
        ('all files', '*.*'),('png files', '*.png'), ('jpg files', '*.jpg')))
        
        Label(root, text=root.filename).grid() # 파일경로 view
        my_image = ImageTk.PhotoImage(Image.open(root.filename))
        result=textExample.get("1.0","end")
        Label(image=my_image).grid() #사진 view
        img = cv2.imread(root.filename)
        a = img.shape[0]
        b = img.shape[1]

    def videocapture():
        video = cv2.VideoCapture('./test.mp4')
        if not video.isOpened():
            root.filename = filedialog.askopenfilename(initialdir='', title='파일선택', filetypes=(
            ('all files', '*.*'),('mp4 files', '*.mp4')))
            video = cv2.VideoCapture(root.filename)

        while True:
            ret, frame = video.read()
            frame = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2RGB)
            cv2.imshow('webcam', frame)
        # press escape to exit
            if (cv2.waitKey(30) == 13):
                img_captured = cv2.imwrite('img.jpg',frame)
                #pg.alert(text='저장되었습니다', title='capture', button='OK')
                break
        video.release()
        cv2.destroyAllWindows()
        
    def on_closing():
        root.destroy()
                
    canvas = Canvas(root, width = a, height = b)

    def draw(event):
        global x0, y0
        canvas.create_line(x0, y0, event.x, event.y)
        x0, y0 = event.x, event.y

    def down(event):
        global x0, y0
        x0, y0 = event.x, event.y
                
    canvas.bind("<B1-Motion>", draw)
    canvas.bind("<Button-1>", down)
    canvas.grid()

    my_btn = Button(root, text='비디오추출', command=videocapture).grid()
    my_btn = Button(root, text='파일열기', command=open2).grid()
    my_btn = Button(root, text='확인', command=on_closing).grid()
    root.mainloop()

    ## 새로 창을 열고 선택한 그림을 띄움
    events = [i for i in dir(cv2) if 'EVENT' in i]

    click = False     # Mouse 클릭된 상태 (false = 클릭 x / true = 클릭 o) : 마우스 눌렀을때 true로, 뗏을때 false로
    x1,y1 = -1,-1


    def draw_rectangle(event, x, y, flags, param):
        num = 1
        global x1,y1, click                                     # 전역변수 사용
        if event == cv2.EVENT_LBUTTONDOWN:                      # 마우스를 누른 상태
            click = True 
            x1, y1 = x,y
            #print("사각형의 왼쪽위 설정 : (" + str(x1) + ", " + str(y1) + ")")
            
        elif event == cv2.EVENT_MOUSEMOVE:                      # 마우스 이동
            if click == True:                                   # 마우스를 누른 상태 일경우
                a=1
                #cv2.rectangle(img,(x1,y1),(x,y),(255,0,0),1)
                #cv2.circle(img,(x,y),5,(0,255,0),-1)
                #print("(" + str(x1) + ", " + str(y1) + "), (" + str(x) + ", " + str(y) + ")")


        elif event == cv2.EVENT_LBUTTONUP:
            click = False;       # 마우스를 때면 상태 변경
            cv2.rectangle(img,(x1,y1),(x,y),(255,0,0),1)

            if x1 < 0:
                x1 = 0
            elif x1 > img.shape[1]:
                x1 = img.shape[1]

            if x < 0:
                x = 0
            elif x > img.shape[1]:
                x = img.shape[1]

            if y1 < 0:
                y1 = 0
            elif y1 > img.shape[0]:
                y1 = img.shape[0]

            if y < 0:
                y = 0
            elif y > img.shape[0]:
                y = img.shape[0]

            if x1 > x:
                tmp = x1
                x1 = x
                x = tmp
            
            if y1 > y:
                tmp = y1
                y1 = y
                y = tmp

            start_location_x.append(x1)
            start_location_y.append(y1)
            end_location_x.append(x)
            end_location_y.append(y)
            
            print("(" + str(x1) + ", " + str(y1) + "), (" + str(x) + ", " + str(y) + ")")

        #cv2.circle(img,(x,y),5,(0,255,0),-1)

    # 캔버스, MouseCallback 함수 설정
    img = cv2.imread(root.filename)
    cv2.namedWindow('image')
    cv2.setMouseCallback('image',draw_rectangle)                # 마우스 이벤트 후 callback 수행하는 함수 지정

    # main문 : 키보드로 esc를 받을때까지 화면을 계속 보여준다.
    while True:
        cv2.imshow('image', img)    # 화면을 보여준다.

        k = cv2.waitKey(1) & 0xFF   # 키보드 입력값을 받고
            
        if k == 27:               # esc를 누르면 종료
            break

    file_data.update({"start_location_x":start_location_x})
    file_data.update({"start_location_y":start_location_y})
    file_data.update({"end_location_x":end_location_x}) 
    file_data.update({"end_location_y":end_location_y})

    with open(file_path, 'w',encoding="utf-8") as make_file:
        json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
        
    cv2.destroyAllWindows()

    #esc를 누르면 저장하고 종료