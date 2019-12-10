# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 10:35

import requests

# IP代理网址:https://www.kuaidaili.com/free/

# proxies = {
#     "http": "http://user:password@10.10.1.10:3128/",
# }

proxies = {
    # 'http':'http://163.204.244.100:9999'
    'http':'121.61.1.245:9999'
}

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"
}

url = "http://httpbin.org/get"

response = requests.get(url,proxies=proxies,headers=headers)

print(response.status_code)
print(response.content.decode())


