# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/17 15:28

# import pandas as pd
import pandas
import numpy

### DataFrame类型数据取行或取列数据:
# 注: 方括号写数字,表示取行数据,对行进行操作
# 注: 方括号写字符串,表示取列数据,对列进行操作
# 传入起始位置start(默认为0),结束位置end(-1表示最后一个),步长间隔step
# 注: 切片操作包头不包尾
data_dict = {'name':['张三1','张三2','张三3','张三4','张三5','张三6'], 'age':[21,30,27,35,19,25], 'sex':['男','女','男','女','男','女']}
pp = pandas.DataFrame(data_dict)

print(pp[:3])      # 获取前3行数据
print(pp[2:])      # 获取从第3行到最后行数据
print(pp['name'])  # 获取所有行数据的name列数据,为Series类型数据
print(pp[:4]['name'])   # 获取前4行数据的name列数据,为Series类型数据

### DataFrame类型数据布尔索引,&且,|或
pf = pandas.DataFrame(numpy.array([['aaa',45],['bbb',120],['ccc',90]]),
                      index=list('abc'), columns=list('AB'))
pf = pandas.read_csv('./dogNames2.csv')
## 示例: 找出数值大于50小于100的数据
print(pf['Count_AnimalName'])
print(pf[ pf['Count_AnimalName'] > 800 ])
# pf['B'].astype('int64')
# print(pf[ pf['B'] > 800 ])

print("***************************************************************")

### 索引方法与属性
df = pandas.DataFrame(numpy.arange(1,13).reshape(3,4), index=list('abc'), columns=list('ABCD'))
# 获取index: df.index
# 设置index: df.index = ['x','y']
# 获取index索引行数据: df.reindex(list("abcedf")) 注: 如果行不存在,NaN补全
# 指定某一列作为index: df.set_index("colnums_name",drop=False)
# 注:drop默认为True,会删除所选列数据,当设置为False会保留该列数据
# 指定某多列作为index复合索引: df.set_index(["colnums1_name",["colnums2_name"],drop=False)
# 返回index的唯一值: df.set_index("colnums_name").index.unique()


