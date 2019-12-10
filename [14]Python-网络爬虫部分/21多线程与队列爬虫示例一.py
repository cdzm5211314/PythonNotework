# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 14:28

### 对列:


### 多线程:


from threading import Thread
from queue import Queue
from fake_useragent import UserAgent
import requests
from lxml import etree

# 爬虫线程类
class CrawlInfo(Thread):

    def __init__(self, queue_url, queue_html):
        Thread.__init__(self)
        self.queue_url = queue_url
        self.queue_html = queue_html

    def run(self):
        headers = {
            "User-Agent": UserAgent().chrome
        }
        while self.queue_url.empty() == False:  # 判断队列是否为空
            response = requests.get(self.queue_url.get(), headers=headers)  # Queue队列,先入先出,获取存入队列中的url地址
            if response.status_code == 200:  # 查看请求是否成功,返回响应
                self.queue_html.put(response.text)  # 把获取到的内容存储都队列中

# 解析线程类
class ParseInfo(Thread):
    def __init__(self, queue_html):
        Thread.__init__(self)
        self.queue_html = queue_html

    def run(self):
        while self.queue_html.empty() == False:
            e = etree.HTML(self.queue_html.get())  # 获取队列中存储的内容
            span_contents = e.xpath('//div[@class="content"]/span[1]')
            # print(span_contents)
            with open("qiushibaike.txt", "a", encoding='utf-8') as f:
                for span in span_contents:
                    info = span.xpath("string(.)")
                    f.write(info + "\n")
                    # print(info)

if __name__ == "__main__":
    # url 存储器
    queue_url = Queue()  # 创建队列
    # 内容 存储器
    queue_html = Queue()  # 创建队列
    base_url = "https://www.qiushibaike.com/8hr/page/{}/"
    for num in range(1, 14):
        page_url = base_url.format(num)
        queue_url.put(page_url)  # 把要爬取的url存储到队列中

    # 创建线程,开启线程
    crawllist = []
    for i in range(3):
        crawlInfo = CrawlInfo(queue_url, queue_html)
        crawllist.append(crawlInfo)
        crawlInfo.start()
    for crawl in crawllist:
        crawl.join()

    parselist = []
    for i in range(3):
        parseInfo = ParseInfo(queue_html)
        parselist.append(parseInfo)
        parseInfo.start()
    for parse in parselist:
        parse.join()





