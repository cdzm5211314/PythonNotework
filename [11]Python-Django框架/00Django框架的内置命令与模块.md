### Django框架内置命令:
- django-admin startproject projectname                 # 创建django工程项目
- python manage.py startapp appname                     # 创建app应用
- python manage.py makemigrations                       # 生成迁移文件
- python manage.py migrate                              # 执行迁移文件
- python manage.py createsuperuser                      # 创建超级管理员用户
- python manage.py flush                                # 清空数据库[yes or no]
- python manage.py dumpdata > mysite_all_data.json      # 导出所有数据
- python manage.py loaddata mysite_all_data.json        # 导入所有数据
- python manage.py dumpdata appname > appname.json      # 导出app应用的数据
- python manage.py loaddata appname.json                # 导入app应用的数据
- python manage.py runserver IP/PORT                    # 启动django工程项目
- python manage.py shell                                # 项目环境终端
- python manage.py dbshell                              # 数据库命令行



### Django框架内置模块与函数: pip install django
- from django.shortcuts import HttpResponse # 返回一个字符串
- from django.shortcuts import render # 返回模版信息
- from django.shortcuts import redirect # 重定向到另一个url
- from django.shortcuts import reverse # 反向解析url地址
- from django.core.urlresolvers import reverse # 反向解析url地址
- from django.http import HttpResponse # 返回一个字符串
- from django.http import JsonResponse # 返回前端页面Json类型数据(即Python字典类型数据)
- from django.conf.urls import url,include # url路由与url路由分发
- from django.conf import settings  # django框架的settings.py配置信息 
- from django.db import models # 模型类
- from django.db.models import Q, F  # ORM查询操作
- from django.contrib import admin # 后台管理
- from django.views.generic import View # 类视图
- from django import forms  # forms.form表单验证模块,forms.ModelForm表单与model模型类结合
- from django.contrib.auth.models import AbstractUser # 用户认证模块模型类(可扩展)
- from django.contrib.auth import authenticate, login, logout, is_authenticated  # 用户信息验证方法,登陆方法,注销方法,用户是否登录验证
- from django.contrib.auth.decorators import login_required  # 登陆验证装饰器
- from django.core.mail import send_mail # 发送邮件
- from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage  # 数据分页显示


