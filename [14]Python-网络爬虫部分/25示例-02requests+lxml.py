# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-16 14:42

# 迁木网: http://www.qianmu.org/ranking/1528.htm

import requests
from lxml import etree

url = 'http://www.qianmu.org/ranking/1528.htm'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36'
}
# 发送请求
res = requests.get(url, headers=headers)

# 使用lxml作为解析对象
htmlElement = etree.HTML(res.content.decode('utf-8'))

# 使用xpath提取数据信息
tr_list = htmlElement.xpath("//div[@class='rankItem'][2]//tr")
# tr_list = htmlElement.xpath("//div[@class='rankItem'][2]//tr[@class='xh-highlight']")
# print(len(tr_list), type(tr_list))
# print(tr_list)

# for tr in tr_list[1:10]:  # 测试一部分数据信息
for tr in tr_list[1:]:
    ranking = tr.xpath("./td[1]/text()")[0]
    if not tr.xpath("./td[2]/a"):
        school_name_zh = tr.xpath("./td[2]/text()")[0]
    else:
        school_name_zh = tr.xpath("./td[2]/a/text()")[0]
        school_detail = tr.xpath("./td[2]/a/@href")[0]
    school_name_en = tr.xpath("./td[3]/text()")[0].strip()
    if not tr.xpath("./td[4]/text()"):
        country = ''
    else:
        country = tr.xpath("./td[4]/text()")[0]
    # print(type(ranking),type(school_name_zh),type(school_detail),type(school_name_en),type(country))
    print('排名: ' + ranking + ', 学校名字(中文): ' + school_name_zh + ', 学校详情: ' + school_detail + ', 学校名字(英文): ' + school_name_en + ', 国家地区: '+ country)





