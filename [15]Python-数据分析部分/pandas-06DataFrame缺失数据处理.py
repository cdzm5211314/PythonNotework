# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/18 14:52

# import pandas as pd
import pandas
import numpy

### 缺失数据通常有两种情况: 空 或 None
## pandas中的NaN与numpy.nan一样
## 判断数据是否为NaN: pandas.isnull(DataFrame) 或 pandas.notnull(DataFrame)

pf = pandas.DataFrame(numpy.arange(1,25).reshape(4,6), index=list('abcd'), columns=list('ABCDEF'))
# print(pf)

## 处理为NaN的数据: 删除 或 填充
# 删除NaN所在的行列
pf.dropna(axis=0)             # 删除行中数据有NaN的所有行
pf.dropna(axis=0, how='all')  # 删除行中所有数据都为NaN的所有行,默认为all
pf.dropna(axis=0, how='any')  # 删除行中有一个数据都为NaN的所有行
pf.dropna(axis=0, how='any', inplace=True)  # 删除行中有一个数据都为NaN的所有行,inplace为True原地修改
# 填充数据
pf.fillna(0)           # 填充NaN为均值
pf.fillna(pf.mean())   # 填充NaN为均值

## 处理为0的数据: pf[pf==0] = numpy.nan
# 注: 计算平均值等情况,NaN是不参与计算的,但是0会参与计算


