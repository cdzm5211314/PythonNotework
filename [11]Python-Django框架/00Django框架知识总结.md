### Django框架知识点总结
***

### Django项目常用命令:
* 创建Django项目: `django-admin startproject projectname`
* 创建APP应用: `python manage.py startapp appname`
* 创建超级管理员用户: `python manage.py createsuperuser`
* 生成迁移文件: `python manage.py makemigrations`
* 执行迁移文件: `python manage.py migrate`
* 启动Djnago项目: `python manage.py runserver IP/PORT`
* Django终端环境: `python manage.py shell`
* 数据库命令行: `python manage.py dbshell`
* 清空数据库[yes or no]: `python manage.py flush`
* 导出所有数据: `python manage.py dumpdata > mysite_all_data.json`
* 导入所有数据: `python manage.py loaddata mysite_all_data.json`
* 导出APP应用数据: `python manage.py dumpdata appname > appname.json`
* 导入APP应用数据: `python manage.py loaddata appname.json`

### Django项目settings.py配置文件:
```
# 查看Django全局的默认配置信息: django/conf/global_settings.py

# 注册应用APP配置属性:
INSTALLED_APPS = []

# 如果创建APP总目录应用: 需要设置总应用包的搜索环境路径
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 数据库连接配置属性: 如 MySQL
# 需要安装: pip install pymysql
# 注:使用MySQL数据库时,需要在项目目录下的__init__py文件中添加以下内容:
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',  # MySQL数据库连接的驱动程序
         'NAME': 'dailyfresh',                  # MySQL数据库名称
         'USER': 'root',                        # MySQL数据库用户名
         'PASSWORD': 'root',                    # MySQL数据库密码
         'HOST': 'localhost',                   # MySQL数据库IP地址
         'PORT': '3306',                        # MySQL数据库PORT端口号
     }
}

# 模版文件的存储路径配置属性:
TEMPLATES = [
   # 如果配置了目录,则优先按照写好的路径去找模板文件,如果找不到才会到app应用下的templates目录中查找模版文件
   'DIRS': [os.path.join(BASE_DIR, 'templates')],  
   # 'DIRS': [ ],  # 如果未配置目录,则会自动的到每个应用中查找templates的目录来作为模板文件的存放目录
   'APP_DIRS': True,  # 默认True表示搜索应用中的 templates 目录
   # 注: 使用{{ MEDIA_URL }}模版全局上下文变量需要在settings.py文件中的变量TEMPLATES中配置如下内容
   'OPTIONS': { 'context_processors': [..., 'django.template.context_processors.media'] }
   # 如果不想每次在模版文件中加载静态文件时都使用{% load static %},那么就把static标签变成Django内置标签
   'builtins': ['django.templatetags.static'],
] 

# 静态文件的存储路径配置信息:
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 上传文件的存储路径配置:
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空
# 上传文件的路由配置信息: 根路由
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# Admin后台管理中文设置:
LANGUAGE_CODE = 'zh-Hans'       # 设置中文,默认为en-us
TIME_ZONE = 'Asia/Shanghai'     # 设置时区,默认为UTC
# USE_I18N = True                 # 是否启动自动翻译,默认为True
# USE_L10N = True                 # 设置以本地格式化显示数字和时间,默认为False
USE_TZ = False                  # 设置使用本地时间,默认为True

# Pyhon脚本调用Django环境:
# 1.加载Django项目的配置信息
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
# 2.导入Django包,并启动Django项目
import django
django.setup()

# Django中的Session配置信息:
# 1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'              # 引擎（默认）
# 2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'           # 引擎
SESSION_CACHE_ALIAS = 'default'                                     # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
# 3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'            # 引擎
SESSION_FILE_PATH = None                                            # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
# 4. 缓存 + 数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'       # 引擎
# 5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎
# 其他公用设置项：
# SESSION_COOKIE_NAME ＝ "sessionid"         # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"                 # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None              # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False             # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True            # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600              # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False        # 是否每次请求都保存Session，默认修改之后才保存（默认）

# 终端打印SQL语句的配置信息:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}

## 补充: APPEND_SLASH = True  默认为True,其作用就是自动在URl地址结尾加'/'
```

### 静态文件与模版文件的访问:
```
### 静态文件设置(settings.py): 在Django中,不被解释器所动态解析的文件就是静态文件
## 设置静态文件的访问路径: 在浏览器中通过哪个地址能够找到静态文件
# STATIC_URL = '/static/'
#  ---> 如果访问路径是 http://localhost:8000/static/...,那么就到静态文件存储路径中找文件而不走路由(urls.py)
## 设置静态文件的存储路径: 指定静态文件存储在服务器上的哪个位置处
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
# 静态文件目录的存放位置：
# 1.在项目的根目录处创建一个 static 目录，用于保存静态文件
# 2.每个应用中也可以创建一个 static 目录，用于保存静态文件

### 如何访问静态文件:
# 1. 直接使用静态文件访问路径进行访问 ---> http://localhost:8000/static/..
# 如: <img src="/static/images/a.jpg">
# 如: <img src="http://localhost:8000/static/images/a.jpg">
# 2. 使用 {% static "xxx" %} 访问静态资源路径
# 2.1.在模板最顶层增加: {% load static %} 或 {% load staticfiles %}
# 2.2.在使用静态资源时:
# <img src="{% static 'images/a.jpg'%}">
# <script src="{% static "mytest.js" %}"></script>

# 或者如果不想每次在模版文件中加载静态文件时都使用{% load static %},那么就把static标签变成Django内置标签:
# 在settings.py文件中属性TEMPLATES/OPTIONS同级下添加: 'builtins':['django.templatetags.static']

## 获取静态文件的前缀: {% get_static_prefix %}   ---> /static/
# {% load static %}
# <img src="{% get_static_prefix %}images/hi.jpg" />   ---> /static/images/hi.jpg

### 模板(Templates)的设置: 在 settings.py 中有一个 TEMPLATES 变量
# 1. BACKEND：指定使用的模板的引擎
# 2. DIRS: 指定模板的存放路径
# 2.1 如果写东西: 则按照写好的路径去找模板
# 2.2 如果未写东西: 那么Django会自动的到每个应用中搜索一个叫templates的目录来作为模板的存放目录
# 3. APP_DIRS: 是否自动搜索应用中的目录,设置为True: 表示搜索应用中的 templates 目录
```

### Django框架中路由分发:
```
# 根路由: 项目根目录下urls.py
from django.conf.urls import url, include
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 路由分发,include为每个APP应用分发一个子路由
    url(r'^URL路径/', include('APP应用名称.urls', namespace='名称空间')),
]

# 子路由: APP应用下urls.py
urlpatterns = [
    url(r'^login/$', views.login_view, name='login'),
]
# url(regex, views, kwargs=None, name=None): 作用是为了匹配浏览器输入的访问路径
# regex: 允许是正则表达式,匹配请求的URL路径
# views: 视对应的图处理函数的名称
# kwargs: 字典类型,用来向views视图函数进行传参,如果没有参数可以省略
# name: 为URL路径起别名,以便反向解析时使用
```

