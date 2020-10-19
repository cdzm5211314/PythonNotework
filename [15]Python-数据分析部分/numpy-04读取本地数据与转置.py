# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/16 12:10


# import numpy as np
import numpy

# CSV:Comma-Separated Value,逗号分隔值文件
# 源文件：换行和逗号分隔行列的格式化文本,每一行的数据表示一条记录

## numpy.loadtxt(fname,dtype=numpy.float,delimiter=None,skiprows=0,usecols=None,unpack=False)
# fname: 文件,字符串或产生器,可以是.gz或.bz2压缩文件
# dtype: 数据类型,可选,CSV的字符串以什么数据类型读入数组中,默认为numpy.float
# 注: 默认情况下对于较大的数据会将其变为科学计数的方式
# delimiter: 分隔字符串,默认是任何空格,改为逗号(,)
# 注: 指定边界符号是什么,如果不指定会导致每行数据为一个整体的字符串而报错
# skiprows: 跳过前X行,一般跳过第一行表头
# usecols: 读取指定的列,索引,元组类型
# unpack: 如果为True,读入属性将分别写入不同数组变量,False读入数据只写入一个数组变量,默认为False
# 注: 默认值为Falase,默认情况有多少条数据,就会有多少行;
# 注: 当值为True时,每一列的数据会组成一行,原始数据有多少列加载出来的数据就有多少行,相当于转置的效果

arr1 = numpy.loadtxt("file_path.csv", delimiter=',', dtype='int')
arr2 = numpy.loadtxt("file_path.csv", delimiter=',', dtype='int', unpack=True)
print(arr1)
print(arr2)


### 二维数组的行列转置
a1 = numpy.arange(12).reshape((3,4))  # 创建3行4列的数据
print(a1.T)             # 行列转置为4行3列的数组
print(a1.transpose())   # 行列转置为4行3列的数组
print(a1.swapaxes(1,0)) # 0轴与1轴交换实现行列转置,为4行3列的数组


