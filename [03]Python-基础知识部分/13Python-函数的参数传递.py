# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 9:11


### 函数的参数传递顺序: 位置参数 -> 默认参数 -> 可变参数(*args) -> 命名关键字参数 -> 关键字参数(**kwargs)
# 位置参数也为必选参数
# 默认参数也叫缺省参数(如果一个函数有缺省参数,则其右侧的所有参数都必须有缺省参数)

## 注: Python2与Python3中: 默认参数与可变参数的位置区别
# Python2: 默认参数必须在可变参数(*args)之前
# Python3: 可变参数(*args)之前也可以在默认参数之前,谁在前谁优先拿到值


########################################################################################
## 位置参数说明:
# 1. 实际参数和形式参数通过位置进行传递的匹配
# 2. 实参个数必须与形参个数相同
# 示例如下:
print(" -------------> 位置参数(即必选参数)...")
def func01(a, b, c):
    print("位置参数: ", a, b, c)

func01(1, 2, 3)  # 位置传参
func01(*[4, 5, 6])  # 序列传参,*表示把序列拆包

########################################################################################
## 默认参数说明:
# 注: 默认参数必须指向不可变对象(也可理解为是位置参数), 如 str None ...
# 1. 函数定义的时候给参数设置默认值
# 2. 默认参数必须定义在位置参数的后面
# 3. 当有多个默认参数的时候,可以不按照默认参数的定义顺序传值,但必须以默认参数名称传值
# 示例如下:
print(" -------------> 默认参数(即默认值参数)...")
def func02(a, b=2, c=3):
    print("位置参数: ", a, b, c)

func02(1)
func02(1, c=111)
func02(10, 20, 30)
func02(100, c=300, b=200)

########################################################################################
## 可变参数说明:
# 1.可变参数接受0-n个参数
# 2.必须定义在默认参数的后面
# 3.可变参数会自动组成一个元组tuple
# 示例如下:
print(" -------------> *args 可变参数...")
def func03(*args):
    print("可变参数: ", args)
    # print("可变参数: ", *args)

func03()
func03(1, 2, 3, 4, 5)
func03(*[1, 2, 3, 4, 5])


########################################################################################
## 命名关键字参数:
# 命名关键字参数必须定义在可变参数后面
## 字典关键字参数: 是指实参为字典，将字典用 ** 拆解后进行关键字传参
# 1.字典的键名和形参名必须一致
# 2.字典键名必须为字符串
# 3.字典的键名要在形参中存在
# 示例如下:
print(" -------------> 命名关键字参数 与 字典关键字参数 ...")
def func04(name, age):
    print("命名(字典)关键字参数: ", name, age)

func04(age=20, name="zhangsan")
func04(**{"age":20, "name":"zhangsan"})


########################################################################################
## 关键字参数说明:
# 1.关键字参数接受0-n个参数
# 2.关键字参数必须定义在命名关键字参数后面
# 2.关键字参数传参时，参数名称必须与形参的名称一致
# 3.关键字参数会自动组装成为一个字典dict
# 示例如下:
print(" -------------> **kwargs 关键字参数...")
def func05(**kwargs):
    print("关键字参数: ", kwargs)
    # print("关键字参数: ", **kwargs)  # **kwargs不支持打印输出

func05()
func05(name="chen", city="beijing", age=21)
func05(**{"name": "dong", "city": "zhengzhou", "age": 25})


########################################################################################
print(" -------------> *args(可变参数) 与 **kwargs(关键字参数)...")
def func06(*args, **kwargs):
    print("可变参数: ", args)
    print("关键字参数: ", kwargs)

# 注: 可变参数与关键字参数可传,可不传
func06()
func06("a", "b", "c", name="chen", age=30, city="郑州")
func06(*["aa","bb","cc"],**{"name":"dong","city":"北京"})


########################################################################################
# 位置形参:
# 语法: def 函数名(形参名1, 形参名2, ...):

# 默认形参:
# 语法: def 函数名(形参名1=值1, 形参名2=值2, ...):

# 可变形参: 收集多个的位置传参
# 语法: def 函数名(*args):

# 命名关键字形参: 所有的参数都必须用关键字传参或字典关键字传参传递
# 语法: def 函数名(命名关键字参名1, 命名关键字参名2, ...):

# 关键字形参: 收集多个的关键字传参
# 语法: def 函数名(**kwargs):

print(" -------------> 函数参数位置的混合使用 ...")
def func(a, b, c=30, d=40, *args, name, age, **kwargs):  # Python2 Python3
# def func000(a, b, *args, c=30, d=40, name, age, **kwargs):  # Python3
    print("位置参数: ", a, b)  # 10 20
    print("默认参数: ", c, d)  # 300 400
    print("可变参数: ", args)  # (500, 600, 'aa', 'bb')
    print("命名关键字参数: ", name, age)  # chen 21
    print("关键字参数: ", kwargs)  # {'city': 'beijing'}


# func(10, 20, 400, 500, 600, "aa", "bb", name="chen", age=21, city="beijing")
# func(10, 20, 300, 400, *[500, 600, "aa", "bb"], name="chen", age=21, **{"city":"beijing"})
# func(10, 20, name="chen", age=21, city="beijing")  # 不修改默认参数的值,且不传可变参数的值