### URL路径向views视图函数传递参数方式:
```
# 第一种传参方式(GET请求): 正则表达式,使用子组()传参,多个参数之间使用"/"隔开
# 注: 在每个URL中捕获的参数都作为一个普通的Python字符串传递给视图函数
# 注: 该种传参方式属于Django标准并非HTTP标准,不能用request.GET['key']获取参数
urlpatterns = [
    # 当访问路径是 http://127.0.0.1:8000/show1/ ---> 无参数
    url(r'^show1/$', show1_views),
    # 当访问路径是 http://127.0.0.1:8000/show2/45/ ---> 位置参数: 45
    url(r'^show2/(\d{2})/$', show2_views),
    # 当访问路径是 http://127.0.0.1:8000/show3/23/78/ ---> 位置参数: 23 78
    url(r'^show3/(\d+)/(\d+)/$', show4_views),
    # 当访问路径是 http://127.0.0.1:8000/show4/123/ ---> 关键字参数: number = 123
    url(r'^show4/(?P<number>\d+)/$', show4_views),
]
# 第一种传参方式之views视图函数接受参数方式:
def show1_views(request):
    pass
def show2_views(request,param):  # param = 45
    pass
def show3_views(request,param1,param2):  # param1 = 23, param2 = 78
    pass
def show4_views(request,number):  # number = 123
    pass
    
# 第二种传参方式(GET请求): 使用路由参数kwargs,传递字典类型参数
# 如访问请求: http://127.0.0.1:8000/show5/
# URL路由及字典参数传递
dict_info = {
    'name':'naruto',
    'age':18,
}
url(r'^show5/$', show5_views, kwargs=dict_info)
def show5_views(request,name,age):  # name = "naruto"  age = 18
    pass
    
# 第三种传参方式(GET请求): 通过传统的"?"传递参数
# 如访问请求: http://127.0.0.1:8000/getParam/?name=zhangsan&age=21
url(r'^getParam/$', getParam)
def getParam(request):
    name = request.GET.get("name")
    age = request.GET.get("age")

# 第四种传参方式(POST请求): form表单提交的参数
# 注: 跨站请求CSRF验证,则需要在FORM表单的第一行增加: {% csrf_token %}
```

### Django框架处理请求方式: FBV 与 CBV
* FBV(function base views): 使用视图函数处理请求
    ```
    # url路由: 
    url(r'^index/$', views.index_view, name='index'),
    # views视图:
    def index_view(request):
       if request.method == "GET":  # 处理get请求
            pass
       else:  # 处理post请求
            pass
    ```
* CBV(class base views): 使用视图类处理请求
    ```
    # url路由:    
    url(r'^index/$', IndexView.as_view(), name='index'),
    # views视图:
    from django.views import View
    class IndexView(View):
        def get(self, resuest):  # 处理get请求
            pass    
        def post(self, request):  # 处理post请求
            pass
    ```
### Django框架的视图层: views
```
略...
```

### HttpRequest对象请求详解:
```
# django.http.HttpRequest对象属性及方法:
request.scheme: 返回请求的协议类型(http/https)
request.body: 返回请求的实体主体(针对POST请求)
request.encoding: 返回浏览器提交数据的编码方式(一般为utf-8)
request.META: 返回请求的元数据(报文信息),Python字典类型
# request.META['REMOTE_ADDR']: 返回客户端IP地址
# request.META['REMOTE_HOST']: 返回客户端主机名
# request.META['HTTP_USER_AGENT']: 返回客户端的User-Agent字符串
request.path: 返回请求地址(不包括域名和端口号)
request.method: 返回请求的方式(常用:GET，POST)
request.GET: 返回类字典的对象(QueryDict对象),包含了GET请求的所有参数
request.POST: 返回类字典的对象(QueryDict对象),包含了POST请求的所有参数
request.FILES: 返回类字典的对象,包含了所有上传的文件
# 注: FILES只存在POST请求中,<input type="file" name="" enctype="multipart/form-data"/> 及{% csrf_token %}
# 注: FILES的键来自<input type="file" name="" />中的name属性,FILES的值为Python字典类型数据(包含以下三个键)
# name: 字符串,表示上传文件的文件名
# content: 上传文件的原始内容
# content-type: 上传文件的内容类型
request.COOKIES: 返回Python字典类型,包含所有的cookie,键和值都字符串
request.session: 返回类字典的对象,表示当前会话对象
request.session.get(key,default=None): 根据键获取session值
request.user: 返回一个表示当前用户是否登录的对象,用于判断用户是否登录
# django.contrib.auth.models.User
# django.contrib.auth.models.AnonymousUser  # 当前用户未登录

request.get_host(): 返回请求的主机地址/域名
request.get_full_path(): 返回请求地址(包括请求参数)
request.is_ajax(): 返回如果请求是通过XMLHttpRequest发起的,则返回True

# QueryDict对象(类字典对象)获取键对应的值:
# 根据键获取值: get()
# 根据键获取列表类型的值: getlist()
```

### HttpResponse对象响应详解:
```
# django.http.HttpResponse对象属性与方法: response = HttpResponse()
# 常用属性:
response.content = ""  # 响应的内容
response.charset = ""  # 响应的内容的编码方式
response.status_code = 200  # 响应的HTTP状态码,默认200
response.content_type = ""  # 响应的数据类型,默认为text/html
# text/html(默认,html文件)
# text/plain(纯文本)
# 注意: 在使用'text/plain'时,需要添加'charset=utf-8',否则会乱码
# text/css(css文件)
# text/javascript(js文件)
# multipart/form-data(文件提交)
# application/json(json传输)
# application/xml(xml文件)

# 常用方法: 
set_cookie(): 用来设置cookie信息
delete_cookie(): 用来删除cookie信息
write(): HttpResponse是一个类似于文件的对象,可以用来写入数据到数据体(content)中


# 响应字符串: 
from django.http import HttpResponse        # 返回一个字符串
from django.shortcuts import HttpResponse   # 返回一个字符串
def function_view(request):
    return HttpResponse('字符串')

# 响应模版及模版渲染数据:
from django.shortcuts import render         # 返回模版信息以及渲染数据
# def render(request, template_name, context=None, content_type=None, status=None, using=None):
def function_view(request):
    return render(request, '模版路径文件.html', context={'data': data})

# 响应URL地址重定向及URL地址反向解析:
from django.http import HttpResponseRedirect    # 重定向到另一个URL地址
from django.shortcuts import redirect           # 重定向到另一个URL地址
from django.shortcuts import reverse            # 反向解析URL地址
from django.core.urlresolvers import reverse    # 反向解析URL地址
def function_view(request):
    return redirect('URL路径')
    return redirect(reverse('命名空间:别名')  # 无参数
    return redirect(reverse('命名空间:别名', args=(param1,param2))  # 元组类型,位置参数(顺序参数)
    return redirect(reverse('命名空间:别名', kwargs={'param1':'value1', 'param2':'value2'}))  # 字典类型,关键字参数

# 响应Json数据:
from django.http import JsonResponse            # 返回Json数据(即字典类型数据)
def function_view(request):
    return JsonResponse('字典数据')
    # 默认只能传递字典类型,如果要传递非字典类型需要设置一下safe关键字参数
    # return JsonResponse('非字典数据', safe=False)

# 响应模版及模版渲染数据: 
from django.template import loader          # 加载模版文件
from django.shortcuts import loader         # 加载模版文件
from django.http import HttpResponse        # 返回一个字符串
from django.shortcuts import HttpResponse   # 返回一个字符串
def function_view(request):
    # 1.通过loader对象加载模板文件
    template = loader.get_template("模板路径文件.html")
    # 2.将模板渲染成字符串,dict字典用于传递参数
    html = template.render({"data":"param"})
    # 3.将字符串通过HttpResponse响应给浏览器
    return HttpResponse(html)
```

