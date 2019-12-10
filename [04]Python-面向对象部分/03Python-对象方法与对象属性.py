# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 14:58

class Person(object):

    def __init__(self,new_name, new_age):
        self.name = new_name  # 对象属性
        self.age = new_age    # 对象属性

    def work(self): # 普通方法

        print("%s今年%s岁了,可以去找工作了..." %(self.name,self.age))

p = Person("张三",25)
print(p.name)       # 对象可以在外部直接访问对象属性
p.work()            # 对象可以在外部直接调用对象方法

# print(Person.name)  # 报错: 类名不可以在外部直接访问对象属性
# Person.work()       # 报错: 类名不可以在外部直接调用对象方法


## 对象属性的赋值规则:
# 首次为属性赋值则创建此属性
# 再次为属性赋值则必变属性的绑定关系

