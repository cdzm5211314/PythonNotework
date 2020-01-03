### Django框架的表单: 
* 基本表单字段的类型与选项: forms.字段类型(字段选项)
    ```
    ## Field
        # required=True,               是否允许为空
        # widget=None,                 HTML插件
        # label=None,                  用于生成Label标签或显示内容
        # initial=None,                初始值
        # help_text='',                帮助信息(在标签旁边显示)
        # error_messages=None,         错误信息 {'required': '不能为空', 'invalid': '格式错误'}
        # validators=[],               自定义验证规则
        # localize=False,              是否支持本地化
        # disabled=False,              是否可以编辑
        # label_suffix=None            Label内容后缀
    ## CharField(Field)
        # max_length=None,             最大长度
        # min_length=None,             最小长度
        # strip=True                   是否移除用户输入空白
    ## DateField(BaseTemporalField)    格式：2015-09-01
    ## DateTimeField(BaseTemporalField)格式：2015-09-01 11:12
    ## FileField(Field):
        # allow_empty_file=False     是否允许空文件
    ## ChoiceField(Field)
        # choices=(),                选项，如：choices = ((0,'上海'),(1,'北京'),)
        # required=True,             是否必填
        # widget=None,               插件，默认select插件
        # label=None,                Label内容
        # initial=None,              初始值
        # help_text='',              帮助提示
    ...等
    ```

* 基本表单类(django.forms.Form): 示例
    ```
    # 1.在APP应用下创建forms.py文件
    # 2.在froms.py文件中定义一个类,并继承django.forms.Form类
    # 3.forms.py文件: 示例,定义一个登陆表单类,如 LoginForm
    from django import Form
    class LoginForm(forms.Form):
        # 属性就是表单字段,对应HTML里的每一个控件
        sname =forms.CharField(max_length=32, label="用户名")
        spasswd = forms.CharField(max_length=32, label="密码")
    
    # 4.login.html文件:
    <form action="/cd_01demoapp/login/" method="post">
        {% csrf_token %}
        {{ loginForm }}
        <input type="submit" value="登陆">
    </form>
    
    # 5.urls.py文件: 
    url(r'^login/$', views.login_view, name='login'),
    
    # 6.views.py文件: 把登陆表单类渲染到template模版的.html文件中
    from .forms import LoginForm
    def login_view(request):
        if request.method == "GET":  # get请求操作
            loginForm = LoginForm()
            return render(request, "login.html", {"loginForm": loginForm})
        else:  # post请求操作
            # 获取表单提交的数据
            loginForm = LoginForm(request.POST)
            # 校验表单提交的数据是否有效
            if loginForm.is_valid():
                # 获取一个字典类型的表单提交数据
                data = loginForm.cleaned_data()
                # 业务处理...
            return HttpResponse("基本表单获取数据")
            
    # 7.login.html文件: 接受视图传递过来表单数据
    <form action="/cd_01demoapp/login/" method="post">
        {% csrf_token %}
        {{ loginForm }}
        <input type="submit" value="登陆">
    </form>
    ```
    
