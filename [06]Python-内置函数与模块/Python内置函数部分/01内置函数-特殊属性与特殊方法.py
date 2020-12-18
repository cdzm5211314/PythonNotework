# -*- coding:utf-8 -*-
# @Desc :
# @Author : Administrator


### 判断两个变量是否为同一个对象(引用): is 或 is not
# 语法: x is y        ---> 是同一个对象返回True,不是返回False
# 语法: x is not y    ---> 不是同一个对象返回True,是返回False


### 判断一个变量值是否在序列中: in 或 not in
# 语法: i in l        ---> 在序列中返回True,不存在返回False
# 语法: i not in l    ---> 不在序列中返回True,存在返回False


### 序列对象的相关函数:
## len(seq)	    返回序列的长度
## max(seq)	    返回序列的最大值的元素
## min(seq)	    返回序列的最小值的元素
## sum(seq)	    返回序列中所有元素的和
## any(seq)	    真值测试，如果列表中其中一个值为真值则返回True
## all(seq)	    真值测试，如果列表中所有值为真值则返回True
## reversed(seq) 将序列进行反转
## sorted(seq, key=None, reverse=False)	返回已经经过排序后的新列表
# 注: reverse:排序规则，reverse=True 降序, reverse=False 升序（默认）


## divmod()函数:
# 把除数和余数运算结果结合起来，返回一个包含商和余数的元组(a // b, a % b)
# 示例如下:
# divmod(7, 2)   ---> (3, 1)
# divmod(8, 2)   ---> (4, 0)


### help(): 查看函数帮助  ---> help(abs)


### id(object): 获取对象的内存地址


### type(object): 判断对象的类型
print(type("字符串类型"))
print(type([2,5,8]))

### isinstance(object, classinfo)	 判断object对象是否是已知的classinfo类型,类似 type()
print(isinstance('abc', str))  # True
print(isinstance('abc', (str,int,list)))  # True
## isinstance() 与 type() 区别：
# type() 不会认为子类是一种父类类型，不考虑继承关系。
# isinstance() 会认为子类是一种父类类型，考虑继承关系。

### issubclass(class, classinfo)  判断class类是否是classinfo类的子类
class A:
    pass
class B(A):
    pass
print(issubclass(B, A))


### __file__: 返回当前文件模块的路径
print(__file__)


### __name__: 判断当前运行的是哪个模块(文件)
# 1）当前文件被调用时,__name__的值为当前模块名
# 2）当前文件被执行时,__name__的值为"__main__"
print(__name__)


### dir(object): object ---> 对象、变量、类型   返回值: 返回一个字符串列表
# dir函数作用:
# 1.如果没有参数调用时，则返回当前作用域内的所有变量的列表
# 2.如果给定一个对象作用参数，则返回这个对象的所有变量的列表
# 2.1对于一个模块,返回这个模块的全部变量
# 2.2对于一个类对象，返回类对象的所有变量，并递归的基类对象的所有变量
# 2.3对于其它对象返回所有变量、类变量和基类变量
print(dir())
print(dir(str))


### globals()	返回当前全局作用域内变量的字典
# 可写的,即可修改该字典中的键值,可新增和删除键值对
### locals()	返回当前局部作用域内变量的字典
# 不可写的,即不可修改字典中已存在的键值的,也不能pop移除键值对,但是可以新增键值对


### __doc__: 返回当前模块或类,或函数等的描述信息: """描述信息"""
class Person(object):
    """这是一个类"""
    pass
def func():
    """这是一个函数"""
print(Person().__doc__)
print(func.__doc__)


### __call__(): 装饰器类,把这个类型的对象当作函数来使用,对象后面加括号,触发执行
# 即: 对象() 或者 类()()
class Test():
    def __init__(self, name):
        self.name = name
        print("类中的__init__初始化方法: " + self.name)
    def __call__(self, param):
        print("类中实现__call__方法: " + param)
t = Test("测试")  # 执行__init__方法
t("参数")         # 执行__call__方法


### __iter__(), __next__():  迭代器类
class ClassMate(object):
    def __iter__(self):
        """ 如果想要一个对象成为可迭代对象,即可以使用for语句,那么必须实现__iter__方法 """
        return self
    def __next__(self):
        pass
classMate = ClassMate()
next(classMate)
next(classMate)
for i in classMate:  # 循环获取__next__返回的值
    print(i)




### __new__(): 负责对象的创建

### __init__(): 负责对象的初始化

### __str__(): 可打印的字符输出

### __repr__(): 运行时的字符串输出

### __del__(): 析构方法,当对象在内存中被释放时,自动触发执行




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


