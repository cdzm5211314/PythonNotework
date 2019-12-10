# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-28 20:05

import pandas
import numpy as np

from pandas import Series,DataFrame

# pandas索引操作: Series索引  DataFrame索引


# Series索引操作:
# data数据,index索引,dtype数据类型,name数据属性命名
s = Series(data=np.random.randint(0,150,size=100),index=np.arange(1,101),dtype=np.int16,name="Python")
# print(s)

# 根据索引取值
# print(s[0]) # 根据不存在的索引取值报错
print(s[2])  # 根据某个索引取值
print(s[[4,5]])  # 根据多个索引取值

# 根据索引切片
print(s[10:15])
print(s[::2])  # 根据索引每隔2个取一个
print(s[::-2])  # 根据索引倒序每隔2个取一个

# Series的检索方法: loc()
print(s.loc[2])
print(s.loc[[4,5]])
print(s.loc[10:15])
print(s.loc[::2])
print(s.loc[::-2])

# iloc() 索引从0开始,数字化默认索引
print(s.iloc[0])
print(s.iloc[[4,5]])
print(s.iloc[10:15])


# DataFrame索引操作:
df = DataFrame(data=np.random.randint(0,150,size=(10,3)), index=list("ABCDEFGHIJ"), columns=["Python","En","Math"])
# print(df)

#

# 使用[],不能获取行样本数据,只能获取列属性数据,列属性比行样本重要
# print(df["C"])  # 不能使用[]获取行的数据,会报错
print(df["Python"])  # 根据列索引,获取一列的数据
print(df[["Python","Math"]])  # # 根据列索引,获取多列的数据

# 使用[],不能对列属性进行切片操作,只能对行样本进行切片操作
# print(df["Python":"En"])  # 不能使用[]进行列属性切片
print(df["C":"J"])  # 使用[]对行样本进行切片操作

# loc[]不能检索列属性,只能检索行样本
# print(df.loc["Python"])  # 报错
print(df.loc["B"])
print(df.loc[["C","D"]])
print(df.loc["C":"J"])
print(df.loc[::2])
print(df.loc[::-3])

# iloc[]索引从0开始,数字化默认索引
print(df.iloc[0:5])
print(df.iloc[::2])

# iloc[]即可以对行样本进行检索(切片),也可以对列属性进行检索(切片)
# 先对行样本,后对列属性
print(df.iloc[::2,1:])


