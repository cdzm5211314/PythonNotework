# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 15:01

import math

class Circle:

    def __init__(self,radius): # 圆的半径: radius
        self.radius = radius
        self.__pi = 3.14  # 私有属性

    # 先有getxxx
    @property  # get
    def pi(self):
        return self.__pi

    # 再有set,因为set依赖get
    @pi.setter  # set
    def pi(self,pi):
        self.__pi = pi

    @property
    def area(self):  # 特殊属性
        return math.pi * self.radius ** 2  # 计算面积

    @property
    def perimeter(self):  # 特殊属性
        return 2 * math.pi * self.radius  # 计算周长

    @staticmethod
    def spam(x, y):
       return x + y

c = Circle(5)

print(c.pi)
c.pi = 5.14
print(c.pi)                 # 对象可以在外部直接访问特殊属性
print(Circle.pi)            # 类名不能在外部直接访问特殊属性
print(c.area)
print(c.perimeter)
print(c.spam(10,20))        # 对象可以在外部直接调用静态方法
print(Circle.spam(30,20))   # 类名可以在外部直接调用静态方法


## 对象可以在外部直接调用静态方法
## 类名可以在外部直接调用静态方法

## 对象可以在外部直接访问特殊属性
## 类名不能在外部直接访问特殊属性

