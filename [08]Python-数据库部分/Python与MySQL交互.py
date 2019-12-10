# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 9:35

## Python程序中使用MySQL数据库,需要安装导入PyMySQL模块
# 安装PyMySQL模块: pip install PyMySQL
# 导入PyMySQL模块: import pymysql

### 创建Connection对象: pymysql.connect(参数列表)
## 参数列表说明:
# host:     连接的MySQL主机地址,如果是本机就是localhost
# port:     连接的MySQL主机端口号,默认是3306
# db:       数据库名称
# user:     连接的用户名
# password: 连接的用户名的密码
# charset:  通信采用的编码方式,默认是"gb2312",要求与数据库创建时指定的编码一致,否则中文会乱码

### Connection对象方法: 作用:建立与数据库的链接
# close()       关闭连接
# commit()      事务，需要提交才会生效
# rollback()    事务，放弃之前的操作
# cursor()      返回Cursor对象，用于执行sql语句并获得结果

### 创建Cursor对象: pymysql.connect(参数列表).cursor()

### Cursor对象方法：作用:执行sql语句
# close()                               关闭
# execute(operation [, parameters ])    执行sql语句，返回受影响的行数
# fetchone()                            执行查询语句时，获取查询结果集的第一个行数据，返回一个元组
# next()                                执行查询语句时，获取当前行的下一行
# fetchall()                            执行查询语句时，获取结果集的所有行，一行构成一个元组，再将这些元组装入一个元组返回
# scroll(value[,mode])                  将行指针移动到某个位置
# mode表示移动的方式
# mode的默认值为relative，表示基于当前行移动到value，value为正则向下移动，value为负则向上移动
# mode的值为absolute，表示基于第一条数据的位置，第一条数据的位置为0

#############################################################################################
### Python与MySQL数据库交互流程:
import pymysql
# 1.创建Connection对象
connection = pymysql.connect("localhost","root","root","test")
# 2.创建Cursor对象
cursor = connection.cursor()
# sql语句
sql = "select * from test_table"
# 3.cursor执行sql语句,返回一个受影响的数据条数
num = cursor.execute(sql)
print(num)
# 获取cursor执行sql语句后的结果集的第一行数据(列表形式)
tuple = cursor.fetchone()
print(tuple)
# 获取cursor执行sql语句后的结果集的所有行数据(列表形式)
tuple = cursor.fetchall()
print(tuple)
# 4.关闭游标和连接
cursor.close()
connection.close()

################################################################################################
### Python与MySQL数据库交互封装:
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

