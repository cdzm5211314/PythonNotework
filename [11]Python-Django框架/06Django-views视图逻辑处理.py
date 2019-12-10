# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-10 15:22

### HttpRequest中的主要内容:
# request.scheme:       请求协议
# request.body:         请求主体
# request.path:         请求路径(具体资源路径)
# request.get_host():   请求的主机地址 / 域名
# request.method:       获取请求方法(如:GET,POST...)
# request.GET:          封装了get请求方式所提交的数据
# request.POST:         封装了post请求方式所提交的数据
# request.COOKIES:      封装了 cookies 中的所有数据
# request.META:         封装了请求的元数据
#   request.META.HTTP_REFERER : 封装了请求的源地址

### 获取请求提交的数据: get 与 post
## get请求方式:
# request.GET['名称']
# request.GET.get('名称')
# 使用表单提交数据: <form method='get'></form>
# 使用地址拼查询字符串: <a href="地址?参数1=值1&参数2=值2"></a>
# 使用URL传参: url(r'^xxx/(\d+)')  ---> 注: 该写法属于Django标准并非HTTP标准,不能用request.GET[]


## post请求方式:
# request.POST['名称']
# CSRF: Cross-Site Request Forgery( 跨站点 请求 伪装)
# 解决跨站请求:
# 1.如果想通过 CSRF 验证，则需要在表单中的第一行增加：{% csrf_token %}
# 2.取消 CSRF 的验证: 删除 settings.py 中 MIDDLEWARE 中 CsrfViewMiddleware 中间件
# 3.在处理函数上增加装饰器: @csrf_protect




