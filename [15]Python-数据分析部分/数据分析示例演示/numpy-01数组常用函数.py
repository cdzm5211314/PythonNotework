# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-09 21:21

import numpy as np

# numpy与Python中的列表(list)相似,但是比列表(list)更强大

li = [1, 3, 5, 7, 9]

# 创建numpy数组
nd = np.array(li)
print(nd)  # [1 3 5 7 9]
print(type(nd))  # <class 'numpy.ndarray'>

# 创建numpy一维,二维...等数组
nd1 = np.array([1, 3, 5, 7, 9])
nd2 = np.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])

# numpy的常用函数: 平均值,最大值,最小值,标准差,方差,n次方(幂),加,减,乘,除
print(nd2.mean())
print(nd2.max())
print(nd2.min())
print(nd2.std())
print(nd2.var())

print(np.power(5, 2))  # 求5的2次方
print(np.add(nd2, 100))  # 数组中的每个元素加100
print(np.subtract(nd2, 100))  # 数组中的每个元素减100
print(np.multiply(nd2, 100))  # 数组中的每个元素乘100
print(np.divide(nd2, 100))  # 数组中的每个元素除100


# 对numpy数组中元素进行排序: sort() 默认从小到大排序
arr1 = np.array(["a", "3", "2", "y"])
arr2 = np.array([["a", "2", "y"], [2, 5, 7], [2, "s", "3"]])
arr1.sort()
print(arr1)  # ['2' '3' 'a' 'y']
arr2.sort()
print(arr2)  # [['2' 'a' 'y'],['2' '5' '7'],['2' '3' 's']]


# numpy模块: 随机数据的生成
# 整数随机数据格式: numpy.random.random_integers(最小值,最大值,个数)
# 正态随机数据格式: numpy.random.normal(平均数,西格玛,个数)
data = np.random.random_integers(2, 35, 10)  # 生成整数随机数据
print(data)  # [25 11 12 18 24 31 23 35 32 8]
data = np.random.normal(5.0, 2.0, 5)  # 生成正态分布随机数据
print(data)  # [ 1.72168167  4.68000836  3.76598832  5.709232   -0.50785851]



