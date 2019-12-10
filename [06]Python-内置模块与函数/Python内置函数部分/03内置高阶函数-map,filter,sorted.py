# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:46



## 高阶函数: ★★★
# map(func, *iterables)
# map作用: 用函数和对可迭代对象中的每一个元素作为参数计算出新的可迭代对象,当最短的一个可迭代对象不再提供数据时此可迭代对象生成结束
# 示例一如下:
def func(x):
    return x ** 2
for x in map(func, range(1, 10)):  # rang(1,10) ---> 1 2 3 4 5 6 7 8 9
    print(x)  # 1 ** 2, 2 ** 2, 3 ** 2, ..., 9 ** 2
# 示例二如下:
# Python内建函数: pow(x, y, z = None) ---> x ** y
for x in map(pow, range(1, 5), range(4,0,-1)):  # range(1, 10) ---> 1,2,3,4,5,6,7,8,9   range(4,0,-1) ---> 4,3,2,1
    print(x)  # 1 ** 4, 2 ** 3, 3 ** 2, 4 ** 1
for x in map(pow, [2,3,5,7], [4,3,2,1], range(5, 10)):
    print(x)  # 2 ** 4 % 5, 3 ** 3 % 6, 5 ** 2 % 7, 7 ** 1 % 8

# filter(function, iterable)
# filter作用: 筛选可迭代对象iterable中的数据,返回一个可迭代器对象，此可迭代对象将对iterable进行筛选
# filter说明: 函数function 将对iterable中的每个元素进行求值，返回False则将此数据丢弃，返回True，则保留此数据
# 示例一如下:
def isodd(x):  # 此函数判断x是否为奇数
    return x % 2 == 1
for x in filter(isodd, range(10)):
    print(x)  #
# 示例二如下:
even = [x for x in filter(lambda x: x % 2 == 0, range(10))]

# sorted(iterable, key=None, reverse=False)
# sorted作用: 将原可迭代对象的数据进行排序，生成排序后的列表iterable 可迭代对象key 函数是用来提供一个值,这个值将作为排序的依据reverse 标志用来设置是否降序排序
# sorted说明: iterable 可迭代对象, key 函数是用来提供一个参考值，这个值将作为排序的依据 ,reverse 标志用来设置是否降序排序
# 示例如下:
L = [5, -2, -4, 0, 3, 1]
L1 = sorted(L)                # [-4, -2, 0, 1, 3, 5]
L2 = sorted(L, reverse=True)  # [5, 3, 1, 0, -2, -4]
L3 = sorted(L, key=abs)       # [0, 1, -2, 3, -4, 5]

