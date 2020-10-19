# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-28 19:18

# 安装: pip install pandas
# pandas基于numpy,pandas中有两个常用类: Series, DataFrame
# pandas可以进行数据分析,处理数据速度快,灵活度高
# pandas中的DataFrame其实就是excel类型数据

# 数据分析使用软件: excel SPSS SAS

import pandas
import numpy as np

from pandas import Series,DataFrame

# 创建Series一维数据:
# Series索引(行)默认值: 0 1 2 ...
ss = Series([1,3,5,7,9])
print(ss)


# 设置索引值,索引名称个数与一维数组元素个数一致
s = Series(data=[120,136,128,98], index=['Math','Python','En','Chinese'])
print(s)

# 查看形状
print(s.shape)  # (4,)
# 获取数据
v = s.values
print(v, type(v))  # [120 136 128  98]  <class 'numpy.ndarray'>

# 平均值,最大值,最小值,标准差,幂运算
print(s.mean())
print(s.max())
print(s.min())
print(s.std())
print(s.pow(2))


######################################################################################
# 创建DatFrame二维数据:
# 所有进行数据分析,数据挖掘的工具最基础的结果: 行 和 列, 行表示样本,列表示属性
# DatFrame索引(行,列)默认值: 0 1 2 ...

# d = DataFrame([[1,4,7],[2,5,8],[3,6,9],[0,10],["a","b","c","d"]])
# print(d)
# 列索引个数与二维数组中一维数组中的元素个数值最大值一致
# 行索引个数与二维数组的元素个数值一致

# 创建0-150之间的随机数,10行3列,行索引"a,b,c,d,e,f,g,h,i,j",列索引"Python,En,Chinese"
df = DataFrame(data=np.random.randint(0,150,size=(10,3)), index=list("abcdefghij"), columns=["Python","En","Chinese"])
print(df)


# 查看形状
print(df.shape)  # (10, 3)
# 获取数据
v = df.values
print(v, type(v))  # 二维数据  <class 'numpy.ndarray'>


# 平均值,最大值,最小值,标准差
print(df.mean())
print(df.max())
print(df.min())
print(df.std())

# ??? 行 对应axis = 0
# ??? 列 对应axis = 1

# 默认是以行为单位来进行计算,要想使用列为单位来进行计算
print(df.mean(axis=1))
