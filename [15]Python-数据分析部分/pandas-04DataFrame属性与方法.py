# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/17 17:12

# import pandas as pd
import pandas
import numpy

### DataFrame类型数据的基本属性信息
# data_dict = {'name':['张三1','张三2'], 'age':[21,30], 'sex':['男','女']}
data_dict = {'name':['张三1','张三2','张三3','张三4','张三5','张三6'], 'age':[21,30,27,35,19,25], 'sex':['男','女','男','女','男','女']}
pp = pandas.DataFrame(data_dict)
print(pp)

# print(pp.index)     # 获取行索引数据
# print(pp.columns)   # 获取列索引数据
# print(pp.values)    # 获取具体的对象值数据,二维ndarray数组
# print(pp.dtypes)    # 获取列数据类型
# print(pp.shape)     # 获取维度数据,几行几列
# print(pp.ndim)      # 获取数据维度

print("**************************************************")

### DataFrame类型数据的整体情况查询
# print(pp.head(3))  # 显示前3行数据,默认5行
# print(pp.tail(2))  # 显示后2行数据,默认5行
# print(pp.info())        # 相关信息概览:如 行数,列数,列索引,列非空值个数,列类型,内存占用
# print(pp.describe())    # 快速综合统计结果: 如 计数,均值,标准差,最小值,1/4中位数,1/2中位数,3/4中位数,最大值

print("**************************************************")

### DataFrame类型数据的排序方法:
# 注: by指定按照某一列列排序,默认按照所有列进行排序
# 注: ascending指定以升序或降序排序,默认是升序(True)
# pp.sort_values(by='columns_name', ascending=False)

print("**************************************************")

### DataFrame类型数据获取行列数据的优化方法:
pp = pandas.DataFrame(numpy.arange(1,25).reshape(4,6), index=list('abcd'), columns=list('ABCDEF'))
print(pp)
## 通过标签索引获取行数据
print(pp.loc['b'])       # 获取b行所有列数据
print(pp.loc['b', 'C'])  # 获取b行C列的数据

print(pp.loc[:, 'C'])      # 获取所有行C列的数据
print(pp.loc[:,['B','D']]) # 获取所有行的B,D列数据

print(pp.loc[['a','c']]) # 获取a,c行的所有列数据
print(pp.loc[['a','c'],:]) # 获取a,c行的所有列数据

print(pp.loc['a':'c',['B','D']])    # 获取a~c行的B,D列数据
print(pp.loc[['a','c'],['B','D']])  # 获取a,c行的B,D列数据

## 通过位置索引获取列数据
print(pp.iloc[1])       # 获取第2行所有列数据
print(pp.iloc[1, 3])    # 获取第2行第4列的数据

print(pp.iloc[:, 3])      # 获取所有行的第4列的数据
print(pp.iloc[:,[2,4]])   # 获取所有行的第3,5列数据

print(pp.iloc[[1,3]])    # 获取第2,4行的所有列数据
print(pp.iloc[[1,3],:])  # 获取第2,4行的所有列数据

print(pp.iloc[0:3,[1,3]])    # 获取第1~3行的第2,4列数据
print(pp.iloc[[0,2],[1,3]])  # 获取第1,3行的第2,4列数据

print("**************************************************")

### DataFrame类型数据的赋值修改
pp.loc['a','B'] = 111           # 修改a行B列的数据值
pp.loc['a':'d','B':'E'] = 222   # 修改a~c行的B~D列的数据值
pp.iloc[1,2] = 333      # 修改第2行的第3列数据值
pp.iloc[1:3,2:5] = 200  # 修改第2~3行的第3~4列数据值

print("**************************************************")

### DataFrame类型数据的常用统计方法
# print(df['columns_name'].sum())     # 求取某列的求和值
# print(df['columns_name'].mean())    # 求取某列的平均值
# print(df['columns_name'].median())  # 求取某列的中位值
# print(df['columns_name'].max())     # 求取某列的最大值
# print(df['columns_name'].argmax())  # 求取某列的最大值索引位置
# print(df['columns_name'].min())     # 求取某列的最小值
# print(df['columns_name'].argmin())  # 求取某列的最小值索引位置
# ...


