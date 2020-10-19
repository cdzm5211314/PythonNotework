# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/18 17:06

# import pandas as pd
import pandas
import numpy

### 时间序列索引: DatetimeIndex理解为时间戳
## start和end以及freq(间隔)配合能够生成start和end范围内以频率freq的一组时间索引
## start和periods(个数)以及freq(间隔)配合能够生成从start开始的频率为freq的periods个时间索引

index = pandas.date_range(start='20200901', end='20201031', freq='D')       # 间隔1天
index = pandas.date_range(start='2020/09/01', end='2020/10/31', freq='3D')  # 间隔3天
index = pandas.date_range(start='2020-09-01', end='2020-10-31', freq='7D')  # 间隔7天
# index = pandas.date_range(start='20200901', periods=10, freq='10D')  # 间隔10天,生成10个数据
print(index)

### 时间序列索引: PeriodIndex理解为时间段
## 把分开的时间字符串通过PeriodIndex的方法转化为pandas的时间类型
# periods = pandas.PeriodIndex(year=df["year"], month=df["month"], day=df["day"], hour=df["hour"], freq="H")


### 把时间字符串转换为时间序列
# df['date_colnums_name'] = pandas.to_datetime(df['date_colnums_name'], format='')
# 注: format参数大部分情况下可以不用写,但是对于pandas无法格式化的时间字符串,我们可以使用该参数,比如包含中文

### pandas重采样: ()频率转化
## 重采样: 指的是将时间序列从一个频率转化为另一个频率进行处理的过程,将高频率数据转化为低频率数据为降采样,低频率转化为高频率为升采样
# df.resample('D').mean()
# df.resample('10D').count()


