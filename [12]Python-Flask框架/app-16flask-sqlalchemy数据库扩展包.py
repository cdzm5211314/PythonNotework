# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# SQLAlchemy是一个关系型数据库框架,它提供了高层的ORM和底层的原生数据库的操作
# flask-sqlalchemy是一个简化了SQLAlchemy操作的flask扩展
# 安装: pip install flask-sqlalchemy
# 安装: pip install flask-mysqldb

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


# 第二种方式(常用): 使用创建类配置参数,如 Config
class Config(object):
    '''配置参数,相当于Django中的settings信息'''
    DEBUG = 'True'  # 开启Flask程序的调试模式
    # SQLAlchemy配置参数: 设置链接数据库的URL
    SQLALCHEMY_DATABASE_URI = "mysql://root:root@127.0.0.1:3306/flaskdemo"
    # SQLAlchemy配置参数: 设置sqlalchemy自动更新跟踪数据库
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    # SQLAlchemy配置参数: 数据库查询时显示原始SQL语句(程序调试的时候可以使用)
    SQLALCHEMY_ECHO = True
    # SQLAlchemy配置参数: 设置每次请求结束后会自动提交数据库中的改动(官方不推荐使用)
    # SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    # form表单需要配置secret_key信息,form表单需要添加csrf_token
    SECRET_KEY = "FlaskTest"

app.config.from_object(Config)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@host:port/datebase?charset=utf8'
# 创建数据库SQLAlchemy工具对象
db = SQLAlchemy(app)


## 数据库表名的常见规范
# ihome -> ih_user  数据库名缩写_表名
# tbl_user  tbl_表名


# 定义数据库模型类
class User(db.Model):
    '''用户表'''
    __tablename__ = 'tbl_users'  # 定义数据库的表名,默认是以模型类名作为表名
    id = db.Column(db.Integer, primary_key=True)  # 整型的主键,默认会设置为自增主键
    name = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(128), unique=True)
    password = db.Column(db.String(128))
    role_id = db.Column(db.Integer, db.ForeignKey('tbl_roles.id'))  # 表名的某个字段

    def __repr__(self):
        '''定义之后,可以先显示对象的时候更直观'''
        return 'User object: name = %s' % self.name


class Role(db.Model):
    '''角色表'''
    __tablename__ = 'tbl_roles'  # 定义数据库的表名
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    users = db.relationship('User', backref='role')

    def __repr__(self):
        return 'Role object: name = %s' % self.name


if __name__ == '__main__':
    # 原始方法: 通过db(SQLAlchemy工具对象)操作数据库
    db.drop_all()    # 清除数据库表的所有数据(一般在第一次使用时操作)
    db.create_all()  # 创建模型类所对应的数据库表

    # 1.数据库表添加数据
    role1 = Role(name='admin')
    # session记录对象任务
    db.session.add(role1)  # 插入一条数据
    # 提交任务到数据库表中
    db.session.commit()

    role2 = Role(name='stuff')
    db.session.add(role2)  # 再次插入一条数据
    db.session.commit()

    us1 = User(name='wang', email='wang@163.com', password='123456', role_id=role1.id)
    us2 = User(name='zhang', email='zhang@189.com', password='201512', role_id=role2.id)
    us3 = User(name='chen', email='chen@126.com', password='987654', role_id=role2.id)
    us4 = User(name='zhou', email='zhou@163.com', password='456789', role_id=role1.id)
    db.session.add_all([us1, us2, us3, us4])  # 一次插入多条数据
    db.session.commit()

    # 2.数据库表查询数据:
    # db.session.query('模型类名字').all() ---> SQLAlchemy的原始方法,如下是flask-sqlalchemy封装的方法
    Role.query.all()    # 查询表中的所有数据,返回一个对象列表
    Role.query.get()    # 根据主键ID值查询一条数据,返回一个对象,如果主键不存在没有返回内容
    Role.query.first()  # 查询表中的第一条数据,返回一个对象

    User.query.filter_by(name='wang').all()     # 查询表中name字段值为'wang'的所有数据,返回一个对象列表
    User.query.filter(User.name=='wang').all()  # 查询表中name字段值为'wang'的所有数据,返回一个对象列表
    User.query.filter_by(name='wang').first()   # 查询表中name字段值为'wang'的第一条数据,返回一个对象
    User.query.filter_by(User.name.endswith('g')).all()  # 查询表中名字结尾为'g'的所有数据,返回一个对象列表

    # 逻辑非,返回名字不等于wang的所有数据
    User.query.filter(User.name != 'wang').all()

    # 逻辑与,返回名字不等于wang并且邮箱是以'163.com'结尾的所有数据
    from sqlalchemy import and_
    User.query.filter(and_(User.name != 'wang', User.email.endswith('163.com'))).all()

    # 逻辑或,返回名字不等于wang或者邮箱是以'163.com'结尾的所有数据
    from sqlalchemy import or_
    User.query.filter(or_(User.name != 'wang', User.email.endswith('163.com'))).all()

    # 逻辑取反,返回名字不等于'chen'的所有数据
    from sqlalchemy import not_
    User.query.filter(not_(User.name == 'chen')).all()

    # 3.数据库表删除数据: 先查询后删除
    user = User.query.first()
    db.session.delete(user)
    db.session.commit()

    # 4.数据库表更新数据: 先查询后更新
    # 第一种更新数据方式
    user = User.query.first()
    user.name = 'dong'
    db.session.commit()
    # 第二种更新数据方式
    User.query.filter_by(name='zhang').update({'name': 'li'})

    # 5.数据库表级联数据查询: 如, 角色表(一) 用户表(多)
    # 查询角色的所有用户：
    role1 = Role.query.get(1)  # 查询tbl_roles表id为1的角色
    role1.users  # 查询该角色的所有用户

    # 查询用户的所属角色
    # 查询用户表id为3的用户
    user1 = User.query.get(3)
    # 查询用户属于什么角色
    user1.role

