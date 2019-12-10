# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 17:04


# 安装: pip install opencv-python  # 处理图片和视频的库

import numpy as np
import matplotlib.pyplot as plt  # 画图工具
from matplotlib import pylab   # 显示图片
import cv2

# cv2模块,使用python方法调用c++方法,即导入cv2就可以使用opencv库
# 注: cv2读取图片时,颜色通道是蓝绿红

c = cv2.imread("./1.jpg")  # 路径不能含有中文
print(type(c))  # <class 'numpy.ndarray'>
print(c.shape)


# 画图及显示图片
# plt.imshow(c)  # 默认通道颜色为红绿蓝
# pylab.show()

# plt.imshow(c[:,:,::-1])  # 改变通道颜色为蓝绿红
# pylab.show()

# cv2显示图片
# 设置图片黑白显示
gray = cv2.cvtColor(c,code=cv2.COLOR_BGR2GRAY)
# cv2.imshow("rose",gray)

# 设置图片缩放
img = cv2.resize(gray,dsize=(200,100))
cv2.imshow("rose",gray)

# 原始显示
# cv2.imshow("rose",c)

# 等待键盘输入
cv2.waitKey(0)  # 无限等待
# cv2.waitKey(3000)  # 3秒后退出
# 释放内存
cv2.destroyAllWindows()



