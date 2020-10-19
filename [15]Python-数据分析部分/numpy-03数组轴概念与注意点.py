# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/16 9:28

# import numpy as np
import numpy

### 数组的轴概念: axis
## 对于一维数组(24,),只有0轴,0也表示行方向
## 对于二维数组(4,6),有0轴和1轴,0表示行方向,1表示列方向
## 对于三维数组(2,3,4),有0轴,1轴和2轴,0表示块方向,1表示行方向,2表示列方向

# 一维数组,求取元素和值,axis可以不指定
arr1 = numpy.arange(24)
print(numpy.sum(arr1, axis=0))

# 二维数组,求取各列与各行的和值
arr2 = numpy.arange(24).reshape((4,6))
print(numpy.sum(arr2, axis=0))  # 求列的和值
print(numpy.sum(arr2, axis=1))  # 求行的和值

# 三维数组,求取各块,各列,各行的和值
arr3 = numpy.arange(24).reshape((2,3,4))
print(numpy.sum(arr3, axis=0))
print(numpy.sum(arr3, axis=1))
print(numpy.sum(arr3, axis=2))


### numpy的注意点: copy与view
## arr1 = arr2  完全不复制,arr1与arr2相互影响
## arr1 = arr2[:]  视图的操作,一种切片,会创建新的数组arr1,但arr1的数据完全由arr2保管,它们数据变化一致
## arr1 = arr2.copy()  复制,arr1与arr2互不影响

### numpy中的nan和inf
# 注: 如何指定一个nan或inf呢?它们type类型为float
## nan表示不是一个数字
## -inf表示负无穷; inf表示正无穷

# numpy.nan == numpy.nan  # False
# numpy.nan != numpy.nan  # True
# nan和任何值计算都为nan
## 判断数组中nan的个数:
arr = numpy.array([1.0,numpy.nan,2.1,4.6,numpy.nan,5.6])
print(numpy.count_nonzero( arr != arr))
## 判断一个数字是否为nan,并把nan替换为0:
arr = numpy.array([1.0,numpy.nan,2.1,4.6,numpy.nan,5.6])
arr[numpy.isnan(arr)] = 0
print(arr)


