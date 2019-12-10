# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from ScrapyExample.items import SuncrawlItem

# http://wz.sun0769.com/index.php/question/report?page=30
# http://wz.sun0769.com/html/question/201907/422049.shtml

class SuncrawlSpider(CrawlSpider):
    name = 'suncrawl'
    allowed_domains = ['wz.sun0769.com']
    start_urls = ['http://wz.sun0769.com/index.php/question/report?page=0']

    rules = (
        Rule(LinkExtractor(allow=r'page=\d+'),callback='parse_item',follow=True),  # 获取页码URL链接
        Rule(LinkExtractor(allow=r'/html/question/\d+/\d+.shtml'), callback='parse_detaile'),  # 获取详情页面URL
    )

    def parse_item(self,response):
        print(response.url)  # 获取页码链接url

    def parse_detaile(self,response):
        # print("***** begin *****")
        print(response.url)
        # print("----- 获取详情页面数据 -----")
        suncrawlItem = SuncrawlItem()
        suncrawlItem['title'] = response.xpath('//div[@class="wzy1"]//span[@class="niae2_top"][1]/text()').extract_first().split("：")[1]
        suncrawlItem['number'] = response.xpath('//div[@class="wzy1"]//span[2]/text()').extract_first().split(":")[1]
        # print(suncrawlItem)
        # print("***** end *****")
        yield suncrawlItem

