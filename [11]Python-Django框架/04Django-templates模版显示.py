# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 14:49

### 静态文件设置(settings.py): 在Django中,不被解释器所动态解析的文件就是静态文件
## 设置静态文件的访问路径: 在浏览器中通过哪个地址能够找到静态文件
# STATIC_URL = '/static/'
#  ---> 如果访问路径是 http://localhost:8000/static/...,那么就到静态文件存储路径中找文件而不走路由(urls.py)
## 设置静态文件的存储路径: 指定静态文件存储在服务器上的哪个位置处
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
# 静态文件目录的存放位置：
# 1.在项目的根目录处创建一个 static 目录，用于保存静态文件们
# 2.每个应用中也可以创建一个 static 目录，用于保存静态文件们

### 访问静态文件:
# 1. 直接使用静态文件访问路径进行访问 ---> http://localhost:8000/static/..
# 如: <img src="/static/images/a.jpg">
# 如: <img src="http://localhost:8000/static/images/a.jpg">
# 2. 使用 {% static "xxx" %} 访问静态资源路径
# 2.1.在模板最顶层增加: {% load static %} 或 {% load staticfiles %}
# 2.2.在使用静态资源时:
# <img src="{% static 'images/a.jpg'%}">
# <script src="{% static "mytest.js" %}"></script>

## 获取静态文件的前缀: {% get_static_prefix %}   ---> /static/
# {% load static %}
# <img src="{% get_static_prefix %}images/hi.jpg" />   ---> /static/images/hi.jpg

## 模板(Templates)的设置: 在 settings.py 中 有一个 TEMPLATES 变量
# 1. BACKEND：指定使用的模板的引擎
# 2. DIRS: 指定模板的存放目录
# 2.1 如果写东西: 则按照写好的路径去找模板
# 2.2 如果未写东西: 那么Django会自动的到每个应用中所有一个叫templates的目录来作为模板的存放目录
# 3. APP_DIRS: 是否自动搜索应用中的目录, True：表示搜索应用中的 templates 的目录



### 模板(Templates)的加载方式:
## 1. 通过 loader 对象获取模板，再通过HttpResponse进行响应
# from django.template import loader
# def xxViews(request):
    # 1.通过 loader 加载模板
    # t = loader.get_template("模板名称.html")
    # 2.将模板渲染成字符串,dict字典用于传参
    # html = t.render({"data":"param"})
    # 3.将字符串通过HttpResponse响应给客户端
    # return HttpResponse(html)
## 2. 使用 render 直接加载并响应模板
# from django.shortcuts import render
# def xxViews(request):
#     return render(request,'模板的名称')


### 模板(Templates)的语法:
## 变量: 将后端的数据传递给模板进行显示,Django中变量传递给模板的数据类型: 字符串，整数，列表，元组，字典，函数，对象
# 变量的语法: {{ 变量名 }} ---> 变量必须要封装到字典中才能传递给模板
# 1. 使用 loader 加载模板
# dic = {
#     '变量名1':'值1',
#     '变量名2':'值2',
# }
# t = loader.get_template('xxx.html')
# html = t.render(locals() 或 dic)
# return HttpResponse(html)

# 2. 使用 render 加载并返回模板
# dic = {
#     '变量名1':'值1',
#     '变量名2':'值2',
# }
# return render(request,'xx.html',dic)


## 标签: 将服务器端的功能嵌入到模板中
# 标签的语法: {% 标签内容 %}
# for标签: 作用：循环遍历 列表，字典，元组
# for标签的语法：
# {% for 变量 in 列表|元组|字典 %}
# {% empty %}  # 可选从句,在给出的组是空的或者没有被找到时，可以有所操作
# {% endfor %}
# 循环中允许使用 forloop 内置变量来获取循环的信息
# forloop.counter:      当前循环遍历的次数
# forloop.first:        判断是否为第一次循环
# forloop.last:         判断是否为最后一次循环
# forloop.parentloop	本层循环的外层循环

# if标签: 在模板中完成变量的判断操作
# if语句支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not 判断
# if标签的语法：如下
# 1. if
# {% if 条件 %}
#     满足条件时要执行的内容
# {% endif %}

# 2. if ... else
# {% if 条件 %}
#   满足条件时要执行的内容
# {% else %}
#   不满足条件时要执行的内容
# {% endif %}

