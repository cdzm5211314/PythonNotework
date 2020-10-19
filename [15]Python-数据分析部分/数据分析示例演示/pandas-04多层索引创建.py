# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-28 20:55

import pandas
import numpy as np

from pandas import Series,DataFrame


# 多层索引,行列

# Series单层索引
s = Series(data=np.random.randint(0,150,size=6), index=list("abcdef"))
print(s)

# Series多层(列)索引
s2 = Series(data=np.random.randint(0,150,size=6),
            index=pandas.MultiIndex.from_product([["张三","李四","王五"],["期中","期末"]]))
print(s2)


# DataFrame二层(行)索引
df = DataFrame(data=np.random.randint(0,150,size=(6,3)), columns=["Python","En","Math"],
               index=pandas.MultiIndex.from_product([["张三","李四","王五"],["期中","期末"]]))
print(df)

# 先获取列,再获取行
print(df["Python"]["李四"]["期末"])
# 先获取行,再获取列
print(df.loc["李四"].loc["期中"]["En"])


# DataFrame三层(行)索引
df2 = DataFrame(data=np.random.randint(0,150,size=(12,3)), columns=["Python","En","Math"],
               index=pandas.MultiIndex.from_product([["张三","李四","王五"],["期中","期末"],["A","B"]]))
print(df2)


# DataFrame多层(列)索引
df3 = DataFrame(data=np.random.randint(0,150,size=(6,6)), index=list("ABCDEF"),
               columns=pandas.MultiIndex.from_product([["Python","En","Math"],["期中","期末"]]))
print(df3)

# 多层索引运算:
print(df3.mean())  # 默认运算行的平均值, axis=0
print(df3.mean().round(2))  # 默认运算行的平均值并保留两位小数 axis=0
print(df3.mean(axis=1))  # 运算列的平均值, axis=1

print(df3.mean(axis=1, level = 0)) # 运算列的平均值,且是获取二维列中第一元素的平均值
print(df3.mean(axis=1, level = 1)) # 运算列的平均值,且是获取二维列中第二元素中的元素平均值


# 行列索引转换
# 从列变成行: stack()
print(df3.stack())  # 默认level = -1
print(df3.stack(level=1))  # level = 1
print(df3.stack(level=0))  # level = 1

# 从行变成列: unstack()
df4 = df3.stack()
print(df4.unstack(level=0))
print(df4.unstack(level=1))


