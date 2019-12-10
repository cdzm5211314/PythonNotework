# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:10


### 迭代器(iterator):
# 迭代器是指用 iter(可迭代对象) 函数返回的对象(实例)
# 迭代器可以用 next(迭代器) 函数获取可迭代对象的数据

## 迭代器说明:
# 迭代器是访问可迭代对象的一种方式
# 迭代器只能向前取值,不会后退
# 用iter()函数可以返回一个可迭代对象的迭代器

## 迭代器的用途: 迭代器对象能用next()函数获取下一个元素

### 迭代器函数:
## iter(iterable)从可迭代对象中返回一个迭代器(iterator),iterable必须是一个能提供迭代器的可迭代对象
# 示例如下:
L = [2, 3, 5, 7]
it = iter(L)  # L表示可迭代对象, it表示迭代器
## next(iterator)从迭代器(iterator)中获取下一条记录,如果无法获取下一条记录,则触发StopIteration异常
# 示例如下:
res = next(it)
print(res) # res就是从迭代器中获取到的数据


### 迭代工具函数: 迭代工具函数的作用是生成一个个性化的可迭代对象
## 函数:
# zip(iter1 [,iter2, iter3,...])   返回一个zip对象,此对象用于生成一个元组，此元组的个数由最小的可迭代对象决定
# 示例如下:
numbers = [10086, 10000, 10010, 95588]
names = ['中国移动', '中国电信', '中国联通']
for n, a in zip(numbers, names):
    print(a, '的客服号码是:', n)
# ---> 中国移动 的客服号码是: 10086
# ---> 中国电信 的客服号码是: 10000
# ---> 中国联通 的客服号码是: 10010

for x in zip(numbers, names):
    print(x)
# ---> (10086, '中国移动')
# ---> (10000, '中国电信')
# ---> (10010, '中国联通')

# 以下用zip函数生成一个字典
d = dict(zip(names, numbers))  # d = {'中国移动': 10086, '中国电信': 10000, '中国联通': 10010}

for x in zip(range(10), numbers, names):
    print(x)
# ---> (0, 10086, '中国移动')
# ---> (1, 10000, '中国电信')
# ---> (2, 10010, '中国联通')

# enumerate(iterable[,start])    [枚举函数]生成带索引的枚举对象，返回迭代类型为索引-值对(index,value)对, 默认索引从零开始,也可以使用start绑定
# 示例如下:
names = ['中国移动', '中国电信', '中国联通']
for x in enumerate(names):
    print(x)
# ---> (0, '中国移动')
# ---> (1, '中国电信')

for x in enumerate(names, start=100):
    print(x)
# ---> (100, '中国移动')
# ---> (101, '中国电信')
# ---> (102, '中国联通')


# ****************************************************************************************** #

### 生成器(generator): 能够动态提供数据的对象,生成器对象也是可迭代对象(实例)
# 生成器有两种: 生成器函数 和 生成器表达式
# 生成器方法:
# 1. __next__(): 获取下一个元素
# 2. send(value): 向每次生成器调用中传值,注意:第一次调用send(None),

## 一,生成器函数:
# 含有 yield 语句的函数是生成器函数，此函数被调用时将返回 一个生成器对象
# 注: yield 翻译为产生（或生成)

## yield 语句: yield 表达式
# yield 语句说明:
# yield用于def函数中，目的是将此函数作为生成器函数使用
# yield用来生成数据，供迭代器 next(it) 函数使用
# 示例如下:
def myYield():
    """生成器函数"""
    yield 2  # 生成2
    yield 3  # 生成3
    yield 5  # 生成5
for x in myYield():
    print(x)  # 分别打印: 2 3 5
# 或使用迭代器函数:如
it = iter(myYield())  # 转换为迭代器
print(next(it))  # 2
print(next(it))  # 3
print(next(it))  # 5
print(next(it))  # StopIteration


# 生成器函数说明:
# 生成器函数的调用将返回一个生成器对象，生成器对象是一个可迭代对象
# 在生成器函数调用return时会出生一个StopIteration异常来通知next(it) 函数不再能提供数据



## 二,生成器表达式: ( 表达式 for 变量　in 可迭代对象 [if 真值表达式] )
# 注: []里的内容可以省略
# 作用: 用推导式的形式生成一个新的生成器
# 示例如下:
gen = (x**2 for x in range(1, 4))
print(gen)
it = iter(gen)  # 转换为迭代器
next(it)    # 1
next(it)    # 4
next(it)    # 9
next(it)    # StopIteration




