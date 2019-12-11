# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-12-10 17:23


# 注: 字符串,列表,元组,集合,字典 在定义的时候 避免使用(str,list,tuple,set,dict)为变量名称


print("***** 如下: 字典 ---> 字符串, 元组, 列表, 集合 *****")
d = {'name': 'Zara', 'age': 7, 'class': 'First'}

print(type(str(d)), str(d))  # <class 'str'> {'name': 'Zara', 'age': 7, 'class': 'First'}
print(type(str(d.__str__())), str(d.__str__()))  # <class 'str'> {'name': 'Zara', 'age': 7, 'class': 'First'}

print(type(tuple(d)), tuple(d))  # <class 'tuple'> ('name', 'age', 'class')
print(type(tuple(d.keys())), tuple(d.keys()))  # <class 'tuple'> ('name', 'age', 'class')
print(type(tuple(d.values())), tuple(d.values()))  # <class 'tuple'> ('Zara', 7, 'First')

print(type(list(d)), list(d))  # <class 'list'> ['name', 'age', 'class']
print(type(list(d.keys())), tuple(d.keys()))  # <class 'list'> ('name', 'age', 'class')
print(type(list(d.values())), tuple(d.values()))  # <class 'list'> ('Zara', 7, 'First')

print(type(set(d)), set(d))  # <class 'set'> {'class', 'name', 'age'}
print(type(set(d.keys())), set(d.keys()))  # <class 'set'> {'name', 'class', 'age'}
print(type(set(d.values())), set(d.values()))  # <class 'set'> {'First', 7, 'Zara'}

########################################################################################

print("***** 如下: 元组 ---> 字符串, 列表, 集合, 字典 *****")
t = (0, 2, 4, 6, 8)

print(type(str(t)), str(t))  # <class 'str'> (0, 2, 4, 6, 8)
print(type(t.__str__()), t.__str__())  # <class 'str'> (0, 2, 4, 6, 8)

print(type(list(t)), list(t))  # <class 'list'> [0, 2, 4, 6, 8]

print(type(set(t)), set(t))  # 去重 <class 'set'> {0, 2, 4, 6, 8}

print("单个元组不可以转字典,但两个元组可以借助zip()转字典")
print( type(dict(zip(("a","b","c"), ("1","2","3")))), dict(zip(("a","b","c"), ("1","2","3"))))
# <class 'dict'> {'a': '1', 'b': '2', 'c': '3'}

########################################################################################

print("***** 如下: 列表 ---> 字符串, 元组, 集合, 字典 *****")
l = [1, 3, 5, 7, 9]

print(type(str(l)), str(l))  # <class 'str'> [1, 3, 5, 7, 9]
print(type(l.__str__()), l.__str__())  # <class 'str'> [1, 3, 5, 7, 9]

print(type(tuple(l)), tuple(l))  # <class 'tuple'> (1, 3, 5, 7, 9)

print(type(set(l)), set(l))  # 去重 <class 'set'> {1, 3, 5, 7, 9}

print("单个列表不可以转字典,但两个列表可以借助zip()转字典")
print( type(dict(zip(["a","b","c"], ["1","2","3"]))), dict(zip(["a","b","c"], ["1","2","3"])))
# <class 'dict'> {'a': '1', 'b': '2', 'c': '3'}

########################################################################################

print("***** 如下: 字符串 ---> 元组, 列表, 集合, 字典 *****")
s = "aabbccddeeff"

print(type(tuple(s)), tuple(s))  # <class 'tuple'> ('a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f')

print(type(list(s)), list(s))  # <class 'list'> ['a', 'a', 'b', 'b', 'c', 'c', 'd', 'd', 'e', 'e', 'f', 'f']

print(type(set(s)), set(s))  # <class 'set'> {'c', 'a', 'b', 'f', 'd', 'e'}

print(type(eval("{'name':'chen', 'age':21}")), eval("{'name':'chen', 'age':21}"))
# <class 'dict'> {'name': 'chen', 'age': 21}

########################################################################################

print("***** 如下: 集合 ---> 字符串, 元组, 列表, 字典 *****")
ss = {"a","b","c","d","e","f"}

print(type(str(ss)), str(ss))  # <class 'str'> {'c', 'd', 'e', 'f', 'a', 'b'}
print(type(ss.__str__()), ss.__str__())  # <class 'str'> {'c', 'd', 'e', 'f', 'a', 'b'}

print(type(tuple(ss)), tuple(ss))  # <class 'tuple'> ('c', 'd', 'e', 'f', 'a', 'b')

print(type(list(ss)), list(ss))  # <class 'list'> ['c', 'd', 'e', 'f', 'a', 'b']

print("单个集合不可以转字典,但两个集合可以借助zip()转字典")
print(type(dict(zip({"a","b","c"}, {"1","2","3"}))), dict(zip({"a","b","c"}, {"1","2","3"})))
# <class 'dict'> {'b': '2', 'a': '1', 'c': '3'}


