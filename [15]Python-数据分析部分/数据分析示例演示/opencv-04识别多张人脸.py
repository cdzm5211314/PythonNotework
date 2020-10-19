# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-27 17:27


import cv2

# opencv检测多张图片可以把图片变成灰色图片,灰色图片与彩色图片尺寸一致,人脸区域不会发生变化
# opencv检测图片时,只能检测正脸

# 加载图片
benpao = cv2.imread("./benpao.jpg")

# benpao是彩色图片(三维数据) ---> 转换为黑白图片
gray = cv2.cvtColor(benpao, code=cv2.COLOR_BGR2GRAY)


# 声明算法,给声明样的特征,识别什么样的事物,如 人脸,眼睛...
face_detect = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# 人脸检测,使用黑白图片
face_zone = face_detect.detectMultiScale(benpao, scaleFactor=1.2, minNeighbors=3)
print(face_zone)

# 人脸的坐标(x横坐标,y纵坐标,w,h人脸宽度)
for x, y, w, h in face_zone:
    # 绘制人脸的区域(矩形)
    cv2.rectangle(benpao, pt1=(x, y), pt2=(x+w, y+h), color=[0, 0, 255], thickness=2)
    # 绘制人脸区域(圆形)
    cv2.circle(benpao, center=(x + w//2, y + h//2), radius=w//2, color=[0,255,0], thickness=2)


# 使用窗口显示转换为黑白的图片
# cv2.imshow("star",gray)

# 使用窗口显示彩色图片
cv2.imshow("star", benpao)

# 退出窗口并释放资源
cv2.waitKey(0)
cv2.destroyAllWindows()

