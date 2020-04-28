# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 9:35

## Python程序中使用MySQL数据库,需要安装导入PyMySQL模块
# 安装PyMySQL模块: pip install PyMySQL
# 导入PyMySQL模块: import pymysql

## 创建Connection对象: pymysql.connect(参数列表)
# connect(host=None, user=None, password="", database=None, port=0, charset='')
# host:     连接的MySQL主机地址,如果是本机就是localhost
# port:     连接的MySQL主机端口号,默认是3306
# db:       数据库名称
# user:     连接的用户名
# password: 连接的用户名的密码
# charset:  通信采用的编码方式,默认是"gb2312",要求与数据库创建时指定的编码一致,否则中文会乱码

## Connection对象方法: 作用:建立与数据库的链接
# cursor()      返回Cursor对象,用于执行sql语句并获得结果
# commit()      事务,需要提交才会生效
# close()       关闭连接
# rollback()    事务,放弃之前的操作

### 创建Cursor对象: pymysql.connect(参数列表).cursor()
# Cursor对象方法: 作用:执行sql语句
# execute()     执行sql语句,返回受影响的行数
# fetchone()    执行查询语句时,获取查询结果集的第一个行数据,返回一个元组
# fetchall()    执行查询语句时,获取查询结果集的所有行数据,一行构成一个元组,再将这些元组装入一个元组返回
# close()       关闭游标


###########################################################################################

### Python与MySQL数据库交互流程:
import pymysql

# connect(host=None, user=None, password="", database=None, port=0, charset='')
# 1.创建Connection数据库对象
connection = pymysql.connect("localhost","root","root","test")

# 2.创建Cursor游标对象
cursor = connection.cursor()

# 3.使用游标对象,执行SQL语句

## 保存数据:
# 要执行的SQL语句: 一次性插入一条数据
sql = "insert into person(name,age) values ('猪八戒',8000)"
cursor.execute(sql)
connection.commit()

sql = 'insert into person(name,age) values(%s,%s)'
cursor.execute(sql,('孙悟空',100000))
connection.commit()

# 要执行的SQL语句: 一次性插入多条数据
sql = 'insert into person(name,age) values(%s,%s)'
datas = [('牛魔王',9000),('铁扇公主',8000),('玉皇大帝',6000)]
cursor.execute(sql, datas)
connection.commit()

## 删除数据:
sql = 'delete from person where age=8000'
cursor.execute(sql)
connection.commit()

## 更改数据:
sql = 'update person set age=%s where name=%s'
cursor.execute(sql,[90000,"玉皇大帝"])
connection.commit()

## 查询数据:
# 要执行的SQL语句
sql = "select * from test_table"
# 使用execute()方法,返回的结果只是获取到的记录数
# num = cursor.execute(sql)
# print(num)
cursor.execute(sql)
# 使用fetchone()方法,返回结果集的第一行数据(列表形式)
tuple1 = cursor.fetchone()
print(tuple1)
# 使用fetchone()方法,返回结果集的所有行数据(列表形式)
tuples2 = cursor.fetchall()
print(tuples2)

# 4.关闭游标和连接
cursor.close()
connection.close()


############################################################################################

### ORM关系对象映射: 安装 pip install SQLAlchemy

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker

# 获取连接数据库
engine = create_engine("mysql+pymysql://username:password@localhost:3306/dbname?charset=utf8",
                       encoding='utf-8', echo=True) # 如果不设置 echo = true 就不打印

Base = declarative_base()  # 生成ORM基类

class User(Base):
    __tablename__ = 'user'  # 数据库表名
    id = Column(Integer, primary_key=True)
    name = Column(String(32))
    password = Column(String(64))

    def __repr__(self):  # 详细打印出用户的信息
        return "<User(name='%s', password='%s')>" %(self.name, self.password)

Base.metadata.create_all(engine)  # 创建表结构

# 创建与数据库的会话session class,注意:这里返回给session的是个class,不是实例对象
Session_class = sessionmaker(bind=engine)
session = Session_class()  # 生成session实例对象

# 创建数据对象,也就是你要在user表中插入这样一条数据(这里只是一个对象)

# 添加一条数据
user = User("zhangsan","123456")
session.add(user)
session.commit()

# 添加多条数据
user2 = User("lisi","123456")
user3 = User("wangwu","123456")
session.add_all([user2, user3])
session.commit()

# ...


############################################################################################

### Python与MySQL数据库交互封装
import pymysql
class MySQLHelper(object):
    config = {
        "host": "localhost",
        "user": "root",
        "password": "root",
        "db": "chenssq"
    }

    def __init__(self):
        self.connection = None
        self.cursor = None

    # 从数据库表中查询一行数据
    def getOne(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchone()
        except Exception as ex:
            print(ex, ex)
        finally:
            self.close()

    # 从数据库表中查询所有行数据
    def getList(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            self.cursor.execute(sql, args)
            return self.cursor.fetchall()
        except Exception as ex:
            print(ex, ex)
        finally:
            self.close()

    # 对数据库进行增,删,改
    def executeDML(self, sql, *args):
        try:
            self.connection = pymysql.connect(**MySQLHelper.config)
            self.cursor = self.connection.cursor()
            # 返回执行sql语句之后受影响的行数
            num = self.cursor.execute(sql, args)
            self.connection.commit()
            return num
        except Exception as ex:
            self.connection.rollback()
            print(ex, ex)
        finally:
            self.close()

    # 关闭资源
    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.connection:
            self.connection.close()

# 测试
if __name__ == "__main__":
    helper = MySQLHelper()
    # print(helper.executeDML("delete from test_table where id = 6"))
    print(helper.executeDML("delete from test_table where id = %s", 5))


