# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-18 10:34

import requests

class TiebaSpider(object):

    def __init__(self, tieba_name):
        self.tieba_name = tieba_name
        self.tieba_url = "https://tieba.baidu.com/f?kw=" + tieba_name + "&ie=utf-8&pn={}"
        self.headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0'}

    def get_url_list(self,num):  # 1.构造url列表
        # urllist = []
        # for i in range(num):
        #     urllist.append(self.tieba_url.format(i * 50))
        # return urllist
        return [self.tieba_url.format(i*50) for i in range(num)]

    def parse_url(self,url):  # 发送请求,获取响应
        print(url)
        response = requests.get(url, headers=self.headers)
        return response.content.decode('utf-8')

    def save_html(self,html_str,page_num):  # 保存html字符串
        file_path = '{}-第{}页.html'.format(self.tieba_name,page_num)
        with open(file_path,'w',encoding="utf-8") as f:  # 月球-第3页.html
            f.write(html_str)

    def run(self,num):  # 实现主要逻辑
        # 1.构造url列表
        urllist = self.get_url_list(num)
        # 2.遍历,发送请求,获取响应
        for url in urllist:
            html_str = self.parse_url(url)
            # 3.保存数据
            page_num = urllist.index(url) + 1  # 页码数
            self.save_html(html_str,page_num)

if __name__ == '__main__':
    tiebaSpider = TiebaSpider("月球")
    tiebaSpider.run(3)


#############################################################################################

# import requests
# import json
#
# class DoubanSpider(object):
#
#     def __init__(self, tvtype):
#         self.tvtype = tvtype
#         self.url_temp = 'https://movie.douban.com/j/search_subjects?type=tv&tag=%s&sort=recommend&page_limit=20&page_start={}' % self.tvtype
#         self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:64.0) Gecko/20100101 Firefox/64.0"}
#
#     def parse_url(self, url):  # 2.发送请求,获取响应
#         print(url)
#         response = requests.get(url, headers=self.headers)
#         return response.content.decode()
#
#     def get_content_list(self, json_str):  # 3.提取数据
#         dict_result = json.loads(json_str)
#         content_list = dict_result['subjects']
#         return content_list
#
#     def save_content_list(self, content_list):  # 4.保存数据
#         with open('douban.json', 'a', encoding='utf-8') as f:
#             for content in content_list:
#                 f.write(json.dumps(content, ensure_ascii=False))
#                 f.write('\n')  # 换行
#             # for i in range(len(content_list)):  # 只保存获取的电视名称,URL地址以及电视评分
#             #     dict = {}
#             #     title = content_list[i]['title']
#             #     url = content_list[i]['url']
#             #     rate = content_list[i]['rate']
#             #     dict["title"] = title
#             #     dict["url"] = url
#             #     dict["rate"] = rate
#             #     f.write(json.dumps(dict, ensure_ascii=False))
#             #     f.write('\n')  # 换行
#         print("保存成功...")
#
#     def run(self):  # 实现主要逻辑
#         num = 0
#         while True:
#             # 1.start_url
#             start_url = self.url_temp.format(num)
#             # 2.发送请求,获取响应
#             json_str = self.parse_url(start_url)
#             # 3.提取数据
#             content_list = self.get_content_list(json_str)
#             # 4.保存数据
#             self.save_content_list(content_list)
#             if len(content_list) < 20:
#                 break
#             # 5.构造下一页的url地址,进入循环
#             num += 20
#
# if __name__ == '__main__':
#     # ['美剧','英剧','韩剧','日剧','国产剧','港剧']
#     douban = DoubanSpider("国产剧")
#     douban.run()
