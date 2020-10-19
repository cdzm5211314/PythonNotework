# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/17 12:39

# import pandas as pd
import pandas
import string
import numpy


### pandas常用的数据类型: Series, DataFrame
## Series: 一维,带标签数组
# 注: Series对象本质有两个数组组成,一个数组构成对象的键(index索引),一个数组构成对象的值(values)
## DataFrame: 二维,Series容器


### Series创建一维带标签索引数组,默认标签索引从0开始
## 注: 如果指定标签索引,需要标签索引个数与数据个数一致
p1 = pandas.Series([11,22,33,44,55])  # 使用默认标签索引,0~4
# print(p1)
p1 = pandas.Series(numpy.arange(5))   # 使用默认标签索引,0~4
# print(p1)

## 使用列表数据作为指定标签索引,a~e
p1 = pandas.Series(numpy.arange(5), index=list('abcde'))
# print(p1)

## 使用字典数据创建数组;并且字典的键作为指定标签索引,字典的值就是数组的元素数据
data_dict = {'name':'张三', 'age':18, 'sex':'男'}
p1 = pandas.Series(data_dict)
# print(p1)

## 注: 使用字典数据创建数组时,当重新给其指定标签索引之后,如果对应的上,就取值,如果对应不上,就取NaN
# NaN为float数据类型;numpy中nan为float,pandas会自动根据数据类更改Series的dtype类型
s_dict = {string.ascii_uppercase[i]:i for i in range(10)}  # 字典推导式
pp1 = pandas.Series(s_dict)
pp2 = pandas.Series(s_dict, index=list(string.ascii_uppercase[5:15]))
# print(pp1, pp2)

### 获取Series类型数据索引与具体的值
s_dict = {string.ascii_uppercase[i]:i for i in range(10)}  # 字典推导式
pp = pandas.Series(s_dict)
# print(pp.index)   # 获取索引数据
# print(pp.values)  # 获取具体的值数据

### 查看与修改Series数据类型
# 注: 与numpy的方法一致
p = pandas.Series([11,22,33,44,55])
## 查看数据类型:
# print(p.dtype)
## 修改数据类型:
p = p.astype(float)
# print(p.dtype)

print("*************************************************************")

### DataFrame创建二维带标签索引数组,默认标签索引都是从0开始
# 注: DataFrame对象即有行索引也有列索引
# 行索引: 表明不同行,横向索引,叫index,0轴,axis=0
# 列索引: 表明不同列,纵向索引,叫columns,1轴,axis=1
pp1 = pandas.DataFrame([[1,2,3,4,5],[11,22,33,44,55]])  # 使用默认行列标签索引
print(pp1)  # 行索引:0,1 列索引:0,1,2,3,4
pp1 = pandas.DataFrame(numpy.arange(12).reshape(3,4))   # 使用默认行列标签索引
print(pp1)  # 行索引:0,1,2 列索引:0,1,2,3

## 使用列表数据指定行列标签索引创建DataFrame二维数组
pp1 = pandas.DataFrame(numpy.arange(12).reshape(3,4), index=list('abc'), columns=list('ABCD'))
print(pp1)
data_dict = [{'name':'张三', 'age':18, 'sex':'男'},{'name':'李四', 'age':18},{'name':'王五','sex':'男'}]
pp1 = pandas.DataFrame(data_dict)
print(pp1)  # 注: 如果有缺失的值,会使用NaN

## 使用字典数据指定行列标签索引创建DataFrame二维数组
# 注: 字典的键会作为二维数组的列标签索引,行标签索引依然使用默认的标签索引,从0开始
data_dict = {'name':['张三','李四'], 'age':[21,30], 'sex':['男','女']}
pp1 = pandas.DataFrame(data_dict)
print(pp1)


