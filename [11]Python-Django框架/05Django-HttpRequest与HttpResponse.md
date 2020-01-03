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
    return JsonResponse({"key": "value"})  # 字典数据
    # 默认只能传递字典类型,如果要传递非字典类型需要设置一下safe关键字参数
    # return JsonResponse('非字典数据', safe=False)

# 响应模版及模版渲染数据: 
from django.template import loader          # 加载模版文件
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

