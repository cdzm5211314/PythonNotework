# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2020-01-02 14:09


### 自定义模版全局上下文步骤:  实现数据的共享

## 1. 在APP应用下创建.py文件,名称任意,如: my_content_processor.py

## 2. 在my_content_processor.py文件中定义功能函数
# def functiondemo(request):

#     return {"key":"value"}  # 以字典的数据形式返回

## 3. 在settings.py文件中配置函数路径
# TEMPLATES = [
#     {
#         'BACKEND': 'django.template.backends.django.DjangoTemplates',
#         'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 如果配置了目录,则按照写好的路径去找模板
#         # 'DIRS': [ ],  # 如果未配置目录,则会自动的到每个应用中查找templates的目录来作为模板的存放目录
#         'APP_DIRS': True,  # True表示搜索应用中的 templates 目录
#         'OPTIONS': {
#             'context_processors': [
#                 'django.template.context_processors.debug',
#                 'django.template.context_processors.request',
#                 'django.contrib.auth.context_processors.auth',
#                 'django.contrib.messages.context_processors.messages',
#                 'django.template.context_processors.media',
#                 # 定义的全局上下文函数路径
#                 "APP应用名称.自定义的上下文文件名称.函数名称",
#             ],
#         },
#     },
# ]


## 4.func.html文件,每个被访问的.html文件都能获取这个值
# {{ key }}



