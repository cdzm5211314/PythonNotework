# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-01 19:46


### map(func, *lst)
## 作用: 将传入的参数func作用到序列的每个元素中,并将结果组成新的列表(Python2)/迭代器(Python3)并返回
# 注意：map()函数不改变原有的list,而是返回一个新的list
# 示例一如下:
def test1(x):
    return x ** 2
for x in map(test1, range(1, 10)):  # rang(1,10) ---> 1 2 3 4 5 6 7 8 9
    print(x)  # 1 ** 2, 2 ** 2, 3 ** 2, ..., 9 ** 2
result = max(test1, range(1, 10))  # <map object at 0x00000000020FDE48>
result2 = list(result)  # [1, 4, 9, 16, 25, 36, 49, 64, 81]

# 示例二如下:
# Python内建函数: pow(x, y, z = None) ---> x ** y
for x in map(pow, range(1, 5), range(4,0,-1)):  # range(1, 10) ---> 1,2,3,4,5,6,7,8,9   range(4,0,-1) ---> 4,3,2,1
    print(x)  # 1 ** 4, 2 ** 3, 3 ** 2, 4 ** 1
for x in map(pow, [2,3,5,7], [4,3,2,1], range(5, 10)):
    print(x)  # 2 ** 4 % 5, 3 ** 3 % 6, 5 ** 2 % 7, 7 ** 1 % 8


### reduce(func, lst[, initializer])
# 作用: 参数函数func必须接收两个参数,reduce()对list的每个元素反复调用函数func,并返回最终结果
def add(x,y):
    return x+y
print(reduce(add, [1,3,5,7,9]))
# 即: 1 + 3 + 5 + 7 + 9
# 执行: 先计算列表的头两个元素add(1,3),得到结果4,再把结果和列表的第三个元素进行计算add(4,5),结果为9,依次类推...
print(reduce(add, [1, 3, 5, 7, 9], 100))
# 执行: 把100当做初始值,并按照上诉方式进行计算


### filter(func, lst)
# 作用: 用于过滤序列,过滤掉不符合条件的元素,返回一个filter对象,要转换为列表使用list()来转换
# 说明: 参数函数func将对lst中的每个元素进行求值,返回False则将此数据丢弃,返回True,则保留此数据
# 示例一如下:
def test2(x):
    return x % 2 == 1  # 此函数判断x是否为奇数
    # return x % 2 == 0  # 此函数判断x是否为偶数
for x in filter(test2, range(10)):
    print(x)  # 1 3 5 7 9
result = filter(test2, range(10))  # <filter object at 0x00000000006ADE80>
result2 = list(result)  # [1, 3, 5, 7, 9]

# 示例二如下:
fn = [x for x in filter(lambda x: x % 2 == 0, range(10))]


### sorted(iterable, key=None, reverse=False)
# 作用: 将原可迭代对象的数据进行排序，生成排序后的列表iterable 可迭代对象key 函数是用来提供一个值,这个值将作为排序的依据reverse 标志用来设置是否降序排序
# 说明: iterable可迭代对象, key函数是用来提供一个参考值,这个值将作为排序的依据 ,reverse标识用来设置是否降序排序(False默认升序)
# 示例如下:
L = [5, -2, -4, 0, 3, 1]
L1 = sorted(L)                # [-4, -2, 0, 1, 3, 5]
L2 = sorted(L, reverse=True)  # [5, 3, 1, 0, -2, -4]
L3 = sorted(L, key=abs)       # [0, 1, -2, 3, -4, 5]


