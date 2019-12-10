# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-17 15:16

import urllib

### urllib.parse模块的常用方法:
## urlunparse()  # 将列表元素拼接成url,接收一个列表的参数，列表的长度必须六个参数以上，要不会抛出异常
# 示例: print(urllib.parse.urlunparse(['http', 'www', 'baidu', 'com', 'dfdf', 'eddffa']))


## urljoin()  # 将第二个参数的url缺少的部分用第一个参数的url补齐
# 注: 连接两个参数的url, 将第二个参数中缺的部分用第一个参数的补齐,如果第二个有完整的路径，则以第二个为主
# 示例: print(urllib.parse.urljoin('https://movie.douban.com/', 'index'))
# 示例: print(urllib.parse.urljoin('https://movie.douban.com/', 'https://accounts.douban.com/login'))


## quote()  # url编码,参数是字符串类型
baseurl = "http://www.baidu.com/s?wd="
key = urllib.parse.quote("python")
url = baseurl + key
print(url)  # http://www.baidu.com/s?wd=python


## urlencode()  # url编码,参数必须为字典类型数据
# print(urllib.parse.urlencode({"name":"张三","age":18}))  # 编码字典类型的数据: name=%E5%BC%A0%E4%B8%89&age=18


## parse_qs()  # url解码
dataurl= urllib.parse.urlencode({"wd":"数据库"})
print(dataurl)                          # wd=%E6%95%B0%E6%8D%AE%E5%BA%93
print(urllib.parse.parse_qs(dataurl))   # {'wd': ['数据库']}



## parse.urlparse()与parse.urlsplit()  # 对url地址进行分割
# url = 'https://www.baidu.com/s?wd=数据库'
# result = parse.urlparse(url)
# result = parse.urlsplit(url)
# print(result)
# print("scheme-协议: ",result.scheme)
# print("netloc-域名: ",result.netloc)
# print("path-查找路径: ",result.path)
# print("query-查询字符串: ",result.query)

