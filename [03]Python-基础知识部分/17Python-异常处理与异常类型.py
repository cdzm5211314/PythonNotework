# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:09


## 什么是异常: 当检测到一个错误时,解释器就无法继续执行了,反而出现了一些错误的提示信息

## 捕获异常语法: try 尝试捕获异常,将程序转为正常状态并继续执行
# 注: 如果尝试执行的代码的异常与要捕获的异常类型不一致,则无法捕获异常
# 1. try ... except ...
# 2. try ... except ... else ...
# 3. try ... except ... else ... finally ...


## 捕获异常的语法样式:
# try:
#     可能触发异常的代码
# except 异常类型1:  # 捕获单个异常
#     如果出现异常执行的代码1
# 注: 当捕获多个异常时,可以把捕获的异常类型的名字,放到except后,并使用元组的方式进行书写
# except (异常类型2, 错误类型3, ...) [as 异常描述信息变量1]:  # 捕获多个异常,并添加异常描述信息
#     如果出现异常执行的代码2
# except Exception as result:  # 捕获所有异常,Exception是所有程序异常类的父类
#     如果出现异常执行的代码
# ...
# else:
#     如果没有出现异常要执行的代码
# finally:
#     无论是否出现异常都要执行的代码

# 语法说明:
# except    子句,可以有一个或多个,但至少要有一个
# as        子句,异常信息描述,可以省略不写
# else      子句,最多只能有一个,也可以省略不写
# finally   子句,最多只能有一个,也可以省略不写

#############################################################################################

## 自定义异常: 继承Exception
# 抛出自定义异常的语法: raise 异常类对象

class ShortInputException(Exception):

    def __init__(self, length, min_len):
        self.length = length    # 用户输入的密码长度
        self.min_len = min_len  # 系统要求的密码最少长度

    # 设置抛出异常的描述信息
    def __str__(self):
        return f"你输入的长度{self.length},不能少于{self.min_len}个字符"

def main():
    try:
        con = input("请输入密码: ")

        # if len(con) < 6:
        #     raise ShortInputException(len(con), 6)  # 主动抛出异常

        sie = ShortInputException(len(con), 6)
        if len(con) < sie.min_len:
            raise sie  # 抛出异常(异常类对象)

    except Exception as result:  # 捕获异常
        print(result)

main()

#############################################################################################

## raise语句(触发异常): 显示的触发异常,如果执行了raise语句,raise后面的语句将不再执行
# 1. raise: 单独一个raise,该语句引发当前上下文中捕获的异常(比如在except块中),或默认引发RuntimeError异常
# 如: raise
# 2. raise 异常类名称: raise后带一个异常类名称,表示引发执行类型的异常
# 如: raise ZeroDivisionError
# 3. raise 异常类名称(描述信息): 在引发指定类型的异常的同时,附带异常的描述信息
# 如: raise ZeroDivisionError("除数不能为零")


## assert语句(断言语句): 用于判断一个表达式,在表达式条件为False的时候触发异常
# 语法: assert 真值表达式, 错误数据(通常是字符串)
# 等同于:
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


###########################################################################################

## Python的异常类型:
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

