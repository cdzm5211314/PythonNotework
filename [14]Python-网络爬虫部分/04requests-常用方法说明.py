# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-17 16:51

# 第三方模块requests,安装: pip install requests

import requests

### requests模块常用方法:
## requests.post('http://httpbin.org/get')          # 请求指定的页面信息，并返回实体主体
## requests.post('http://httpbin.org/post')         # 提交的数据则放在实体数据中
## requests.put('http://httpbin.org/put')           # 从客户端向服务器传送的数据取代指定的文档的内容
## requests.delete('http://httpbin.org/delete')     # 请求服务器删除指定的页面
## requests.head('http://httpbin.org/get')          # 只请求页面的首部
## requests.options('http://httpbin.org/get')


### 基本的GET请求
response = requests.get('http://httpbin.org/get')
### 带参数的GET请求(两种方式): params参数是字典类型,也可以是json类型
response = requests.get("http://httpbin.org/get?name=germey&age=22")
data = {'name': 'germey','age': 22}
response = requests.get("http://httpbin.org/get", params=data)
### 带请求头信息(User-Agent)的GET请求
headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36'
}
response = requests.get("https://www.zhihu.com/explore", headers=headers)


### 基本的POST请求: data参数是字典类型,也可以是json类型
data = {'name': 'germey', 'age': '22'}
response = requests.post("http://httpbin.org/post", data=data)


### 高级的POST请求: 文件上传
files = {'file': open('cookie.txt', 'rb')}
response = requests.post("http://httpbin.org/post", files=files)


### IP代理请求
## 普通代理: proxies = {"协议":"协议://IP地址:端口号"}
## 私密代理: proxies = {"协议":"协议://账号:密码@IP地址:端口号"}
proxies = {
    'http': '121.61.1.245:9999'
}
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
}
url = "http://httpbin.org/get"
response = requests.get(url, proxies=proxies, headers=headers)


### url地址的编码与解码
response1 = requests.utils.quote('https://tieba.baidu.com/?kw=李毅')
# https%3A//tieba.baidu.com/%3Fkw%3D%E6%9D%8E%E6%AF%85
response2 = requests.utils.unquote('https://tieba.baidu.com/?kw=%E6%9D%8E%E6%AF%85')
# https://tieba.baidu.com/?kw=李毅


### 证书验证: 处理不信任的SSL证书: verify = False
response = requests.get('https://www.12306.cn/mormhweb/', verify=False)
### 超时设置:
response = requests.get('http://www.baidu.com', timeout=1)
### 异常处理: requests.exceptions.RequestException
# 遇到网络问题（如：DNS查询失败、拒绝连接等）时，Requests会抛出一个ConnectionError 异常
# 遇到罕见的无效HTTP响应时，Requests则会抛出一个 HTTPError 异常
# 若请求超时，则抛出一个 Timeout 异常
# 若请求超过了设定的最大重定向次数，则会抛出一个 TooManyRedirects 异常



### 请求响应response方法:
# response.text                     # 返回string字符串类型
# response.content                  # 返回bytes字节类型
# response.content.decode('utf-8')  # 对bytes类型数据进行utf-8解码成字符串
# response.json()                   # 返回json类型
# 注: 当返回的是json数据时,使用response.json()会把json数据自动load成字典类型数据,如果不是json数据,使用response.json()会报错
# response.encoding                 # 获取响应字符编码
# response.encoding="utf-8"         # 对响应数据进行编码
# response.url                      # 返回数据的URL地址
# response.status_code              # 返回服务器响应码
# response.headers                  # 获取响应头内容
# response.request.headers          # 获取请求头内容
# response.cookie                   # 获取cookie