### URL地址的反向解析: 命名空间(namespace) + 别名(name) [+ 参数]
```
# views视图: 一般与URL重定向一块使用
from django.shortcuts import redirect           # 重定向到另一个URL地址
from django.shortcuts import reverse            # 反向解析URL地址
return redirect(reverse('命名空间:别名')  # 无参数
return redirect(reverse('命名空间:别名', args=(param1,param2))  # 元组类型,位置参数(顺序参数)
return redirect(reverse('命名空间:别名', kwargs={'param1':'value1', 'param2':'value2'}))  # 字典类型,关键字参数

# templates模版:
{% url '命名空间:别名' %}  # 无参数
{% url '命名空间:别名' param1 param2 %}  # 位置参数(顺序参数)
{% url '命名空间:别名' param1=value1 param2=value2 %}  # 关键字参数
```

### 文件的上传与下载:
```
### 第一种方式文件的上传: 上传文件到本地目录(原生方式)
# 1.xxx.html文件:
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="fileupload">
    <input type="submit" value="上传文件">
</form>

# 2.urls.py:  
urlpatterns = [
    url(r'^upload/', view=upload_file, name='upload'),
]

# 3.views.py文件:
from django.shortcuts import HttpResponse
def upload_file(request):
    if request.method == "POST":
        # file_obj根据xxx.html中文件上传的name属性值,得到一个文件对象
        file_obj = request.FILES.get("fileupload", None)  
        import os
        if not os.path.exists('media'):  # 判断文件存放目录是否存在
            os.makedirs("media")  # 创建文件存放目录
        with open(os.path.join(os.getcwd(), 'media', file_obj.name), 'wb') as ft:
                # ft.write(file_obj.read())      # 一次性读取文件内容然后写入数据保存
                for chunk in file_obj.chunks():  # 分块读取文件内容然后写入数据保存
                    ft.writer(chunk)
        return HttpResponse("上传文件成功...")


### 第二种方式文件的上传: 上传文件到本地目录(admin后台上传文件)
# 1. settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    # 注:文件上传路径信息:MEDIA + upload_to ---> /media/images/文件
    # 注:数据库im字段信息: images/文件 
    im = models.ImageField(upload_to="images")  

# 3.admin.py文件: 注册模型类
from .models import UploadModel
admin.site.register(UploadModel)

# 4.创建超级管理员账户,访问: http://127.0.0.1:8000/admin 上传文件


### 第三种方式文件的上传: 上传文件到本地目录(信息写入数据库)
# 1.xxx.html文件:
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="fileupload">
    <input type="submit" value="上传文件">
</form>

# 2.urls.py:  
urlpatterns = [
    url(r'^upload/', view=upload_file, name='upload'),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    # 注:文件上传路径信息:MEDIA + upload_to ---> /media/images/文件
    # 注:数据库im字段信息: images/文件 
    im = models.ImageField(upload_to="images")  

# 4.views.py文件:
from django.shortcuts import HttpResponse
from .models import UploadModel
def upload_file(request):
    if request.method == "POST":
        file_obj = request.FILES.get("fileupload", None)  
        # 上传文件信息写入数据库
        UploadModel.objects.create(im=file_obj)
        return HttpResponse("上传文件成功...")


### 上传图片文件后的图片显示: 即图片文件的读取
# 1.settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.urls.py文件: 项目根路由,文件读取的配置信息
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    im = models.ImageField(upload_to="images") 

# 4.views.py文件: 
from .models import UploadModel
from django.shortcuts import render
def show_image(request):
    upall = UploadModel.objects.all()
    return render(request, 'show.html', {'uploadall':upall})

# 5.show.html文件:
{% for file in uploadall %} 
    <image src="/media/{{ file.im }}" />  # 显示图片
    <image src="{{ MEDIA_URL }}{{ file.im }}" />  # 显示图片
    # 注: 使用MEDIA_URL模版上下文变量需要在settings.py文件中的变量TEMPLATES中配置如下内容
    # 'django.template.context_processors.media'
{% endfor%} 


    
### 文件的下载: URL地址预览(图片)和文件下载
# 1.settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.urls.py文件: 项目根路由,文件读取的配置信息
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    im = models.ImageField(upload_to="images") 
    
# 4.xxx.html文件
<a href="/download/?file={{ file.im }}">下载</a>

# 5. urls.py文件:
url(r'^download/$',views.download_file),

# 6.views.py文件
def download_file(request):
    # 获取请求参数,图片的存储位置
    fi = request.GET.get('file', '')
    # 获取文件名
    # file_name = fi.split("/")[-1]      # 字符串分割,取列表最后一个元素
    file_name = fi.[fi.rindex("/")+1:]   # 进行字符串切片分割
    import os
    from django.shortcuts import HttpResponse
    # 获取文件的绝对路径
    file_path = os.path.join(os.getcwd(), 'media', fi.replace('/', '\\'))
    with open(file_path, 'rb') as ft:
        
        ## 默认预览图片: 
        response = HttpResponse(ft.read())  # 读取文件内容写入到页面
        response["Content-Type"] = "image/png"
        response["Content-Disposition"] = "inline;filename=" + file_name
        
        ## 第一种文件下载方式: from django.shortcuts import HttpResponse
        response = HttpResponse(ft.read())  # 读取文件内容写入到页面
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
        ## 第二种文件下载方式: from django.http import StreamingHttpResponse
        response =StreamingHttpResponse(ft)  # 传入文件句柄对象
        response['Content-Type']='application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
        ## 第三种文件下载方式[推荐使用]: from django.http import FileResponse
        # FileResponse是StreamingHttpResponse的子类,内部使用迭代器进行数据流传输
        response =FileResponse(ft)  # 传入文件句柄对象
        response['Content-Type']='application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
    return response
```

### Django定制错误页面(重定向):
```
## Django自定义全局的403,404,500错误页面
# 1.自定义xxx.html文件错误页面: 403.html 404.html 500.html
<body>
    HTTP 403 - 禁止访问
    HTTP 404 - 无法找到文件
    HTTP 500 - 内部服务器错误
</body>

# 2.编写views.py文件视图函数:
def permission_denied(request):
    return render(request, '403.html')
def page_not_found(request):  
    return render(request, '404.html')
def page_error(request):
    return render(request, '500.html')

# 3.配置urls.py文件: 根路由 ---> 指向视图函数
# 如: handlerXXX = 'appname.views.view_function_name'
handler403 = permission_denied
handler404 = page_not_found
handler500 = page_error

# 4.配置settings.py文件: 关闭debug,配置allowend_hosts
DEBUG = False  # 关闭 
ALLOWED_HOSTS = ["*"]
```

