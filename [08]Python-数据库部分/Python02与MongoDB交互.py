# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 9:36

## Python程序中使用MongoDB数据库,需要安装导入pymongo模块
# 安装pymongo模块: pip install pymongo
# 导入pymongo模块: import pymongo


## Python与MongoDB交互流程:

import pymongo

# 1.创建数据库连接
# client = pymongo.MongoClient("localhost",27017)
client = MongoClient("mongodb://localhost:27017/")
# client.admin.authenticate('admin','123')  # 如果设置了密码,就执行这一步操作

# 2.获取数据库
# db = client.数据库名
# db = client['数据库名']

# 3.获取集合
collection = db.person
# collection = db['person']

# 获取集合
# cellection = client['数据库名']['集合名']


### 操作数据库中的集合[即表]文档[即数据]: CRUD增删改查
## 添加一个文档数据: insert()
result = collection.insert({"name":"张三","age":35,"address":"重庆"})
print(result)  # 值是 mongod集合的 _id

## 添加多个文档数据: insert_many()
result = collection.insert_many([{"name":"abc1","age":15,"address":"重庆"}, {"name":"abc2","age":20,"address":"tianjin"}])

## 删除一个文档数据: delete_one()
collection.delete_one({"name":"test10010"})
## 删除全部文档数据: delete_many()
collection.delete_many({"name":"test10010"})

## 修改一个文档数据: update_one()
collection.update_one({"name":"清晨起来开开窗,老婆美美哒"},{"$set":{"name":"老婆美美哒"}})
## 修改多个文档数据: update_many()
collection.update_many({"name":"777"},{"$set":{"age":"10"}})

## 查询一条文档数据: find_one() 只返回一条数据
## find_one()
result = collection.findOne({"name":"test10005"})
## 查询所有文档数据: find() 返回所有满足条件的数据;如果条件为空,则返回数据库的所有
result = collection.find({"name":"test10005"})

## 查询所有结果集总数: count()
result = collection.find().count()

## find()条件查询:
result = collection.find({"age":{"$gt":25}})  # result是那块数据的地址 find()里面可以写条件
for coll in result:
    print(coll)  # coll是每一个数据的集合,在python3里也就是字典,coll也可以取这个集合的元素列coll["name"]

## 统计: count()
result = collection.find({"age":{"$gt":25}}).count()
print(res)

## 排序: sort()
result = collection.find({"age":{"$gt":25}}).sort("age")  # 升序
result = collection.find({"age":{"$gt":25}}).sort("age",pymongo.DESCENDING)  # 降序
for s in result:
    print(s)

## 分页: limit()
result = collection.find().skip(8).limit(4)
for f in result:
    print(f)

## 根据id查询,需要导入模块
from bson.objectid import ObjectId  # 用于id查询
result = collection.find({"_id":ObjectId("5af1072e8fdd1b19e8a4d149")})
print(result[0])

## 断开或关闭链接
client.close()


