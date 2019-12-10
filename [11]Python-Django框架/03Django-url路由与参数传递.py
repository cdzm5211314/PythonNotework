# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 11:05

### Django路由URL的使用:
## urls.py: 默认在主目录中，主路由配置文件，会包含最基本的地址映射。
# 作用：通过urls中定义好的地址找到对应的视图处理函数


## url()的语法: 作用：为了匹配用户的访问路径
# from django.conf.urls import url
# url(regex, views, kwargs=None, name=None)
# 1.regex: 允许是正则表达式，匹配请求的url
# 2.views: 对应的视图处理函数的名称
# 3.kwargs: 字典，用来向views传参，如果没有参数可以省略
# 4.name: 为url起别名，在地址反向解析时使用


## url向视图views传递参数:
# 注: 每个在URL中捕获的参数都作为一个普通的Python字符串传递给视图
# 第一种方式: 使用正则表达式传参
# 使用子组传参，一个子组就是一个参数，要传递多个参数的话需要使用多个子组，中间用 / 隔开, 子组 - ()
urlpatterns = [
    # 当访问路径是 http://127.0.0.1:8000/show 的时候,交给show1_views处理 ---> 无参数
    # url(r'^show/$', show1_views),

    # 当访问路径是 http://127.0.0.1:8000/show/45 的时候,交给show2_views函数处理 ---> 位置参数: 45
    # url(r'^show/(\d{2})/$', show2_views),

    # 当访问路径是 http://127.0.0.1:8000/show/23/78 的时候,交给show3_views函数处理 ---> 位置参数: 23 78
    # url(r'^show/(\d+)/(\d+)/$', show4_views),

    # 当访问路径是 http://127.0.0.1:8000/show/123 的时候,交给show3_views函数处理 ---> 关键字参数: number = 123
    # url(r'^show/(?P<number>\d+)/$', show4_views),
]
def show1_views(request):
    pass
def show2_views(request,param):  # param = 45
    pass
def show3_views(request,param1,param2):  # param1 = 23, param2 = 78
    pass
def show4_views(request,number):  # number = 123
    pass

# 第二种方式: 使用url()第三个参数 - 字典传参
dict_info = {
    'name':'naruto',
    'age':18,
}
# url(r'^show5/$', show4_views, dict_info)
def show5_views(request,name,age):  # name = "naruto"  age = 18
    pass


### url()的name参数: 作用 ---> 反向解析
## 在模板上做反向解析
# 1.基本解析: {% url '别名' %}
# 2.带参解析: {% url '别名' '参数1' '参数2' %}
## 在视图上做反向解析
# from django.core.urlresolvers import reverse
# 1.基本解析: url = reverse('别名')                       # url 就是通过别名解析出来的地址
# 2.带参解析: url = reverse('别名',args=(参数1,参数2))    # url 就是通过别名解析出来的地址


### 分布式URL路由系统: 路由分发及命名空间
## 路由分发
from django.conf.urls import url,include
urlpatterns = [
    url(r'^app01/', include('app01.urls',namespace='app01')),         # 分发指向应用下的urls.py路由(即引入应用的url路由)
    # 如: url(r'^user/',include('user.urls',namespace='user')),      # 用户模块
    # 如: url(r'^order/',include('order.urls',namespace='order')),   # 订单模块
    # 如: url(r'^cart/',include('cart.urls',namespace='cart')),      # 购物车模块
    # 如: url(r'^',include('goods.urls',namespace='goods')),         # 商品模块
]
## 反向解析: 命名空间 + 别名
# 模版中使用: {% url '命名空间:别名' param1=12 param2=99 %}
# 视图中使用: reverse('命名空间:别名', kwargs={'pk':11})



### Django2.0版本路由系统替换成如下写法:
## path()处理字符串路由,re_path()处理正则表达式路由
# from django.urls import path, re_path
# urlpatterns = [
#     path('articles/2003/', views.special_case_2003),      # path: 匹配任何非空字符串,包含了路径分隔符
#     path('articles/<int:year>/', views.year_archive),     # int: 匹配正整数,包含 0
#     path('articles/<str:name>/', views.name_archive),     # str: 匹配除了路径分隔符（/）之外的非空字符串,这是默认的形式
#     path('articles/<Uuid:id>/', views.article_detail),    # uuid: 匹配格式化的uuid,如 075194d3-6885-417e-a8a8-6c931e272f00
#     path('articles/<slug:slug>/', views.article_detail),  # slug: 匹配字母、数字以及横杠、下划线组成的字符串
#     re_path(r'^userList/(\d*)/',views.List),
#     re_path(r'^articles/(?P<year>[0-9]{4})/',views.year),
# ]



## 补充: APPEND_SLASH = True  默认为True,其作用就是自动在网址结尾加'/'

