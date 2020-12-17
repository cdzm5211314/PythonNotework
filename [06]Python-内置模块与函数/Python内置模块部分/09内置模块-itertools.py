# -*- coding:utf-8 -*-
# @Desc : 
# @Date : 2020-12-17 9:27

import itertools

## itertools.count(start[, step])
# start:循环开始的数字; step:循环中的间隔


## itertools.cycle(iterable)
# 环状循环: 无限循环迭代器中的元素,相当于while True
n = itertools.cycle('abcd')
for i in n:
    print(i)
# 执行结果: a b c d a b c d a b ...


## itertools.repeat(object[, times])
# 重复循环: 重复循环迭代对象object,除非设置times对象,否则一直循环下去
# n = itertools.repeat('hello')
n = itertools.repeat('hello', 5)
for i in n:
    print(i)
# 执行结果1: hello hello hello ...
# 执行结果2: hello hello hello hello hello


## itertools.chain(*iterables)
# 链式迭代: 可以串联多个可迭代对象
n = itertools.chain('abc', [2, 1, 3],{30, 20, 10})
for i in n:
    print(i)
# 执行结果: a b c 2 1 3 10 20 30


## itertools.product(*iterables, repeat=1)
for temp in itertools.product([1, 2, 3], repeat=2):
    print(temp)
# 执行结果: (1, 1) (1, 2) (1, 3) (2, 1) (2, 2) (2, 3) (3, 1) (3, 2) (3, 3)


## itertools.permutations(iterable[, r])
# 排列: 不重复,无序
for temp in itertools.permutations([1, 2, 3], 3):
    print(temp)
# 执行结果: (1, 2, 3) (1, 3, 2) (2, 1, 3) (2, 3, 1) (3, 1, 2) (3, 2, 1)


## itertools.combinations(iterable, r)
# 组合: 不重复,有序
for temp in itertools.combinations([1, 2, 3, 4], 3):
    print(temp)
# 执行结果: (1, 2, 3) (1, 2, 4) (1, 3, 4) (2, 3, 4)


