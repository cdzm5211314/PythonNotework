# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 9:59

# CSV是一种通用的、相对简单的文件格式，被用户、商业和科学广泛应用
# 术语“CSV”泛指具有以下特征的任何文件：
# 1. 纯文本，使用某个字符集，比如ASCII、Unicode、EBCDIC或GB2312；
# 2. 由记录组成（典型的是每行一条记录）；
# 3. 每条记录被分隔符分隔为字段（典型分隔符有逗号、分号或制表符；有时分隔符可以包括可选的空格）；
# 4. 每条记录都有同样的字段序列。

import csv

## csv文件数据的读取(两种方式):
# 第一种方式:
# with open("response1.csv",encoding="ut-8") as fp:
#     reader = csv.reader(fp)  # reader是一个迭代器,会包含第一行标题行数据
#     # next(reader)  # csv文件第1行数据,标题行数据不会读取
#     for x in reader:  # 遍历迭代器,返回一个列表类型数据
#         print(x["index"])  # 列表的下标index

# 第二种方式:
# with open("response2.csv",encoding="ut-8") as fp:
#     reader = csv.DictReader(fp)  # reader是一个迭代器,不会包含第一行标题行数据
#     for x in reader:  # 遍历迭代器,返回一个字典类型数据
#         print(x["key"])  # 字典的键key

## csv文件数据的写入(两种方式):

# 第一种方式:
headers1 = ["name","age","classroom"]  # 表头信息
values1 = [
    ("zhangsan",18,111),
    ("lisi",21,222),
    ("wangwu",37,111),
]
with open("response1.csv","w",encoding="utf-8",newline="") as fp:  # newline为空值,避免换行
    writer = csv.writer(fp)
    writer.writerow(headers1)  # 写入一行数据: 写入头部信息
    writer.writerows(values1)  # 一次写入多行数据: 写入具体数据

# 第二种方式:
headers2 = ["name", "age", "classroom"]
values2 = [
    {"name":"张三","age":30,"classroom":10},
    {"name":"李四","age":18,"classroom":11},
    {"name":"王五","age":25,"classroom":13}
]
with open("response2.csv","w",encoding="utf-8",newline="") as fp:  # newline为空值,避免换行
    writer = csv.DictWriter(fp,headers2)  # headers2为传入的头部信息
    writer.writeheader() # 真正把头部信息写入到csv文件中
    writer.writerow({"name":"徐六","age":35,"classroom":15})  # 写入一行具体的数据
    writer.writerows(values2)  # 一次写入多行数据




