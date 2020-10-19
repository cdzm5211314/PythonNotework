# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 18:13


import cv2
import matplotlib.pyplot as plt  # 画图工具
from matplotlib import pylab   # 显示图片


# 使用cv2读取视频
cap = cv2.VideoCapture("./03.mp4")
print(cap)  # <VideoCapture 0000000002A2D850>
# 视频对象,就是图片数据,一帧帧的图片数据就在cap对象中

flag,frame = cap.read()
print(flag)
# 画图并显示图片
plt.imshow(frame)
pylab.show()

# 释放视频资源
cap.release()

########################################################################################
cap = cv2.VideoCapture("./03.mp4")

flag,frame = cap.read()

index = 1
while True:

    # 循环退出语句
    if flag == False:
        break

    # 显示图片frame,窗口名字video
    cv2.imshow("video",frame)

    # 将视频图片保存到本地
    # plt.imsave("./images/%d.jpg" %(index),frame)  # 默认红绿蓝
    plt.imsave("./images/%d.jpg" %(index),frame[:,:,::-1])  # 改成蓝绿红

    # 什么时候退出循环,当在键盘上输入q就退出循环
    if ord("q") == cv2.waitKey(30):
        break

    # 继续读取照片数据
    flag,frame = cap.read()
    index+=1

# 循环结束,释放资源
cv2.destroyAllWindows()
cap.release()
