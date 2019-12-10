# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 8:55

import requests
from lxml import etree
import time

class BaiduImageSpider:
    def __init__(self):
        self.headers = {"User-Agent":"Mozilla/5.0"}
        self.baseurl = "http://tieba.baidu.com"
        self.pageurl = "http://tieba.baidu.com/f?"

    # 获取所有帖子URL列表
    def getPageUrl(self,params):
        res = requests.get(self.pageurl,params=params,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 构建解析对象
        parseHtml = etree.HTML(html)
        # 帖子链接列表
        t_list = parseHtml.xpath('//div[@class="t_con cleafix"]/div/div/div/a/@href')
        # t_list : ['/p/233432','/p/2039820',..]
        print(t_list)
        for t_link in t_list:
            # 拼接帖子完整链接
            t_link = self.baseurl + t_link
            self.getImageUrl(t_link)

    # 获取帖子中图片URL列表
    def getImageUrl(self,t_link):
        res = requests.get(t_link,headers=self.headers)
        res.encoding = "utf-8"
        html = res.text
        # 构造解析对象
        parseHtml = etree.HTML(html)
        img_list = parseHtml.xpath('//img[@class="BDE_Image"]/@src')
        print(img_list)
        for img_link in img_list:
            self.writeImage(img_link)

    # 保存到本地
    def writeImage(self,img_link):
        # 获取图片的bytes
        res = requests.get(img_link,headers=self.headers)
        res.encoding = "utf-8"
        html = res.content
        # filename
        filename = img_link[-12:]
        with open(filename,"wb") as f:
            f.write(html)
            time.sleep(0.5)
            print("%s下载成功" % filename)

    # 主函数
    def workOn(self):
        name = input("请输入贴吧名:")
        begin = int(input("请输入起始页:"))
        end = int(input("请输入终止页:"))

        for n in range(begin,end+1):
            pn = (n-1)*50
            params = {
                "kw":name,
                "pn":str(pn)
            }
            self.getPageUrl(params)

if __name__ == "__main__":
    spider = BaiduImageSpider()
    spider.workOn()


