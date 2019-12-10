# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-12-10 10:26

# 注: 遇见第一个*装包(赋值时),遇见第二个*拆包(传参时)

# 字符串str的装包与拆包
s = "hello world"
x, y, *z = "hello world"  # 装包 z = ['l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']
print(*z)  # 拆包: l l o   w o r l d
print(x, y, z)  # h e ['l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd']

x, *y, z = s
print(x, y, z)  # h ['e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l'] d

print(*"hello world")  # 字符串拆包 h e l l o   w o r l d

# 字符串 -> 元组
ss = 'h', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd'
print(ss)

############################################################################################

# 列表list的装包与拆包
l = ['aa', 'bb', "cc", "dd"]
x, y, *z = ['aa', 'bb', "cc", "dd"]
print(x, y, z)  # aa bb ['cc', 'dd']

x, *y, z = ['aa', 'bb', "cc", "dd"]
print(x, y, z)  # aa ['bb', 'cc'] dd

print(*['aa', 'bb', "cc", "dd"])  # 列表拆包 aa bb cc dd


############################################################################################

# 元组tuple的装包与拆包
t = (1, 3, 5, 7, 9)
x, y, *z = (1, 3, 5, 7, 9)
print(x, y, z)  # 1 3 [5, 7, 9]

x, *y, z = (1, 3, 5, 7, 9)
print(x, y, z)  # 1 [3, 5, 7] 9

print(*(1, 3, 5, 7, 9))  # 元组拆包 1 3 5 7 9

tt = 2, 4, 6, 8
print(tt)  # (2, 4, 6, 8)


############################################################################################

def function1(a, b, *args):
    print(a, b)   # 1 3
    print(args)   # 装包: (5, 7, 9)
    print(*args)  # 拆包: 5 7 9

# *args作为形参时是用来接收多余的未命名参数,args是元组
function1(1, 3, 5, 7, 9)


def function2(x, y, **kwargs):
    print(x, y)         # aa bb
    print(kwargs)       # 装包: {'name': '张三', 'age': 21}
    # print(**kwargs)     # **kwargs不支持打印输出
    test(**kwargs)

def test(name, age):  # 此处的参数名一定要和字典的键的名称一致
    print(name, age)  # 张三 21

# **kwargs作为形参时是用来接收key=value这种命名参数,kwargs是字典
function2("aa", "bb", name="张三", age=21)


# 总结:
# *args作为形参时是用来接收多余的未命名参数，而**kwargs是用来接收key=value这种类型的命名参数，args是元组，kwargs是字典
# *和**在函数体中除了拆包之外,并没有其他作用
# 装包的含义就是把未命名参数和命名参数分别放在元组或者字典中


