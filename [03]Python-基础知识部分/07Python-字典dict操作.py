# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-02 15:09

# 字典dict:
# 1. 字典是一种可变的容器，可以存储任意类型的数据
# 2. 字典中的每个数据都是用'键'(key) 进行索引，而不像序列可以用下标来进行索引
# 3. 字典的数据没有先后顺序关系，字典的存储是无序的
# 4. 字典中的数据以键(key)-值(value)对进行映射存储
# 5. 字典的键不能重复，且只能用不可变类型作为字典的键。

# 字典的字面值表示方式: 用{}括起来,以冒号(:) 分隔键-值对,各键值对用分号分隔开

# 创建空字典: d = {}
# 创建非空的字典:
# d = {'name': 'tarena', 'age': 15}
# d = {1:'壹', 2:'贰'}

# 字典的构造函数: dict()
# dict()            创建一个空字典,等同于 {}
# dict(iterable)    用可迭代对象初始化一个字典
# dict(**kwargs)    关键字传参形式生成一个字典
# 创建示例:
# d = dict()
# d = dict([('name', 'tarena'), ('age',15)])
# d = dict(name='tarena', age=15)

# 字典的键索引: 用[] 运算符可以获取字典内'键'所对应的'值'
# 语法: 字典[键]  ---> 获取数据元素
d = dict(name='tarena', age=15)
print(d['age'])  # 15

# 添加/修改字典元素:  字典[键] = 表达式
# 注: 当键存在就是修改键对应的值,当键不存在就是添加一个键值对
# 示例:
d = {}
d['name'] = 'tarena'  # 创建一个新的键值对
d['age'] = 15  # 创建键值对
d['age'] = 16  # 修改键值对

# del 语句删除字典的元素
# 语法: del 字典[键]
# 示例:
d = {'name': 'china', 'pos': 'asia'}
del d['pos']
print(d)
del d['name']
print(d)   # {}


# 字典的 in / not in 运算符:
# 可以用 in 运算符来判断一个'键'是否存在于字典中,如果存在则返回True, 否则返回False
# not in 与 in 返回值相反
# 示例:
# d = {'a': 1, 'b': 2}
# 'a' in d     # True
# 1 in d       # False
# 100 not in d # True
# 2 not in d   # True

# 字典的迭代访问: 字典是可迭代对象，字典只能对键进行迭代访问
d = {'name': 'tarena', (2002, 1, 1): '生日'}
for x in d:
    print(x)

## 字典dict的常用方法:
# D.clear()	            清空字典
# D.pop(key)	        移除键，同时返回此键所对应的值
# D.copy()	            返回字典D的副本,只复制一层(浅拷贝)
# D.update(D2)	        将字典 D2 合并到D中，如果键相同，则此键的值取D2的值作为新值
# D.get(key, default)	返回键key所对应的值,如果没有此键，则返回default
# D.keys()	            返回可迭代的 dict_keys 集合对象
# D.values()	        返回可迭代的 dict_values 值对象
# D.items()	            返回可迭代的 dict_items 对象

di = {
    "name":"zhangsan",
    "age":20,
}

for k in  di.keys():
    print(k)

for v in  di.values():
    print(v)

for k,v in  di.items():
    print(k,v)

