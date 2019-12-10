# -*- coding:utf-8 -*-
# @Desc :  代理池的校验模块
# @Author : Administrator
# @Date : 2019-11-18 10:22


import requests
import random


# from fake_useragent import UserAgent
# ua = UserAgent()
# 1.准备User-Agent列表
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1",
    "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0",
    "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50",
    "Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50",
]
# 2.实现一个方法,获取随机的User-Agent请求头
def get_request_headers():
    headers = {
        "User-Agent": random.choice(USER_AGENTS),
        # "User-Agent": ua.chrome,
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "zh-CN,zh;q=0.9",
        # "Accept-Language": "en_US,en;q=0.5",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate",
    }
    return headers


	
class Proxy(object):

    def __init__(self, ip, port, protocol=-1):
        self.ip = ip  # 代理IP地址
        self.port = port  # 代理IP端口号
        self.protocol = protocol  # 代理IP支持的协议: http 0, https 1, http&https 2

    def __str__(self):

        return str(self.__dict__)



def check_proxy(proxy):
    '''检测指定的 代理IP, 支持协议类型'''

    # 根据proxy对象构造,请求使用的代理
    proxies = {
        "http": "http://{}:{}".format(proxy.ip, proxy.port),
        "https": "https://{}:{}".format(proxy.ip, proxy.port),
    }

    # 测试该代理IP
    http = _check_http_proxy(proxies)
    https = _check_http_proxy(proxies, False)

    if http and https:
        # 如果http和https都可以请求成功,说明支持两种协议,协议类型为2
        proxy.protocol = 2
    elif http:
        # 如果只有http可以请求成功,说明支持http协议,协议类型为0
        proxy.protocol = 0
    elif https:
        # 如果只有https可以请求成功,说明支持https协议,协议类型为1
        proxy.protocol = 1
    else:
        proxy.protocol = -1

    return proxy


	
def _check_http_proxy(proxies, is_http=True):

    if is_http:  # is_http=True
        test_url = "http://httpbin.org/get"
    else:  # is_http=False
        test_url = "https://httpbin.org/get"

    try:
        # 发送请求,获取响应数据
        res = requests.get(url=test_url, headers=get_request_headers(), timeout=10, proxies=proxies)
        # print("------- 请求状态码: %s" %res.status_code)
        if res.ok:
            return True
	
    except Exception as e:
        if is_http:
            print("******* HTTP请求出现错误!")
        else:
            print("******* HTTPS请求出现错误!")
        return False



if __name__ == "__main__":
    proxy = Proxy(ip="180.158.11.89", port="58080")
    res = check_proxy(proxy)  # res为Proxy的对象
    print(res.__dict__)


