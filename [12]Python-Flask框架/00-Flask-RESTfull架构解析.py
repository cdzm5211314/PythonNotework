# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-20 20:12


# RESTfull:是 API 设计规范，用于 Web 数据接口的设计


# RESTful架构: 
# 每个URL代表一种资源
# 客户端和服务器之间,传递这种资源的某种表现层
# 客户端通过四个http动词,对服务器资源进行操作,实现表现层状态转换


# 标准的HTTP方法: 由HTTP动词对资源进行具体操作,常用的HTTP动词有如下四个
# GET     SELECT: 从服务器获取资源
# POST    CREATE: 在服务器新建资源
# PUT     UPDATE: 在服务器更新资源
# DELETE  DELETE: 从服务器删除资源


# 状态码: HTTP状态码就是一个三位数,分成五个类别,如下
# 1xx：相关信息
# 2xx：操作成功
# 3xx：重定向
# 4xx：客户端错误
# 5xx：服务器错误



# 如何设计符合RESTful风格的API
# 1.域名: 示例如下
# 将api部署在专用域名下: http://api.example.com
# 将api放在主域名下: http://www.example.com/api/

# 2.版本: 示例如下
# 将API的版本号放在url中
# http://www.example.com/app/1.0/info
# http://www.example.com/app/1.2/info

# 3.路径,使用标准的HTTP方法: 示例如下
# 获取所有商品:         GET http://www.example.com/app/goods
# 获取指定商品的信息:    GET http://www.example.com/goods/ID
# 新建商品的信息:        POST http://www.example.com/goods
# 更新指定商品的信息:    PUT http://www.example.com/goods/ID
# 删除指定商品的信息:    DELETE http://www.example.com/goods/ID

# 4.过滤信息: 如果资源数据较多,服务器不能将所有数据一次全部返回给客户端,API应该提供参数,过滤返回结果,示例如下
# 指定返回数据的数量:              http://www.example.com/goods?limit=10
# 指定返回数据的开始位置:          http://www.example.com/goods?offset=10
# 指定第几页，以及每页数据的数量:   http://www.example.com/goods?page=2&per_page=20

# 5.状态码: 常用状态码示例如下
# 200 OK  : 服务器成功返回用户请求的数据
# 201 CREATED: 用户新建或修改数据成功
# 202 Accepted: 表示请求已进入后台排队
# 400 INVALID REQUEST: 用户发出的请求有错误
# 401 Unauthorized: 用户没有权限
# 403 Forbidden: 访问被禁止
# 404 NOT FOUND: 请求针对的是不存在的记录
# 406 Not Acceptable: 用户请求的的格式不正确
# 500 INTERNAL SERVER ERROR: 服务器发生错误

# 6.错误信息: 一般来说,服务器返回的错误信息,以键值对的形式返回
# {
#     error:'Invalid API KEY'
# }

# 7.响应结果: 示例如下
# 返回商品列表:       GET     http://www.example.com/goods
# 返回单个商品:       GET     http://www.example.com/goods/cup
# 返回新生成的商品:   POST    http://www.example.com/goods
# 返回一个空文档:     DELETE  http://www.example.com/goods


# 注: 服务器返回的数据格式,应该尽量使用JSON,避免使用XML
# 后端WEB开发一般套路步骤: 1.获取参数, 2.校验参数, 3.业务逻辑处理, 4.返回值


