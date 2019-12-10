# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-10 14:51

### Django框架内置auth认证模块: 主要方法如下
from django.contrib.auth import authenticate, login, logout
## authenticate()  # 验证用户名与密码是否正确,提供username和password两个关键字参数
# user = authenticate(username="username", password= "password")  # 调用该函数,如果验证成功,返回一个User对象,如果验证不成功,返回一个匿名用户对象(AnonymousUser)

## login()  # 接受HttpRequest对象和认证了的User对象
# login(request, user_obj)  # 调用该函数,把验证成功后的User对象封装到request.user中
# 注意：只要使用login(request, user_obj),request.user就能拿到当前登录的用户对象。否则request.user得到的是一个匿名用户对象（AnonymousUser Object）。

## logout()  # 接受Httprequest对象
# logout(request)  # 调用该函数,将当前请求的session信息会全部删除,即退出登陆

## is_authenticated()  # 用来判断当前请求是否通过认证(判断是否登录) ---> request.user.is_authenticated()



## login_requierd()  # auth提供的装饰器工具,用来快捷的给某些视图函数添加登陆校验
# from django.contrib.auth.decorators import login_required
# @login_required
# def my_view(request):
#     pass
# 注: 若用户没有登录,则会跳转到django默认的 登录URL '/accounts/login/' 并传递当前访问url的绝对路径(登陆成功后,会重定向到该路径)
# 自定义登陆的url,则在settings.py文件中通过LOGIN_URL进行修改:
# LOGIN_URL = '/user/login/'  # 这里配置项目登录页面的路由

## create_user()  # auth 提供的一个创建新用户的方法，需要提供必要参数（username、password）等
# from django.contrib.auth.models import User
# user = User.objects.create_user(username='用户名',password='密码',email='邮箱',)

## create_superuser()  # auth 提供的一个创建新的超级用户的方法，需要提供必要参数（username、password）等
# from django.contrib.auth.models import User
# user = User.objects.create_superuser(username='用户名',password='密码',email='邮箱',)

## check_password(raw_password)  # auth 提供的一个检查密码是否正确的方法，需要提供当前请求用户的密码。密码正确返回True，否则返回False
# result = user_obj.check_password('密码')

## set_password(raw_password)  # auth 提供的一个修改密码的方法，接收 要设置的新密码 作为参数
# user_obj.set_password('新密码')
# user_obj.save()



### 扩展默认的auth_user表,并添加属性信息[两种方式]
# 第一种: 在models文件定义个用户类(表),一对一关联django框架的auth_user表
# 注意: to="User" 与 to=User 的区别: to="User" 在当前文件中找这个User模型类
from django.db import models
from django.contrib.auth.models import User
class UserInfo():  # class User(AbstractUser):
    '''用户模型类'''
    user = models.OneToOneField(to=User)

# 第二种: 可以定义一个抽象模型基类,可供模型类继承使用
from django.db import models
class BaseModel(models.Model):
    '''抽象模型基类'''
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,verbose_name='删除标记')
    class Meta:
        abstract = True  # 说明是一个抽象基类

# 1.在应用app的models.py中定义用户模型类继承AbstractUser模块和继承定义的抽象基类
from django.contrib.auth.models import AbstractUser
class UserInfo(AbstractUser, BaseModel):  # class User(AbstractUser):
    '''用户模型类'''
    create_time = models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    update_time = models.DateTimeField(auto_now_add=True,verbose_name='更新时间')
    is_delete = models.BooleanField(default=False,verbose_name='删除标记')
    class Meta:
        db_table = 'df_user'
        verbose_name = '用户'
        verbose_name_plural = verbose_name

# 2.如上扩展内置的auth_user表之后,一定要在settings.py中告诉Django,现在使用新定义的UserInfo表来做用户认证表
AUTH_USER_MODEL = "app应用名称.UserInfo"
# settings配置默认检查用户是否活跃状态is_axtive,不活跃返回None
# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.ModelBackend']
# settings配置设置不检查用户的活跃状态is_active
# AUTHENTICATION_BACKENDS = ['django.contrib.auth.backends.AllowAllUsersModelBackend']