### Cookie与Session:
```
## Cookie的操作: 存, 取, 删
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False)
# 注:参数解释,key:cookie的名字, value:cookie的值, max_age:cookie存在时间,秒为单位, expires:具体的时间为单位
# 注: cookie不设置过期时间的话,默认关闭浏览器就失效

response = HttpResponse('保存cookie')
response.set_cookie('username', username,)  # 设置cookie的键与值
response.set_signed_cookie('username', username, salt='asdasd') # 设置cookie的键与值,加盐

cookies = request.COOKIES  # 获取所有的cookie信息
username = request.COOKIES.get('username')  # 获取指定cookie的值
username = request.get_signed_cookie('username', salt='asdasd') # 获取cookie的值,注:如果加盐,盐要相同否则取不到值

response = HttpResponse('删除cookie')
response.delete_cookie('username')  # 删除指定的cookie

request.COOKIES.has_key("username")  # 判断所有cookie信息是否存在某个cookie,存在返回True


## Session的操作:
request.session['username'] = username  # 设置session的键与值
request.session.set_expiry(value)       # 设置Session的过期时间
* 如果value是个整数,session会在多少秒数后失效
* 如果value是个datetime日期值,session就会在这个日期后失效
* 如果value是0,用户关闭浏览器session就会失效
* 如果value是None,session会依赖全局session失效策略
username = request.session.get('username')  # 获取session的值
del request.session['username']  # 删除指定的session的值,但不会删除数据库表中的session数据
request.session.delete() # 删除所有session数据
request.session.flush()  # 删除所有session数据,并删除数据库表中的session数据
request.session.clear()  # 删除所有session数据,但不会删除数据库表中的session数据,只删除cookie中的sessionid
request.session.logout() # 退出登陆,删除所有session数据,并删除数据库表中的session数据
# request.session.clear_expired()           # 将所有session失效日期小于当前日期的数据删除
# request.session.session_key               # 用户session的随机字符串,获取sessionid信息
# request.session.exists("session_key")     # 检查用户session的随机字符串在数据库session表中中是否存在

## 获取session中所有的键,值,键值对
# request.session.keys()
# request.session.values()
# request.session.items()
# request.session.iterkeys()
# request.session.itervalues()
# request.session.iteritems()


### Django中默认支持Session,其内部提供了5种类型的Session配置
## 1. 数据库: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
## 2. 缓存: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存,也可以是memcache）,此处别名依赖缓存的设置
## 3. 文件: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎
SESSION_FILE_PATH = None  # 缓存文件路径,如果为None,则使用tempfile模块获取一个临时地址tempfile.gettempdir()
## 4. 缓存 + 数据库: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # 引擎
## 5. 加密Cookie: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎

## settings.py配置文件中设置默认操作(通用配置)
# SESSION_COOKIE_NAME ＝ "sessionid"  # Session的cookie保存在浏览器上时的key,即:sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"          # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None        # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False       # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True      # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600        # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```

### 模型类与数据库表的正逆向操作:
* 模型类正向生成数据库表:
    ```
    # APP应用下的models.py文件自定义模型类:
    # 生成迁移文件: python manage.py makemigrations
    # 执行迁移文件: python manage.py migrate
    ```
* 数据库表逆向生成模型类:
    ```
    # 根据数据库表自动生成对应的Model代码,并打印出来
    python manage.py inspectdb
    # 根据数据库表自动生成对应的Model代码到指定的APP应用下的models.py文件中
    # 注: 此APP应用必须已经创建了并在settings中注册了
    python manage.py inspectdb > student/models.py
    # 如果多个数据库,根据配置数据库别名指定哪个数据库表自动生成对应的Model代码
    python manage.py inspectdb --database default > student/models.py
    # 根据指定的数据库表自动生成对应的Model代码
    python manage.py inspectdb --database default table1 table2 > student/models.py
    ```

### Django框架的分页功能:
```
### 使用Django框架内置分页器Paginator封装分页实现:
## Paginator分页器对象属性:
# Paginator分页器对象: paginator = Paginator(all_data,num_page)  # all_data数据集,num_page每一页的数据数
# 返回总数量: paginator.count  # 对象总数
# 返回总页数: paginator.num_pages  # 页码总数
# 返回页码列表(即显示页码数): paginator.page_range  # 页码列表,从1开始,如[1,2,3,4,5,...]
# 返回Page对象(即根据页码数值获取第几分页对象): pages = paginator.page(num)  # 如:第一分页的对象paginator.page(1)   第二分页的对象paginator.page(2)

## Page分页对象的属性与方法: 整数,具体的某一个页面
# 分页对象属性(即当前page对象关联的Pagintor对象): paginator 
# 当前页面上的所有数据: object_list
# 当前页的页码值(即第几分页的当前页码值)属性: pages.number
# 是否有上一页: pages.has_previous()
# 上一页的页码: pages.previous_page_number()
# 是否有下一页: pages.has_next()
# 下一页的页码: pages.next_page_number()
# 是否有上一页或下一页: pages.has_other_pages()
# 返回当前页起始的对象序号: pages.start_index()
# 返回当前页结束的对象序号: pages.end_index()

## 视图:views.py
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
## 分页函数: views.py
def paging(request):
    page_num = request.GET.get('page_num',defaule=1)  # 获取url传递过来的页码数值,默认值为1,可自定义
    all_data = Entity.objects.all()  # 数据查询结果集
    paginator = Paginator(all_data,3)  # 创建分页对象,设置每页显示几条数据
    try:
        pages = paginator.page(page_num)  # 获取页码值对应的分页对象
    except PageNotAnInteger:  # 页码不是整数时引发该异常
        pages = paginator.page(1)  # 获取第一页数据返回
    except EmptyPage:  # 页码不在有效范围时(即数据为空,或参数页码值大于或小于页码范围)引发该异常
        # pages = paginator.page(paginator.num_pages)
        if int(page_num) > paginator.num_pages:
            # 参数页码值大于总页码数: 获取最后一页数据返回
            pages = paginator.page(paginator.num_pages)
        else:
        # 参数页码值小于最小页码数: 获取第一页数据返回
            pages = paginator.page(1)

    ## 这部分是为了当有大量数据时,保证所显示的页码数量不超过10
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)

    return render(request,'papgin.html',{'pages':pages,'dis_range': dis_range})


## 模版:templates
# {# 分页显示 #}
# {# 是否有上一页,有就获取上一页的页码值 #}
# {% if pages.has_previous %}
#   <li class="long"><a href="?page_num={{ pages.previous_page_number }} ">上一页</a></li>
# {% endif %}
#
# {# 所有页码值 #}
# {% for num in pages.paginator.page_range %}
#   {# 选中当前页码进行标识 #}
#   <li {% if num == pages.number %} class="active" {% endif %} ><a href="?page_num={{ num }}">{{ num }}</a></li>
# {% endfor %}
#
# {# 是否有下一页,有就获取下一页的页码值 #}
# {% if pages.has_next %}
#   <li class="long"><a href="?page_num={{ pages.next_page_number }}">下一页</a></li>
# {% endif %}
```

### Django框架的模型层: models
* 字段类型: models.字典类型()
    ```
    # 自增长字段,int类型:
        AutoField:
        BigAutoField:
    # 字符串类型:
        CharField: 字符串类型字段
        TextField: 文本字段
    # 布尔型:
        BooleanField: 不允许为空
        NullBooleanField: 允许为空
    # 二进制数据
        BinaryField:
    # 日期时间:
        DateField: # 年月日
        DateTimeField: # 年月日时分秒
    # 整型:
        SmallIntegerField: 6个字节整数
        IntegerField: 11个字节整数
        BigIntegerField: 20个字节整数
        PositiveSmallIntegerField: 5个字节正整数
        PositiveIntegerField: 10个字节正整数
    # 浮点型:
        FloatField: 
        DecimalField: 
    # 其他类型:
        UUIDField: uuid为通用唯一标识符
        ImageField: 图片字段(保存和处理上传的图片),依赖宇Pillow组件
        FileField: 文件字段(保存和处理上传的文件),Imagefield继承于FileField
        FilePathField: 文件路径字段
        EmailField: Email字段,检查Email的合法性
        URLField: URL地址字段,检查URL合法性
        IPAddressField: IP字段,十进制表示的IP地址
        GenericIPAddressField: IP字段,IPv4和IPv6地址表示,检查IP地址合法性
    # 关系字段类型:
        OneToOneField: 一对一
        ForeignKey: 一对多
        ManyToManyField: 多对多
    ...等字段类型
    ```
    
