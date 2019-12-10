# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:09


## 什么是错误: 错误是指由于逻辑或语法等导致一个程序无法正常执行的问题

## 什么是异常:
# 异常是程序出错时标识的一种状态
# 当异常发生时，程序不会再向下执行，而转去调用此函数的地方待处理此错误并恢复为正常状态

## try 语句的两种语法: try - except 与 try - finally
# try - except语句: 作用 ---> 尝试捕获异常,将程序转为正常状态并继续执行
# try - except语法：
# try:
#     可能触发异常的语句
# except 错误类型1 [as 变量1]:
#     异常处理语句1
# except 错误类型2 [as 变量2]:
#     异常处理语句2
# except (错误类型3, 错误类型4, ...) [as 变量3]:
#     异常处理语句3
# ...
# except:
#     异常处理语句other
# else:
#     末发生异常时执行的语句
# finally:
#     最终执行语句

# 语法说明:
# as        子句是用于绑定错误对象的变量，可以省略不写
# except    子句可以有一个或多个，但至少要有一个
# else      子句最多只能有一个，也可以省略不写
# finally   子句最多只能有一个，也可以省略不写

# try - finally语句: 作用 ---> 通常用try-finally语句来做触发异常时必须要处理的事情,无论异常是否发生，finally子句都会被执行
# 注:try - finally语句不会改变程序的(正常/异常)状态
# try - finally语法:
# try:
#     可能触发异常的语句
# finally:
#     最终语句
# 说明: finally 子句不可以省略,一定不存在except子句



## raise 语句: 作用 ---> 触发一个错误,让程序进入异常状态
# 语法一: raise 异常类型
# 语法二: raise 异常对象


## assert 语句(断言语句): 作用 ---> 当真值表达式为False时,用错误数据创建一个 AssertionError 类型的错误,并进入异常状态
# 语法: assert 真值表达式, 错误数据(通常是字符串)
# 类似于:
# if 真值表达式 == False:
#     raise AssertionError(错误数据)
# assert语句示例如下:
def get_age():
    a = int(input("请输入年龄: "))
    # 以下语句会在a不在 [0,140]时触发AssertionError错误
    assert 0 <= a <= 140, '年龄不在合法的范围内'
    return a
try:
    age = get_age()
except AssertionError as e:
    print("错误原因是:", e)  # 错误原因是: 年龄不在合法的范围内
    age = 0
print("年龄是:", age)


## 异常小结:
# 接收错误消息语句:
# try - except
# 做必须要处理的事情的语句:
# try - finally
# 发错误消息的语句:
# raise  语句
# assert 语句



### Python的异常类型:
#   错误类型	            说明
# ZeroDivisionError	    除(或取模)零 (所有数据类型)
# ValueError	        传入无效的参数
# AssertionError	    断言语句失败
# StopIteration	        迭代器没有更多的值
# IndexError	        序列中没有此索引(index)
# IndentationError	    缩进错误
# OSError	            输入/输出操作失败
# ImportError	        导入模块/对象失败
# NameError	            未声明/初始化对象 (没有属性)
# AttributeError	    对象没有这个属性
# BaseException	        所有异常的基类
# SystemExit	        解释器请求退出
# KeyboardInterrupt	    用户中断执行(通常是输入^C)
# Exception	            常规错误的基类
# GeneratorExit	        生成器(generator)发生异常来通知退出
# StandardError	        所有的内建标准异常的基类
# ArithmeticError	    所有数值计算错误的基类
# FloatingPointError	浮点计算错误
# OverflowError	        数值运算超出最大限制
# EOFError	            没有内建输入,到达EOF 标记
# EnvironmentError	    操作系统错误的基类
# OSError	            操作系统错误
# WindowsError	        系统调用失败
# LookupError	        无效数据查询的基类
# KeyError	            映射中没有这个键
# MemoryError	        内存溢出错误(对于Python 解释器不是致命的)
# UnboundLocalError	    访问未初始化的本地变量
# ReferenceError	    弱引用(Weak reference)试图访问已经垃圾回收了的对象
# RuntimeError	        一般的运行时错误
# NotImplementedError	尚未实现的方法
# SyntaxError Python	语法错误
# TabError	            Tab和空格混用
# SystemError	        一般的解释器系统错误
# TypeError	            对类型无效的操作
# UnicodeError	        Unicode 相关的错误
# UnicodeDecodeError	Unicode 解码时的错误
# UnicodeEncodeError	Unicode 编码时错误
# UnicodeTranslateError	Unicode 转换时错误

## 以下为警告类型
# Warning	                    警告的基类
# DeprecationWarning	        关于被弃用的特征的警告
# FutureWarning	                关于构造将来语义会有改变的警告
# OverflowWarning	            旧的关于自动提升为长整型(long)的警告
# PendingDeprecationWarning	    关于特性将会被废弃的警告
# RuntimeWarning	            可疑的运行时行为(runtime behavior)的警告
# SyntaxWarning	                可疑的语法的警告
# UserWarning	                用户代码生成的警告

