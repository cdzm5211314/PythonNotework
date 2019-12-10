# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 9:12

### 递归函数(recursion): 函数直接或间接的调用自身
## 直接调用自身示例:
# def story():
#     print("从前有座山")
#     print("山上有座庙")
#     print('庙里有人老和尚讲故事:')
#     story()  # 直接调用自身
# story()

## 间接调用自身示例:
# def test():
#     print("test ...")
#     demo()
# def demo():
#     print("demo ...")
#     test()
# demo()

## 递归函数说明:
# 1.递归一定要控制递归的层数,当符合某一条件时要终止递归
# 2.几乎所有的递归都能用while循环来代替
## 递归的优缺点:
# 优点：递归可以把问题简单化，让思路更为清晰，代码更简洁
# 缺点: 递归因系统环境影响大，当递归深度太大时，可能会得到不可预知的结果

## 控制递归层数的示例如下：
def func(n):
    print("递归进入第", n, "层")
    if n == 3:
        return
    func(n + 1)
    print("递归退出第", n, '层')
func(1)
print("程序结束")


### 斐波那契数列: 1,1,2,3,5,8,13,21,34,......
# 除第一,第二个数之外,后面的任意一个数都是前两个数相加得到
# 求斐波那契数列的前N位是何值???
# def fib(max):
#     n, a, b = 0, 0, 1
#     while n < max:
#         print(b)
#         a, b = b, a+b
#         n = n + 1
#     return "done"
# fib(10)

# 递归方式求斐波那契数列的第N位数是何值???
# def factorial(n):
#     if n == 1 or n == 2:
#         return 1
#     return factorial(n-1) + factorial(n-2)
# print(factorial(10))

# ----------------------------------------------------------------------------------------- #

## 高阶函数(High Order Function):
# 高阶函数需满足下列任意条件:
# 1.函数接受一个或多个函数作为参数传入
# 2.函数返回一个函数
# 示例如下:
def func1():
    print("func1 函数...")
def func(func1):
    return func1
res = func(func1)  # ---> 调用func函数,返回一个函数名为func1的内存地址
res()  # ---> 实际是调用func1函数
print(res)

# ----------------------------------------------------------------------------------------- #

## 函数的闭包(closure): 将内嵌函数的语句和这些语句的执行环境打包在一起时，得到的对象称为闭包(closure)
# 闭包必须满足3个条件:
# 1.外部函数中定义了内部函数
# 2.外部函数必须有返回值且必须是内部函数名
# 3.内部函数必须引用外部函数中的变量
# 闭包示例如下:
def func(var):
    def test(args):
        return args ** var
    print(locals())
    return test
res = func(3)  # ---> 调用func函数,并把实参3传递给var变量,返回一个函数名为test的内存地址
res2 = res(2)  # ---> 实际为调用test函数,并把实参2传递给args变量,返回一个运算结果
print(res)
print(res2)
res3 = func(2)(5)
print(res3)

# ----------------------------------------------------------------------------------------- #
import time
from functools import wraps
### 装饰器(decorators): 函数装饰器是指装饰的是一个函数，传入的是一个函数，返回的也是一个函数的函数
## 装饰器原则：
# 1.不修改被修饰函数的源代码
# 2.不修改被修饰函数的调用方式

## 装饰器实现：装饰器 = 高阶函数 + 函数嵌套 + 闭包

## 函数装饰器的语法:
# def 装饰器函数名(参数):
#     语句块
#     return 函数对象

## 被装饰函数的语法
# @装饰器函数名
# def 函数名(形参列表):
#     语句块

# 注: 多层装饰器,首先执行离被装饰函数最近的那个装饰器函数

"""
def decorate(func):
    print("decorate被执行...1...")
    def wrapper():
        print("wrapper被执行...3...")
        func()
        print("wrapper被执行...5...")
    print("decorate被执行...2...")
    return wrapper
@decorate
def demo():
    print("被装饰函数demo...4...")
demo()
1. Python解释器从上往下执行程序,此示例先加载函数
2. 当出现@decorate时,Python解释器底层就会执行装饰器函数(decorate)
3. 将被装饰函数(demo)作为参数传递给装饰器函数(decorate)的形参(func) ---> func = demo
4. 装饰器函数返回内部函数名(wrapper) ---> demo = wrapper
5. 当调用demo()函数,实际上调用的是wrapper()
"""

## 示例如下:
def decorate(fn):
    @wraps(fn)
    def wrapper(name, x):
        print("发送消息:", name, '来银行办理业务...')
        fn(name, x)
        print("发送消息:", name, '办了', x,'元的业务...')
    return wrapper
@decorate
def withdraw(name, x):
    print(name, '取钱', x, '元')
withdraw('小王', 300)


## 万能装饰器:
def decorate(func):
    def wrapper(*args, **kwargs):
        print(args, kwargs)
        result = func(*args, **kwargs)
        return result
    return wrapper
@decorate
def demo1():
    return "被装饰函数demo1..."
@decorate
def demo2(s):
    return "被装饰函数demo2..."
@decorate
def demo3(name="lisi"):
    return "被装饰函数demo3..."
res1 = demo1()
res2 = demo2("zhangsan")
res3 = demo3(name="wangwu")


############################################################################################
## 装饰器示例如下: 无参数
# 定义装饰器：功能 - 查看源程序函数demo的运行时间
def decorate(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        stop_time = time.time()
        print("demo函数的运行时间：%s"%(stop_time - start_time))
        return res
    return wrapper

# 源程序代码函数demo
@decorate
def demo():
    time.sleep(2)
    print("demo函数执行完毕...")
    return "源程序函数demo"
s = demo()
print(s)  # 源程序函数demo


## 装饰器示例如下: 有参数
# 定义装饰器：功能 - 查看源程序函数demo的运行时间
# 为装饰器传递一个参数，只需要在最外层在创建一个函数,并返回一个函数名
def param(p_type):
    def decorate(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("装饰器参数：%s" %p_type )
            start_time = time.time()
            res = func(*args, **kwargs)
            stop_time = time.time()
            print("demo函数的运行时间：%s"%(stop_time - start_time))
            return res
        return wrapper
    return decorate

# 源程序代码函数demo
@param(p_type = "param")
def demo():
    time.sleep(2)
    print("demo函数执行完毕...")
    return "源程序函数demo"
s = demo()
print(s)  # 源程序函数demo

"""
带参数的装饰器有三层:
最外层(第一层)的函数负责接收装饰器参数, 返回的是第二层函数
中间层(第二层)的函数负责接收被装饰的函数, 返回的是第三层函数
最内层(第三层)的函数负责接收被装饰的函数的参数, 执行被装饰的函数
"""

