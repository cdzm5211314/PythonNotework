# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 13:54

# tesseract下载安装: https://digi.bib.uni-mannheim.de/tesseract/
# 语言包下载地址: https://github.com/tesseract-ocr/tessdata/find/master

# 安装tesseract及配置环境变量:
# 1. 设置path环境变量[安装路径]: path: E:\Tesseract-OCR
# 2. 创建新的环境变量[安装路径下]: TESSDATA_PREFIX: E:\Tesseract-OCR\tessdata

# 终端命令识别图片验证: tesseract -v
# tesseract imagename.png[目标图片文件名,需加格式后缀] outputfile.txt[是转换结果文件名]
# 如: tesseract aaaimg.png bbbfile.txt
# 如: tesseract aaaimg.png bbbfile.txt -l chi_sim[指定识别语言-中文,默认是英文]

### Python代码中使用tesseract识别图形验证码
# 安装pytesseract: pip install pytesseract
# 如果没有PIL模块,需要安装: pip install PIL


import pytesseract
from PIL import Image

# 指定tesseract.exe的安装路径的所在位置
pytesseract.pytesseract.tesseract_cmd = "E:\Tesseract-OCR\tesseract.exe"
# 打开需要识别的图片
image = Image.open("img.png")
# 将图片中的内容转换为文字信息
text = pytesseract.image_to_string(image)  # 默认识别英文
# text = pytesseract.image_to_string(image,lang="chi_sim")  # 设置识别中文
print(text)  # 识别图片后的内容

####################################################################################################
### 登陆豆瓣使用验证码示例
import requests
from lxml import etree
import pytesseract
from PIL import Image
from selenium import webdriver

url = "https://www.douban.com/"
headers = {"User-Agent": "Mozilla/5.0"}
## 请求豆瓣网登陆url地址,获取响应
res = requests.get(url, headers=headers)
res.encoding = "utf-8"
html = res.text  # 获取请求响应的内容
## 使用xpath表达式把响应中的验证码图片的链接给拿到
parseHtml = etree.HTML(html)
imgurl = parseHtml.xpath('//img[@class="captcha_image"]/@src')[0]
## 请求验证码图片url地址,得到响应图片内容(字节流)
res = requests.get(imgurl, headers=headers)
res.encoding = "utf-8"
imgcontent = res.content
## 把图片内容保存到本地
with open("验证码.jpg", "wb") as f:
    f.write(imgcontent)
## 使用pytesseract识别本地图片(验证码.jpg) ---> 转为字符串内容
image = Image.open("验证码.jpg")
img_str = pytesseract.image_to_string(image)  # 识别图片获取内容
print(img_str)
## 把识别后的字符串内容输入到验证码框中
driver = webdriver.Chrome()
driver.get(url)
driver.find_element_by_name("captcha-solution").send_keys(img_str)
driver.save_screenshot("验证码输入.png")
## 关闭浏览器
driver.quit()
