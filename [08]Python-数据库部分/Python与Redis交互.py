# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 15:27

## Python程序中使用Redis数据库,需要安装导入redis模块
# 安装redis模块: pip install redis
# 导入redis模块: import redis

import redis

### 连接池: 创建数据库链接
# redis使用connection pool来管理对一个redis server 的所有连接,实现多个Redis实例共享一个连接池
pool = redis.ConnectionPool(host='localhost', port=6379,password="password",db='database')  # db参数可不填
red = redis.Redis(connection_pool=pool)

### 创建数据库连接: # db参数可不填
red = redis.Redis(host='localhost', port=6379, password='password', db='database')
red = redis.StrictRedis(host="localhost", port=6379, password="password", db="database")


### 增加数据：
red.set("name", "pjj")  # 插入字符串类型数据，成功返回True，否则返回False
red.setex("name", 5, "pjj")  # 插入字符串类型的数据，5秒后自动删除，成功True,失败False
red.mset({"name":"pjj","age":90,"school":"beijing"})  # 一次性插入多条数据，成功True，失败False
red.append("name","pxx")  # 字符串追加，最终得到的是name:pjjpxx,成功返回name的长度，否则返回新元素的长度

## 删除数据：
red.delete("name")  # 删除name及对应的元素
red.expire("name", 5)  # 设置name及对应的元素5秒后过期，也就是变相的删除操作

## 查询和获取:
red.keys()  # 查询所有的键，返回二进制list，可以遍历后.decode()解码获取
red.exists("name")  # 查询name是否存在 存在返回True，否则返回False
red.type("name")  # 查询name的类型
red.ttl("name")  # 查询name元素的过期时间，没有过期时间返回-1，已经过期返回-2，否则返回具体秒数


################################################################
### Python与Redis数据库交互流程:
import redis
## 创建链接
red = redis.StrictRedis(host="localhost",port=6379,password="password")
## 方法一：根据数据类型的不同，调用相应的方法
# 添加数据
# red.set("str","hell")
# 获取数据
# result = red.get("str")
# print(result)

## 方法二：pipeline
# 缓冲多条命令，然后依次执行，可以减少服务器-客户端的tcp数据包
pipe = red.pipeline()
pipe.set("str2","你好")
pipe.set("str3","你好啊")
pipe.set("str4","nihao")
pipe.execute()