* 字段选项: models.字典类型(字段选项)
    ```
    primary_key: 设置主键,对AutoField设置主键后,就会代替原来的自增 id 列
    max_length: 字符串最大长度
    unique=True: 字段值唯一,不允许重复,默认为Flase
    null=True: 数据库中字段允许为空,默认False
    blank=True: 在admin后台提交表单允许为空,默认Flase,当设置为True时,null属性值必须为True
    verbose_name: 在admin后台的显示字段名称
    editable=True: 在admin后台中是否可编辑,默认为True
    default: 为字段设置默认值(数据库与admin后台)
    auto_now=True: 自动创建--->无论添加或修改,都是当前操作的时间
    auto_now_add=True: 自动创建--->永远是创建时的时间
    choices: 轻量级的配置字段可选属性的定义(首先在模型类中定义一个列表或元组提供选择)
    db_column: 在数据库中的字段名称,默认和变量同名
    db_index = True: 在数据库中是否设置为索引,默认为False  
    upload_to="upload/images/": 文件上传功能;指定文件上传的目录位置,相对项目根目录
    ...等字段选项
    ```
    
* 元数据: class Meta
    ```
    class Meta:
        db_table = "table_name"  # 指定数据库表名
        ordering = ['order_date']  # 指定返回结果集按照哪个或哪些字段排序
        verbose_name = "student"   # 给模型类起一个可读的名字
        verbose_name_plural = verbose_name  # 模型的复数形式
        abstract = True/False    # 是否作为一个抽象类,默认为False
        unique_together = ("address", "note")  # 联合唯一健,还可以用二维元组((), ())
        app_label = 'app_name'  # 模型类属于哪一个应用
        ...等元数据属性
    ```
    
* 自定义模型类管理器
    ```
    # 注: 模型类可以定义使用多个管理器
    # 1.在models.py文件中定义一个类并继承Manager类
    from django.db.models.manager import Manager
    class ModelClazzManager(Manager):
        # 应用1.改变原有查询的结果集: 如all()
        # 应用2.封装方法:用户操作模型类对应的数据表(增删改查)
        # self.model: 获取self对象所在的模型类(即ModelClazz模型类)
        pass
        
    # 2.在models.py文件中模型类中定义管理器类对象属性
    from django.db import models
    class ModelClazz(models.Model):
        name = models.CharField(max_length=32)
        # 自定义一个模型器管理类对象(...)
        manages = ModelClazzManager()
        # objects = ModelClazzManager()  # 可以使用原有的管理器对象名称
        # 注: 模型类也可以重写(增删改查)操作数据方法,实现逻辑操作
        
    # 3.如果重新定义的管理器为manages,就不能使用原有的管理器objects了
    # 如,是: ModelClazz.manages.all() 而不是: ModelClazz.objects.all()
    ```
    
### 关系字段类型: 一对一, 一对多, 多对多
* 关系字段中的属性设置值:
    ```
    ## to: 要关联的表名
    注: to='ModelName'  # 加引号,这个表能找到就可以,不用引号,类必须在此模型类上面定义
    ## to_filed: 要关联的表中的字段名称
    ## related_name: 给模型类主表定义一个属性
    ## on_delete: 当删除关联表中的数据时，当前表与其关联的行的行为
    # 1. models.CASCADE: 将定义有外键的模型对象同时删除,django模板的默认操作
    # 2. model.PROTECT: 阻止上面的删除操作,但是弹出ProtectedError异常
    # 3. models.SET_NULL: 将外键字段设为null,只有当字段设置了null=True时,方可使用该值
    # 4. models.SET_DEFAULT: 将外键字段设为默认值,只有当字段设置了default参数时,方可使用
    # 5. models.DO_NOTHING: 什么也不做
    # 6. models.SET: 设置为一个传递给SET()的值或者一个回调函数的返回值,注意大小写
    ```
    
* OneToOneField: 一对一关系,将关系字段定义在任意一端中,如: 学生与学生证
    ```
    # 注: 关系字段定义在哪个模型类中,哪个模型类对应的表就是子表
    class Student(models.Model):  # 学生模型类
        # sno = models.AutoField(primary_key=True)  # 学生学号
        sno = models.CharField(max_length=20)  # 学生学号
        sname = models.CharField(max_length=32)  # 学生姓名
        class Meta:
            db_table = "t_student"  # 数据库表
    # 数据库表(t_student即主表)字段: id, sno, sname  
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    
    class Card(models.Model):  # 学生证模型类
        cno = models.CharField(max_length=20)  # 学生证编号
        cmajor = models.CharField(max_length=32)  # 学生证专业
        # student = models.OneToOneField(Student, primary_key=True) # 关联另一个模型类,设置外键属性
        student = models.OneToOneField(Student)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性student后,会在关联的模型类中增加一个隐式的属性: card
        class Meta:
            db_table = "t_card"  # 数据库表
    # 数据库表(t_card即子表)字段: id, cno, cmajor, student_id
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    # student_id表示在模型类中设置了外键属性student后,在数据库表中指向关联数据库表的主键ID
    
    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如查询: Card.objects.first().student
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如查询: Student.objects.first().card
    ```
    
* ForeignKey: 一对多关系,将关系字段定义在多的一端中,如: 作者和书籍
    ```
    # 注: 关系字段定义在哪个模型类中,哪个模型类对应的表就是子表
    class Author(models.Model):  # 作者
        aname = models.CharField(max_length=32)  # 作者姓名
    class Meta:
        db_table = "t_author"
    # 数据库表(t_author即主表)字段: id aname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段

    class Book(models.Model):  # 书籍
        bname = models.CharField(max_length=32)  # 书籍名称
        author = models.ForeignKey(Author)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性author后,会在关联的模型类中增加一个隐式的属性: book_set
    class Meta:
        db_table = "t_book"
    # 数据库表(t_book即为子表)字段: id bname author_id
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    # author_id表示在模型类中设置了外键属性author后,在数据库表中指向关联数据库表的主键ID

    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如(跨表)对象查询 - 对象.关联字段.字段: Book.objects.first().author.aname
    # 如(跨表)字段查询 - 关联字段__字段: Book.objects.values_list("author__aname")
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如(跨表)对象查询 - 对象.隐式属性: Author.objects.first().book_set.all()
    # 如(跨表)对象查询 - 对象.隐式属性: Author.objects.first().book_set.all().values_list("bname")
    # 如(跨表)字段查询 - 表名__字段: Author.objects.values_list("book__bname")
    ```

