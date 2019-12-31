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

