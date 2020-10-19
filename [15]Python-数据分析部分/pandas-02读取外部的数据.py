# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/10/17 16:24

# import pandas as pd
import pandas
import pymysql
import pymongo

### pandas读取外部数据,如CSV,MySQL,MongoDB,JSON,excel数据

## 从.csv文件中读取数据
pandas.read_csv('filename.csv')

## 从MySQL数据库读取数据
conn = pymysql.connect(host="localhost", user="username", passwd="password",db="database_name", charset="utf8")
sql_query = 'select * from database_name.table_name'
pandas.read_sql(sql_query, conn)

## 从MongoDB数据库读取数据
client = pymongo.MongoClient('localhost', 27017)
collection = client['dbname']['cellname']
data = list(collection.find())  # 获取所有数据
d = data[0]  # 获取所有数据中的第一条数据
p = pandas.Series(d)
print(p.index)  # 第一条数据的所有数据描述
print(p.values) # 第一条数据的所有数据具体值

pp = pandas.DataFrame(data)
print(pp)
