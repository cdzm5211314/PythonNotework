# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 14:45

### 单例模式方式一: __new__()
class Singleton(object):
    __instance = None  # 私有化
    # 重复父类的__new__方法
    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super(Singleton,cls).__new__(cls,*args,**kwargs)
        return cls.__instance

class Demo(Singleton):
    def __init__(self):
        print("Demo类的初始化方法...")

d1 = Demo()
d2 = Demo()
print(id(d1))  # 4903992
print(id(d2))  # 4903992

### 单例模式方式二: 模块方式(Python独有的)
# 注:Python模块加载只执行一次
## singleton.py
# class MySingleton(object):
#     def run(self):
#         print("MySingleton run ...")
# mySingle = MySingleton()

## main.py
# from singleton import mySingle
# from singleton import mySingle as single
# print(id(mySingle))
# print(id(single))


