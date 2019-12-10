# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-12 9:59

from django import forms

# 定义一个注册的form类
class RegForm(forms.Form):

    username = forms.CharField(
        max_length=16,
        label="用户名",
        error_messages={
            "max_length":"用户名最长16位",
            "required": "用户名不能为空",
        }
    )
    password = forms.CharField(
        min_length=6,
        label="密码",
        widget= forms.widgets.PasswordInput(),
        error_messages={
            "min_length":"用户名最少6位",
            "required": "密码不能为空",
        }
    )

    re_password = forms.CharField(
        max_length=6,
        label="确认密码",
        widget= forms.widgets.PasswordInput(),
    )

    email = forms.EmailField(
        label="邮箱",
        widget= forms.widgets.EmailInput(),
        error_messages={
            "invalid": "邮箱格式不正确",
        }
    )

### 把定义的Form类生产form表单:
## urls.py
# from app01 import views
# url(r'^/reg/',views.register)
## views.py
# from django.shortcuts import render
# def register(request):
#     regForm_obj = RegForm()
#     return render(request,"register.html",{"regForm_obj":regForm_obj})
## templates/register.html
# <form action="/reg/">
#     {% csrf_token %}
#     {{ regForm_obj.username.lable }}
#     {{ regForm_obj.username}}
#     {{ regForm_obj.password.lable }}
#     {{ regForm_obj.password}}
#     {{ regForm_obj.email.lable }}
#     {{ regForm_obj.email}}
# </form>
# <form action="/reg/">
#     {% csrf_token %}
#     {% for field in regForm_obj.fields %}
#         {{ field.lable }}
#         {{ field }}
#     {% end for %}
# </form>


# ********************************************************************************* #
### Form类表单:
from django import forms
# initial  初始值，input框里面的初始值
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        initial="张三"  # 设置默认值
    )
    pwd = forms.CharField(min_length=6, label="密码")

# error_messages  重写错误信息:
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        initial="张三",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短8位"
        }
    )
    pwd = forms.CharField(min_length=6, label="密码")

# password  密码
class LoginForm(forms.Form):
    pwd = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True)
    )

# radioSelect  单选值为字符串
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        initial="张三",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短8位"
        }
    )
    pwd = forms.CharField(min_length=6, label="密码")
    gender = forms.fields.ChoiceField(
        choices=((1, "男"), (2, "女"), (3, "保密")),
        label="性别",
        initial=3,
        widget=forms.widgets.RadioSelect()
    )

# Select  单选
class LoginForm(forms.Form):
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
# Select  多选
class LoginForm(forms.Form):
    hobby = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )

# checkbox  单选
class LoginForm(forms.Form):
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
# checkbox 多选
class LoginForm(forms.Form):
    hobby = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )


### Django Form 所有内置字段:
# Field
#     required=True,               是否允许为空
#     widget=None,                 HTML插件
#     label=None,                  用于生成Label标签或显示内容
#     initial=None,                初始值
#     help_text='',                帮助信息(在标签旁边显示)
#     error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
#     validators=[],               自定义验证规则
#     localize=False,              是否支持本地化
#     disabled=False,              是否可以编辑
#     label_suffix=None            Label内容后缀
# CharField(Field)
#     max_length=None,             最大长度
#     min_length=None,             最小长度
#     strip=True                   是否移除用户输入空白
# IntegerField(Field)
#     max_value=None,              最大值
#     min_value=None,              最小值
# FloatField(IntegerField)
# DecimalField(IntegerField):
#     max_value=None,              最大值
#     min_value=None,              最小值
#     max_digits=None,             总长度
#     decimal_places=None,         小数位长度
# BaseTemporalField(Field)
#     input_formats=None          时间格式化
# DateField(BaseTemporalField)    格式：2015-09-01
# TimeField(BaseTemporalField)    格式：11:12
# DateTimeField(BaseTemporalField)格式：2015-09-01 11:12
# DurationField(Field)            时间间隔：%d %H:%M:%S.%f
# RegexField(CharField)
#     regex,                      自定制正则表达式
#     max_length=None,            最大长度
#     min_length=None,            最小长度
#     error_message=None,         忽略，错误信息使用 error_messages={'invalid': '...'}
# EmailField(CharField):
# FileField(Field):
#     allow_empty_file=False     是否允许空文件
# ImageField(FileField)
# 注：需要PIL模块，pip3 install Pillow
# 以上两个字典使用时，需要注意两点：
# - form表单中 enctype="multipart/form-data"
# - view函数中 obj = MyForm(request.POST, request.FILES)
# URLField(Field)
# BooleanField(Field)
# NullBooleanField(BooleanField)
# ChoiceField(Field)
#     choices=(),                选项，如：choices = ((0,'上海'),(1,'北京'),)
#     required=True,             是否必填
#     widget=None,               插件，默认select插件
#     label=None,                Label内容
#     initial=None,              初始值
#     help_text='',              帮助提示
# ModelChoiceField(ChoiceField)
#     django.forms.models.ModelChoiceField
#     queryset,                  # 查询数据库中的数据
#     empty_label="---------",   # 默认空显示内容
#     to_field_name=None,        # HTML中value的值对应的字段
#     limit_choices_to=None      # ModelForm中对queryset二次筛选
# ModelMultipleChoiceField(ModelChoiceField)
#     django.forms.models.ModelMultipleChoiceField
# TypedChoiceField(ChoiceField)
#     coerce = lambda val: val   对选中的值进行一次转换
#     empty_value= ''            空值的默认值
# MultipleChoiceField(ChoiceField)
# TypedMultipleChoiceField(MultipleChoiceField)
#     coerce = lambda val: val   对选中的每一个值进行一次转换
#     empty_value= ''            空值的默认值
# ComboField(Field)
#     fields=()                  使用多个验证，如下：即验证最大长度20，又验证邮箱格式
#     fields.ComboField(fields=[fields.CharField(max_length=20), fields.EmailField(),])
# MultiValueField(Field)
# PS: 抽象类，子类中可以实现聚合多个字典去匹配一个值，要配合MultiWidget使用
# SplitDateTimeField(MultiValueField)
#     input_date_formats=None,   格式列表：['%Y--%m--%d', '%m%d/%Y', '%m/%d/%y']
#     input_time_formats=None    格式列表：['%H:%M:%S', '%H:%M:%S.%f', '%H:%M']
# FilePathField(ChoiceField)     文件选项，目录下文件显示在页面中
#     path,                      文件夹路径
#     match=None,                正则匹配
#     recursive=False,           递归下面的文件夹
#     allow_files=True,          允许文件
#     allow_folders=False,       允许文件夹
#     required=True,
#     widget=None,
#     label=None,
#     initial=None,
#     help_text=''
# GenericIPAddressField
#     protocol='both',           both,ipv4,ipv6支持的IP格式
#     unpack_ipv4=False          解析ipv4地址，如果是::ffff:192.0.2.1时候，可解析为192.0.2.1， PS：protocol必须为both才能启用
# SlugField(CharField)           数字，字母，下划线，减号（连字符）
# UUIDField(CharField)           uuid类型


### 字段校验:
## 1. RegexValidator验证器
from django.forms import Form
from django.forms import fields
from django.core.validators import RegexValidator
class MyForm(Form):
    user = fields.CharField(
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
    )
## 2. 自定义验证函数
import re
from django.forms import Form
from django.forms import widgets
from django.forms import fields
from django.core.exceptions import ValidationError

# 验证规则
def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')

class PublishForm(Form):
    title = fields.CharField(max_length=20,
                             min_length=5,
                             error_messages={'required': '标题不能为空',
                                             'min_length': '标题最少为5个字符',
                                             'max_length': '标题最多为20个字符'},
                             widget=widgets.TextInput(attrs={'class': "form-control",
                                                             'placeholder': '标题5-20个字符'}))

    # 使用自定义验证规则
    phone = fields.CharField(validators=[mobile_validate, ],
                             error_messages={'required': '手机不能为空'},
                             widget=widgets.TextInput(attrs={'class': "form-control",
                                                             'placeholder': u'手机号码'}))
    email = fields.EmailField(required=False,
                              error_messages={'required': u'邮箱不能为空','invalid': u'邮箱格式错误'},
                              widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': u'邮箱'}))

## 3. Hook方法: 局部钩子 ---> 在Fom类中定义 clean_字段名() 方法，就能够实现对特定字段进行校验
class LoginForm(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        initial="张三",
        error_messages={
            "required": "不能为空",
            "invalid": "格式错误",
            "min_length": "用户名最短8位"
        },
        widget=forms.widgets.TextInput(attrs={"class": "form-control"})
    )

    # 定义局部钩子，用来校验username字段
    def clean_username(self):
        value = self.cleaned_data.get("username")
        if "666" in value:
            raise ValidationError("光喊666是不行的")
        else:
            return value
## 4. Hook方法: 全局钩子 --->
class LoginForm(forms.Form):

    password = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
    )
    re_password = forms.CharField(
        min_length=6,
        label="确认密码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'form-control'}, render_value=True)
    )

    # 定义全局的钩子，用来校验密码和确认密码字段是否相同
    def clean(self):
        password_value = self.cleaned_data.get('password')
        re_password_value = self.cleaned_data.get('re_password')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            raise ValidationError('两次密码不一致')


