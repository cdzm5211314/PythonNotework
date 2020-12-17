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
# def func(n):
#     print("递归进入第", n, "层")
#     if n == 3:
#         return
#     func(n + 1)
#     print("递归退出第", n, '层')
# func(1)
# print("程序结束")


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

## 高阶函数需满足下列任意条件:
# 1.函数的参数接受一个或多个函数名作为实参
# 2.函数的返回值为一个函数的函数名
## 示例如下:
# 普通函数
# def func1():
#     print("func1 函数...")
# 高阶函数
# def func(func1):
#     return func1
# res = func(func1)  # ---> 调用func函数,返回一个函数名为func1的内存地址
# print(res)  # 返回一个函数的内存地址
# res()  # ---> 实际是调用func1函数

# ----------------------------------------------------------------------------------------- #

## 函数的闭包必须满足3个条件:
# 1.外部函数中定义了内部函数
# 2.外部函数必须有返回值且返回的是内部函数的函数名
# 3.内部函数必须引用外部函数中的变量
# 闭包示例如下:
def func(var):
    def test(args):
        return args ** var
    return test
res = func(3)  # ---> 调用func函数,并把实参3传递给var变量,返回一个函数名为test的内存地址,即res=test
res2 = res(2)  # ---> 实际为调用test函数,并把实参2传递给args变量,返回一个运算结果,即 res2 = args ** var
print(res2)
res3 = func(2)(5)
print(res3)

print(" ----- 闭包函数的特点(好处)演示 ----- begin ")
def wrapper_func(a, b):
    c = 10
    def inner_func():
        result = a + b + c
        print("a + b + c = " + str(result))
    return inner_func

ifunc = wrapper_func(3, 5)  # 第一次调用外层函数并传值
ifunc1 = wrapper_func(7, 9)  # 第二次调用外层函数并传值
ifunc1()  # 调用 第二次调用外层函数 返回的函数
ifunc()  # 调用 第一次调用外层函数 返回的函数

print(" ----- 闭包函数的特点(好处)演示 ----- end ")

# ----------------------------------------------------------------------------------------- #

### 装饰器(decorators):
# 函数装饰器是指装饰的是一个函数,传入的是一个函数名,返回的也是一个函数的函数名
## 装饰器原则：
# 1.不修改被修饰函数的源代码
# 2.不修改被修饰函数的调用方式
# 3.满足1,2的情况下给程序增加功能

## 装饰器实现：装饰器 = 高阶函数 + 闭包

# 注: 多层装饰器,首先执行离被装饰函数最近的那个装饰器函数

"""
# 装饰器函数
def decorate(func):
    print("decorate被执行...1...")
    def wrapper():
        print("wrapper被执行...3...")
        func()
        print("wrapper被执行...5...")
    print("decorate被执行...2...")
    return wrapper

# 被装饰的函数    
@decorate
def demo():
    print("被装饰函数demo...4...")

# 调用被装饰的函数    
demo()

## 函数的执行顺序
1. Python解释器从上往下执行程序,此示例先加载函数
2. 当出现@decorate时,Python解释器底层就会执行装饰器函数(decorate)
3. 将被装饰函数(demo)作为参数传递给装饰器函数(decorate)的形参(func) ---> func = demo
4. 装饰器函数返回内部函数名(wrapper) ---> demo = wrapper
5. 当调用demo()函数,实际上调用的是wrapper()
"""

## 示例如下:

import time
from functools import wraps

def decorate(fn):
    @wraps(fn)  # 还原被装饰器修改的原函数属性
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
"""
带参数的装饰器有三层:
最外层(第一层)的函数负责接收装饰器参数, 返回的是第二层函数
中间层(第二层)的函数负责接收被装饰的函数, 返回的是第三层函数
最内层(第三层)的函数负责接收被装饰的函数的参数, 执行被装饰的函数
"""
## 装饰器示例如下: 被装饰函数 - 无参数,无返回值
# 定义装饰器：功能 - 查看函数demo的运行时间
# 装饰器函数: 无参数
def decorate(func):
    def wrapper():
        import time
        start_time = time.time()
        func()
        stop_time = time.time()
        print("被装饰函数'demo'运行时间：%s" % (stop_time - start_time))
    return wrapper

# 被装饰的函数
@decorate  # 相当于: demo = decorate(demo) 即 demo = wrapper
def demo():
    for i in range(100000):
        pass
    print("被装饰函数'demo'执行完毕...")

