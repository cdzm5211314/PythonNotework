# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:45


## lambda表达式: 即匿名函数,作用等同于def定义的函数
# 语法: lambda [参数1, 参数2, ...]: 表达式  ---> [] 里的内容可以省略
# 注: lambda返回值是一个函数的地址,也就是函数对象
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


### lambda 函数的参数形式:
## 1.无参数:
fn = lambda: 100
print(fn())

## 2.一个参数:
fn = lambda a: a
print(fn("Hello"))

## 3.默认参数:
fn = lambda a, b, c=100: a + b + c
print(fn(10,50))
print(fn(10,50,80))

## 4.可变参数(*args和**kwargs):
fn = lambda *args: args
print(fn(2,4,6))  # (2, 4, 6)
fn = lambda **kwargs: kwargs
print(fn(name="Tom", age=5))  # {'name': 'Tom', 'age': 5}

## 5.带判断的lambda函数
fn = lambda a, b: a if a>b else b
print(fn(3,5))  # 5
print(fn(8,6))  # 8


## 列表数据按字典key的值进行排序
stu = [
    {"name":"Tom", "age":12},
    {"name":"Jack", "age": 22},
    {"name":"Rose", "age":18},
]
# 按name值升序排序
stu.sort(key=lambda x: x["name"])
print(stu)
# [{'name': 'Jack', 'age': 22}, {'name': 'Rose', 'age': 18}, {'name': 'Tom', 'age': 12}]
# 按name值降序排序
stu.sort(key=lambda x: x["name"], reverse=True)
print(stu)
# [{'name': 'Tom', 'age': 12}, {'name': 'Rose', 'age': 18}, {'name': 'Jack', 'age': 22}]

