# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 9:17

## 全局变量
# 定义在函数外部，模块内部的变量称为全局变量
# 全局变量，所有的函数都可以直接访问（但函数内部不能将其直接赋值)

## 局部变量:
# 定义在函数内部的变量称为局部变量(函数的形参也是局部变量)
# 局部变量只能在函数内部使用
# 局部变量在函数调用时才能够被创建，在函数调用之后会自动销毁


# 局部变量说明:
# 1.在函数内首次对变量赋值是创建局部变量,再次为变量赋值是修改局部变量的绑定关系
# 2.在函数内部的赋值语句不会对全局变量造成影响
# 3.局部变量只能在其被声明的函数内部访问，而全局变量可以在整个模块范围内访问


## globals 和 locals 函数
# globals()  返回当前全局作用域内变量的字典
# locals()  返回当前局部作用域内为量的字典


## 函数变量: 函数名是变量，它在创建函数时绑定一个函数
# 示例如下:
def f1():
    print("f1被调用")
fx = f1
fx()  # 等同于 f1()

## 一个函数可以作为另一个函数的参数传递
# 示例如下:
def f1():
    print("hello")
def f2():
    print('world')
def fx(fn):
    print(fn)  # fn是一个函数对象的地址
    fn()  # 调用谁?  ---> 哪个函数作为参数传递进来就调用哪个函数
fx(f1)    # 此语句在做什么？ ---> 调用fx函数,并把f1函数作为参数传递进去
fx(f2)

## 函数可以返回另一个函数(即:另一个函数可以返回一个函数)


## Python的四个作用域:
# 局部作用域                       Local function             L
# 外部嵌套函数作用域                Enclosing Function Locals   E
# 函数定义所在模块(文件)的作用域      Global(Mudule)              G
# Python内置模块的作用域            Builtin(python)             B

# 变量名的查找规则: L --> E  --> G  --> B
# 注: 在默认情况下，对变量名赋值会创建或改变本作用域内的变量


## global 语句:
# 作用:
# 1.告诉解释器, global语句声明的一个或多个变量，这些变量的作用域为模块级的作用域，也称作全局变量
# 2.全局声明(global)将赋值变量映身到模块文内部的作用域
# 语法: global 变量1, 变量2, ...
# 示例如下:
v = 100
def fn():
    global v
    v = 200
fn()
print(v)  # 200

# global语句说明:
# 1.全局变量如果要在函数内部被赋值，则必须经过全局声明（否则会被认为是局部变量)
# 2.全局变量在函数内部不经过声明就可以直接访问
# 3.不能先声明局部的变量，再用global声明为全局变量，此做法不附合规则
# 4.global 变量列表里的变量不能出现在此作用域内的形参列表里


## nonlocal 语句:
# 作用: 告诉解释器,　nonlocal声明的变量不是局部变量，也不是全局变量，而是外部嵌套函数内的变量
# 语法: nonlocal 变量名1, 变量名2, ...

# nonlocal语句说明:
# 1.nonlocal语句只能在被嵌套函数内部进行使用
# 2.访问nonlocal变量将对外部嵌套函数的作用域的变量进行操作
# 3.当有两层或两层以上的函数嵌套时，访问nonlocal变量只对最近一层的变量进行操作
# 4.nonlocal语句的变量列表里的变量名，不能出现在此函数的参数列表中



