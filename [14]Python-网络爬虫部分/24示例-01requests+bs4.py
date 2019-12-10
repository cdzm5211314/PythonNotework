# -*- coding:utf-8 -*-
# @Desc : 需求: 爬取下厨房首页的所有图片
# @Author : Administrator
# @Date : 2019-09-16 11:26

# 下厨房: http://www.xiachufang.com/

import os
import requests
from bs4 import BeautifulSoup
from urllib import parse

# 发送请求
res = requests.get('http://www.xiachufang.com/')
# 使用BeautifulSoup作为解析对象
# bs = BeautifulSoup(res.text, 'lxml')  # res.text 获取的响应内容是字符串类型的数据,有可能产生乱码
bs = BeautifulSoup(res.content.decode('utf-8'), 'lxml')  # res.content 获取的响应内容是bytes类型的数据,所以需要utf-8解码

# 提取首页中的所有img标签数据
img_list = []
for img in bs.select('img'):
    # 然后获取img标签中的图片的地址
    if img.has_attr('data-src'):
        img_list.append(img.attrs['data-src'])
    else:
        img_list.append(img.attrs['src'])

# 然后根据图片的地址列表信息下载图片
# 存放下载图片的目录格式
image_dir = os.path.join(os.path.curdir, 'images')
# 判断目录是否存在,不存在就创建此目录
# if not os.path.isdir(image_dir):
#     os.mkdir(image_dir)  # 创建目录

print(len(img_list))
for img_url in img_list[:len(img_list) - 2]:
    img = parse.urlparse(img_url)  # 拆分url路径地址信息
    filename = img.path[1:].split('@')[0]  # 获取图片文件的名字
    filepath = os.path.join(image_dir, filename)  # 组建 图片目录 + 图片文件
    if not os.path.isdir(os.path.dirname(filepath)):
        os.mkdir(os.path.dirname(filepath))  # 创建文件
    # print(filepath)
    # print(img_url)  # 小图片形式的地址
    url = '%s://%s/%s' % (img.scheme, img.netloc, filename)
    # print(url)
    res = requests.get(url)  # 请求图片url地址信息
    with open(filepath, 'wb') as f:
        for chunk in res.iter_content(1024):  # 图片文件较大时可以根据字节快去读取内容
            f.write(chunk)
        print(filename + ' 图片下载完成...')
