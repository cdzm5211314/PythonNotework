# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-02 14:48


## 创建空列表的字面值: L = []  # L绑定空列表
## 创建非空列表: L = [1, 2, [3.1, 3.2, 3.3], 4]

## 列表的构造(创建)函数: list()
# list()          # 生成一个空的列表 等同于[]
# list(iterable)  # 用可迭代对象创建一个列表
# 如: L = list("ABCD")           # L ---> ['A','B','C','D']
# 如: L = list(range(1, 10, 2))  # L ---> [1, 3, 5, 7, 9]

## 列表的索引赋值操作: 列表是可变的序列，可以通过索引赋值改变列表中的元素
# 语法: 列表[索引] = 表达式

## 列表的切片操作: 列表的切片取值返回一个列表，规则等同于字符串的切片规则
# 列表的切片赋值语法:  列表[切片] = 可迭代对象
# 说明: 切片赋值的赋值运算符的右侧必须是一个可迭代对象
# L = [2,3,4]
# L[0:1] = [1.1, 2.2]
# print(L)  # [1.1, 2.2, 3, 4]
# L[1:1] = [5, 6]
# print(L)  # [2, 5, 6, 3, 4]

## del 语句: 用于删除列表元素
# 语法:
    # del 列表[索引]
    # del 列表[切片]

## 列表list的常用方法:
# L.index(v [, begin[, end]])	返回对应元素的索引下标, begin为开始索引，end为结束索引,当 value 不存在时触发ValueError错误
# L.insert(index, obj)	        将某个元素插放到列表中指定的位置
# L.count(x)	                返回列表中元素的个数
# L.remove(x)	                从列表中删除第一次出现在列表中的值
# L.copy()	                    复制此列表（只复制一层，不会复制深层对象)
# L.append(x)	                向列表中追加单个元素
# L.extend(lst)	                向列表追加另一个列表
# L.clear()	                    清空列表,等同于 L[:] = []
# L.sort(reverse=False)	        将列表中的元素进行排序，默认顺序按值的小到大的顺序排列
# L.reverse()	                列表的反转，用来改变原列表的先后顺序
# L.pop([index])	            删除索引对应的元素，如果不加索引，默认删除最后元素，同时返回删除元素的引用关系

## 字符串文本解析方法: split() 和 join()
# S.split(sep=None)  # 分割: 将字符串使用sep为分隔符进行分割,返回分割后的字符串的列表,当不给定参数时,用空白字符作为分隔符进行分割
# S.join(iterable)   # 拼接: 使用S字符串将iterable可迭代对象中的字符串进行拼接,返回一个新的字符串
# 示例: split()
# s = 'Beijing is capital'
# L = s.split(' ')  # L = ['Beijing', 'is', 'capital']
# 示例: join()
# s = '\\'
# L = ['C:', 'Programe files', 'python3']
# s2 = s.join(L)  # s2 = b'C:\Programe files\python3'


# 列表数据按字典key的值进行排序
stu = [
    {"name":"Tom", "age":12},
    {"name":"Jack", "age": 22},
    {"name":"Rose", "age":18},
]

# 按name值升序排序
stu.sort(key=lambda x: x["name"])
print(stu)
# 按name值降序排序
stu.sort(key=lambda x: x["name"], reverse=True)
print(stu)

