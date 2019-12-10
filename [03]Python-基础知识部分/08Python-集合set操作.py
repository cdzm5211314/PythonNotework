# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-02 15:35

# 集合set:
# 集合是可变的容器
# 集合内的数据对象是唯一的（不能重复多次的)
# 集合是无序的存储结构，集合中的数据没有先后关系
# 集合内的元素必须是不可变对象
# 集合是可迭代的
# 集合是相当于只有键没有值的字典(键则是集合的数据)

# 创建空的集合:
s = set()  # set() 创建一个空的集合
# 创建非空集合:
s1 = {1, 2, 3}  # 集合中的三个整数1,2,3


# 集合的构造函数: set()
# set()             # 创建空集合
# set(iterable)     # 用可迭代对象创建一个新的集合对象
# 示例:
s2 = set("ABC")                         # {'A', 'C', 'B'}
s3 = set('ABCCBA')                      # {'A', 'C', 'B'}
s4 = set({1:"一", 2:'二', 5:'五'})      # {1, 2, 5}
s5 = set((2,3,5,7))                     # {2, 3, 5, 7}
s6 = set([1, 3.14, False])              # {False, 1, 3.14}   # 列表是可变对象  此处why???
# s = set([1, 2, [3.1, 3.2], 4])        # 报错: [3.1, 3.2]是可变对象

# 集合的运算: 交集，并集，补集，子集，超集
# & 生成两个集合的交集
# | 生成两个集合的并集
# -  生成两个集合的补集
# ^ 生成两个集合的对称补集
# < 判断一个集合是另一个集合的子集
# > 判断一个集合是另一个集合的超集
# ==  != 集合相同/不同

## 集合set的常用方法:
# S.add(e)	                            在集合中添加一个新的元素e；如果元素已经存在，则不添加
# S.remove(e)	                        从集合中删除一个元素，如果元素不存在于集合中，则会产生一个KeyError错误
# S.discard(e)	                        从集合S中移除一个元素e,在元素e不存在时什么都不做;
# S.clear()	                            清空集合内的所有元素
# S.copy()	                            将集合进行一次浅拷贝
# S.pop()	                            从集合S中删除一个随机元素;如果此集合为空，则引发KeyError异常
# S.update(s2)	                        用 S与s2得到的全集更新变量S
# S.difference(s2)	                    用S - s2 运算，返回存在于在S中，但不在s2中的所有元素的集合
# S.difference_update(s2)	            等同于 S = S - s2
# S.intersection(s2)	                等同于 S & s2
# S.intersection_update(s2)	            等同于S = S & s2
# S.isdisjoint(s2)	                    如果S与s2交集为空返回True,非空则返回False
# S.issubset(s2)	                    如果S与s2交集为非空返回True,空则返回False
# S.issuperset(...)	                    如果S为s2的子集返回True,否则返回False
# S.symmetric_difference(s2)	        返回对称补集,等同于 S ^ s2
# S.symmetric_difference_update(s2)	    用 S 与 s2 的对称补集更新 S
# S.union(s2)	                        生成 S 与 s2的全集


## 固定集合frozenset: 固定集合是不可变的，无序的，含有唯一元素的集合
# 作用：固定集合可以作为字典的键，也可以作为集合的值（元素)

# 创建空的固定集合
# fs = frozenset()
# 创建非空的固定集合
# fs = frozenset([2,3,5,7])

# 构造函数:
# frozenset()
# frozenset(可迭代对象) # 同set函数一致,返回固定集合

