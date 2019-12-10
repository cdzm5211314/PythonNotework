# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-02 17:22

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
# 4.lambda 比函数简单，且可以随时创建和销毁，有利于减少程序的偶合度



## help(): 查看函数帮助  ---> help(abs)



## 序列相关函数: ★
# len(seq)	    返回序列的长度
# max(x)	    返回序列的最大值的元素
# min(x)	    返回序列的最小值的元素
# sum(x)	    返回序列中所有元素的和
# any(x)	    真值测试，如果列表中其中一个值为真值则返回True
# all(x)	    真值测试，如果列表中所有值为真值则返回True
# reversed(seq)	返回反向顺序的迭代器对象
# sorted(iterable, key=None, reverse=False)	返回已排序的列表

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



## 迭代器函数iter和next:
# iter(iterable) 从可迭代对象中返回一个迭代器,iterable必须是能提供一个迭代器的对象
# next(iterator) 从迭代器iterator中获取一下个记录，如果无法获取一下条记录，则触发 StopIteration 异常


## 迭代工具函数: ★★★
# zip(iter1 [,iter2, iter3,...]) 返回一个zip对象此对象用于生成一个元组，此元组的个数由最小的可迭代对象决定
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
## 以下用zip函数生成一个字典
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

## 对象的属性管理函数: ★★
# getattr(obj, name[, default])	从一个对象得到对象的属性；getattr(x, 'y') 等同于x.y; 当属性不存在时,如果给出default参数,则返回default,如果没有给出default 则产生一个AttributeError错误
# hasattr(obj, name)	        用给定的name返回对象obj是否有此属性,此种做法可以避免在getattr(obj, name)时引发错误
# setattr(obj, name, value)	    给对象obj的名为name的属性设置相应的值value, set(x, 'y', v) 等同于 x.y = v
# delattr(obj, name)	        删除对象obj中的name属性, delattr(x, 'y') 等同于 del x.y


## eval(), exec() 函数:
# eval(source, globals=None, locals=None)	把一个字符串source当成一个表达式来执行，返回表达式执行后的结果
# 示例如下:
x = 100
y = 200
a = eval('x+y')
print(a)
# exec(source, globals=None, locals=None)	把一个字符串source当成程序来执行．
# 示例如下:
x = 100
y = 200
s = 'z = x+y; print(z); del z; print("删除成功")'
exec(s)  # 执行s绑定的语句
# 注: eval() 和 exec()的两个参数globals 和 locals 是用来设置'表达式'或'程序'运行的全局变量和局部变量



## globals() / locals() 函数:
# globals()	返回当前全局作用域内变量的字典
# locals()	返回当前局部作用域内变量的字典


## dir函数: dir([对象]) ---> 返回一个字符串列表
# dir函数作用:
# 1.如果没有参数调用，则返回当前作用域内的所有变量的列表
# 2.如果给定一个对象作用参数，则返回这个对象的所有变量的列表
# 2.1对于一个模块,返回这个模块的全部变量
# 2.2对于一个类对象，返回类对象的所有变量，并递归的基类对象的所有变量
# 2.3对于其它对象返回所有变量、类变量和基类变量



## 字节串的生成函数bytes:
# bytes()	                        生成一个空的字节串 等同于 b''
# bytes(整型可迭代对象)	            用可迭代对象初始化一个字节串
# bytes(整数n)	                    生成n个值为0的字节串
# bytes(字符串, encoding='utf-8')	用字符串的转换编码生成一个字节串



## 字节数组的生成函数bytearray:
# bytearray()	                        创建空的字节数组
# bytearray(整数)	                    用可迭代对象初始化一个字节数组
# bytearray(整型可迭代对象)	            生成n个值为0的字节数组
# bytearray(字符串, encoding='utf-8')	用字符串的转换编码生成一个字节数组



## 用于类型判断的函数:
# isinstance(obj, class_or_tuple)	返回这个对象obj 是否是 某个类的对象,或者某些类中的一个类的对象,如果是返回True,否则返回False
# type(obj)	返回对象的类型



## super函数:
# super(type, obj)	返回绑定超类的实例(要求obj必须为type类型的实例)
# super()	        返回绑定超类的实例,等同于:super(class, 实例方法的第一个参数)，必须用在方法内



## 用于类的函数:
# issubclass(cls, class_or_tuple)	判断一个类是否继承自其它的类,如果此类cls是class 或tuple中的一个派生子类则返回True,否则返回False


## divmod()函数:
# 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
# 示例如下:
# divmod(7, 2)   ---> (3, 1)
# divmod(8, 2)   ---> (4, 0)