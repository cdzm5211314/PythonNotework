# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:45


## lambda表达式(又称匿名函数): ★★
# 作用: 创建一个匿名函数对象,同 def 类似，但不提供函数名
# 语法: lambda [参数1, 参数2, ...]: 表达式  ---> [] 里的内容可以省略
# 示例如下:
def func(x, y):
    return x + y
print('2 + 3 =', func(2, 3))
# 以上func函数可以改写为:
func2 = lambda x, y: x + y
print('2 + 3 =', func2(2, 3))
# 语法说明:
# 1.lambda 只是一个表达式，它用来创建一个函数对象
# 2.当lambda表达式调用时，先执行冒号后(:)的表达式，并返回表达式的结果的引用
# 3.lambda 表达式创建的函数只能包含一条"表达式"

