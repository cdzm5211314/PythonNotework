# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/17 15:27


# import pandas as pd
import pandas
import string

### 根据索引或序号位置(即行序号,默认从0开始)获取数组的数据
# 注: 获取一个的时候直接传入index索引或序号,获取多个时候传入index索引列表或序号列表
# 注: 序号位置即行序号,默认从0开始
# 注: 如果index索引或序号位置不存在,则报错
data_dict = {'name':'张三', 'age':18, 'sex':'男', 'tel':'10086'}
p = pandas.Series(data_dict)
# print(p['age'])   # 根据index索引获取数组的一个值
# print(p[1])       # 根据序号位置获取数组的一个值
# print(p[['name','sex']])  # 根据index索引列表获取数组的多个值
# print(p[[0,2]])   # 根据序号位置列表获取数组的多个值

### 使用布尔索引获取数组的数据
# 注: 前提数组中数据为数字类型
p = pandas.Series([11,22,33,44,55])
p = p[ p > 22 ]  # 获取数组值大于22的数据
# print(p)

print("*************************************************************")

### 根据切片获取数组的值:
# 传入起始位置start(默认为0),结束位置end(-1表示最后一个),步长间隔step
# 注: 切片操作包头不包尾
s_dict = {string.ascii_uppercase[i]:i for i in range(10)}  # 字典推导式
pp = pandas.Series(s_dict)
print(pp[:])      # 获取数组的所有数据
print(pp[:3])     # 获取从开始行到第3+1行数据
print(pp[7:])     # 获取从第7+1行到最后行数据
print(pp[5:-1])   # 获取从第5+1行到倒数第2行数据
print(pp[1:-1:2]) # 获取从第1+1行到倒数第2行数据,且间隔2行的数据



