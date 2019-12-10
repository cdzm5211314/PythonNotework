# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ScrapyexampleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass


# 腾讯招聘
class TengxunItem(scrapy.Item):
    recruitPostName = scrapy.Field()
    locationName = scrapy.Field()
    categoryName = scrapy.Field()
    lastUpdateTime = scrapy.Field()
    postURL = scrapy.Field()

# 阳光热线
class SuncrawlItem(scrapy.Item):
    title = scrapy.Field()
    number = scrapy.Field()

# 有缘网
class YycrawlfbsItem(scrapy.Item):
    name = scrapy.Field()
    age = scrapy.Field()
    header_url = scrapy.Field()