# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-12-06 15:23

# Gerapy 是一款分布式爬虫管理框架,支持 Python 3,基于 Scrapy、Scrapyd、Scrapyd-Client、Scrapy-Redis、Scrapyd-API、Scrapy-Splash、Jinjia2、Django、Vue.js 开发

# 1.Scrapy：是一个基于Twisted的异步IO框架，有了这个框架，我们就不需要等待当前URL抓取完毕之后在进行下一个URL的抓取，抓取效率可以提高很多。
# 2.Scrapy-redis：虽然Scrapy框架是异步加多线程的，但是我们只能在一台主机上运行，爬取效率还是有限的，Scrapy-redis库为我们提供了Scrapy分布式的队列，调度器，去重等等功能，有了它，我们就可以将多台主机组合起来，共同完成一个爬取任务，抓取的效率又提高了。
# 3.Scrapyd：分布式爬虫完成之后，接下来就是代码部署，如果我们有很多主机，那就要逐个登录服务器进行部署，万一代码有所改动..........可以想象，这个过程是多么繁琐。Scrapyd是专门用来进行分布式部署的工具，它提供HTTP接口来帮助我们部署，启动，停止，删除爬虫程序，利用它我们可以很方便的完成Scrapy爬虫项目的部署。
# 4.Gerapy：是一个基于Scrapyd，Scrapyd API，Django，Vue.js搭建的分布式爬虫管理框架。简单点说，就是用上述的Scrapyd工具是在命令行进行操作，而Gerapy将命令行和图形界面进行了对接，我们只需要点击按钮就可完成部署，启动，停止，删除的操作。


# Gerapy框架安装: pip install gerapy

# Gerapy框架是否安装成功: 执行 gerapy

# 初始化Gerapy项目: 新建一个目录,并在该目录下执行 gerapy init 进行初始化
# 注: 会在该目录下生成一个名字为gerapy的文件夹,进入gerapy该文件下,会看到一个projects的文件夹

# 初始化数据库: 进入到gerapy目录下执行 gerapy migrate
# 注: 会在gerapy目录下生产一个sqlite数据库,同时创建数据表

# 运行Gerapy服务: 执行 gerapy runserver
# 注: 本地执行gerapy runserver即可,远程执行 gerapy runserver 0.0.0.0:8000

# 访问Gerapy管理界面: http://127.0.0.1:8000 （8000为默认端口）




