# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/15 13:15


# import numpy as np
import numpy


## 创建numpy一维,二维...等数组
nd1 = numpy.array([1, 3, 5, 7, 9])
nd2 = numpy.array([[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]])

## numpy的元素统计函数:
# 注: 多维数组默认统计全部维度，axis参数可以按指定轴心统计，值为0则按行行方向统计列，值为1则按列方向统计行
print(numpy.mean(nd1))  # 所有元素的均值
print(numpy.sum(nd1))   # 所有元素的求和
print(numpy.max(nd1))   # 所有元素的最大值
print(numpy.min(nd1))   # 所有元素的最小值
print(numpy.std(nd1))   # 所有元素的标准差
print(numpy.var(nd1))   # 所有元素的方差
print(numpy.cumsum(nd1))    # 返回一个一维数组,每个元素都是之前元素的累加和
print(numpy.cumprod(nd1))   # 返回一个一维数组,每个元素都是之前元素的累乘积
print(numpy.sum(nd2, axis=0)) # 数组的按行方向统计列的和
print(numpy.sum(nd2, axis=1)) # 数组的按列方向统计行的和
print(numpy.argmax(nd2, axis=0)) # 数组中每列数据最大值的索引位置
print(numpy.argmin(nd2, axis=1)) # 数组中每行数据最小值的索引位置

print("--------------------------------------------")

## numpy的元素计算函数:
print(numpy.power(nd2, 2))       # 数组中每个元素的2次方
print(numpy.add(nd2, 100))       # 数组中的每个元素加100
print(numpy.subtract(nd2, 100))  # 数组中的每个元素减100
print(numpy.multiply(nd2, 100))  # 数组中的每个元素乘100
print(numpy.divide(nd2, 100))    # 数组中的每个元素除100
print(numpy.ceil(nd2))           # 数组中的元素向上最接近的整数
print(numpy.floor(nd2))          # 数组中的元素向下最接近的整数
print(numpy.rint(nd2))           # 数组中的元素进行四舍五入
print(numpy.isnan(nd2))          # 判断数组中的元素是否为NaN
print(numpy.abs(nd2))            # 数组中的元素进行绝对值
print(numpy.where(nd2, 100, 200))     # 数组中的元素进行三元运算,x if condition else y

print("--------------------------------------------")

## numpy的元素判断函数:
print(numpy.any(nd1 > 0))  # 数组中至少有一个元素满足指定条件,返回True
print(numpy.all(nd2 > 0))  # 数组中所有的元素满足指定条件,返回True

## numpy的元素去重排序函数: 找到唯一值并返回排序结果,类似于Python的set集合
arr = numpy.array([[1, 2, 1], [2, 3, 4]])
arr = numpy.unique(arr)
print(arr)  # [1 2 3 4]

## 对数组中的元素进行排序: sort() 默认从小到大排序
arr = numpy.array([["a", "2", "y"], [2, 5, 7], [2, "s", "3"]])
arr.sort()
print(arr)  # [['2' 'a' 'y'],['2' '5' '7'],['2' '3' 's']]