* 模型表单类(django.forms.ModelForm): 示例
    ````
    # 1.models.py文件: 存在模型类
    from django.db import models
    class User(models.Model):
        uname = models.CharField(max_length=100, unique=True, verbose_name="用户名")
        upasswd = models.CharField(max_length=100, blank=True, null=True, verbose_name="密码")
    
    # 2.在APP应用下创建forms.py文件
    # 3.在froms.py文件中定义一个类,并继承django.forms.ModelForm类
    # 4.forms.py文件: 示例,定义一个用户类,如 UserModelForm
    from .models import *
    class UserForm(forms.ModelForm):
        class Meta:
            model = User  # 指向模型类
            fields = ["uname","upasswd"]  # 取出该模型类的哪些字段,在表单中显示
            # exclude = ["uname"]         # 除去该模型类的哪些字段,该模型类中的其他字段在表单中显示
     
    # 5.login.html文件:
    <form action="/cd_01demoapp/register/" method="post">
        {% csrf_token %}
        {{ userForm.uname.label }}: {{ userForm.uname }}}
        {{ userForm.upasswd.label }}: {{ userForm.upasswd }}}
        <input type="submit" value="注册">
    </form>
    
    # 6.urls.py文件: 
    url(r'^register/$', views.register_view, name='register'),
    
    # 7.views.py文件: 把注册表单类渲染到template模版的.html文件中
    from .forms import UserModelForm
    def register_view(request):
        if request.method == "GET":  # get请求操作
            userForm = UserForm()
            return render(request, "register.html", {"userForm": userForm})
        else:  # post请求操作
            # 获取表单提交的数据
            userForm = userForm(request.POST)
            # 校验表单提交的数据是否有效
            if userForm.is_valid():
                # 插入数据到数据库
                # user = userForm.save()  # 默认事务提交
                user = userForm.save(commit=False)  # 设置事务不提交
                # 其他业务处理...
                user.save()  # 再次提交
            return HttpResponse("模型表单数据入库")
            
    # 8.login.html文件: 接受视图传递过来表单数据
    <form action="/cd_01demoapp/login/" method="post">
        {% csrf_token %}
        {{ userForm.uname.label }}: {{ userForm.uname }}}
        {{ userForm.upasswd.label }}: {{ userForm.upasswd }}}
        <input type="submit" value="登陆">
    </form>
    ````
    
* 表单字段的验证方式:
    ```
    ## 第一种方式: 内置验证器
    ## 第二种方式: 自定义验证函数
    ## 第三种方式: Hook方法,局部钩子 ---> 在Fom类中定义 clean_字段名() 方法,就能够实现对某个字段进行校验
    # 1. forms.py文件:
    from .models import *
    class UserForm(forms.ModelForm):
        spasswd = forms.CharField(max_length=32, widget=forms.PasswordInput, label="密码: ")
        spasswd2 = forms.CharField(max_length=32, widget=forms.PasswordInput, label="确认密码: ")
        class Meta:
            model = User  # 指向模型类
            fields = ["sname"]  # 取出该模型类的哪些字段,在表单中显示
        # 校验表单类的某个字段: 使用 clean_字段名称() 方法
        def clean_spasswd2(self):
            # value = self.cleaned_data.get("name")  # 获取表单提交的某个数据
            data = self.cleaned_data  # 获取表单提交的所有数据
            if data["spasswd"] != data["spasswd2"]:  # 判断两次密码是否一致
                # 添加字段校验的错误信息
                self.errors['spasswd2'] = ['两次密码输入不一致']  # 可能多种情况校验,错误信息定义为列表
                # raise forms.ValidationError("两次密码输入不一致")
            return data['spasswd2']
            
    # 2. views.py文件:
    # POST请求后校验数据
    from .forms import UserForm
    # 获取表单提交的数据
    userForm = UserForm(request.POST)    
    # 校验表单提交的数据是否有效
    if loginForm.is_valid():
        user = userForm.save(commit=False)
        user.spasswd = userForm.clean_spasswd2()  # 进行字段数据校验
        user.save()
        return HttpResponse("用户注册成功...")
    return render(request,'register.html', {"userForm": userForm})
    
    # 3. register.html文件:
    {# 获取字段校验的错误信息 #}
    {{ userForm.errors.spasswd2.0 }}
    
    
    ## 第四种方式: Hook方法,全部钩子 ---> 在Fom类中定义 clean() 方法,就能够实现对所有字段进行校验
    # forms.py文件: 
    def clean(self):
        password_value = self.cleaned_data.get('password')
        re_password_value = self.cleaned_data.get('re_password')
        if password_value == re_password_value:
            return self.cleaned_data
        else:
            self.add_error('re_password', '两次密码不一致')
            # raise ValidationError('两次密码不一致')
    ```


