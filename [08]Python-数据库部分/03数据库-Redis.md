### 终端命令行链接数据库:
- 注: 远程链接需要注释掉: 配置文件xxx.conf中的bind 127.0.0.1信息
- 链接后,使用ping命令查看链接是否正常(PONG),然后可以设置修改密码: config set requirepass password
- 无密码链接数据库:
    > 本地: redis-cli  
    远程: redis-cli -h 192.168.23.145 -p 6379
- 有密码链接数据库:
    > 本地: redis-cli ---> auth "password"  
    本地: redis-cli -a "password"  
    远程: redis-cli -h 192.168.23.145 -p 6379 ---> auth "password"  
    远程: redis-cli -h 192.168.23.145 -p 6379 -a "password"


### Redis数据库是key-value的数据结构,值的类型分为5种:
- 字符串(string)
- 哈希(hash)
- 列表(list)
- 集合(set)
- 有序集合(zset)

### Redis数据库的键命令操作: 删除[对string,hash,list,set,zset都适用]
- 查看所有符合给定模式的键: keys *
- 查看名称中包含a的键: keys 'a*'
- 查看键对应的value值的类型: type key
- 判断键是否存在,如果存在返回1,不存在返回0: exists key1
- 删除键以及对应的值: del key1 key2 ...
- 查看键的有效时间(以秒为单位): ttl key
- 设置键的过期时间(以秒为单位): expire key seconds
- 注:如果没有指定键的过期时间,则⼀直存在,直到使⽤del移除

### 字符串类型数据操作: string
- 保存数据:
    - 设置一个键值: set key value  `注:如果键不存在就添加,键存在就是修改`
    - 设置多个键值: mset key1 value1 key2 value2 ...
    - 设置键值过期时间(以秒为单位): setex key seconds value
    - 对键对应的值进行追加值: append key value
- 获取数据:
    - 根据键获取值,如果不存在此键返回nil: get key
    - 根据多个键获取多个值: mget key1 key2 ...
- 修改数据:

- 删除数据:
    - 删除所有的键值对: flushall


### 哈希类型数据操作: 
- hash 用于存储对象,对象的结构为属性,值;值的类型为string
- 设置单个属性: hset key field value
    > hset user name itheima
- 设置多个属性: hmset key field1 value1 field2 value2 ...
    > hmset u2 name itcast age 11
- 获取指定键的属性: hget key
    > hkeys u2
- 获取⼀个属性的值: hget key field
    > hget u2 'name'
- 获取多个属性的值: hmget key field1 field2 ...
    > hmget u2 name age
- 获取所有属性的值: hvals key
    > hvals u2
- 删除属性,属性对应的值也会被删除: hdel key field1 field2
    > hdel u2 age
- 删除键(也会删除对应的属性与值): 
    > del key


### 列表类型数据操作: 
- list 列表的元素类型为string,按照插⼊顺序排序
- 在左侧插入数据: lpush key value1 value2 ...
    > lpush a1 a b c
- 在右侧插⼊数据: rpush key value1 value2 ...
    > rpush a1 0 1
- 在指定元素的前或后插⼊新元素: linsert key before(或 after) 现有元素 新元素
    > linsert a1 before b 3
- 获取: start、stop为元素的下标索引,索引从左侧开始，第⼀个元素为0;索引可以是负数，表示从尾部开始计数，如-1表示最后⼀个元素
    - 返回列表⾥指定范围内的元素: lrange key start stop
    
- 设置[修改]指定索引位置的元素值: lset key index value

- 删除: 将列表中前count次出现的值为value的元素移除
    > count > 0: 从头往尾移除  
    count < 0: 从尾往头移除  
    count = 0: 移除所有
- 删除指定元素: lrem key count value
- 删除列表: del key


### 集合类型数据操作: 
- set 无序,唯一,不重复,元素为string类型
- 注: 无法修改集合set数据
- 给集合中添加元素: sadd key member1 member2 ... 
    > sadd a3 zhangsan sili wangwu
- 获取集合中的所有元素: smembers key
    > smembers a3
- 删除集合中的指定元素: srem key
    > srem a3 wangwu
- 删除键(也会删除键对应的数据): del key


### 有序集合类型数据操作: 
- zset 有序,唯一,不重复,元素为string类型
- 注: 无法修改集合zset数据,集合的每个元素都会关联一个double类型的score,表示权重,通过权重将元素从小到大排序
- 给集合添加元素: zadd key score1 member1 score2 member2 ...
    > zadd a4 4 lisi 5 wangwu 6 zhaoliu 3 zhangsan
- 获取指定范围内的元素: zrange key start stop
    > zrange a4 0 -1
- 返回score值在min和max之间的元素: zrangebyscore key min max
    > zrangebyscore a4 5 6
- 返回成员member的score值: zscore key member
    > zscore a4 zhangsan
- 删除集合中指定的元素: zrem key member1 member2 ...
    > zrem a4 zhangsan
- 删除集合中权重在指定范围的元素: zremrangebyscore key min max
    > zremrangebyscore a4 5 6
- 删除键(也会删除键对应数据): del key



