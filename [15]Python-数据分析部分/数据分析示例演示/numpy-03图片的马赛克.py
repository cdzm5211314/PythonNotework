# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 13:04


import numpy as np
import matplotlib.pyplot as plt
# %matplotlib inline


nd = plt.imread("./1.jpg")
print(nd.shape)

# 马赛克: 本质上就是切片操作

# 整个图片马赛克实现:
nd2 = nd[::5,::5]
plt.imshow(nd2)


# 图片中某个部分马赛克实现:
msk = nd.copy()  # 原图只能读操作,此处复制一份
print(msk.shape)  # (460, 437, 3)

# 获取需要进行马赛克处理的尺寸数据
nd3 = nd[30:350,50:380]
print(nd3.shape)  # (320, 330, 3)
# 对获取的部分尺寸进行马赛克处理
nd4 = nd3[::5,::5]
print(nd4.shape)  # (64, 66, 3)
#

# msk[30:350,50:380] = nd4  # 会报错,形状不匹配
# 解决
for i in range(64):
    for j in range(66):
        msk[30 + i*5:30 + 5 + i*5,50 + j*5:50 + 5 + j*5] = nd4[i,j]

plt.imshow(msk)



