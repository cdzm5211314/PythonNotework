# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:50


### zip(iter1 [,iter2, iter3,...])
# 将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的对象
# 注: 参数为多个序列时,以元素个数最小的序列为准
# 示例如下:
names = ['中国移动', '中国电信', '中国联通']
numbers = [10086, 10000, 10010, 95588]
for a, n in zip(names, numbers):
    print(a, '的客服号码是:', n)
# ---> 中国移动 的客服号码是: 10086
# ---> 中国电信 的客服号码是: 10000
# ---> 中国联通 的客服号码是: 10010
for x in zip(numbers, names):
    print(x)
# ---> (10086, '中国移动')
# ---> (10000, '中国电信')
# ---> (10010, '中国联通')
for x in zip(range(10), numbers, names):
    print(x)
# ---> (0, 10086, '中国移动')
# ---> (1, 10000, '中国电信')
# ---> (2, 10010, '中国联通')

## 以下用zip函数生成一个字典
d = dict(zip(names, numbers))
# d = {'中国移动': 10086, '中国电信': 10000, '中国联通': 10010}


### enumerate(iterable[,start])
# 生成带索引的枚举对象，返回迭代类型为索引-值对(index,value)对, 默认索引从零开始,也可以使用start绑定
# 示例如下:
names = ['中国移动', '中国电信', '中国联通']
for x in enumerate(names):
    print(x)
# ---> (0, '中国移动')
# ---> (1, '中国电信')
for i, x in enumerate(names):
    print(i,x)
# ---> 0 中国移动
# ---> 1 中国电信
# ---> 2 中国联通
for x in enumerate(names, start=100):
    print(x)
# ---> (100, '中国移动')
# ---> (101, '中国电信')
# ---> (102, '中国联通')


