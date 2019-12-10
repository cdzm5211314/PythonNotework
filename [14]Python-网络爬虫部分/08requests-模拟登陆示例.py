# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 10:36

import requests

# 第一种方式: 实例化session,使用session发送post请求,在使用session获取登录后的页面
login_url = 'http://www.renren.com/PLogin.do'
headers1 = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
login_data = {
    'email': '18103763930',
    'password': '****123456'
}
session = requests.session()
# 使用session发送post请求,cookie保存在其中
session.post(login_url, data=login_data, headers=headers1)
# 再次使用session进行请求登录之后才能访问的地址
response1 = session.get('http://www.renren.com/893394172/profile', headers=headers1)
print(response1.status_code)



# 第二种方式: 在headers中添加Cookie键,值为Cookie字符串[在浏览器查找到Cookie]
headers2 = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0",
    'Cookie	': 'anonymid=jqma53ha-4lq03c; depovince=GW; jebecookies=f27ad1d9-e893-4362-816e-edab83c7a3d2|||||; _r01_=1; JSESSIONID=abcdb8i787r_wa2ggnOGw; ick_login=c00b9ba3-4fef-46e8-9d21-f94e21bd3f4e; jebe_key=250a4e73-4c3d-435a-b08e-5975c32b76e7%7C5b34e73601acb25887c4068b9cf69955%7C1546863158289%7C1%7C1546863160263; _de=CBAB31EED2C8716972FFEFECAA50653A696BF75400CE19CC; p=b449d11fe07d755337c4ec118d00c4ec2; first_login_flag=1; ln_uact=123309778@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2cd030579721cee5eb9463cb4b2be8c52; societyguester=2cd030579721cee5eb9463cb4b2be8c52; id=893394172; xnsid=d7c58014; loginfrom=null; ver=7.0; wp_fold=0'
}
url2 = 'http://www.renren.com/893394172/profile'
response2 = requests.get(url2, headers=headers2)
print(response2.status_code)



# 第三种方式: 在请求中添加cookies参数,接受字典类型的cookie
headers3 = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
cookies = 'anonymid=jqma53ha-4lq03c; depovince=GW; jebecookies=f27ad1d9-e893-4362-816e-edab83c7a3d2|||||; _r01_=1; JSESSIONID=abcdb8i787r_wa2ggnOGw; ick_login=c00b9ba3-4fef-46e8-9d21-f94e21bd3f4e; jebe_key=250a4e73-4c3d-435a-b08e-5975c32b76e7%7C5b34e73601acb25887c4068b9cf69955%7C1546863158289%7C1%7C1546863160263; _de=CBAB31EED2C8716972FFEFECAA50653A696BF75400CE19CC; p=b449d11fe07d755337c4ec118d00c4ec2; first_login_flag=1; ln_uact=123309778@qq.com; ln_hurl=http://head.xiaonei.com/photos/0/0/men_main.gif; t=2cd030579721cee5eb9463cb4b2be8c52; societyguester=2cd030579721cee5eb9463cb4b2be8c52; id=893394172; xnsid=d7c58014; loginfrom=null; ver=7.0; wp_fold=0'
# 字典推导式
cookies = {i.split("=")[0]: i.split("=")[1] for i in cookies.split("; ")}
# print(cookies)
url3 = 'http://www.renren.com/893394172/profile'
response3 = requests.get(url3, headers=headers3, cookies=cookies)
print(response3.status_code)

#########################################################################
# 如果一个响应中包含了cookie,name可以利用cookies属性拿到这个返回的cookie值
response = requests.get("http://www.baidu.com")
print(response.cookies.get_dict())



