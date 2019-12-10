# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-27 17:28


import cv2

# 声明算法,给声明样的特征,识别什么样的事物,如 人脸,眼睛...
face_detect = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# 识别视频
cap = cv2.VideoCapture("./05.mp4")
# 识别电脑摄像头
# cap = cv2.VideoCapture(0)

# 查看视频(帧数)一秒多少帧,即能得到多少毫秒放一张照片: 1000(毫秒) / num
# num = cap.get(propId=cv2.CAP_PROP_FPS)

index = 1
while True:

    # 读取视频中的图片
    flag, frame = cap.read()

    if flag == False:
        break

    # 把视频中的图片变成黑白图片,尺寸没有变化
    gray = cv2.cvtColor(frame, code=cv2.COLOR_BGR2GRAY)

    # 人脸检测,使用黑白图片
    face_zone = face_detect.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

    # 人脸的坐标(x横坐标,y纵坐标,w,h人脸宽度)
    for x, y, w, h in face_zone:
        # 绘制人脸的区域(矩形)
        cv2.rectangle(frame, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
        # 绘制人脸区域(圆形)
        cv2.circle(frame, center=(x + w // 2, y + h // 2), radius=w // 2, color=[0, 255, 0], thickness=2)

    # 保存图片
    cv2.imwrite("./face/%d.jpg" % (index), frame)

    # 使用窗口显示彩色图片
    cv2.imshow("video", frame)

    index += 1
    # 当在键盘上输入q就退出循环
    if ord("q") == cv2.waitKey(10):
        break

# 退出窗口并释放资源
cv2.waitKey(0)
cv2.destroyAllWindows()
