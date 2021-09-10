# -*- coding:utf-8 -*-
# @Desc : 


import requests
from requests import Response


response1: Response = requests.get('http://httpbin.org/get')

# 变量名后加': 类型'，好处是编程时会自动提醒(提示)对象中的属性及方法
response2: Response = requests.get('http://httpbin.org/get')


def download1(url):
    return 'hello word'
result1 = download1('http://httpbin.org/get')

# 声明函数时，参数名后加': 类型'，表示参数值的类型
# 在函数后面加' -> 类型'，表示函数返回的数据(结果)类型
def download2(url: str) -> str:
    return 'hello word'
result2 = download2('http://httpbin.org/get')


