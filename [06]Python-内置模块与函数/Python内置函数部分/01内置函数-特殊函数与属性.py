# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator


### 判断两个变量是否绑定同一个对象: is 或 is not
# 如果是同一个对象返回True
# 如果不是同一个对象返回Flase
# 注: is 和 is not 作用相反

# 语法: x is y        ---> 是同一个对象返回True,不是返回Flase
# 语法: x is not y    ---> 不是同一个对象返回True,是返回Flase


### id(object): 获取对象的内存地址
# a = 10
# print(id(a))


### type(object): 返回对象的类型
print(type("字符串类型"))
print(type([2,5,8]))


### dir(object): object ---> 对象、变量、类型   返回值: 返回一个字符串列表
# dir函数作用:
# 1.如果没有参数调用，则返回当前作用域内的所有变量的列表
# 2.如果给定一个对象作用参数，则返回这个对象的所有变量的列表
# 2.1对于一个模块,返回这个模块的全部变量
# 2.2对于一个类对象，返回类对象的所有变量，并递归的基类对象的所有变量
# 2.3对于其它对象返回所有变量、类变量和基类变量
print(dir())
print(dir(str))


### __doc__: 当前文件描述,为模块字符串,模块字符串写在Python文件的第一行,三个引号包含起来的字符串
class Person(object):
    """这是一个类"""
    pass
def func():
    """这是一个函数"""
print(Person().__doc__)
print(func.__doc__)


### __file__: 当前文件路径
print(__file__)


### __name__: 判断运行的是哪个模块(文件)
# 1）当前文件被调用时,__name__的值为当前模块名
# 2）当前文件被执行时,__name__的值为"__main__"
print(__name__)


### __new__(): 负责对象的创建

### __init__(): 负责对象的初始化

### __str__(): 改变对象的字符串显示

### __repr__(): 改变对象的字符串显示

### __del__(): 析构方法,当对象在内存中被释放时,自动触发执行

### __call__(): 把这个类型的对象当作函数来使用,对象后面加括号,触发执行
# 即: 对象() 或者 类()()
class Test():
    def __init__(self, name):
        self.name = name
        print("类中的__init__初始化方法: " + self.name)
    def __call__(self, param):
        print("类中实现__call__方法: " + param)

t = Test("测试")  # 执行__init__方法
t("参数")         # 执行__call__方法


# globals()	返回当前全局作用域内变量的字典
# locals()	返回当前局部作用域内变量的字典