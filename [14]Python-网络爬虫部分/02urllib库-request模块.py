# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-17 14:24

# Python2：urllib2、urllib
# Python3：把urllib2和urllib合并,urllib.request

# encode() : 字符串 --> bytes
# decode() : bytes  --> 字符串

import urllib

### urllib.request模块的常用方法:
## response = urllib.request.urlopen(url)       # get请求,查询参数在URL地址中显示
# 参数说明: url表示请求的地址
# 作用: 向网站发起一个请求并获取响应
# 返回值: 是一个http.client.HTTPResponse对象,这个对象是一个类文件句柄对象
## urllib.request.Request(url,data=data,headers=headers)  # 构建post请求对象req,
# 注: data表单数据以bytes类型提交,不能是str
# 处理form表单数据为bytes类型:
# 1.把提交的form表单数据定义为字典类型: data = {key:value}
# 2.把定义为字典类型的form表单数据进行编码: data = urllib.parse.urlencode(data)
# 3.把编码后的form表单数据转为bytes数据类型: data = bytes(data)


## urllib.request.Request(url,data=data,headers=headers)  # 添加请求头信息User-Agent,字典形式存在headers中
# 示例:
# url = "http://www.baidu.com/"
# headers = {
#     "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.100 Safari/537.36"
# }
# 1.创建请求对象(包含User-Agent)
# req = urllib.request.Request(url,headers=headers)
# 2.获取响应对象
# response = urllib.request.urlopen(req)
# 3.获取响应数据
# data_str = res.read().decode("utf-8")


## urllib.request.ProxyHandler()  # 设置IP代理
# 1.使用ProxyHandler,传入IP代理构建一个handler
handler = urllib.request.ProxyHandler({"https":"112.87.71.209:9999"})
# 2.使用已创建的handler构建以个opener
opener = urllib.request.build_opener(handler)
# 如果需要添加请求头(User-Agent)信息需要使用Request类
# req = request.Request(url,headers)
# response = opener.open(req)
# 3.使用opener去发送一个请求open()
response = opener.open("http://www.baidu.com")

# Handler处理器分类:
# HTTPHandler()                            # 没有任何特殊功能
# ProxyHandler({"协议":"IP地址:端口号"})   # 普通代理
# ProxyBasicAuthHandler(密码管理器对象)    # 私密代理
# HTTPBasicAuthHandler(密码管理器对象)     # web客户端认证


## urllib.request.Request(url,data=data,headers=headers)  # 添加cookie信息模拟登陆,字典形式存在headers中
login_before = "http://www.renren.com/SysHome.do"  # 人人网登陆页面
login_after = "http://www.renren.com/893394172/profile"  # 人人网登陆后个人主页
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36",
    "Cookie":"anonymid=jtpd8l73-kbnu9w; depovince=GW; _r01_=1; JSESSIONID=abcKxe6-uz3U-fd0nK4Mw; ick_login=17af5e13-8091-4915-b704-ba0dd553a56c; ick=2cebb1a8-320f-409f-b97c-d7689da8ea12; first_login_flag=1; ln_uact=18103763930; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; jebe_key=09416abf-1d11-4c6c-8467-da91b972e2bc%7C5b34e73601acb25887c4068b9cf69955%7C1553579872178%7C1%7C1553579871820; jebecookies=b17c717a-60d0-41e2-b6e1-8d14325adb62|||||; _de=3F1C6150E59B993580B4C5FE015D8D28; p=a31aab50cb8d58a4f779dfd1cf9c348c2; t=1da5424772e1107fe8c4e9fc60151a562; societyguester=1da5424772e1107fe8c4e9fc60151a562; id=893394172; xnsid=475dd7b9; loginfrom=syshome; wp_fold=0"
}
req = urllib.request.Request(url=login_after, headers=headers)
response = urllib.request.urlopen(req)


## urlretrieve()  # 把请求响应的数据保存到本地文件中
# 函数原型: def urlretrieve(url, filename=None, reporthook=None, data=None)
result = urllib.request.urlretrieve("http://www.baidu.com",'baidu.txt')


### http.client.HTTPResponse(即请求响应对象)方法:
# read()                    # 读取响应的所有字节数据,bytes
# read().decode('utf-8'))   # 读取响应的所有字符串数据,string
# readline()                # 读取响应的一行数据,字节bytes数据
# readlines()               # 读取响应的多行数据,字节bytes列表
# getcode()                 # 获取请求后的响应状态码
# geturl()                  # 返回实际的URL地址,常常重定向之后使用







### http.cookiejar模块管理cookie模拟登陆
# http.cookiejar模块主要的类有: CookieJar, FileCookieJar, MozillaCoookieJar, LWPCookieJar
from http.cookiejar import CookieJar
# 1.创建CookieJar对象
cookiejar = CookieJar()
# 2.使用CookieJar对象创建一个HTTPCookieProcess对象
handler = urllib.request.HTTPCookieProcessor(cookiejar)
# 3.使用上一步的handler创建一个opener
opener = urllib.request.build_opener(handler)
# 4.使用opener发送登陆请求(人人网的账号和密码)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36"
}
data = {
    "email": "1810376****",
    "password": "****123456"
}
login_before = "http://www.renren.com/PLogin.do"  # 人人网登陆页面
req = urllib.request.Request(url=login_before, data=urllib.parse.urlencode(data).encode("utf-8"), headers=headers)
response = opener.open(req)
# 登陆成功后,访问个人主页
# 获取个人主页页面的时候,不需要新建opener,而是使用之前创建的opener,之前的opener包含了登陆所需要的cookie信息
login_after = "http://www.renren.com/893394172/profile"  # 人人网登陆后个人主页
req2 = urllib.request.Request(url=login_after, headers=headers)
response = opener.open(req2)



### cookie信息的加载与保存
from http.cookiejar import  MozillaCookieJar
mozillacookiejar = MozillaCookieJar("cookie.txt")
handler = urllib.request.HTTPCookieProcessor(mozillacookiejar)
opener = urllib.request.build_opener(handler)
## 保存
opener.open("http://httpbin.org/cookies/set?user=zhangsan")
mozillacookiejar.save(ignore_discard=True)
## 加载
mozillacookiejar.load(ignore_discard=True)
opener.open("http://httpbin.org/cookies")
for cookie in mozillacookiejar:
    print(cookie)