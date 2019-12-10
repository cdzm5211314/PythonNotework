# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 13:42


import requests
from lxml import etree
from queue import Queue
import threading
import time

class bsSpider:
    def __init__(self):
        self.baseurl = "http://www.budejie.com/"
        self.headers = {"User-Agent":"Mozilla/5.0"}
        # url队列
        self.urlQueue = Queue()
        # 响应队列
        self.resQueue = Queue()

    # 生成URL队列
    def getUrl(self):
        for pNum in range(1,51):
            # 拼接URL
            url = self.baseurl + str(pNum)
            self.urlQueue.put(url)

    # 响应队列
    def getHtml(self):
        while True:
            url = self.urlQueue.get()
            res = requests.get(url,headers=self.headers)
            res.encoding = "utf-8"
            html = res.text
            # 放到响应队列
            self.resQueue.put(html)
            # 清除此任务
            self.urlQueue.task_done()

    # 解析页面
    def getContent(self):
        while True:
            # 从响应队列中依次获取html源码
            html = self.resQueue.get()
            parseHtml = etree.HTML(html)
            r_list = parseHtml.xpath('//div[@class="j-r-list-c-desc"]/a/text()')
            for r in r_list:
                print(r+"\n")
            # 清除任务
            self.resQueue.task_done()

    def run(self):
        # 存放所有的线程
        thread_list = []
        # 获取url队列
        self.getUrl()
        # 创建getHtml线程
        for i in range(5):
            threadRes = threading.Thread(target=self.getHtml)
            thread_list.append(threadRes)

        # 解析线程
        for i in range(3):
            threadParse = threading.Thread(target=self.getContent)
            thread_list.append(threadParse)

        # 所有线程开始干活
        for th in thread_list:
            th.setDaemon(True)
            th.start()

        # 如果队列为空,则执行其他程序
        self.urlQueue.join()
        self.resQueue.join()

        print("运行结束")

if __name__ == "__main__":
    begin = time.time()
    spider = bsSpider()
    spider.run()
    end = time.time()
    print(end-begin)

