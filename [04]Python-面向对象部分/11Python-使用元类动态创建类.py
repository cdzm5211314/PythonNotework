# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020-05-31 16:55

# 元类: type()

# 直接定义类
class Demo(object):
    num = 10

d = Demo()
print(d.__class__)  # 实例对象由哪个类创建
print(d.__class__.__class__)  # 类又是由元类创建
print(d.__class__.__class__.__class__)  # 元类又是由元类创建

print("-" * 50)

def object_func(self):
    print("--- 实例方法 ---")

@classmethod
def class_func(cls):
    print("--- 类方法 ---")

@staticmethod
def static_func():
    print("--- 静态方法 ---")

## 创建类
# 第一个参数: 字符串 - 指定创建的类的名字
# 第二个参数: 元组 - 指定创建的类需要继承哪个类,可省略
# 第三个参数: 字典 - 指定创建的类添加类属性,类方法,实例方法,静态方法,可省略
Demo1 = type("Demo1", (Demo,), {"count":0,
                                "object_func":object_func,
                                "class_func":class_func,
                                "static_func":static_func}
             )

# 创建类的实例对象
d1 = Demo1()
d1.object_func()  # 调用实例方法
Demo1.class_func()  # 调用类方法
Demo1.static_func()  # 调用静态方法
print(Demo1.num, Demo1.count)  # 调用类属性
print("*" * 50)

#######################################################################################
### ### Python3 - 使用自定义方法创建类
# 方法的第一个参数: 接受定义的类的名字(字符串)
# 方法的第二个参数: 接受定义的类的父类名字(元组)
# 方法的第三个参数: 接受定义的类的类属性,类方法,静态方法,实例方法组成的字典
def upper_attr(class_name, class_parents, class_attr):
    # 遍历属性字典,把不是__开头的属性名字变成大写
    new_attr = {}
    for key, value in class_attr.items():
        if not key.startswith("__"):  # 判断字典中key属性是否是以__开头
            new_attr[key.upper()] = value  # 把不是以__开头的key属性变为大写

    # 调用元类type()来创建一个类
    return type(class_name, class_parents, new_attr)


# 指定以upper_attr方法创建类,默认是以type()元类方式创建类
class Foo(object, metaclass=upper_attr):
    bar = "zip"

print(hasattr(Foo, 'bar'))  # False
print(hasattr(Foo, 'BAR'))  # True

f = Foo()
# print(f.bar)  # 报错
print(f.BAR)  # zip
print("*" * 50)


#######################################################################################
### Python3 - 使用自定义元类创建类
class UpperAttrMetaClass(type):

    def __new__(cls, class_name, class_parents, class_attr):
        # 遍历属性字典,把不是__开头的属性名字变成大写
        new_attr = {}
        for key, value in class_attr.items():
            if not key.startswith("__"):  # 判断字典中key属性是否是以__开头
                new_attr[key.upper()] = value  # 把不是以__开头的key属性变为大写

        # 方法一: 通过'type'来做类对象的创建
        return type(class_name, class_parents, new_attr)

        # 方法二: 复用'type.__new__()'方法
        # return type.__new__(cls, class_name, class_parents, new_attr)

class Foo2(object, metaclass=UpperAttrMetaClass):
    bar = "zip"

ff = Foo2()
# print(ff.bar)  # 报错
print(ff.BAR)  # zip


