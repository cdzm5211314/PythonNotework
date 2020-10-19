# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/18 15:25

# import pandas as pd
import pandas
import numpy

### 数据的合并: join()
## 注: 默认情况下把行索引相同的数据合并在一起
df1 = pandas.DataFrame(numpy.arange(1,13).reshape(3,4), index=list('abc'), columns=list('ABCD'))
df2 = pandas.DataFrame(numpy.arange(1,9).reshape(2,4), index=list('ab'), columns=list('EFGH'))
print(df1.join(df2))
#    A   B   C   D    E    F    G    H
# a  1   2   3   4  1.0  2.0  3.0  4.0
# b  5   6   7   8  5.0  6.0  7.0  8.0
# c  9  10  11  12  NaN  NaN  NaN  NaN
print(df2.join(df1))
#    E  F  G  H  A  B  C  D
# a  1  2  3  4  1  2  3  4
# b  5  6  7  8  5  6  7  8

print("*****************************************************************")

### 数据的合并: merge()
## 注: 按照指定的列把数据按照一定的方式合并在一起
df11 = pandas.DataFrame(numpy.arange(1,13).reshape(3,4), index=list('abc'), columns=list('ABCD'))
df22 = pandas.DataFrame(numpy.arange(1,9).reshape(2,4), index=list('ab'), columns=list('EFGH'))
# 默认合并方式: inner 交集
print(df1.merge(df2, left_on='B', right_on='F'))
print(df1.merge(df2, left_on='B', right_on='F', how='inner'))
#    A  B  C  D  E  F  G  H
# 0  1  2  3  4  1  2  3  4
# 1  5  6  7  8  5  6  7  8
# 指定合并方式: outer 并集,NaN补全
print(df1.merge(df2, left_on='B', right_on='F', how='outer' ))
#    A   B   C   D    E    F    G    H
# 0  1   2   3   4  1.0  2.0  3.0  4.0
# 1  5   6   7   8  5.0  6.0  7.0  8.0
# 2  9  10  11  12  NaN  NaN  NaN  NaN
# 指定合并方式: left 左边为准,NaN补全
print(df1.merge(df2, left_on='B', right_on='F', how='left'))
#    A   B   C   D    E    F    G    H
# 0  1   2   3   4  1.0  2.0  3.0  4.0
# 1  5   6   7   8  5.0  6.0  7.0  8.0
# 2  9  10  11  12  NaN  NaN  NaN  NaN
# 指定合并方式: right 左边为准,NaN补全
print(df1.merge(df2, left_on='B', right_on='F', how='right'))
#    A  B  C  D  E  F  G  H
# 0  1  2  3  4  1  2  3  4
# 1  5  6  7  8  5  6  7  8

print("*****************************************************************")

### 数据的分组: groupby()
## 注: 分组后的DataFrameGroupBy类型对象可以进行遍历操作也可以调用聚合方法
df111 = pandas.DataFrame(numpy.arange(1,13).reshape(3,4), index=list('abc'), columns=list('ABCD'))
grouped = df111.groupby(by='B')  # 根据某列进行分组;pandas.core.groupby.generic.DataFrameGroupBy
# grouped = df111.groupby(by=[df111['B'],df111['D']])  # 根据多列进行分组;pandas.core.groupby.generic.DataFrameGroupBy
# 进行遍历操作
# for i in grouped:  # 遍历出来的是元组数据
#     print(i, type(i))
for i,j in grouped:  # 遍历出来的是元组数据
    print(i, j, type(j))  # j为DataFrame类型数据

# 调用聚合方法
print(type(grouped['C'].count()))  # pandas.core.series.Series
print(type(df111.groupby(by='B').count()))  # pandas.core.frame.DataFrame
print(type(df111.groupby(by=[df111['B'],df111['D']]).count()))  # pandas.core.frame.DataFrame
print(type(df111[['C']].groupby(by=[df111['B'],df111['D']]).count()))  # pandas.core.frame.DataFrame
print(type(df111.groupby(by=[df111['B'],df111['D']])[['C']].count()))  # pandas.core.frame.DataFrame
print(type(df111.groupby(by=[df111['B'],df111['D']]).count()[['C']]))  # pandas.core.frame.DataFrame


