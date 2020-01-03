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



### django.forms.Form 基本表单类:
from django import forms
# initial: 初始默认值,input框里面的初始值
class LoginForm1(forms.Form):
    username = forms.CharField(
        min_length=8,
        label="用户名",
        initial="张三"
    )
    pwd = forms.CharField(min_length=6, label="密码")

# error_messages: 表单错误信息提示
class LoginForm2(forms.Form):
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

# password: 表单密码框
class LoginForm3(forms.Form):
    pwd = forms.CharField(
        min_length=6,
        label="密码",
        widget=forms.widgets.PasswordInput(attrs={'class': 'c1'}, render_value=True)
    )

# radioSelect: 表单单选框,单选值为字符串
class LoginForm4(forms.Form):
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

# Select: 表单单选
class LoginForm5(forms.Form):
    hobby = forms.fields.ChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
        label="爱好",
        initial=3,
        widget=forms.widgets.Select()
    )
# Select: 表单多选
class LoginForm6(forms.Form):
    hobby = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"), ),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.SelectMultiple()
    )

# checkbox: 表单单选
class LoginForm7(forms.Form):
    keep = forms.fields.ChoiceField(
        label="是否记住密码",
        initial="checked",
        widget=forms.widgets.CheckboxInput()
    )
# checkbox: 表单多选
class LoginForm8(forms.Form):
    hobby = forms.fields.MultipleChoiceField(
        choices=((1, "篮球"), (2, "足球"), (3, "双色球"),),
        label="爱好",
        initial=[1, 3],
        widget=forms.widgets.CheckboxSelectMultiple()
    )



from django.forms import Form
from django.forms import fields
from django.core.validators import RegexValidator
## 1. 内置校验器
class MyForm(Form):
    user = fields.CharField(
        validators=[RegexValidator(r'^[0-9]+$', '请输入数字'), RegexValidator(r'^159[0-9]+$', '数字必须以159开头')],
    )



### 2. 自定义验证函数
import re
from django.forms import Form
from django.forms import widgets
from django.forms import fields
from django.core.exceptions import ValidationError

## 验证规则
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



### 3. Hook方法: 局部钩子 ---> 在Fom类中定义 clean_字段名() 方法，就能够实现对某个字段进行校验
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

    # 定义局部钩子,用来校验username字段
    def clean_username(self):
        value = self.cleaned_data.get("username")
        if "666" in value:
            raise ValidationError("光喊666是不行的")
        else:
            return value



### 4. Hook方法: 全局钩子 ---> 在Fom类中定义 clean() 方法,就能够实现对所有字段进行校验
class LoginForm2(forms.Form):

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

    # 定义全局的钩子,用来校验密码和确认密码字段是否相同
    def clean(self):
        password_value = self.cleaned_data.get('password')
        re_password_value = self.cleaned_data.get('re_password')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            # raise ValidationError('两次密码不一致')


