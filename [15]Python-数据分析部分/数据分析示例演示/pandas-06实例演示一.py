# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-29 19:05


import pandas
import numpy as np
from pandas import Series,DataFrame

# csv类型文本文件:
# 如果使用excel打开,是格式化的文件,所以excel可以直接读取成表格

"""" .csv文件数据
"state","abbreviation"
"Alabama","AL"
"Alaska","AK"
"Arizona","AZ"
"""
# csv_data = pandas.read_csv("./csv_data.csv")
# 获取行列数据: values[第几行][第几列]
# print(csv_data.shape)  # 查看DataFrame数据有多少行多少列
# print(csv_data.values)  # 得到二维数组类型的数据:[[第一行数据],[第二行数据],...,[最后一行数据]]
# print(len(csv_data.values))    # len得到二维数组数据中有多少元素
# print(len(csv_data.values[2])) # len得到二维数组数据中第二个元素数据中有多少元素
# print(csv_data.values[3][1])   # 获得二维数组数据第三行(第4个元素)第一列(第2个元素)数据
# print(csv_data.T)  # 转置行列数据


# 示例: 使用pandas分析美国人口数据
# 使用pandas读取csv类型文件
areas = pandas.read_csv("./state-areas.csv")  # 美国各州面积
print(areas.shape)  # (52, 2)
abbrevs = pandas.read_csv("./state-abbrevs.csv")  # 美国各州缩写
print(abbrevs.shape)  # (51, 2)
population = pandas.read_csv("./state-population.csv")  # 美国人口数据
print(population.shape)  # (2544, 4)
# print(areas,abbrevs,population)

# 分析以上数据:
# population数据多,abbrevs数据少, population数据中的state/region与abbrevs数据中的abbreviation简历对应关系
# 所以使用merge()进行数据融合

# left_on,right_on: 左右和右边分别根据哪个列属性进行融合
# how: 融合方式,inner内连接(两个DataFrame数据都有的keys才会保留),outer外连接(无论有没有都保留)
# how="outer" 融合方式数据绝不对丢失,有可能出现NaN空值
population2 = population.merge(abbrevs, how="outer", left_on="state/region",right_on="abbreviation")
print(population2)


# 删除一列数据: drop()
population2.drop(labels="abbreviation", axis=1, inplace=True)
print(population2)

# 查看是否有空值
print(population2.isnull().any())

# 定位为空的数据
cond = population2['state'].isnull()
print(cond)

# 当state为空时,返回,因为上述判断为空返回True
# 去重操作,保留非重复值
param = population2[cond]["state/region"].unique()
print(param)  # ['PR' 'USA'] 获取到了缩写为PR,USA对应洲名state为空
# USA ---> United States
# PR ---> Puerto Rico

# 给空值添加值
cond2 = population2["state/region"] == "USA"  # 找到为空的数据
print(cond2)
population2["state"][cond2] = "United States"  # 对空数据进行赋值
cond3 = population2["state/region"] == "USA"
population2["state"][cond3] = "Puerto Rico"


# 查看是否有空值???
print(population2)
print(population2.isnull().any())



