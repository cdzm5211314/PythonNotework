# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-29 20:12


import pandas
import numpy as np
from pandas import Series,DataFrame

# 10行5列数据
df = DataFrame({"Hand":["right","left","right","left","right","right","left","left","left","right"],
                "Smoke":["yes","no","yes","no","no","no","yes","no","yes","yes",],
                "sex":["male","female","male","male","male","female","male","female","female","female"],
                "weight":[93,110,90,95,120,98,92,100,113,89],
                "IQ":[100,102,98,108,110,120,88,86,95,75]
                })
print(df)

# 分组聚合查看规律: 某一条件下的查看数据的规律
# 聚合: mean max min std ...等
# data = df.groupby(by=["Hand"])[["weight","IQ"]]
# print(data)  # <pandas.core.groupby.generic.DataFrameGroupBy object at 0x000000000574B0B8>

data = df.groupby(by=["Hand"])[["weight","IQ"]].mean().round(2)
print(data)
data = df.groupby(by=["Hand"])[["weight"]].mean().round(2)
print(data)

data = df.groupby(by=["Hand"])[["weight"]].apply(np.mean).round(1)
print(data)

data = df.groupby(by=["Hand"])[["weight"]].transform(np.mean).round(1)
print(data)


# ??? pandas - 30






