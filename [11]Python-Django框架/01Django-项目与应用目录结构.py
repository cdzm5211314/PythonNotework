# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 10:25

## Django框架模式: MTV
# M ：Models ---> 数据库模型
# T ：Templates ---> 模板(网页)
# V ：Views ---> 视图


## Django框架安装:
# pip install django            安装最新版本
# pip install django==1.11.11   安装指定版本

## 进入Python终端交互模式:
# python 或 ipython


### 创建Django项目:
# django-admin startproject 项目名


### Django项目的目录结构:
## manage.py: 包含执行django中的各项操作的指令(子命令) 如：
# 启动服务：python manage.py runserver
# 创建应用：python manage.py startapp 应用名称
# 创建管理员：python manage.py createsuperuser
# 等 ...

## 主目录: (与项目名称一致的目录)
# 1. __init__.py: 项目的初始化文件，服务被启动，该文件自动被运行
# 2.urls.py: 项目的基础url配置文件(基础的路由配置)
# 3.wsgi.py: Web Server Gateway Interface, Web服务网关接口
# 4.settings.py: 项目的配置文件
# 4.1) BASE_DIR: 获取当前项目的绝对路径
# 4.2) DEBUG: 是否启用调试模式
# True: 启用调试模式（开发环境中推荐）
# False: 不启用调试模式（生产环境中推荐）
# 4.3) ALLOWED_HOSTS:  设置允许访问到本项目的地址列表
# 如果为空的话，只有本机(localhost/127.0.0.1)才能访问
# 如果允许在局域网中被外部机器访问的话：推荐写 ['*'],表示任何能够表示该机器的地址都能访问到当前项目
# 如果允许被其他机器访问的话，启动服务时，必须使用以下方式： python manage.py runserver 0.0.0.0:端口号
# 4.4) INSTALLED_APPS: 指定已安装的应用，如果有自定义应用的话，需要在此注册
# 4.5) MIDDLEWARE: 中间件，如果有自定义的中间件，需要在此注册
# 4.6) ROOT_URLCONF: 用于指定项目的基础路由配置文件
# 4.7) TEMPLATES: 指定模板的信息
# 4.8) DATABASES: 指定数据库的信息
# 配置数据库信息: 首先要创建数据库 ---> create database aixianfeng default charset=utf8;
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME':  'aixianfeng',  # 数据库名称
        'HOST': 'localhost',    # IP地址
        'PORT': 3306,           # 端口号
        'USER': 'root',         # 数据库用户名
        'PASSWORD': 'root',     # 数据库密码
    }
}
# 4.9) LNAGUAGE_CODE: 语言设置，如果需要中文的话，允许将值更改为 "zh-Hans"
# 4.10) TIME_ZONE: 指定时区，中国时区的话，允许将值设置为 "Asia/Shanghai"




### 项目的应用:
# 应用就是网站中的一个独立的程序模块,在Django中,主目录一般不处理用户的具体请求,主目录主要做的是项目的初始化以及请求的分发(分布式请求处理)，而具体的请求由各个应用去处理
# 创建应用APP的命令: python manage.py startapp 应用名称
# 注册应用APP: 在settings.py中有个变量INSTALLED_APPS,在列表中追加自定义应用名称
INSTALLED_APPS = [
    'app01.apps.App01Config',
    '应用名称',
]
## 项目的应用目录结构:
# 1.migrations: 目录存放数据的中间文件
# 2.__init__.py: 应用的初始化文件
# 3.admin.py: 应用的后台管理配置文件
# 4.app.py: 应用的属性配置文件
# 5.models.py: Models与模型相关的映射文件
# 6.tests.py: 应用的单元测试文件
# 7.views.py: 定义视图处理函数的文件



