from tkinter import *
import cv2 as cv
from PIL import Image, ImageTk
import os
import socket
url_s = 'http://192.168.1.1:8080/?action=stream'
capture = cv.VideoCapture(url_s)
# 创建一个socket:
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# # 建立连接:
s.connect(('192.168.1.1', 2001))

#摄像机设置
#0是代表摄像头编号，只有一个的话默认为0


def getframe():
    ref,frame=capture.read()
    cv.imwrite(tempimagepath,frame)

def closecamera():
    capture.release()


def getframe():
    ref, frame = capture.read()
    cv.imwrite(tempimagepath, frame)


def closecamera():
    capture.release()


# 界面相关
window_width = 640
window_height = 480
image_width = int(window_width * 0.6)
image_height = int(window_height * 0.6)
imagepos_x1 = int(window_width * 0.2)
imagepos_y1 = int(window_height * 0.1)
butpos_x1 = 250
butpos_y1 = 350
imagepos_x2 = int(window_width * 0.2)
imagepos_y2 = int(window_height * 0.1)
butpos_x2 = 250
butpos_y2 = 400
imagepos_x3 = int(window_width * 0.2)
imagepos_y3 = int(window_height * 0.1)
butpos_x3 = 100
butpos_y3 = 400
imagepos_x4 = int(window_width * 0.2)
imagepos_y4 = int(window_height * 0.1)
butpos_x4 = 400
butpos_y4 = 400

top = Tk()
top.wm_title("face recognition")
top.geometry(str(window_width) + 'x' + str(window_height))


def tkImage():
    ref, frame = capture.read()
    cvimage = cv.cvtColor(frame, cv.COLOR_BGR2RGBA)
    pilImage = Image.fromarray(cvimage)
    pilImage = pilImage.resize((image_width, image_height), Image.ANTIALIAS)
    tkImage = ImageTk.PhotoImage(image=pilImage)
    return tkImage


def button1():
    print('前')
    s.send(b'3')

# 控件定义1
canvas1 = Canvas(top, bg='white', width=image_width, height=image_height)  # 绘制画布
b1 = Button(top, text='上', width=15, height=2, command=button1)

# 控件位置设置
canvas1.place(x=imagepos_x1, y=imagepos_y1)
b1.place(x=butpos_x1, y=butpos_y1)
def button2():
    print('停')
    s.send(b'0')

# 控件定义2
canvas2 = Canvas(top, bg='white', width=image_width, height=image_height)  # 绘制画布
b2 = Button(top, text='停', width=15, height=2, command=button2)

# 控件位置设置
canvas2.place(x=imagepos_x2, y=imagepos_y2)
b2.place(x=butpos_x2, y=butpos_y2)
def button3():
    print('左')
    s.send(b'2')

# 控件定义3
canvas3 = Canvas(top, bg='white', width=image_width, height=image_height)  # 绘制画布
b3 = Button(top, text='左', width=15, height=2, command=button3)

# 控件位置设置
canvas3.place(x=imagepos_x3, y=imagepos_y3)
b3.place(x=butpos_x3, y=butpos_y3)
def button4():
    print('右')
    s.send(b'1')

# 控件定义4
canvas4 = Canvas(top, bg='white', width=image_width, height=image_height)  # 绘制画布
b4 = Button(top, text='右', width=15, height=2, command=button4)

# 控件位置设置
canvas4.place(x=imagepos_x4, y=imagepos_y4)
b4.place(x=butpos_x4, y=butpos_y4)
if __name__ == "__main__":
    while (True):
        picture = tkImage()
        canvas1.create_image(0, 0, anchor='nw', image=picture)
        canvas2.create_image(0, 0, anchor='nw', image=picture)
        canvas3.create_image(0, 0, anchor='nw', image=picture)
        canvas4.create_image(0, 0, anchor='nw', image=picture)
        top.update()
        top.after(100)

    top.mainloop()
    closecamera()