* ManyToManyField: 多对多关系,将关系字段定义在任意一端中,如: 课程与教师
    ```
    class Course(models.Model):  # 课程
        cname = models.CharField(max_length=32)  # 课程名称
    class Meta:
        db_table = "t_course"
    # 数据库表(t_course)字段: id cname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段

    class Teacher(models.Model):  # 教师
        tname = models.CharField(max_length=32)  # 教师姓名
        course = models.ManyToManyField(Course)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性course后,会在关联的模型类中增加一个隐式的属性:teacher_set
    class Meta:
        db_table = "t_teacher"

    # 数据库表(t_teacher)字段: id tname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    
    ## 注:多对多关系中,Django默认会自动生成第三张(中间)表:
    # 数据库表(t_teacher_course)字段: id teacher_id course_id
    # teacher_id: 指向模型类对应数据库表(即t_teacher)主键
    # course_id: 指向模型类对应数据库表(即t_course)主键
    
    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如: Teacher.objects.first().course.all()
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如: Course.objects.first().teacher_set.all()
    
    # 注:可以自定义第三张表,不使用Django默认生成
    class Teacher_Course(models.Model):
        teacher = models.ForeignKey(Teacher)  # 关联另一个模型类,设置外键属性
        course = models.ForeignKey(Course)    # 关联另一个模型类,设置外键属性
    ```
    
### Django定义完模型类生成数据库表:
```
# 生成迁移文件: python manage.py makemigrations
# 执行迁移文件: python manage.py migrate

# 注:当模型类发生变更后需要重新生成数据库表
# 1.删除数据库表: 删除该模型类对应的数据表
# 2.删除数据库表信息: 删除django_migrations表中关于该模型类的迁移记录信息
# 3.删除APP应用文件: 删除./app_dir/migrations/迁移文件
# 4.再次生成迁移文件及执行迁移文件,生成对应的模型类数据库表
```

### Django框架ORM: 对象关系映射
* 添加数据: 
    ```
    # 1. Entity.objects.create(属性=值,属性=值)  # 返回值:创建好的实体对象
    
    # 2. 创建一个 Entity 对象，并通过 save() 进行保存
    obj = Entity(属性=值,属性=值)
    obj.save()
    
    # 3. 使用字典构建对象，并通过 save() 进行保存
    dic = {
        '属性1':'值1',
        '属性2':'值2',
    }
    obj=Entity(**dic)
    obj.save()
    ```
* 删除数据:
    ```
    # 删除一条或多条数据: 先查询后删除
    auList = Author.objects.filter(mid="1001)
    auList.delete()
    ```
* 修改数据:
    ```
    ## 修改单个对象: 可以对对象的全部属性值进行修改
    # 1.查: 通过查询得到要修改的实体对象
    # 2.改: 通过对象的属性修改对象的值
    # 3.保存: 通过对象的 save() 保存回数据库
    ## 批量修改数据: 推荐使用
    # 调用QuerySet对象的update(属性=值,属性=值)实现批量修改
    # 如: Entity.objects.filter(sname="王五").update(spasswd="555555")
    # SQL语句: UPDATE `stu` SET `spasswd` = '555555' WHERE `stu`.`sname` = '王五'
    ```  
* 显示底层的SQL语句: 测试
    ```
    # 1.Movie.objects.all().query.__str__()  # 针对select查询
    # 2.自定义函数
    from django.db import connection
    def showsql():
        query = connection.queries  # 打印所有底层执行过的SQL语句
        print(query[-1]['sql'])     # 取出最后一条SQL语句
    ```    
* 查询数据:
    * 基本查询方法: 13个基本方法
        ```
        ## 返回QuerySet对象的方法: all(), filter(), exclude(), order_by(), reverse(), distinct()
        ## 返回特殊的QuerySet对象的方法有: values(), values_list()
        # values()      返回一个可迭代的字典序列
        # values_list() 返回一个可迭代的元祖序列
        ## 返回具体对象的方法: get(), first(), last()
        ## 返回布尔值的方法：exists()
        ## 返回计数值的方法: count()
        
        ## 查询所有数据: all()
        # Entity.objects.all()  # 返回值：QuerySet(查询结果集,是一个封装了若干对象的列表)
        
        ## 只查询一条数据: get(条件)
        # Entity.objects.get(条件)
        # 注: 该方法只能查询一条数据,查询多于一条数据或没查询出结果的话那么都会抛异常
        
        ## 查询返回指定列: values() 与 values('列1','列2',...)
        # 作用: 查询一个QuerySet中的部分列，并封装成字典，再放到列表中
        # Entity.objects.values()
        # Entity.objects.values('列1','列2')
        # Entity.objects.all().values()
        # Entity.objects.filter().values()
        
        ## 查询返回指定列: values_list() 与 values_list('列1','列2')
        # 作用: 查询一个QuerySet中的部分列，并封装成元组，再放到列表中
        # Entity.objects.values_list()
        # Entity.objects.values_list('列1','列2')
        # Entity.objects.all().values_list()
        # Entity.objects.filter().values_list()
        # 总结: values()和values_list()里面写什么字段,就相当于select查询什么字段
        
        ## 根据条件查询部分行数据: filter(条件)
        # 语法: Entity.objects.filter(条件)
        # 1.构建等值条件:
        # 示例: Author.objects.filter(id=1)
        # 示例: Author.objects.filter(id=1,name='隔壁老王')
        # 2.构建不等值条件: __gt, __lt, __contains,__startswith,__endswith, __in, __range, __date, ...
        # Entity.objects.filter(属性__查询谓词=值)
        # 即: ### 单表查询的双下划线操作 ###
        # 示例: Entity.objects.filter(id__gt=5)              # 获取id大于5的数据
        # 示例: Entity.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的数据
        # 示例: Entity.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
        # 示例: Entity.objects.exclude(id__in=[11, 22, 33])  # not in
        # 示例: Entity.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
        # 示例: Entity.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and
        
        ## 对条件取反: exclude(条件)
        # Entity.objects.exclude(条件)
        # 示例: Author.objects.exclude(id=1)             # select * from index_author where not(id=1)
        # 示例: Author.objects.exclude(id=1,age__lt=30)  # select * from index_author where  not (id=1 and age < 30)
        
        ## 排序查询: order_by()
        # Entity.objects.order_by('列1','-列2')
        # 注: 默认是升序排序，列名前加 - 则表示降序排序
        
        ## reverse()  # 对查询结果反向排序,通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)
        ## distinct()  # 从返回结果中剔除重复纪录(注意只有在PostgreSQL中支持按字段去重)
        ## count()  # 返回数据库中匹配查询(QuerySet)的对象数量。
        ## first()  # 返回第一条记录
        ## last()  # 返回最后一条记录
        ## exists()  # 如果QuerySet包含数据，就返回True，否则返回False
        ```
    * 聚合函数总结: 
        ```
        ## 聚合函数: 
        # 1.Avg():   平均值
        # 2.Min():   最小值
        # 3.Max():   最大值
        # 4.Sum():   求和
        # 5.Count(): 计数

        ## 聚合查询(不带分组): aggregate()
        # Entity.objects.all().aggregate(别名=聚合函数('列'))
        # 示例: Author.objects.all().aggregate(avg=Avg('age'))
        # 示例: Book.objects.aggregate(average_price=Avg('price'))
        
        ## 聚合查询(带分组): annotate() ---> annotate()前面的values("列1","列2")表示按照哪个列进行分组
        # Entity.objects.all().values('分组列1','分组列2').annotate(别名=聚合函数('列')).values('查询列1','查询列2','查询列3')
        # Entity.objects.filter(条件).values('分组列').annotate(别名=聚合函数('列')).filter(条件)
        # 示例: Employee.objects.values("dept").annotate(avg=Avg("salary").values(dept, "avg")
        ```
    
    * F查询与Q查询:
        ```
        ## F(): 在执行中获取某列的值
        # from django.db.models import F
        # 示例: Author.objects.all().update(age=F('age')+10)  # update author set age=age+10
        # 示例: Book.objects.filter(commnet_num__gt=F('keep_num'))
        
        ## Q(): 在查询条件中可以完成 |(OR) 和 &(AND) 和 ~(非) 操作
        # from django.db.models import Q
        # 示例: Author.objects.filter(Q(id=1)|Q(age=48))  # select * from author where id=1 or age=48
        # 示例: Book.objects.filter(Q(authors__name="小仙女")|Q(authors__name="小魔女"))
        ```
        
    * SQL原生查询:
        ```
        # 第一种包含主键:
        # Manager.raw(raw_query, params=None, translations=None)
        # raw_query: 执行的sql语句
        # params: 需要格式化的参数,类型:列表
        # translations: 值为字典,将查出来的数据键值对化,根据模型属性声明查询出来的键,如:{模型属性:键}
            Person.objects.raw('SELECT * FROM myapp_person LIMIT 1')[0]
            Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
            
        # 第二种不包含主键:
            # 若你同时使用不止一个数据库,你可以使用 django.db.connections 获取指定数据库的连接(和指针)
            # from django.db import connections 是一个类字典对象,它允许你通过连接别名获取指定数据库连接
            # 如: connections['my_db_alias'].cursor()
            
            from django.db import connection  # 代表默认数据库连接
            cursor = connection.cursor()  # 获取指针对象
            # 1.调用 cursor.execute(sql, [params]) 方法执行该SQL语句
            # 2.调用 cursor.fetchone() 或 cursor.fetchall() 方法获取结果数据
        ```
        
    * ForeignKey查询: 多表查询
        ```
        ## 正向查找: 对象查找(跨表)  ---> 对象.关联字段.字段
        # book_obj = Book.objects.first()   # 第一本书对象
        # book_obj.publisher                # 获取这本书关联的出版社的对象
        # book_obj.publisher.name           # 获取这本书关联的出版社的名称
        ## 正向查找: 字段查找(跨表) ---> 关联字段__字段
        # Book.objects.values_list("publisher__name")
        
        ## 反向查找: 对象查找(跨表)  ---> obj.表名_set
        # publisher_obj = Publisher.objects.first()     # 第一个出版社对象
        # books = publisher_obj.book_set.all()          # 获取这个出版社出版过的所有书的对象
        # titles = books.values_list("title")           # 再获取这个出版社出版过的所有书的书名
        ## 反向查找: 字段查找(跨表) ---> 表名__字段
        # titles = Publisher.objects.values_list("book__title")
        ```

### Django框架后台管理: Admin
```
# 后台管理访问: http://localhost:8000/admin

# 使用Admin后台系统管理模型类(即数据库数据)
0.Admin后台管理页面中文设置: settings.py
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

1.创建超级管理员用户: python manage.py createsuperuser

2.在APP应用下的admin.py文件中使用内置方式注册模型类
from .models import Student
admin.site.register(Student)

3.在APP应用下的admin.py文件中使用自定义方式注册模型类
from .models import Student
@admin.register(Student)  # 简写注册,等同于: admin.site.register(Student, StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "author",deletes]  # 定制显示的列: 即admin后台显示的模型字段名称或自定义函数名称
    list_display_link = ["author"]  # 定制列可以点击跳转: 点击哪个字段进入编辑页面
    list_filter = ["author"]  # 定制右侧快速过滤查询: 根据字段过滤
    search_fields = ["name"]  # 定制快速搜索框: 根据字段搜索
    raw_id_fields = ["关联字段"]  # 后台显示关联字段所属的信息
    ordering = ["排序字段"]
    list_per_page = 10  # 默认为100条
    actions_on_top = True  # 显示顶部的选项
    actions_on_bottom = True  # 显示底部的选项
# admin.site.register(Student, StudentAdmin)  # 自定义方式注册模型类

### 定制信息字段详情:
## list_display : 定义在 列表页 上显示的字段们
# 取值：由属性名组成的元组或列表
## 2.list_display_links : 定义在列表页中也能够连接到详情页的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须要出现在list_display中
## 3.list_editable : 定义在列表页中就允许修改的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须出现在list_display中但不能出现在list_display_links中
## 4.search_fields : 添加允许被搜索的字段们
# 取值：由属性名组成的元组或列表
## 5.list_filter : 列表页的右侧增加过滤器，实现快速筛选
# 取值：由属性名组成的元组或列表
## 6.date_hierarchy : 列表页的顶部增加时间选择器，取值必须是DateField 或 DateTimeField的列名
## 7.fields : 在详情页中，指定显示哪些字段并按照什么样的顺序显示
# 取值：由属性名组成的元组或列表
## 8.fieldsets : 在详情页面中，对字段们进行分组显示的
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

### 编辑关联对象:
## 在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种
# 类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑
# 子类TabularInline：以表格的形式嵌入
# 子类StackedInline：以块的形式嵌入
## 在app01/admin.py文件中添加如下代码：
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo    # 关联子对象（多类对象）
 
class AreaAdmin(admin.ModelAdmin):
    inlines = [AreaStackedInline]
```

### Django框架的模版层: templates
```
将后端的数据传递给模板进行显示,Django中变量传递给模板的数据类型: 字符串,整数,列表,元组,字典,函数,对象
# 变量标签: {{ 变量名 }} ---> 变量必须要封装到字典中才能传递给模板
# 块标签: 如 {% for %}{{ endfor }}, {% if %}{{ endif }} ...
```
* 模版中的标签语法: {% 标签内容 %}
    ```
    ### for标签: 
    ## 作用: 循环遍历 列表,字典,元组
    ## 语法: 如下
    {% for 变量 in 列表|元组|字典 %}  # 循环取值reversed倒序: {% for 变量 in 列表 reversed %}
    {% empty %}  # 可选从句,未获取到数据时,执行的内容
    {% endfor %}
    ## for循环中允许使用 forloop 内置变量来获取循环的信息:
    forloop.counter:      当前循环遍历的次数,从1开始
    forloop.counter0:     当前循环遍历的次数,从0开始
    forloop.revcounter:   当前循环遍历的次数,序号倒序
    forloop.first:        判断是否为第一次循环
    forloop.last:         判断是否为最后一次循环
    forloop.parentloop	  本层循环的外层循环
    
    ### if标签: 
    ## 作用: 在模板中完成变量的判断操作,支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not 判断
    ## 语法: 如下
    # 第一种格式: if
    {% if 条件 %}
        满足条件时要执行的内容
    {% endif %}
    
    # 第二种格式: if ... else
    {% if 条件 %}
      满足条件时要执行的内容
    {% else %}
      不满足条件时要执行的内容
    {% endif %}

    # 第三种格式: if ... elif ... else
    {% if 条件1 %}
      满足条件1时要执行的内容
    {% elif 条件2 %}
      或满足条件2时要执行的内容
    {% else %}
      或以上条件都不满足时要执行的内容
    {% endif %}
    ```
* 模版常用内置标签: 
    ````
    {# 单行注释 #%}
    {% comment %} 多行注释 {% endcomment %}
    {% autoescape off %} 解析标签内容 {% endautoescape %}
    {% autoescape on %} 自动转义为普通字符串(默认) {% endautoescape %}
    {% debug %} 输出整个调试信息,包括当前上下文和导入的模块
    {% block %} 定义可以被子模板覆盖的块,为模板继承时使用 {% endblock %} 
    {% extends "xxx.html" %} 带引号,作为父模板的名称来扩展
    {% extends variable %} 使用的变量variable;如果变量的计算结果为字符串,Django将使用该字符串作为父模板的名称,如果变量评估为一个Template对象,Django将使用该对象作为父模板
    {% include "xxx.html" %} 模版中包含使用某个组件(.html)
    ...等
    ````    
    
* 模版常用内置过滤器: filter
    ```
    # 过滤器的作用: 在变量输出显示之前,对变量进行筛选和过滤
    # 过滤器的语法: {{ 变量|过滤器 }} 或 {{ 变量|过滤器1|过滤器2 }} 或 {{ 变量|过滤器:参数 }}
    {{ variable|upper }}             ---> 将variable变为大写
    {{ variable|add:num }}           ---> 将num值累加到variable之后
    {{ variable|default:"nothing" }} ---> 如果一个变量是false或者为空,使用给定的默认值,否则使用变量的值
    {{ variable|length }}            ---> 返回值的长度,作用于字符串和列表
    {{ variable|safe }}              ---> 对variable不进行转义
    {{ variable|date:"Y-m-d H:i:s"}} ---> 日期格式化
    {{ variable|truncatechars:n }}   ---> 将variable截取保留至n位字符(包含...)
    {{ variable|slice:"2:-1"}}       ---> 切片
    ...等
    ```

* 自定义过滤器: filter 
    ```  
    ## 语法样式: {{ 变量|过滤器名称:参数 }}
    ## 自定义过滤器步骤: 过滤器本质就是带有一个或两个参数的Python函数
    # 1.在APP应用目录下创建包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为过滤器文件,如 app01_filters.py
    # 3.编写自定义过滤器filter,示例代码如下:
    from django import template
    register = template.Library()
    # 如果未设置name属性值,默认会使用函数名作为过滤器名字
    @register.filter(name="get1")  # name属性值为自定义过滤器名字,
    def get1_filter(variable):  # variable为使用过滤器的变量
        return "{} SB".format(variable)
    @register.filter(name="get2")  # name属性值为自定义过滤器名字
    def get2_filter(variable, arg):  # variable为使用过滤器的变量,arg为传递的参数
        return variable.replace(arg, "")
    # 4.在模版文件.html中使用自定义过滤器filter
    {# 4.1 加载自定义过滤器filters文件 #}
    {% load app01_filters %}
    {# 4.2 使用自定义过滤器filter #}
    {{ variable|get1 }}    
    {{ variable|get2:"0" }}
    ```
    
* 自定义标签: simple_tag 
    ```
    ## 语法样式: {% 标签名称 参数1 参数2 ... %}
    ## 自定义标签步骤: 标签本质就是带有多个参数的Python函数
    # 1.在APP应用目录下创建包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为标签文件,如 app01_tags.py
    # 3.编写自定义标签tag,示例代码如下:
    from django import template
    register = template.Library()
    @register.simple_tag(name="plus")  # name属性值为自定义标签名字
    def plus_tag(a, b, c):  # a,b,c为传递给标签的参数(形参)
        return "{} + {} + {}".format(a, b, c)
    # 4.在模版文件.html中使用自定义标签simple_tag
    {# 4.1 加载自定义标签tags文件 #}
    # {% load app01_tags %}
    {# 4.2 使用自定义标签tag #}
    # {% plus "1" "2" "abc" %} # 1.2,abc为传递给标签的参数(实参)  
    ```

* 自定义标签和自定义过滤器的区别:
```
1.标签:是为了做一些功能;过滤器:是对斜杠前面的数据做过滤
2.标签可以写任意个形参,而过滤器最大只能写2个形参,如果过滤器需要接收多个参数,需要将参数存放在列表,元组,字典等数据中
3.过滤器可以用在if等语句后,标签不可以
```

* 模版的继承:
```
## 继承父模版(extends): 在子模版的第一行使用 {% extends '父模板名称.html' %}
## 预留块(block): 在父模板中要标识出哪些内容在子模板中允许被修改,被填充
# 1.在父模板中正常显示
# 2.在子模板中,如果不修改的话则按父模板的显示,要是修改的话则按照子模板的内容显示
# {% block xxx %}
# {% endblock %}
## 组件(页面): 将常用的页面内容如导航条,页尾信息等页面保存在单独的.html文件中,然后在需要使用的地方按如下语法导入即可
# {% include 'navbar.html' %}
```

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
    
### Django框架的中间件: middleware
```
# Django框架有默认的中间件: settings.py文件的 MIDDLEWARE = []
# 中间件的执行顺序: 自上而下,全局操作Django项目的请求与响应

### 中间件的常用方法: process_request() 和 process_response()
from django.utils.deprecation import MiddlewareMixin
class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 请求从wsgi拿到的时候
        返回值: None或HttpResponse对象
            如果是None,继续执行后续的中间件的process_request方法
            如果是HttpResponse对象,不执行后续的中间件的process_request方法
        """
        pass

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        :param request: 浏览器发来的请求对象
        :param view_func: 将要执行的视图函数的名字
        :param view_args: 位置参数
        :param view_kwargs: 关键字参数
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 在urls.py中找到与视图的对应关系后,在执行真正的视图函数之前调用
        返回值:
            如果是None,继续执行后续的中间件的process_view方法
            如果是HttpResponse对象,不执行后续的中间件的process_view方法
        """
        pass
        
    def process_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 请求有响应的时候
        返回值: 必须是HttpResponse对象
        """
        pass

    def process_exception(self, request, exception):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数中抛出异常时执行
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass

    def process_template_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数完成后执行,前提是:视图函数返回的对象有一个render()方法(或表明该对象是一个TemplateResponse对象或等价方法)
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass
        
## 注:除了process_response()方法必须返回HttpResponse对象,其他几个方法的返回值可以是None或HttpResponse对象:
# 如果是None,则按照Django定义的规则往下执行
# 如果是HttpResponse对象,则直接将该对象返回给用户
## 注: Django调用 注册的中间件里面的五个方法的执行顺序:
# process_request  ---> urls.py ---> process_view ---> view.py ---> process_exception ---> process_template_response ---> process_response

### 自定义中间步骤:
# 1.在项目根目录下创建包目录,如包名称为middleware
# 2.在创建的middleware包目录下创建.py文件,如文件名称为mymiddleware.py
# 3.在创建的mymiddleware.py文件中编写中间件类,并继承MiddlewareMixin基类
from django.utils.deprecation import MiddlewareMixin
class XxxMiddleware(MiddlewareMixin):
    '''然后根据功能需要,重写那五个方法中的某个或多个方法,如下所示'''
    def process_request(self, request):
        print("request路径: ", request.GET.path)
        print("访问服务器的IP地址: ", request.META.get("REMOTE_ADDR"))
# 4.启用(注册)中间件,在settings.py中进行配置,如MIDDLEWARE添加: 包名.文件名.类名
# 如: 'middleware.mymiddleware.XxxMiddleware'
```



