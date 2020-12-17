# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:10

from collections import Iterable, Iterator


## 可迭代对象(Iterable): 可作用于for循环语句的对象叫可迭代对象
# 如: 字符串, 列表, 元组, 字典, 集合, ...

## 迭代器(Iterator)有两个基本方法: iter() 和 next()

## 迭代器(Iterator)说明:
# 迭代器是访问可迭代对象的一种方式
# 使用iter()函数可以返回一个可迭代对象的迭代器,如: iter(str), iter(list), iter(tuple) ...
# 使用next()函数可以获取迭代器的元素,只能向下一直获取元素,直到所有元素被访问完才结束,迭代器只能往前不会后退
# 注: 如果next(迭代器)无法获取下一条记录,则触发StopIteration异常


## 迭代器函数示例:
# iter(iterable)从可迭代对象中返回一个迭代器(iterator),iterable必须是一个能提供迭代器的可迭代对象
L = [2, 3, 5]
it = iter(L)  # L表示:可迭代对象, it表示:迭代器
# 1.使用next()函数获取迭代器元素
# print(next(it))  # 2
# print(next(it))  # 3
# print(next(it))  # 5
# print(next(it))  # 从迭代器中获取元素时,如果无法获取下一条记录,则触发StopIteration异常
# 2.使用for循环语句获取迭代器元素
for temp in it:
    print(temp)

############################################################################################

## 创建类为迭代器:
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()
# 注: __iter__()方法返回一个特殊的迭代器对象,这个迭代器对象实现了__next__()方法并通过 StopIteration 异常标识迭代的完成

# 示例如下:
from collections import Iterable, Iterator

class ClassMate(object):

    def __init__(self):
        self.names = list()
        self.current_num = 0

    def add(self, name):
        self.names.append(name)

    def __iter__(self):
        """ 如果想要一个对象成为可迭代对象,即可以使用for语句,那么必须实现__iter__方法 """
        # 需要返回一个迭代器,迭代器中必须有两个方法: __iter__(), __next__()
        return self

    def __next__(self):
        if self.current_num < len(self.names):
            result = self.names[self.current_num]
            self.current_num += 1
            return result
        else:
            raise StopIteration()

classMate = ClassMate()
classMate.add("张三")
classMate.add("李四")
classMate.add("王五")

print("判断classMate对象是否是可迭代对象:", isinstance(classMate, Iterable))
print("判断classMate对象是否是迭代器:", isinstance(classMate, Iterator))

# 1.使用next()获取迭代器中的元素
# print(next(classMate))
# print(next(classMate))
# print(next(classMate))
# print(next(classMate))

# 2.使用for语句获取迭代器中的元素
for temp in classMate:
    print(temp)

# 迭代器的应用示例: 斐波那契数列
class Fibonacci(object):
    def __init__(self, all_num):
        self.all_num = all_num
        self.current_num = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_num < self.all_num:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_num += 1
            return result
        else:
            raise StopIteration

fibo = Fibonacci(10)
for temp in fibo:
    print(temp)

############################################################################################

### 迭代工具函数: 迭代工具函数的作用是生成一个个性化的可迭代对象
# 如: zip(), enumerate()

## zip()语法: zip(iterable1 [,iterable2, iterable3, ...])
# 作用: 返回一个zip对象,此对象用于生成一个元组,此元组的个数由最小的可迭代对象决定
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

for x in zip(range(10), numbers, names):
    print(x)
# ---> (0, 10086, '中国移动')
# ---> (1, 10000, '中国电信')
# ---> (2, 10010, '中国联通')

## 使用用zip函数对两个可迭代对象生成一个字典
d = dict(zip(names, numbers))  # d = {'中国移动': 10086, '中国电信': 10000, '中国联通': 10010}


## enumerate()语法:  enumerate(iterable[,start])
# 作用: [枚举函数]生成带索引的枚举对象,返回迭代类型为"索引-值"对(index,value)对, 默认索引从零开始,也可以使用start绑定
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


#############################################################################################

### 生成器(generator): 能够动态提供数据的对象,生成器也是特殊的迭代器
# 创建生成器有两种: 生成器表达式 和 生成器函数

## 一.生成器表达式: (表达式 for 变量　in 可迭代对象 [if 真值表达式])
# 作用: 用推导式的形式生成一个新的生成器对象
# 示例如下:
gen = (x**2 for x in range(1, 4))
print(gen)  # <generator object <genexpr> at 0x00000000029FB0A0>
# 1.使用next()方法获取生成器数据
# 注: 当使用next()函数获取完数据,会触发StopIteration异常来通知next()函数不再能提供数据
print(next(gen))  # 1
print(next(gen))  # 4
print(next(gen))  # 9
print(next(gen))  # StopIteration
# 2.使用for循环语句获取生成器数据
for temp in gen:
    print(temp)  # 1 4 9


## 二.生成器函数: 含有yield关键字的函数就是生成器函数,此函数被调用时将返回一个生成器对象
# 注: 生成器对象也就是迭代器对象
# 注: yield关键字用于def函数中,目的是将此函数作为生成器函数使用,yield用来生成数据,供next(it)函数使用

# 示例如下:
def create_fibo_num(all_num):
    """ 生成器函数 """
    current_num = 0
    a, b = 0, 1
    while current_num < all_num:
        # 如果函数使用了yeild关键字,那么这个函数就不在是普通的函数,而已一个生成器的模版(生成器函数)
        yield a
        a, b = b, a + b
        current_num += 1

# 如果调用一个函数的时候,发现此函数中有yeild关键字,那么就不是简单的调用函数,而是创建一个生成器对象
obj = create_fibo_num(10)

# 1.使用next()方法获取生成器数据
# 注: 当使用next()函数获取完数据,会触发StopIteration异常来通知next()函数不再能提供数据
print(next(obj))
print(next(obj))
print(next(obj))

# 2.使用for循环语句获取生成器数据
for temp in obj:
    print(temp)


## 通过send()函数来启动生成器
# 注: 第一次调用传值send(None)
def myList(num):
    now = 0  # 当前迭代值，初始为0
    while now < num:
        val = yield now  # 返回当前迭代值,并接受可能的send发送值
        now = now + 1 if val is None else val  # val为None,迭代值自增1,否则重新设定当前迭代值为val

my_list = myList(5)  # 得到一个生成器对象
# my_list.send(None)   # send()函数一般不会放到第一次启动生成器,如果非要放在第一次,那么就需要传递None
print(my_list.next())  # 返回当前迭代值
print(my_list.next())
my_list.send(3)        # 重新设定当前的迭代值
print(my_list.next())


