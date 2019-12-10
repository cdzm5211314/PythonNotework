# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 12:49

### 斗鱼直播爬取

from selenium import webdriver
from lxml import etree
import time

# 把Chrome设置无界面浏览器
opt = webdriver.ChromeOptions()
opt.set_headless()
# 创建浏览器对象,发请求
driver = webdriver.Chrome(options=opt)
driver.get("https://www.douyu.com/directory/all")
i = 1

# 循环
while True:
    # 解析(driver.page_source)
    # 获取主播名称 和 观众人数
    parseHtml = etree.HTML(driver.page_source)
    names = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-name ellipsis fl"]')
    numbers = parseHtml.xpath('//div[@id="live-list-content"]//span[@class="dy-num fr"]')

    for name,number in zip(names,numbers):
        print("\t主播名称：%s \t观众人数：%s" %
              (name.text.strip(),number.text.strip()))
        #for name,number in [("主播1","20万"),("主播2","15万")]
    print("第%d页爬取成功" % i)
    i += 1
    # 判断是否需要点击下一页
    # 能点 ：点击,继续循环
    if driver.page_source.find("shark-pager-disable-next") == -1:
        driver.find_element_by_class_name("shark-pager-next").click()
        time.sleep(1)
    else:
        break
    # 不能点 ：break

print("一共爬取了%d页" % i)



################################################################################
### 京东商品爬取
from selenium import webdriver
import time
import csv

# 接受用户输入,访问京东
pro = input("请输入要爬取的商品：")
driver = webdriver.Chrome()
driver.get("https://www.jd.com/")
i = 1
# 发送文字到搜索框,点击搜索
text = driver.find_element_by_class_name("text")
text.send_keys(pro)

button = driver.find_element_by_class_name("button")
button.click()
time.sleep(1)

while True:
    # 动态加载-->全部加载
    # 执行脚本,进度条拉到底部
    driver.execute_script(
        'window.scrollTo(0,\
         document.body.scrollHeight)')
    time.sleep(2)
    # 正常解析爬取
    r_list = driver.find_elements_by_xpath \
        ('//div[@id="J_goodsList"]//li')

    # r为每一个商品的节点对象
    for r in r_list:
        m = r.text.split('\n')
        # ["￥52.80","Python...","200+",]
        price = m[0]
        name = m[1]
        commit = m[2]
        market = m[3]

        with open("商品.csv","a",newline="",encoding="gb18030") as f:
            writer = csv.writer(f)
            L = [name.strip(),price.strip(),
                 commit.strip(),market.strip()]
            writer.writerow(L)

    print("第%d页爬取成功" % i)
    i += 1
    # 点击下一页
