# -*- coding: utf-8 -*-

# Scrapy settings for ScrapyExample project
#
# For simplicity, this file contains only settings considered important or
# commonly used. You can find more settings consulting the documentation:
#
#     https://doc.scrapy.org/en/latest/topics/settings.html
#     https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#     https://doc.scrapy.org/en/latest/topics/spider-middleware.html

BOT_NAME = 'ScrapyExample'

SPIDER_MODULES = ['ScrapyExample.spiders']
NEWSPIDER_MODULE = 'ScrapyExample.spiders'

### 配置日志信息目录与文件以及日志级别
# import datetime
# # 获取当前时间current_time
# CURRENT_TIME = datetime.datetime.now()
# # 项目目录下新建log目录:
# LOG_FILE_PATH = 'logs/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year,CURRENT_TIME.month,CURRENT_TIME.day)
# # 日志信息的存储文件位置,设置后终端不会显示日志信息:
# LOG_FILE = LOG_FILE_PATH
# LOG_LEVEL = "INFO"

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ScrapyExample (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'

# Obey robots.txt rules
ROBOTSTXT_OBEY = False

# Configure maximum concurrent requests performed by Scrapy (default: 16)
#CONCURRENT_REQUESTS = 32

# Configure a delay for requests for the same website (default: 0)
# See https://doc.scrapy.org/en/latest/topics/settings.html#download-delay
# See also autothrottle settings and docs
#DOWNLOAD_DELAY = 3
# The download delay setting will honor only one of:
#CONCURRENT_REQUESTS_PER_DOMAIN = 16
#CONCURRENT_REQUESTS_PER_IP = 16

# Disable cookies (enabled by default)
#COOKIES_ENABLED = False

# Disable Telnet Console (enabled by default)
#TELNETCONSOLE_ENABLED = False

# Override the default request headers:
#DEFAULT_REQUEST_HEADERS = {
#   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
#   'Accept-Language': 'en',
#}

# Enable or disable spider middlewares
# See https://doc.scrapy.org/en/latest/topics/spider-middleware.html
#SPIDER_MIDDLEWARES = {
#    'ScrapyExample.middlewares.ScrapyexampleSpiderMiddleware': 543,
#}

# Enable or disable downloader middlewares
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html
#DOWNLOADER_MIDDLEWARES = {
#    'ScrapyExample.middlewares.ScrapyexampleDownloaderMiddleware': 543,
#}

# Enable or disable extensions
# See https://doc.scrapy.org/en/latest/topics/extensions.html
#EXTENSIONS = {
#    'scrapy.extensions.telnet.TelnetConsole': None,
#}

# Configure item pipelines
# See https://doc.scrapy.org/en/latest/topics/item-pipeline.html
ITEM_PIPELINES = {
   # 'ScrapyExample.pipelines.ScrapyexamplePipeline': 300,
   # 'ScrapyExample.pipelines.TengxunPipeline': 200,
   # 'ScrapyExample.pipelines.SuncrawlPipeline': 100,
   # 'ScrapyExample.pipelines.YycrawlfbsPipeline': 200,
   # 分布式爬虫设置redis为item,pipeline
   'scrapy_redis.pipelines.RedisPipeline' : 300
}
# Enable and configure the AutoThrottle extension (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/autothrottle.html
#AUTOTHROTTLE_ENABLED = True
# The initial download delay
#AUTOTHROTTLE_START_DELAY = 5
# The maximum download delay to be set in case of high latencies
#AUTOTHROTTLE_MAX_DELAY = 60
# The average number of requests Scrapy should be sending in parallel to
# each remote server
#AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0
# Enable showing throttling stats for every response received:
#AUTOTHROTTLE_DEBUG = False

# Enable and configure HTTP caching (disabled by default)
# See https://doc.scrapy.org/en/latest/topics/downloader-middleware.html#httpcache-middleware-settings
#HTTPCACHE_ENABLED = True
#HTTPCACHE_EXPIRATION_SECS = 0
#HTTPCACHE_DIR = 'httpcache'
#HTTPCACHE_IGNORE_HTTP_CODES = []
#HTTPCACHE_STORAGE = 'scrapy.extensions.httpcache.FilesystemCacheStorage'



### scrapy-redis分布式爬虫配置信息
# 必须:指定使用scrapy-redis的调度器(Scheduler),确保request保存到redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 必须:指定使用scrapy-redis的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 必须:不清理redis队列
SCHEDULER_PERSIST = True
# 必须:指定redis数据库的连接参数
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379

REDIS_ENCODING = 'utf-8'