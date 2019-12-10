# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator
# @Date : 2019-10-28 20:55

import pandas
import numpy as np

from pandas import Series,DataFrame


df = DataFrame(data=np.random.randint(0,150,size=(100,5)), index=np.arange(100,200), columns=["Python","En","Math","Java","MySQL"])
# print(df)

# 判断DataFrame是否存在空数据: 列属性
print(df.isnull())  # 有空数据返回True,无空数据返回False
print(df.isnull().any())  # any()有一个True就返回True,没有(即都是Flase)就返回False
# df.isnull().any() 返回都是Flase,说明没有空数据

print(df.notnull())  # 有空数据返回Flase,无空数据返回True
print(df.notnull().all())  # all()有一个Flase就返回Flase,没有(即都是True)就返回True
# df.notnull().all() 返回都是True,说明没有空数据



# 给DataFrame设置一些空数据
for i in range(30):
    # 行索引
    index = np.random.randint(100,200,size=1)[0]
    cols = df.columns
    # 列索引
    col = np.random.choice(cols)  # choise()随机获取

    # 设置空数据
    df.loc[index,col] = None
    # df.loc[index,col] = np.NAN

# print(df)
# DataFrame在显示数据的时候,会将空数据表示成NaN(not a number)

# 统计各个列属性有多少空数据: sum()
# print(df2.isnull().sum())

# 对列属性数据中的空数据以固定值填充: fillna()
# df2 = df.fillna(value=0)
# print(df2)

# 对列属性数据中的空数据以平均值填充: fillna()
# df2 = df.fillna(value=df.mean())
# # df2.astype(np.int16)
# print(df2)

# 对列属性数据中的空数据以中位数填充:
# df2 = df.fillna(value=df.median())
# print(df2)

# 对列属性数据中的空数据以众数填充:
# pass

# 对列属性数据中的空数据以前置填充:
# df2 = df.fillna(method="ffill")  # 注意axis参数

# 对列属性数据中的空数据以前置填充:
# df2 = df.fillna(method="bfill")  # 注意axis参数

# 当数据量足够大,空数据比较少,可以直接删除空数据
df2 = df.dropna()
print(df2)

# 查看DataFrame数据的前几行数据,后几行数据
# print(df.head())  # 默认前5行
# print(df.tail())  # 默认后5行

# 查看DataFrame数据中某列数据去重后的数据
print(df["Python"].unique())

# 查看DataFrame数据中某列数据出现的个数
print(df["Python"].value_counts())



