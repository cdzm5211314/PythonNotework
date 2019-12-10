# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-16 17:32

### 管理站点(admin): http://localhost:8000/admin
## 创建后台管理员账号:
# python manage.py createsuperuser
# Username: 输入用户名，默认为系统账户名
# Email Address: 电子邮件
# Password: 密码
# Password(agian): 重复密码


### setting.py设置要使用的数据库类型
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',  # 使用的数据库类型
#         'NAME': 'pythondb',                    # 数据库名称
#         'HOST': 'localhost',                   # IP地址
#         'POST': 3306,                          # 端口号
#         'USER': 'root',                        # 用户名
#         'PASSWORD': 'root',                    # 密码
#     }
# }

### 在app应用下的models.py中定义模型类
# from django.db import models
# class Book(models.Model):
#     name = models.CharField(max_length=64)
#     author = models.CharField(max_length=20)

### 生成迁移文件,执行迁移文件
# python manage.py makemigrations
# python manage.py migrate


### 在app应用下的admin.py中完成模型类注册
## 使用内置方法完成注册
# from django.contrib import admin
# from .models import Book
# admin.site.register(Book)  # 注册

## 自定义数据库管理页面并注册:
from django.contrib import admin
from django.utils.safestring import mark_safe
# from .models import Book
# @admin.register(Book)  # 简写注册,等同于以下的: admin.site.register(Book, BookAdmin)
class BookAdmin(admin.ModelAdmin):
    def deletes(self):
        return mark_safe("<a href=''>删除</a>")
    list_display = ["name", "author",deletes]  # 定制显示的列: 展示模型字段或自定义函数名称
    list_display_link = ["author"]  # 定制列可以点击跳转: 点击哪个字段进入编辑页面
    list_filter = ["author"]  # 定制右侧快速筛选栏: 根据字段过滤
    search_fields = ["name"]  # 定制快速搜索栏:
    ## 批量操作
    def patch_init(self, request, queryset):
        queryset.update(name = "zhangsan")
    patch_init.short_description = "批量初始化name的名字"
    actions = ["patch_init"]
# admin.site.register(Book, BookAdmin)  # 注册


### 定制信息字段详情:
## list_display : 定义在 列表页 上显示的字段们
# 取值：由属性名组成的元组或列表
# 2.list_display_links : 定义在列表页中也能够连接到详情页的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须要出现在list_display中
# 3.list_editable : 定义在列表页中就允许修改的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须出现在list_display中但不能出现在list_display_links中
# 4.search_fields : 添加允许被搜索的字段们
# 取值：由属性名组成的元组或列表
# 5.list_filter : 列表页的右侧增加过滤器，实现快速筛选
# 取值：由属性名组成的元组或列表
# 6.date_hierarchy : 列表页的顶部增加时间选择器，取值必须是DateField 或 DateTimeField的列名
# 7.fields : 在详情页中，指定显示哪些字段并按照什么样的顺序显示
# 取值：由属性名组成的元组或列表
# 8.fieldsets : 在详情页面中，对字段们进行分组显示的
# 注意：fieldsets 与 fields 是不能共存的
# 取值：
# fieldsets = (
#     #分组1
#     ('分组名称',{
#         'fields':('属性1','属性2'),
#         'classes':('collapse',)
#     }),
#     #分组2
#     ()
# )





