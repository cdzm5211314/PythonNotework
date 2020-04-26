# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 14:58


class Person(object):

    # 类属性就是类所拥有的属性,它被此类的所有对象所共有,在内存中只存在一个
    count = 0  # 类属性

    def __init__(self,new_name, new_age):
        self.name = new_name
        self.age = new_age

    @classmethod
    def work(cls): # 类方法
        cls.count += 1
        print("类方法被调用...")

p = Person("张三",25)
print(p.count)       # 对象可以在外部直接访问类属性
p.work()             # 对象可以在外部直接调用类方法

print(Person.count)  # 类名可以在外部直接访问对象属性
Person.work()        # 类名可以在外部直接调用对象方法


## 对象可以在外部直接访问(或调用)类属性(或类方法)
## 类名可以在外部直接访问(或调用)类属性(或类方法)
