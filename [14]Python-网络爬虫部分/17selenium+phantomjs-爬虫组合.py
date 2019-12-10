# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-19 10:34

## selenium + phantomjs: 网络爬虫组合(已弃用)
# selenium: Web自动化测试工具
# phantomjs：无界面浏览器(在内存执行页面加载)

# selenium安装: pip install selenium
# phantomjs安装: 下载地址:https://phantomjs.org/download.html,
# 安装一: Python安装目录的Scripts目录下,如 E:\Developer_Tools\PythonEnvs\python36\Scripts\phantomjs.exe
# 安装二: 每次使用指定绝对路径,如: E:\phantomjs.exe

# 测试是否安装成功: 进入Python虚拟环境,执行phantomjs命令

########################################################################################################

### selenium + phantomjs 使用:
from selenium import webdriver
## 创建浏览器对象
driver = webdriver.PhantomJS()
# driver = webdriver.PhantomJS(executable_path = "E:\phantomjs.exe")
# print(driver)
## 发送请求获取网页信息: get()
driver.get("http://www.baidu.com")
## 获取网页截屏
driver.save_screenshot("baidu.png")
## 获取响应的html源码
data = driver.page_source
print("下载成功")
## 关闭浏览器
driver.quit()

### driver浏览器对象方法:
## driver.get(url)  # 发送请求
## driver.page_source  # 获取响应的html源码
## driver.page_source.find("字符串")  # 从html源码中搜索指定字符串,查找失败返回-1

## 定位标签元素查找: find_element是获取第一个满足条件的元素,find_elements是获取所有满足条件的元素(列表)
# content = driver.find_element_by_id("id属性").text      # 获取id属性标签元素的文本内容
# inputTag = driver.find_element_by_id("id属性")
# inputTag = driver.find_element_by_class_name("class属性")
# inputTag = driver.find_element_by_name("name属性")
# inputTag = driver.find_element_by_tag_name("标签名称")
# inputTag = driver.find_element_by_xpath("xpath语法")
# inputTag = driver.find_element_by_css_selector("css选择器")

## 根据定位标签进行操作
# inputTag.send_keys("内容")
# inputTag.click()  # 单击点击