#############################################################################################################
'''
# 常用的SQLAlchemy字段类型:
类型名:   	    Python中类型:	                说明:
Integer	        int	                            普通整数，一般是32位
SmallInteger	int	                            取值范围小的整数，一般是16位
BigInteger	    int或long	                    不限制精度的整数
Float	        float	                        浮点数
Numeric	        decimal.Decimal	                普通整数，一般是32位
String	        str	                            变长字符串
Text	        str	                            变长字符串，对较长或不限长度的字符串做了优化
Unicode	        unicode	                        变长Unicode字符串
UnicodeText	    unicode	                        变长Unicode字符串，对较长或不限长度的字符串做了优化
Boolean	        bool	                        布尔值
Date	        datetime.date	                时间
Time	        datetime.datetime	            日期和时间
LargeBinary	    str	                            二进制文件

# 常用的SQLAlchemy列选项:
选项名:	        说明:
primary_key	    如果为True，代表表的主键
unique	        如果为True，代表这列不允许出现重复的值
index	        如果为True，为这列创建索引，提高查询效率
nullable	    如果为True，允许有空值，如果为False，不允许有空值
default	        为这列定义默认值

# 常用的SQLAlchemy关系选项:
选项名:    	    说明:
backref	        在关系的另一模型中添加反向引用
primary join	明确指定两个模型之间使用的联结条件
uselist	        如果为False，不使用列表，而使用标量值
order_by	    指定关系中记录的排序方式
secondary	    指定多对多中记录的排序方式
secondary join	在SQLAlchemy中无法自行决定时，指定多对多关系中的二级联结条件

# 常用的SQLAlchemy查询过滤器:
过滤器:        	说明:
filter()	    把过滤器添加到原查询上，返回一个新查询
filter_by()	    把等值过滤器添加到原查询上，返回一个新查询
limit()	        使用指定的值限定原查询返回的结果
offset()	    偏移(跳过几条数据)原查询返回的结果，返回一个新查询
order_by()	    根据指定条件对原查询结果进行排序，返回一个新查询
group_by()	    根据指定条件对原查询结果进行分组，返回一个新查询

# 常用的SQLAlchemy查询执行器:
方法:         	说明:
all()	        以列表形式返回查询的所有结果
first()	        返回查询的第一个结果，如果未查到，返回None
first_or_404()	返回查询的第一个结果，如果未查到，返回404
get()	        返回指定主键对应的行，如不存在，返回None
get_or_404()	返回指定主键对应的行，如不存在，返回404
count()	        返回查询结果的数量
paginate()	    返回一个Paginate对象，它包含指定范围内的结果

'''
