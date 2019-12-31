# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-31 10:56

### 第三方验证码的使用与配置:
## 1.安装: pip install django-simple-captcha

## 2.将captcha安装在settings的installed_apps里面:
# INSTALLED_APPS = [
#     # 配置第三方验证码
#     'captcha',
# ]

## 3.将captcha配置url: 项目/urls.py
# url(r'^captcha/',include('captcha.urls')),

## 4.迁移同步，生成captcha所依赖的表:
# python manage.py makemigrations
# python manage.py migrate

## 5.将captcha字段在forms类当中进行设置: 如 注册页面需要使用验证码 users/forms.py
from django import forms
from captcha.fields import CaptchaField
# 注册form表单
class UserRegisterForm(forms.Form):
    email = forms.EmailField(required=True,min_length=10,error_messages={
        'required':'邮箱必须填写',
        'min_length':'邮箱最小长度10'
    })
    password = forms.CharField(required=True,min_length=3,error_messages={
        'required': '密码必须填写',
        'min_length': '密码最小长度3'
    })
    captcha = CaptchaField()  # 验证码!!!

## 6.在后台逻辑当中，get请求里面实例化我们的form,将form对象返回到页面
# def user_register(request):
#     if request.method == 'GET':
#         # 此处实例化forms类,目的不是为了验证,而是为了使用验证码
#         user_register_form = UserRegisterForm()
#         return render(request,'register.html',{'user_register_form':user_register_form})

## 7.在html页面上获取验证码: {{ user_register_form.captcha }}



