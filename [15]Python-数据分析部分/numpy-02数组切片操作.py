# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-13 11:42


import numpy as np
import matplotlib.pyplot as plt # 画图
import matplotlib.pylab as plb  # 图片显示

# 安装: pip install matplotlib

# numpy数组切片操作: 按照下标取某一段的元素
# 格式:array[index:end:step]  --->  数组[起始下标:结束下标:步长(间隔)],  间隔默认为1
# 注: end > index
# 注: step为正数(正的数),step为负数(倒着数)
# 注: 如果index没有数值,表示从0开始取,如果end没有数值,表示取到最后一个
# 注: 如果end给定了数值,取得是起始下标位置到end-1下标位置的元素
nd1 = np.array([1,3,5,7,9,11,13,15,17,19])
nd2 = np.array([[1,3,5,7,9],[-1,-3,-5,-7,-9],[2,4,6,8,10],[-2,-4,-6,-8,-10]])
# 一维数组
# print(nd1[:2])  # 表示取下标0-1的元素,包头不包尾
# print(nd1[1:])  # 表示取下标1-最后一个下标的元素
# print(nd1[0:1])  # 表示取下标0-1的元素,包头不包尾
# print(nd1[2:4])  # 表示取下标2-3的元素,包头不包尾
# print(nd1[::2])  # 表示取出间隔为2的所有元素


# 多维数组: 二维数组(几行几列) 多维数组(...,几页几行几列)
# print(nd2[0:2])
# 对列进行切片操作,先行后列
print(nd2[:,:])  # 切片时, : ,左右两边没有索引值,表示保留所有
print(nd2[::2])  # 取出二维数组中间隔2的所有元素
print(nd2[1:3,2:5])  # 表示取多维数组的第二行和第三行,然后再取出第二行第三行中的第三列,第四列和第五列
print(nd2[1:3,2:5:2])  # 表示取多维数组的第二行和第三行,然后再取出第二行第三行中的第三列,第四列和第五列并且间隔为2


# 获取彩色图片(三维)的数据数组
nd = plt.imread("./qq.png")  # 加载图片
# print(nd)  # 三维数组 数据
# plt.imshow(nd)  # 画图
# 显示图片的形状数据
print(nd.shape)  # (423, 914, 4)  高度, 长度, 颜色(0,1,2)
# 注: 颜色通道默认为红绿蓝, nd(:,:,::-1) ---> 蓝绿红
# 对图片进行切片操作
nd3 = nd[0:200,300:700]
# plt.imshow(nd3)
# plb.show()
nd4 = nd[0:200,300:700,::-1]  # 蓝绿红
# plt.imshow(nd4)
# plb.show()
nd5 = nd[0:200,300:700,[1,2,0]]  # 绿,蓝,红
# plt.imshow(nd5)
# plb.show()