# 调用被装饰的函数
demo()


## 装饰器示例如下: 被装饰函数 - 有参数,无返回值
# 定义装饰器：功能 - 查看函数demo的运行时间
# 装饰器函数: 无参数
def decorate(func):
    def wrapper(x, y):
        print("装饰器参数: [x = %s], [y = %s]" %(x, y))
        start_time = time.time()
        func(x, y)
        stop_time = time.time()
        print("被装饰函数'demo'运行时间：%s" % (stop_time - start_time))
    return wrapper

# 被装饰的函数
@decorate  # 相当于: demo = decorate(demo) 即 demo = wrapper
def demo(a, b):
    for i in range(100000):
        pass
    print("被装饰函数'demo'执行完毕... %s" %(a + b))

# 调用被装饰的函数
demo(2, 5)


## 装饰器示例如下: 被装饰函数 - 不定长参数,无返回值
# 定义装饰器：功能 - 查看函数demo的运行时间
# 装饰器函数: 无参数
def decorate(func):
    def wrapper(*args, **kwargs):
        print("装饰器参数: [x = %s], [y = %s]" %(args, kwargs))
        start_time = time.time()
        # func(args, kwargs)  # 错误:相当于传递两个参数,一个元组,一个字典
        func(*args, **kwargs)  # 对传递的参数进行拆包
        stop_time = time.time()
        print("被装饰函数'demo'运行时间：%s" % (stop_time - start_time))
    return wrapper

# 被装饰的函数
@decorate  # 相当于: demo = decorate(demo) 即 demo = wrapper
def demo(*args, **kwargs):
    for i in range(100000):
        pass
    print("被装饰函数'demo'元组参数: ", args)
    print("被装饰函数'demo'字典参数: ", kwargs)
    print("被装饰函数'demo'执行完毕...")

# 调用被装饰的函数
demo(2, 3, name="张三", age=18)


## 装饰器示例如下: 被装饰函数 - 不定长参数,有返回值
# 定义装饰器：功能 - 查看函数demo的运行时间
# 装饰器函数: 无参数
def decorate(func):
    def wrapper(*args, **kwargs):
        print("装饰器参数: [x = %s], [y = %s]" %(args, kwargs))
        start_time = time.time()
        # func(args, kwargs)  # 错误:相当于传递两个参数,一个元组,一个字典
        result = func(*args, **kwargs)  # 对传递的参数进行拆包
        stop_time = time.time()
        print("被装饰函数'demo'运行时间：%s" % (stop_time - start_time))
        return result
    return wrapper

# 被装饰的函数
@decorate  # 相当于: demo = decorate(demo) 即 demo = wrapper
def demo(*args, **kwargs):
    for i in range(100000):
        pass
    print("被装饰函数'demo'元组参数: ", args)
    print("被装饰函数'demo'字典参数: ", kwargs)
    print("被装饰函数'demo'执行完毕...")
    return "success"

# 调用被装饰的函数
result = demo(2, 3, name="张三", age=18)
print(result)


## 装饰器示例如下: 被装饰函数 - 不定长参数,有返回值
# 定义装饰器：功能 - 查看函数demo的运行时间
# 装饰器函数: 带参数
# 注: 需要在装饰器函数外面新建一个函数,用来接收装饰器参数
def param_func(param):
    def decorate(func):
        def wrapper(*args, **kwargs):
            if param == "china":
                print("你好")
            elif param == "america":
                print("hello")
            else:
                return
            # return func(args, kwargs)  # 错误:相当于传递两个参数,一个元组,一个字典
            return func(*args, **kwargs)  # 对传递的参数进行拆包
        return wrapper
    return decorate

# 被装饰的函数
@param_func("china")
def demo1(*args, **kwargs):
    print("被装饰函数'demo1': 我来自中国")

# 被装饰的函数
@param_func("america")
def demo2(*args, **kwargs):
    print("被装饰函数'demo2': I am from America")

# 调用被装饰的函数
demo1()
print("*" * 30)
demo2()

## 注: 多个装饰器对同一个函数进行装饰时,最上方装饰器最后执行


############################################################################################
## 类装饰器
class Test():

    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        print("装饰器添加的额外功能...")
        return self.func()

# 被装饰的函数
@Test  # 相当于: demo = Test(demo) 即 Test()
def demo():
    print("被装饰函数'demo'执行完毕...")
    return "success"

# 调用被装饰的函数
result = demo()
print(result)


