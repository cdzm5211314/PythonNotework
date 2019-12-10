# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:50


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

