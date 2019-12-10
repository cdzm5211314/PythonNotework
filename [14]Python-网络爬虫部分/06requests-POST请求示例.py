# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 10:34

import requests

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
post_data = {
    'from': 'zh',
    'to	': 'en',
    'query': '人生苦短',
}
post_url = 'https://fanyi.baidu.com/basetrans'
# requests.post()函数中data接受的是一个字典类型的数据
rel = requests.post(post_url, data=post_data, headers=headers)
print("结果: " + rel.content.decode('utf8'))

##########################################################################################################
## 获取到的json数据
url = "https://www.lagou.com/jobs/positionAjax.json?city=%E5%8C%97%E4%BA%AC&needAddtionalResult=false"
headers = {
    "Referer":"https://www.lagou.com/jobs/list_python?labelWords=&fromSearch=true&suginput=",
    "User-Agent":"Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:65.0) Gecko/20100101 Firefox/65.0"
}
data = {
    "first": "true",
    "pn": "1",
    "kd": "python"
}
response = requests.post(url,data=data,headers=headers)  # 此网站获取的是json类型的字符串数据
print(response.text)  # 此网站获取的是json类型的字符串数据
print(response.json())


