# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2020-01-06 15:06


### Django修改APP应用名称在Admin后台显示的名称
# 注: Admin后台默认显示的APP应用名称为创建APP应用时的名称

## 第一种方式:
# 1. 修改APP应用目录下的app.py文件, 添加如下内容, verbose_name
class PostConfig(AppConfig):
    name = 'post'
    verbose_name = '博客管理1'  # APP应用名称在Admin后台设置为中文名称显示
# 2. 修改APP应用目录下的__init__.py文件: 添加如下内容, default_app_config
default_app_config = 'post.apps.PostConfig'  # 配置Admin后台定制APP应用名称的类路径

## 第二种方式: 直接修改APP应用下的__init__.py文件,添加如下内容
# -*- coding:utf-8 -*-
from django.apps import AppConfig
import os

default_app_config = 'post.PostConfig'
VERBOSE_APP_NAME = "博客管理2"  # APP应用名称在Admin后台设置为中文名称显示

def get_current_app_name(_file):
    return os.path.split(os.path.dirname(_file))[-1]

class PostConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME




