
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

### Django2.0之后版本路由系统替换成如下写法:
```
## path()处理字符串路由,re_path()处理正则表达式路由
# from django.urls import path, re_path
urlpatterns = [
    path('articles/2003/', views.special_case_2003),      # path: 匹配任何非空字符串,包含了路径分隔符
    path('articles/<int:year>/', views.year_archive),     # int:  匹配正整数,包含 0
    path('articles/<str:name>/', views.name_archive),     # str:  匹配除了路径分隔符（/）之外的非空字符串,这是默认的形式
    path('articles/<Uuid:id>/', views.article_detail),    # uuid: 匹配格式化的uuid,如 075194d3-6885-417e-a8a8-6c931e272f00
    path('articles/<slug:slug>/', views.article_detail),  # slug: 匹配字母、数字以及横杠、下划线组成的字符串
    re_path(r'^userList/(\d*)/',views.List),
    re_path(r'^articles/(?P<year>[0-9]{4})/',views.year),
]
```

