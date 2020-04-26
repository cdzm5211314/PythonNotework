# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 14:58

class Person(object):

    def __init__(self,new_name, new_age):
        self.name = new_name  # 对象属性
        self.age = new_age    # 对象属性

    def work(self): # 普通方法
        # 对象(self)可以直接在内部直接访问对象属性
        print("%s今年%s岁了,可以去找工作了..." %(self.name,self.age))

    def demo(self):
        # print(self.gender)
        # 对象(self)可以直接在内部直接访问对象方法
        self.work()


p = Person("张三",25)
print(p.name)       # 对象可以在外部直接访问对象属性
p.work()            # 对象可以在外部直接调用对象方法

# print(Person.name)  # 报错: 类名不可以在外部直接访问对象属性
# Person.work()       # 报错: 类名不可以在外部直接调用对象方法

# 外部添加对象属性
# p.gender = "男"  # 给对象添加属性
# p.gender = "女"  # 给对象属性更改值
# p.demo()

## 对象属性的赋值规则: 对象.属性名 = 属性值
# 首次为属性赋值则添加此属性
# 再次为属性赋值则改变属性的绑定关系(即更改属性值)


## 对象可以在外部直接访问(或调用)对象属性(或对象方法)
## 类名不能在外部直接访问(或调用)对象属性(或对象方法)