# 3. if ... elif ... else
# {% if 条件1 %}
#   满足条件1时要执行的内容
# {% elif 条件2 %}
#   或满足条件2时要执行的内容
# {% elif 条件3 %}
#   或满足条件3时要执行的内容
# {% else %}
#   或以上条件都不满足时要执行的内容
# {% endif %}


## 内置过滤器(Filters): 在变量输出显示之前，对变量进行筛选和过滤
# 过滤器的语法: {{ 变量|过滤器:参数 }}
# 常用过滤器:
# {{ value|upper }}             ---> 将value变为大写
# {{ value|add:num }}           ---> 将num值累加到value之后
# {{ value|default:"nothing" }} ---> 如果一个变量是false或者为空,使用给定的默认值.否则使用变量的值
# {{ value|length }}            ---> 返回值的长度，作用于字符串和列表
# {{ value|safe }}              ---> 对value不进行转义
# {{ value|date:"Y-m-d H:i:s"}} ---> 日期格式化
# {{ value|truncatechars:n }}   ---> 将value截取保留至n位字符(包含...)
# {{value|slice:"2:-1"}}        ---> 切片
# ...


## 自定义过滤器(Filters): {{ 变量|过滤器名称:参数 }}
# 说明: 只是带有一个或两个参数的Python函数
# 1.在app应用目录下创建的package包目录名称必须为: templatetags
# 2.在templatetags目录下创建一个名称任意的.py文件作为过滤器文件,如 app01_filters
# 3.编写自定义过滤器filter,示例代码如下:
from django import template
register = template.Library()
@register.filter(name="cut")  # 为自定义过滤器取个名字
def cut(value, arg):  # 第一个为变量,第二个是参数
    return value.replace(arg, "")
@register.filter(name="addSB")  # 为自定义过滤器取个名字
def add_sb(value):  # value为变量
    return "{} SB".format(value)
# 4.在模版文件.html中使用自定义过滤器filter
# {# 先导入我们自定义过滤器filter文件 #}
# {% load app01_filters %}
# {# 使用我们自定义过滤器filter #}
# {{ somevariable|cut:"0" }}
# {{ d.name|addSB }}


## 跨站请求伪造保护: 在页面的form表单里面写上{% csrf_token %}

## with: 定义一个中间变量，多用于给一个复杂的变量起别名
# 注: 等号左右不要加空格,示例如下
# {% with total=business.employees.count %}
# {{ total }} employee{{ total|pluralize }}
# {% endwith %}
# {% with business.employees.count as total %}
# {{ total }} employee{{ total|pluralize }}
# {% endwith %}


### 模板(Templates)的继承:
## 继承母版: 在子页面最上方使用 {% extends '父模板名称.html' %}
## 块(block): 在父模板中要标识出哪些内容在子模板中允许被修改
# 1.在父模板中正常显示
# 2.在子模板中，如果不修改的话则按父模板的显示，要是修改的话则按照子模板的内容显示
# {% block xxx %}
# {% endblock %}
## 组件: 将常用的页面内容如导航条,页尾信息等页面保存在单独的文件中，然后在需要使用的地方按如下语法导入即可
# {% include 'navbar.html' %}

## 自定义标签(simple_tag): {% 标签名称 参数1 参数2 ... %}
# 说明: 和自定义过滤器filter类似,只不过接收更灵活的参数
# 1.在app应用目录创建的package包目录名称必须为: templatetags
# 2.在templatetags目录下创建一个名称任意的.py文件作为标签文件,如 app01_tags
# 3.编写自定义标签tags,示例代码如下:
from django import template
register = template.Library()
@register.simple_tag(name="plus")
def plus(a, b, c):
    return "{} + {} + {}".format(a, b, c)
# 4.在模版文件.html中使用自定义标签simple_tag
# {% load app01_tags %}
# {% plus "1" "2" "abc" %}

## inclusion_tag: 多用于返回html代码片段



### 自定义标签和自定义过滤器的区别：
# 1.标签:是为了做一些功能, 过滤器:是对斜杠前面的数据做过滤。
# 2.标签可以写任意个形参,而过滤器最大只能写2个形参,如果过滤器需要接收多个参数,需要将参数存放在列表,元组,字典等数据中
# 3.过滤器可以用在if等语句后,标签不可以



