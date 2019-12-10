# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 14:58

import requests
import re
import pymongo

class MaoyanSpider:
    def __init__(self):
        self.baseurl = "http://maoyan.com/board/4?offset="
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.page = 1
        self.offset = 0
        self.proxies = {"http":"http://309435365:szayclhp@123.206.119.108:16817"}
        self.conn = pymongo.MongoClient("localhost",27017)
        self.db = self.conn.Film
        self.myset = self.db.top100


    # 下载页面
    def loadPage(self,url):
        res = requests.get(url,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        self.parsePage(html)

    # 解析页面
    def parsePage(self,html):
        p = re.compile('<div class="movie-item-info">.*?title="(.*?)".*?<p class="star">(.*?)</p>.*?releasetime">(.*?)</p>',re.S)
        r_list = p.findall(html)
        #        print(r_list)
        # [("霸王别姬","张国荣","1994-01-01"),(),()...]
        self.writeTomysql(r_list)

    def writeTomysql(self,r_list):
        for r_tuple in r_list:
            name = r_tuple[0].strip()
            star = r_tuple[1].strip()
            releasetime = r_tuple[2].strip()
            D = {"name":name,
                 "star":star,
                 "releasetime":releasetime}
            self.myset.insert(D)
        print("存入数据库成功")


    def workOn(self):
        while True:
            c = input("爬取请按y(y/n):")
            if c.strip().lower() == "y":
                self.offset = (self.page-1)*10
                url = self.baseurl + str(self.offset)
                self.loadPage(url)
                self.page += 1
            else:
                print("爬取结束,谢谢使用!")
                break

if __name__ == "__main__":
    spider = MaoyanSpider()
    spider.workOn()



