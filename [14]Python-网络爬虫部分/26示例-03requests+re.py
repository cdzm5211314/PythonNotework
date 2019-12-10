# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-16 17:00


import re
import requests

url = 'https://www.gushiwen.org/default_1.aspx'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}

# 发送请求
res = requests.get(url, headers=headers)
str_text = res.content.decode('utf-8')

# 使用re正则表达式提取数据
titles = re.findall(r'<div class="cont">.*?<b>(.*?)</b>', str_text, re.DOTALL)  # 诗词名称
# print(titles)
dynastys = re.findall(r'<p class="source">.*?<a.*?>(.*?)</a>', str_text, re.DOTALL)  # 朝代
# print(dynastys)
authors = re.findall(r'<p class="source">.*?<a.*?>.*?<a.*?>(.*?)</a>', str_text, re.DOTALL)  # 作者
# print(authors)
content_tags = re.findall(r'<div class="contson" .*?>(.*?)</div>', str_text, re.DOTALL)  # 诗词内容
# print(content_tags)

contents = []  # 诗词内容列表
for content in content_tags:
    tx = re.sub(r'<.*?>', '', content)
    # print(tx.strip())  # 去除空格
    contents.append(tx.strip())
print(contents)


peoms = []
for value in zip(titles, dynastys, authors, contents):
    title, dynasty, author, content = value
    # 诗词,朝代,作者,内容 组合成字典类型
    peom = {
        "title": title,
        "dynasty": dynasty,
        "author": author,
        "content": content
    }
    peoms.append(peom)

# 打印显示组合后数据
for peom in peoms:
    print(peom)
    print("*" * 30)