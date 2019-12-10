# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class ScrapyexamplePipeline(object):
    def process_item(self, item, spider):
        return item


# 腾讯招聘
import json
class TengxunPipeline(object):
    def process_item(self, item, spider):
        # print("--------------")
        # print(item,type(item))
        # print("--------------")
        zhaopin_info = dict(item)
        with open("腾讯招聘.json","a",encoding="utf-8") as f:
            f.write(json.dumps(zhaopin_info,ensure_ascii=False) + "\n")  # 数据带有中文,需要设置参数ensure_ascii=False
        # return item

# 阳光热线
import json
class SuncrawlPipeline(object):
    def __init__(self):
        # pass
        self.filename = open("阳光热线.json","a",encoding="utf-8")
    def process_item(self, item, spider):
        # print(self.filename,"0123456789")
        # print(" --- ",item)
        info = json.dumps(dict(item),ensure_ascii=False)
        # with open("阳光热线.json","a",encoding="utf-8") as f:
        #     f.write(info + "\n")
        # print(" +++ ",info)
        self.filename.write(info + "\n")
        # return item
    def close_spider(self,spider):
        # print(self.filename,"9876543210")
        self.filename.close()
        # pass

# 有缘网
class YycrawlfbsPipeline(object):
    def __init__(self):
        self.filename = open("有缘网.json","a",encoding="utf-8")

    def process_item(self, item, spider):
        # print(self.filename)
        info_str = json.dumps(dict(item),ensure_ascii=False)
        self.filename.write(info_str + "\n")

    def close_spider(self,spider):
        self.filename.close()