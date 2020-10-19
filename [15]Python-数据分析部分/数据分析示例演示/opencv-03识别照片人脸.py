# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-27 16:52


import cv2


# 人脸是有特征数据的,获取到了人脸特征,然后交给cv2的算法,就可以根据人脸特征查找(识别)人脸
# 去官网下载文件: https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml

# 读取加载图片
zly = cv2.imread("./zly0.jpg")

# 声明算法,给声明样的特征,识别什么样的事物,如 人脸,眼睛...
face_detect = cv2.CascadeClassifier("./haarcascade_frontalface_default.xml")

# 人脸检测
face_zone = face_detect.detectMultiScale(zly, scaleFactor=1.1, minNeighbors=5)
print(face_zone)  # [[175  34 192 192]]

# 人脸的坐标(x横坐标,y纵坐标,w,h人脸宽度)
for x, y, w, h in face_zone:
    # 绘制人脸的区域(矩形)
    cv2.rectangle(zly, pt1=(x, y), pt2=(x + w, y + h), color=[0, 0, 255], thickness=2)
    # 绘制人脸区域(圆形)
    cv2.circle(zly, center=(x + w//2, y + h//2), radius=w//2, color=[0,255,0], thickness=3)

# 使用窗口显示图片
cv2.imshow("star", zly)

# 退出窗口并释放资源
cv2.waitKey(0)
cv2.destroyAllWindows()


