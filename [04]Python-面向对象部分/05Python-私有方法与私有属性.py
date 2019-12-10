# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 15:00

# 封装: 1.私有化属性 2.定义公有set和get方法
# __属性: 将属性私有化,访问范围仅仅限于类中

class Person(object):

    _sex = "男"         # 受保护的
    __country = "中国"  # 类的私有属性

    def __init__(self,new_name):
        self.name = new_name  # 对象属性
        self._age = 20        # 受保护的
        self.__addr = "北京"  # 对象的私有属性

    # 定义公有的set和get方法
    # set
    def setAddr(self,addr):
        self.__addr = addr

    # get
    def getAddr(self):
        return self.__addr

    def _sayAge(self):  # 受保护的
        print("说出你的年龄...")

    def __secrecyWork(self): # 对象的私有方法
        print("工作性质保密...")


p = Person("lisi")
# print(p._sex)             # 对象能在外部直接访问类的受保护属性
# print(p.__country)        # 对象不能在外部直接访问类的私有属性
# print(p._age)             # 对象能在外部直接访问对象的受保护属性
# print(p.__addr)           # 对象不能在外部直接访问对象的私有属性
# print(p._sayAge())        # 对象能在外部直接访问对象的受保护方法
# print(p.___secrecyWork)   # 对象不能在外部直接访问对象的私有方法

# print(Person._sex)             # 类能在外部直接访问类的受保护属性
# print(Person.__country)        # 类不能在外部直接访问类的私有属性
# print(Person._age)             # 类不能在外部直接访问对象的受保护属性
# print(Person.__addr)           # 类不能在外部直接访问对象的私有属性
# print(Person._sayAge())        # 类可以能在外部直接访问对象的受保护方法,但需要一个对象参数
# print(Person.___secrecyWork)   # 对象不能在外部直接访问对象的私有方法


