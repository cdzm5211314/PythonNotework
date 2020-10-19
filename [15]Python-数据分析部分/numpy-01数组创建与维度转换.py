# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/15 13:14

# import numpy as np
import numpy


### 注: 数组里的所有元素必须是相同类型

### 创建一维数组
## 方式一
a1 = numpy.array([1,3,5,7,9])
# a2 = numpy.array(range(1,10,2))
# print(a1, type(a1))  # [1 3 5 7 9] <class 'numpy.ndarray'>
# print(a2, type(a2))  # [1 3 5 7 9] <class 'numpy.ndarray'>
## 方式二
# numpy.arange([start,] stop[, step], dtype=None)
# a3 = numpy.arange(12)
# print(a3, type(a3))  # [ 0  1  2  3  4  5  6  7  8  9 10 11] <class 'numpy.ndarray'>

### 创建二维数组
aa1 = numpy.array([[1,3,5,7,9],[2,4,6,8,10]])
# print(aa1, type(aa1))  # [[ 1  3  5  7  9],[ 2  4  6  8 10]] <class 'numpy.ndarray'>

### 创建三维数组
aaa1 = numpy.array([[[1,2,3],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(aaa1, type(aaa1))

### 查看数组的维度个数: ndarray.ndim
print(a1.ndim)    # 1,表示一维数组
print(aa1.ndim)   # 2,表示二维数组
print(aaa1.ndim)  # 3,表示三维数组

### 查看数组的数据类型: ndarray.dtype
# print(a1.dtype)    # int32
# print(aa1.dtype)   # int32
# print(aaa1.dtype)  # int32

### 查看数组的维度大小(即形状): ndarray.shape
# print(a1.shape)    # (5,) 表示为一维数组,且数据个数为5个
# print(aa1.shape)   # (2, 5) 表示为2行5列的二维数组,且数据个数为2*5=10个
# print(aaa1.shape)  # (2, 2, 3) 表示为2块2行3列的三维数组,且数据个数为2*2*3=12个

### 修改数组的形状
## 注: 是一个返回值,不会修改原数组
## 把一个共24个数据的一维数组转换为二维数组或三维数组
# t1 = numpy.arange(24)  # 创建一个一维数组
# print(t1)
# [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
# 转换为二维数组,如 4行6列 ---> 4*6=24
# print(t1.reshape((4,6)))
# 返回值: [[ 0  1  2  3  4  5][ 6  7  8  9 10 11][12 13 14 15 16 17][18 19 20 21 22 23]]
# 转换为三维数组,如 2块3行4列 ---> 2*3*4=24
# print(t1.reshape((2,3,4)))
# 返回值: [[[ 0  1  2  3][ 4  5  6  7][ 8  9 10 11]] [[12 13 14 15][16 17 18 19][20 21 22 23]]]

## 把一个4行6列共24个数据的二维数组转换为一维数组或三维数组
# t2 = numpy.arange(24).reshape((4,6))  # 创建一个二维数组
# print(t2)
# [[ 0  1  2  3  4  5][ 6  7  8  9 10 11][12 13 14 15 16 17][18 19 20 21 22 23]]
# 转换为一维数组
# print(t2.reshape((24,)))  # 根据二维数组的具体元素个数(行数*列数)直接转换为一维数组
# print(t2.reshape((t2.shape[0]*t2.shape[1],)))  # 根据二维数组的形状数据(元组角标获取行数与列数)计算得到个数,然后转为一维数组
# print(t2.flatten())  # 使用numpy库的flatten方法折叠为一维数组
# 转换为三维数组,如 2块3行4列 ---> 2*3*4=24
# print(t2.reshape((2,3,4)))

## 把一个2块3行4列共24个数据的三维数组转换为一维数组或二维数组
# t3 = numpy.arange(24).reshape((2,3,4))  # 创建一个三维数组
# print(t3)
# [[[ 0  1  2  3][ 4  5  6  7][ 8  9 10 11]] [[12 13 14 15][16 17 18 19][20 21 22 23]]]
# 转为为一维数组
# print(t3.reshape((24,)))
# 返回值: [ 0  1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 16 17 18 19 20 21 22 23]
# 转换为二维数组,如 4行6列 ---> 4*6=24
# print(t3.reshape((4,6)))
# 返回值: [[ 0  1  2  3  4  5][ 6  7  8  9 10 11][12 13 14 15 16 17][18 19 20 21 22 23]]


### 构建其他数组:
## 构建全为0的数组
zeros_arr = numpy.zeros((3, 4), int)
print(zeros_arr.shape)
print(zeros_arr)

## 构建全为1的数组
ones_arr = numpy.ones((2, 3), int)
print(ones_arr)

## 初始化数组,不是总是返回全0,有时返回的是未初始的随机值（内存里的随机值）
empty_arr1 = numpy.empty((3, 3))
empty_arr2 = numpy.empty((3, 3), int)
print(empty_arr1, empty_arr2)

## 构建对角线为1的正方形数组(方阵)
eye_arr = numpy.eye(5)  # 5行5列的二维数组
print(eye_arr)

