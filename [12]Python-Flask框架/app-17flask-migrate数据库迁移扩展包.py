# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# 在Flask中可以使用Flask-Migrate扩展,来实现数据迁移,并且集成到Flask-Script中,所有操作通过命令就能完成
# 为了导出数据库迁移命令,Flask-Migrate提供了一个MigrateCommand类,可以附加到flask-script的manager对象上
# 安装: pip install flask-migrate

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

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

app.config.from_object(Config)

# 创建数据库SQLAlchemy工具对象: flask_sqlalchemy
db = SQLAlchemy(app)

# 创建数据库迁移工具对象: flask_migrate
# 第一个参数: Flask的实例, 第二个参数: SQLAlchemy数据库实例
migrate = Migrate(app, db)

# 创建脚本启动命令管理类对象: flask_script
manager = Manager(app)
# 向manager对象中添加数据库的操作命令
manager.add_command('db',MigrateCommand)  # 此处db与数据库SQLAlchemy工具对象db不是一个意思,这个db只是操作命令的一个名字


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
    # 通过manager对象启动flask程序
    manager.run()


#############################################################################################
# 终端命令操作:
# 创建迁移仓库(初始化): python xxx.py db init  ---> 仅可调用一次
# 生成迁移文件: python xxx.py db migrate  ---> 相当于Django中的: python manage.py makemigrations
# 生成数据库表: python xxx.py db upgrade  ---> 相当于Django中的: python manage.py migrate
# 如: python xxx.py db upgrade -m '此次操作的说明信息'
# 回退数据库: python xxx.py db downgrade '回退的版本号(查看历史记录)'
# 查看历史记录: python xxx.py db history


