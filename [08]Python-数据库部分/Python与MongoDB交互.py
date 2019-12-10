# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 9:36

## Python程序中使用MongoDB数据库,需要安装导入pymongo模块
# 安装pymongo模块: pip install pymongo
# 导入pymongo模块: import pymongo

## Python与MongoDB交互流程:
# conn = pymongo.MongoClient("localhost",27017)
# db = conn.库名
# myset = db.集合名
# myset.insert(字典)

#################################################################################
### Python与MongoDB数据库交互流程:
import pymongo

# 创建数据库链接
client = pymongo.MongoClient("localhost", 27017)
# client = MongoClient("mongodb://localhost:27017/")

# 获取(切换)数据库
db = client.test
# db = client['test']

# 获取集合[即表](person)
collection = db.person
# collection = db['person']

### 操作数据库中的集合[即表]文档[即数据]: CRUD增删改查
## 添加一个文档数据 insert
# result = collection.insert({"name":"张三","age":35,"address":"重庆"})
# print(result)  # 值是 mongod集合的 _id
## 添加多个文档数据
# collection.insert([{"name":"abc1","age":15,"address":"重庆"},{"name":"abc2","age":20,"address":"tianjin"}])

## 修改一个文档数据 update_one
# collection.update_one({"name":"清晨起来开开窗,老婆美美哒"},{"$set":{"name":"老婆美美哒"}})
## 修改多个文档数据 update
# collection.update({"name":"777"},{"$set":{"age":"10"}})

## 删除一个文档数据 delete
# collection.remove({"name":"老婆美美哒"}
## 删除全部文档数据
# collection.remove()

### 查询文档数据: find_one()只查询一条  find()查询全部
## find_one()查询一条文档数据
result = collection.findOne()

## find()查询所有
# result = collection.find().count()
# for coll in result:
#     print(result)

## find()条件查询
# result = collection.find({"age":{"$gt":25}})  # result是那块数据的地址 find()里面可以写条件
# for coll in result:
#     print(coll)  # coll是每一个数据的集合,在python3里也就是字典,coll也可以取这个集合的元素列coll["name"]

## count()统计
# result = collection.find({"age":{"$gt":25}}).count()
# print(res)

## sort()排序
# result = collection.find({"age":{"$gt":25}}).sort("age")  # 升序
# result = collection.find({"age":{"$gt":25}}).sort("age",pymongo.DESCENDING)  # 降序
# for s in result:
#     print(s)

## limit()分页
# result = collection.find().skip(8).limit(4)
# for f in result:
#     print(f)

## 根据id查询，需要导入模块
# from bson.objectid import ObjectId  # 用于id查询
# result = collection.find({"_id":ObjectId("5af1072e8fdd1b19e8a4d149")})
# print(result[0])


## 断开或关闭链接
client.close()



