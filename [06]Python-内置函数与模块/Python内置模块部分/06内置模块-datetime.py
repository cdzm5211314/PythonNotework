# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator
# @Date : 2019-07-31 16:06


import time
import datetime

### time

## 延迟几秒
# time.sleep(3)
# print("我延迟了多久")


## 获取时间戳
print(time.time())  # 1570256238.560449

## 将时间戳 转换为 字符串
t_str = time.ctime()  # 参数: 接受一个时间戳,默认不传参数,是当前的时间戳
# t_str = time.ctime(time.time())  # 参数: 接受一个时间戳
print(t_str)  # Sat Oct  5 14:15:52 2019

## 将时间戳 转换为 时间元组
t_tuple = time.localtime()  # 参数: 接受一个时间戳,默认不传参数,是当前的时间戳
# t_tuple = time.localtime(time.time())  # 参数: 接受一个时间戳
print(t_tuple)  # time.struct_time(tm_year=2019, tm_mon=10, tm_mday=5, tm_hour=14, tm_min=15, tm_sec=52, tm_wday=5, tm_yday=278, tm_isdst=0)
print(t_tuple.tm_year, t_tuple.tm_mon, t_tuple.tm_mday)  # 2019 10 5


## 将时间元组 转换为 时间戳
t_tuple = time.localtime()
print(time.mktime(t_tuple))  # 1570256152.0

## 将时间元组 转换为 时间格式的字符串
t_tuple = time.localtime()
t_str = time.strftime("%Y-%m-%d %H:%M:%S", t_tuple)
print(t_str)  # 2019-10-05 14:21:20

## 将时间元组 转换为 时间格式的字符串
print(time.strftime('%Y-%m-%d %H:%M:%S'))  # 默认为当前时间,2019-10-05 14:15:52


## 将时间格式的字符串 转换为 时间元组
# tt = time.strptime("2017-05-25 14:32:58","%Y-%m-%d %H:%M:%S")
tt = time.strptime("2018/06/27 14:32:58", "%Y/%m/%d %H:%M:%S")
print(t_tuple)  # time.struct_time(tm_year=2017, tm_mon=5, tm_mday=25, tm_hour=14, tm_min=32, tm_sec=58, tm_wday=3, tm_yday=145, tm_isdst=-1)


## 将时间元组 转换成 默认的时间格式的字符串: 参数--->时间元组,无参数默认为当前时间元组
print(time.asctime())
## 将时间戳 转换成 默认的时间格式的字符串: 参数--->时间戳,无参数默认为当前的时间戳
print(time.ctime())

print("**********************************************************************************")

### datatime: 有几个类
# tate : 表示年月日
# time : 表示时分秒
# datetime : 表示年月日时分秒
# timedelta

## 获取当前日期
print(datetime.date.today())  # 2019-10-05

## 获取当前日期时间
print(datetime.datetime.now())  # 2019-10-05 14:37:56.656263

## 获取时间差之后的时间
print(datetime.datetime.now())  # 获取当前时间
print(datetime.datetime.now() + datetime.timedelta(days=3))         # 获取当前时间三天后的时间
print(datetime.datetime.now() + datetime.timedelta(days=-3))        # 获取当前时间三天前的时间
print(datetime.datetime.now() + datetime.timedelta(hours=5))        # 获取当前时间五小时后的时间
print(datetime.datetime.now() + datetime.timedelta(hours=-5))       # 获取当前时间五小时前的时间
print(datetime.datetime.now() + datetime.timedelta(minutes=20))     # 获取当前时间二十分钟后的时间
print(datetime.datetime.now() + datetime.timedelta(minutes=-20))    # 获取当前时间二十分钟前的时间
print(datetime.datetime.now() + datetime.timedelta(weeks=2))        # 获取当前时间两周后的时间
print(datetime.datetime.now() + datetime.timedelta(weeks=-2))       # 获取当前时间两周前的时间

## 替换当前时间的小时与分钟
print(datetime.datetime.now().replace(hour=16, minute=30))
# datetime.strptime(date_string, format)  # 给定时间格式解析字符串

