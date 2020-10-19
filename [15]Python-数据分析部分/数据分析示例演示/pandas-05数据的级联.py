# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-28 22:00

import pandas
import numpy as np

from pandas import Series,DataFrame

# 数据分析数据挖掘: 有数据的情况
# 数据预处理
# 数据清洗(空数据,异常值)
# 数据集成(多个数据合并到一起,级联),数据可能存放在多个表中
# 数据转化
# 数据规约(属性减少(不重要的属性删除),数据减少去重操作)


# 数据集成:

# numpy数组的集成: concatenate()
# 行合并: 默认行合并,axis=0
nd1 = np.random.randint(0,150,size=(5,10))  # 5行10列
nd2 = np.random.randint(0,150,size=(6,10))  # 6行10列
# print(nd1,nd2)
nd3 = np.concatenate([nd1,nd2])
print(nd3)

# 列合并: axis=1
nd4 = np.random.randint(0,150,size=(5,10))  # 5行10列
nd5 = np.random.randint(0,150,size=(5,5))   # 5行5列
# print(nd4,nd5)
nd6 = np.concatenate((nd4,nd5), axis=1)
print(nd6)



# pandas的集成: append(), concat()
# 3行3列,行索引:A,B,C 列索引:Python,En,Math
df1 = DataFrame(data=np.random.randint(0,150,size=(3,3)), index=list("ABC"), columns=["Python","En","Math"])
# 6行3列,行索引:D,E,F,G,H,I 列索引:Python,En,Math
df2 = DataFrame(data=np.random.randint(0,150,size=(6,3)), index=list("DEFGHI"), columns=["Python","En","Math"])
# print(df1,df2)

# 行合并: 默认行合并,axis=0
df3 = df1.append(df2)  # 注意: 需要列属性相同
print(df3)
df4 = pandas.concat([df1,df2])
print(df4)

# 列合并: axis=1
df5 = pandas.concat([df1,df2],axis=1)
print(df5)


# concat()配置stack()和unstack()合并数据,并且进行表格形式的转变
# 期中成绩: 6行3列,行索引:A,B,C,D,E,F 列索引:Python,En,Math
df6 = DataFrame(np.random.randint(0,150,size=(6,3)), index=list("ABCDEF"), columns=["Python","En","Math"])
# 期末成绩: 6行3列,行索引:A,B,C,D,E,F 列索引:Python,En,Math
df7 = DataFrame(np.random.randint(0,150,size=(6,3)), index=list("ABCDEF"), columns=["Python","En","Math"])
# print(df6,df7)

df8 = pandas.concat([df6,df7],axis=0, keys=["期中","期末"])
print(df8)
df9 = df8.unstack(level=0)  # 行转换为列
print(df9)
df10 = df9.stack()  # 列转换为行
print(df10)


#############################################################################################
# pandas中数据的集成方法: append(),concat()
# pandas中重要的级联方法: merge() 融合,根据某一共同属性进行级联
# 注: DataFrame列属性不同,那么融合结果就会出现NaN空值
# 6行3列 列索引:name,sex,id 行索引:默认0开始
df11 = DataFrame({"name":["A","B","C","D","E","F"],
                  "sex":["男","女","女","女","男","男"],
                  "id":[1,2,3,4,5,6]})

# 6行3列 列索引:age,salary,id 行索引:默认0开始
df12 = DataFrame({"age":[23,45,19,32,27,20],
                  "salary":[4500,5800,3700,6500,6000,7200],
                  "id":[1,2,3,4,5,7]})
print(df11,df12)

df13 = df11.append(df12)  # 因为两个DataFrame列属性不同,所以合并出现NaN空值
# print(df13)

df14 = pandas.concat([df11,df12],axis=1)  # 行级联,会有两列id属性
print(df14)

df15 = df11.merge(df12)  # 行级联,会把相同列属性的数据保留出来
print(df15)

df16 = df11.merge(df12, how="outer")
print(df16)

#############################################################################################
# 给DataFrame中追加数据:
# 6行3列,行索引:A,B,C,D,E,F 列索引:Python,En,Math
df17 = DataFrame(data=np.random.randint(0,150,size=(6,3)), index=list("ABCDEF"), columns=["Python","En","Math"])
print(df17)

# 求行属性平均值,且保留两位小数
s1 = df17.mean().round(2)
print(s1)

# 追加行平均值
df_s1 = DataFrame(s1)  # 转换为DataFrame数据
df_s1.columns = ["score_mean"]  # 给列属性取个别名
df_s1 = df_s1.T  # 行列数据转换
print(df_s1)

# 追加数据
df18 = df17.append(df_s1)
print(df18)

# ------------------------------------------------ #

# 求列属性平均值,且保留一位小数
s2 = df17.mean(axis=1).round(1)
print(s2)

# 追加列平均值
df_s2 = DataFrame(s2)  # 转换为DataFrame数据
df_s2.columns = ["score_mean_2"]  # 给列属性取个别名
print(df_s2)

# 融合数据
df19 = df17.merge(df_s2, left_index=True, right_index=True)
print(df19)



