# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 11:30

# 安装: pip install lxml
from lxml import etree

htmlElement = etree.HTML("text")   # 参数为一个字符串
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

htmlElement = etree.parse("text.html")  # 参数为一个html格式文件
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

parse = etree.HTMLParse(encoding="utf-8")  # 解析参数
htmlElement = etree.parse("text.html", parse=parse)
print(etree.tostring(htmlElement, encoding="utf-8").decode("utf-8"))

###########################示例如下##################################
import requests

url = "https://www.qidian.com/all?chanId=4&subCateId=12"
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}

response = requests.get(url, headers=headers)
htmlElement = etree.HTML(response.text)  # 接受一个字符串参数,返回的是一个Element对象

names = htmlElement.xpath('//h4/a/text()')
authors = htmlElement.xpath('//p[@class="author"]/a[@class="name"]/text()')
# print(names)  # 列表数据
# print(authors)  # 列表数据

for name, author in zip(names, authors):
    print("书名: " + name, " ---> ", "作者: " + author)

for num in range(len(names)):
    print(names[num], " : ", authors[num])


