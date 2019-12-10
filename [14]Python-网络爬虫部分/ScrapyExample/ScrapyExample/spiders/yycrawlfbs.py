# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ScrapyExample.items import YycrawlfbsItem
from scrapy_redis.spiders import RedisCrawlSpider


# http://www.youyuan.com/lover/
# http://www.youyuan.com/find/beijing/mm18-0/advance-0-0-0-0-0-0-0/p2/

## 更改自动爬虫(CrawlSpider)为分布式爬虫(RedisCrawlSpider)
# class YycrawlfbsSpider(CrawlSpider):
class YycrawlfbsSpider(RedisCrawlSpider):
    name = 'yycrawlfbs'
    # 可选: 分布式注销域配置,在__init__初始化方法获取动态域范围
    allowed_domains = ['youyuan.com']
    # 必须:分布式爬虫需要注销start_urls
    # start_urls = ['http://www.youyuan.com/find/beijing/mm18-0/advance-0-0-0-0-0-0-0/p1/']
    # 必须:分布式爬虫需要配置信息: redis_key = "爬虫类名:start_urls"
    redis_key = "YycrawlfbsSpider:start_urls"

    # 为spider爬虫配置单独的pipeline
    # custom_settings = {
    #     "ITEM_PIPELINES": {
    #         'ScrapyExample.pipelines.YycrawlfbsPipeline': 300,
    #     }
    # }

    rules = (
        # 提取url地址页码
        Rule(LinkExtractor(allow=r'youyuan.com/find/beijing/mm18-0/advance-0-0-0-0-0-0-0/p\d+/'), callback='parse_item', follow=True),
        # 提取个人主页详情url地址
        Rule(LinkExtractor(allow=r'youyuan.com/\d+-profile/'), callback='parse_detaile', follow=True),

    )
    # 可选: 分布式爬虫动态域范围获取
    # def __init__(self, *args, **kwargs):
    #     domain = kwargs.pop('domain','')
    #     self.allowed_domains = filter(None, domain.split(","))
    #     super(YycrawlfbsSpider, self).__init__(*args, **kwargs)

    def parse_item(self, response):
        print(response.url)

    def parse_detaile(self, response):
        print("***** begin *****")
        youyuanItem = YycrawlfbsItem()
        youyuanItem["name"] = response.xpath('//div[@class="con"]//p[@class="top_tit"]/span/text()').extract_first()
        youyuanItem["age"] = response.xpath('//div[@class="con"]/dl/dd//p[@class="local"]/text()').extract_first().split("  ")[1]
        youyuanItem["header_url"] = response.xpath('//div[@class="con"]/dl/dt/img/@src').extract_first()
        print(youyuanItem)
        print("***** end *****")
        yield youyuanItem