# -*- coding: utf-8 -*-
import scrapy
import json
from ScrapyExample.items import TengxunItem

# 腾讯招聘: https://careers.tencent.com/search.html?index=2  ---> 返回不是想要的数据
# https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563868856736&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex=2&pageSize=10&language=zh-cn&area=cn

class TengxunSpider(scrapy.Spider):
    name = 'tengxun'
    allowed_domains = ['careers.tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563868856736&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'.format(i) for i in range(1,11)]

    def parse(self, response):
        # 把响应的json字符串数据转换为Python字典类型数据
        json_dict = json.loads(response.text)
        # # 招聘标题
        # recruitPostName = json_dict['Data']['Posts'][0]['RecruitPostName']
        # # 招聘城市
        # locationName = json_dict['Data']['Posts'][0]['LocationName']
        # # 招聘类别
        # categoryName = json_dict['Data']['Posts'][0]['CategoryName']
        # # 招聘时间
        # lastUpdateTime = json_dict['Data']['Posts'][0]['LastUpdateTime']
        # # 详细内容ID
        # postId = json_dict['Data']['Posts'][0]['PostId']
        # # 招聘详情页url
        # postURL = json_dict['Data']['Posts'][0]['PostURL'].split("0")[0]
        # postURL = postURL + postId
        # 获取每个招聘的信息
        info_dict = json_dict['Data']['Posts']
        # print(info_dict,type(info_dict))
        for dic in info_dict:
            ti = TengxunItem()
            ti['recruitPostName'] = dic['RecruitPostName']
            ti['locationName'] = dic['LocationName']
            ti['categoryName'] = dic['CategoryName']
            ti['lastUpdateTime'] = dic['LastUpdateTime']
            postId = dic['PostId']
            postURL = dic['PostURL']
            ti['postURL'] = postURL + postId
            print("*",ti)
            yield ti

