### 终端命令行链接数据库:
- 注: 远程链接需要注释掉: 配置文件xxx.conf中的bind_ip = 127.0.0.1 信息
    > mongo 192.168.23.145:27017  
    mongo 192.168.23.145:27017/dbname  
    mongo 192.168.23.145:27017/dbname -u user -p password


### MongoDB数据库的操作:
- 显示所有用户: show users
- 查看所有数据库: show dbs
- 创建/切换数据库: use 数据库名称
- 查看当前正在使用的数据库: db 或者 db.getName()
- 删除数据库: db.dropDatabase() `注: 删除数据库之前首先你已进入数据库(use 数据库名称)`
- 显示当前数据库中的集合: show collections
- 查看当前数据库中的集合: show tables
- 显示集合操作命令: db.yourCollection.help()
- 断开数据库连接: exit
- 显示数据库操作命令: db.help()

### MongoDB数据库集合操作:(即表的操作)
- 创建集合的两种方式:
    - 第一种: db.createCollection("集合名称")      
        > 如: db.createCollection("student")
    - 第二种: db.集合名称.insert(文档)    
        > 如: db.student.insert({name:"zhangsan", age:19, address:"上海"})
    - 注: 前者创建了一个空的集合;后者创建了一个集合并添加了一个文档(即表数据)
- 删除当前数据库中的集合(即表): db.集合名称.drop()    
    > 如：db.student.drop()
- 查看当前数据库中的集合(即表): show tables

### MongoDB数据库集合的文档操作:(即表中数据的操作[CRUD增删改查])
- 添加文档(即数据): inster()
    - db.集合名称.insert(文档) 或 db.集合名称.insert([文档1,文档2,....])
        > 如：插入一个文档：db.student.insert({name:"zhangsan",age:19,address:"上海"})  
        如：插入多个文档：db.student.insert([{name:"lisi2",age:12,address:"河"},{name:"wangwu",age:30,address:"天津"}])

- 添加文档(即数据): save()
    - 注: 如果不指定_id字段，save()方法类似于insert()方法，如果指定_id字段，则会更新该_id字段的数据
    - db.集合名称.save(文档)
        > 添加: 如: db.student.save({name:"liuliu",age:25,address:"666"})  
        修改: 如: db.student.save({_id:ObjectId("5af003107a4440acc28674e6"),name:"777",age:777,address:"777"})

- 删除文档(即数据): remove()
    - db.集合名称.remove()
        > 示例: db.student.remove({name:"zhangsan"}) `删除所有name属性值为zhangsan的数据`  
        示例: db.student.remove({name:"zhangsan"},{justOne:true})  `justOne为true或1时,只删除一条文档(数据)`

- 修改文档(即数据): update()
    - db.集合名称.update(文档)
        > 如: db.student.update({name:"liuliu"},{age:25}) `把数据name属性与值更新为只有age属性与值`  
        如: 更新一条: db.student.update({name:"liuliu"},{$set:{age:25}})  
        如: 更新多条：db.student.update({name:"liuliu"},{$set:{age:25}},{multi:true})  
        如: 累加：db.student.update({name:"liuliu"},{$inc:{age:25}})


- 查询文档(即数据): find()
    - db.集合名称.find()
        > 如：db.student.find()  `查询所有数据`  
        如: db.student.findOne({name:"liuliu"}) `查询匹配条件的第一条数据`  
        如: db.student.find().pretty()

### 条件查询运算符:
- 大于: $gt  语法:db.集合名称.find({<key>:{$gt:<value>}})
    > 示例：db.student.find({age:{$gt:25}})
    
- 大于等于: $gte   语法:db.集合名称.find({<key>:{$gte:<value>}})
    > 示例：db.student.find({age:{$gte:25}})
    
- 小于: $lt  语法:db.集合名称.find({<key>:{$lt:<value>}})
    > 示例：db.student.find({age:{$lt:25}})
    
- 小于等于: $lte   语法:db.集合名称.find({<key>:{$lte:<value>}})
    > 示例：db.student.find({age:{$lte:25}})
    
- 大于等于 和 小于等于: $gte 和 $lte 语法:db.集合名称.find({<key>:{$gte:<value>,$lte:<value>}})
    > 示例：db.student.find({age:{$gte:20,$lte:27}})
    
- 等于: 语法:db.集合名称.find({<key>:<value>})
    > 示例：db.student.find({age:777})
    
- 使用_id进行查询: 语法:db.集合名称.find({"_id":ObjectId("id值")})
    > 示例：db.student.find({"_id":ObjectId("5af1072e8fdd1b19e8a4d149")})
    
- 查询某个结果集的数据条数: count()
    > 示例：db.student.find().count()
    
- 查询某个字段的值当中是否包含另一个值: 
    > 示例：db.student.find({name:/en/})
    
- 查询某个字段的值是否以另一个值开头: 
    > 示例：db.student.find({name:/^en/})
    
- limit() 和 skip(): 
    > limit()：读取指定数量的数据记录 示例: db.student.find().limit(2)  
    skip(): 读取跳过指定数量的数据记录 示例: db.student.find().skip(3)  
    
- limit() 和 skip() 联合使用: 通常用这种方式实现分页功能
    > 示例第一次: db.student.find().skip(3).limit(3)  
    示例第二次: db.student.find().skip(6).limit(3)

- 排序: sort()  语法: db.集合名称.find({<key>:<value>}).sort({<key>:1|-1})
    > 示例: 按照年龄升序: db.student.find().sort({age:1})  
    示例: 按照年龄降序: db.student.find().sort({age:-1})

