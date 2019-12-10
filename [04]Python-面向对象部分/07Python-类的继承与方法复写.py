# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 15:03

## 继承/派生
# 1. 继承是指从已有的类中衍生出新类,新类具有原类的行为,并能扩展新的行为
# 2. 派生就是从一个已有类中衍生(创建)新类,在新类上可以添加新的属性和行为

## 继承和派生的目的:
# 继承是延续旧类的功能
# 派生是为了在旧类的基础上添加新的功能

# 作用:
# 1.用继承派生机制,可以将一些共有功能加在基类中,实现代码的共享
# 2.在不改变基类的基础上改变原有功能

## 继承/派生的名词:
# 基类(base class), 超类(super class), 父类(father class)
# 派生类(derived class) / 子类(child class)


## 继承关系中: 子类拥有父类以及父类的父类的所有属相和方法,子类也可以封装自己特有的属性和方法
## 覆盖(复写): 在继承关系中,子类实现了与基类同名的方法,在子类对象调用该方法时,对象调用的是子类中的覆盖的方法


# 在子类的对象方法中不能访问父类的私有属性
# 在子类对象的方法中不能调用父类的私有方法

# 子类的调用顺序: 先在自己中查找,如果没有再去父类中查找

class Person():

    # def __init__(self):  # 无参
    #     self.name = "匿名"
    #     self.age = 21
    #     print("父类的init方法!!!")

    # def __init__(self, name):  # 有参
    #     self.name = name
    #     self.age = 21
    #     print("父类的init方法!!!")

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("父类的init方法!!!")

    def eat(self):
        print(self.name + "正在吃饭...")

    def run(self):
        print(self.name + "正在跑步...")

class Student(Person):

    # def __init__(self):  # 无参
    #     # 调用父类的init方法
    #     super().__init__()  # super()父类对象,super(Student,self).__init__()
    #     print("---> student 的 init 方法")

    # def __init__(self,name):  # 有参
    #     # 调用父类的init方法
    #     super().__init__(name)
    #     print("---> student 的 init 方法")

    def __init__(self,name,age,clazz):  # 学生类的独有属性
        # 调用父类的init方法
        super().__init__(name,age)
        self.clazz = clazz
        print("---> student 的 init 方法")

    # 学生类独有的动作
    def study(self):
        print(self.name + "正在学习知识...")

    # 子类与父类中有同名的方法,即方法的复写
    # def eat(self):
    #     print(self.name + "正在吃饭...,喜欢吃大米饭!!!")

    def eat(self,food):
        print(self.name + "正在吃饭...,喜欢吃%s!!!" %food)


class Employee(Person):

    def __init__(self, name, age, salary):  # 雇员类的独有属性
        # 调用父类的init方法
        super().__init__(name, age)
        self.salary = salary
        print("---> employee 的 init 方法")

class Doctor(Person):
    pass


# stu = Student()  # 无参
# stu = Student("Tom")  # 有参
# stu.run()

# 学生类的独有属性
stu = Student("tom",21,"python2班")
stu.run()
stu.study()
# stu.eat()
stu.eat("鸡腿肉")

# 雇员类的独有属性
emp = Employee('lily',25,3500)
emp.run()

