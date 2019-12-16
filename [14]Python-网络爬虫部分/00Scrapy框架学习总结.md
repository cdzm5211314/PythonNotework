### Scrapy框架常用的基本命令:
- 全局命令:
    - scrapy --help  # 查看scrapy的使用命令
    - scrapy view "url地址"  # 该命令会将网页document内容下载下来,并且在浏览器显示
    - scrapy fetch "url地址"  # 该命令会通过scrapy downloader将网页源码下载下来显示
    - scrapy startproject "工程名"  # 创建项目工程
    - scrapy genspider "爬虫名字" "爬虫的域名"  # 创建爬虫文件
    - scrapy shell "url地址"  # 命令行交互模
    - scrapy runspider "爬虫文件名.py"  # 启动爬虫程序
- 项目命令:
    - scrapy list  # 列出项目下的爬虫
    - scrapy check  # 检查代码是否有错误
    - scrapy crawl "爬虫名字"  # 启动弄爬虫程序
### Scrapy项目目录结构
```
|- scrapyproject: 项目根目录
    |- scrapyproject: 项目同名目录
        |- spiders: 项目的爬虫文件目录
            |- __init__.py
        |- __init__.py: 项目的初始化文件，用来对项目做初始化工作
        |- items.py: 项目的数据容器文件，用来定义要获取的数据结构
        |- middlewares.py: 项目的中间件文件
        |- pipelines.py: 项目的管道文件，用来对items中的数据进行进一步的加工处理
        |- settings.py: 项目的设置文件，包含了项目的设置信息
    |- scrapy.cfg: 项目的配置文件
```

### 创建爬虫文件
> 注:如果一个项目中有多个爬虫,爬虫名称必须是唯一   
* 创建基础的爬虫模版:
> scrapy genspider [-t basic] 爬虫名称 爬虫网站域名  
```python
# 基本爬虫文件基本内容
import scrapy
class QsbkSpider(scrapy.Spider):
    name = 'qsbk' # 爬虫的名称(唯一)
    allowed_domains = ['qiushibaike.com']  # 允许爬虫爬取的域名
    start_urls = ['http://qiushibaike.com/']  # 开始爬取的网址
    def parse(self, response):  # 解析响应数据response
        pass 
```
* 创建自动的爬虫模版:
> scrapy genspider -t crawl 爬虫名称 爬虫网站域名  
```python
# 自动爬虫文件基本内容
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
class QsbkSpider(CrawlSpider):
    name = 'qsbk'  # 爬虫名称
    allowed_domains = ['qiushibaike.com']  # 允许的域名,只有在这个里面指定的域名的url才会被提取
    start_urls = ['http://qiushibaike.com/']
    rules = (
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # 可以写多个Rule匹配规则
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="bookname"]//a[4]'), callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        item = {}
        return item
        
## LinkExtractor的参数详解: LinkExtractor就是url链接提取器，自动提取出来我们需要爬取的url链接
# allow=()：允许的url，所有满足这个正则表达式的url都会被提取出来 　
# deny=()：禁止的url,所有满足这个正则表达式的url都不会被提取出来
# allowed_domains=(): 允许的域名,只有在这个里面指定的域名的url才会被提取
# deny_domains=(): 禁止的域名,所有在这个里面指定的域名的url都不会被提取
# deny_extensions = None: 默认值为None,排除非网页链接
# restrict_xpaths=()：使用xpath表达式提取，和allow共同作用过滤链接
# restrict_css=(): 使用css选择器提取,和allow共同作用过滤链接
# tags=('a','area'): 接收一个标签(字符串)或一个标签列表,提取指定标签内的链接
# attrs=('href',): 默认提取tags里的href属性，也就是url链接
# unique=True: 默认值为True,是否应对提取的链接应用重复过滤
# process_value=None: 默认值为None,作用比较强大了,他接受一个函数,可以立即对提取到的地址做加工,优先级要大于allow 
# strip: 默认值为True,是把地址前后多余的空格删除

## LinkExtractor有唯一的公共方法extract_links(response),它接受一个Response对象,并返回一个scrapy.link.Link对象

## Rule的参数详解: 如下
# LinkExtractor(): 一个LinkExtractor对象,用来定义爬虫规则
# callback: 满足这个规则的url,应该要执行哪个回调函数,因为CrawlSpaider使用了parse作为回调函数,因此不要覆盖parse作为回调函数自己的回调函数
# follow: 默认为True(跟进),根据该规则从response中提取到的链接是否需要继续跟进,如果callback有值,默认follow为False
# process_links: 从link_extractor中获取到链接后会传递到这个函数,用来过滤不需要爬取的链接(过滤链接的函数)
# process_request: 一个过滤链接Request的函数
# cb_kwargs: 传递给回调函数的参数字典

# 注: Rule无论有无callback，都由同一个_parse_response函数处理，只不过他会判断是否有follow和callback

``` 
### 测试执行爬虫文件
* 第一种方式(全局): 即未创建项目,终端命令行
> scrapy runspider 爬虫文件.py  
* 第二种方法(项目): 即创建过项目,终端命令行  
> scrpay crawl 爬虫名称           # 有日志信息  
> scrpay crawl 爬虫名称 --nolog   # 无日志信息  
> scrpay crawl 爬虫名称 -o 文件名称 ---》 scrpay crawl qidian -o book.json   
> scrpay crawl 爬虫名称 -o 文件名称 ---》 scrpay crawl qidian -o book.csv  
* 第三种方式(项目): 运行文件
```python
# 在项目根目录下(即settings.py文件同级目录下)创建如run.py文件
from scrapy.cmdline import execute
execute(["scrapy","crawl","爬虫名称","--nolog"])
execute("scrapy crawl 爬虫名称 --nolog".split())
# 然后执行run.py文件,就是运行爬虫文件
# 注: 测试爬虫文件可能报错:ModuleNotFoundError: No module named 'win32api'.需要安装模块:`pip install pypiwin32`

## 在PyCharm中运行run.py文件: 配置信息
# 1.选项: 在菜单栏 ---> Run ---> Editconfigurations ---> + ---> python
# 2.配置信息: name ---> 随便命名(文件名称)   Script ---> run.py文件路径   Working directory ---> 工程项目路径 

```
### Scrapy Shell: 终端测试数据提取
> 首先进入到Scrapy项目根目录  
> 然后`workon`到Python虚拟环境  
> 使用`scrapy shell "url地址"`发起请求  
> 测试爬取的数据...  

### Scrapy项目设置信息文件:`settings.py`
```python
### robots.txt: 是遵循Robot协议的一个文件,保存在网站服务器中,作用是需要爬虫文件不能爬取本网站的哪些内容,默认是开启的  
ROBOTSTXT_OBEY = True  # 设置成False,是拒绝遵守Robot协议 

### 设置请求头信息(模拟客户端浏览器):
USER_AGENT = 'ScrapyDemo (+http://www.yourdomain.com)'
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0'
USER_AGENT = [
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
  "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
  "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
]
### 默认的请求头信息,也可以添加User-Agent头信息:
DEFAULT_REQUEST_HEADERS = {
   'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
   'Accept-Language': 'en',
   'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
}

### 添加日志文件信息
## 设置日志的级别或者把日志信息存储到文件中
# 日志的级别(从高到低): CRITICAL(严重错误) ERROR(一般错误) WARNING(警告) INFO(一般信息) DEBUG(调试信息)[默认级别]
# 日志信息级别:  
# LOG_LEVEL = "INFO"  
# 以每天日期为日志文件名称  
# import datetime  
# 获取当前时间current_time   
# CURRENT_TIME = datetime.datetime.now()  
# 项目目录下新建log目录:  
# LOG_FILE_PATH = 'logs/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year,CURRENT_TIME.month,CURRENT_TIME.day)  
# 日志信息的存储文件位置,设置后终端不会显示日志信息:  
# LOG_FILE = LOG_FILE_PATH  


```

### 编写爬虫文件数据容器: `items.py`
```python
import scrapy
class PaChongItem(scrapy.Item):
    author = scrapy.Field()  # 存储数据字段 
    content = scrapy.Field() # 存储数据字段 
# PaChongItem类型数据转换为字典类型数据: dict(PaChongItem())
```
### 编写爬虫文件数据爬取: `爬虫文件.py`
```python
from ./items import PaChongItem
def parse(self, response):
    item = PaChongItem()
    item["author"] = response.xpath('.//div[@class = "author clearfix"]//img/@alt').extract_first()
    item["content"] = response.xpath('.//a//span/text()').extract_first().strip()  
    yield item  # 推送item数据到pipeline
    # 或者如下所写:
    # author = response.xpath('.//div[@class = "author clearfix"]//img/@alt').extract_first()
    # content = response.xpath('.//a//span/text()').extract_first().strip() 
    # item = QsbkItem(author = author,content = content)   
    # yield item  # 推送item数据到pipeline
```
### XPATH爬虫文件数据提取选择器
```python
# / :                       表示在子标签中查找
# // :                      表示在子孙标签中查找
# .// :                     表示当前对象的子孙标签中查找
# /div :                    表示子标签的div标签
# //div :                   表示子孙中的所有div标签
# /div[@class='name'] :     表示子标签的div标签并且class属性值为name的
# //div[@class='name'] :    表示子孙标签的div标签并且class属性值为name的
# //div/text() :            表示所有子孙标签下的文本内容
# obj.xpath("string(.)") :  表示取当前标签下的所有文本内容
# obj.extract() :           列表中的每一个对象转换为字符串
# obj.extract_first() :     获取列表中的第一个元素
# ''.join(obj.xpath("表达式").extract()): 将序列中的元素以指定的字符连接成一个新的字符串
```
### spider爬虫文件获取数据的方法
- scrapy.selector.unified.SelectorList对象: getall() == extract() , get() == extract_first()
- scrapy.selector.unified.Selector对象: getall() == extract() , get() != extract_first()

### 编写爬虫文件数据处理: `pipelines.py`
- spider爬虫文件使用`yield`只能推送字典类型数据和item类型数据到pipeline
- spider爬虫文件使用`return`一次性返回所有的item到pipeline
- 注: spider爬虫文件可以配置自己单独的pipeline,这样数据就不会存储到其他的pipeline中
```python
# 1. 编写一个spider爬虫文件对应的pipeline类,类中有三个方法
class PaChongPipeline(object):
    def __init__(self,conn_str):
        self.conn_str = conn_str
    @classmethod
    def from_crawler(cls, crawler):
        # 初始化时候，用于创建pipeline对象
        conn_str = crawler.settings.get('DB')
        return cls(conn_str)
    def open_spider(self,spider):
        """开启爬虫时执行,只执行一次,可省略"""
        pass
    def process_item(self, item, spider):
        """爬虫有数据传送过来,就作处理"""
        return item  # 交给下一个pipeline处理
        # raise DropItem()  # 抛出异常DropItem表示终止，否则继续交给后续的pipeline处理
    def close_spider(self,spider):
        """关闭爬虫时执行,只执行一次,可省略"""
        pass
# 2. 在settings.py文件开启pipeline
# 注: 在此为spider爬虫文件开启pipeline,数值越小,优先级越高(同时数据也会存到其他的pipeline中)
ITEM_PIPELINES = {
   'ScrapyCrawler.pipelines.ScrapycrawlerPipeline': 300,  # 项目创建时自动生成的
}
```

### 为spider爬虫文件设置自己单独的pipeline
```python
# settings配置的是全局的pipeline管道
ITEM_PIPELINES = {
   'ScrapyCrawler.pipelines.PaChongPipeline': 200,
}
# 第一种: 直接在spider爬虫文件中里设置pipeline管道
custom_settings = {
    "ITEM_PIPELINES": {
        'ScrapyCrawler.pipelines.PaChongPipeline': 300,
    }
}
# 第二种: 可以在 pipeline 里判断是哪个爬虫的结果 ---> spider.name 属性
class PaChongPipeline(object):
    def process_item(self, item, spider):
        if spider.name == "爬虫名字1":
            print("处理spider1的数据")
        elif spider.name == "爬虫名字2":
            print("处理spider2的数据")
        else:
            print("处理其他spiser的数据")
```


### Request与Response对象的讲解
```python
## Request: 发送请求,参数详解
# url: request对象发送请求的url地址
# callback: 在下载器下载完相应的数据后执行的回到函数
# method: 请求方式,默认为`GET`方法,可以设置为其他方法
# headers: 请求头,对于一些固定的设置,可以放在`settings.py`文件中设置,对于非固定的,可以在发送请求时指定
# meta: 比较常用,用于在不同的请求之间传递数据时使用
# encoding: 编码,默认为`utf-8`,使用默认就可以了
# dot_filter: 默认为True,表示不对URL过滤去重,在执行多次重复请求的时候用的比较多,设置为Flase表示对URL去重
# errback: 在发生错误的时候执行的函数

## Response: 由Scrapy自动构建,主要用来提取数据,属性详解
# text: 将返回来的数据作为`unicode`字符串返回
# body: 将返回来的数据作为`bytes`字符串返回
# xpath: 提取数据选择器
# css: 提取数据选择器
# meta: 从其他请求传递过来的`meta`属性,可以用来保持多个请求之间的数据连接
# encoding: 返回当前字符串编码和解码的格式

# 注: 1.如果我们请求数据的时候发送POST请求,需要使用Resquest子类FormRequest来实现
# 注: 2.如果我们在爬虫一开始就发送POST请求,需要在爬虫类中重写`start_request(self)`方法,并且不在调用start_url列表中的url
```

### 下载文件和图片的: FilesPipeline, ImagesPipeline
```python
## FilesPipeline: 自动下载文件: from scrapy.pipelines.files import FilesPipeline
# 1. 定义一个Item,在Item中定义两个属性file_urls和files,file_urls用来存储需要下载的文件的url地址,是一个列表
# 2. 当文件下载完成后,会把文件的相关信息存储到Item的files属性中,如:下载路径,下载url和文件的校验码等
# 3. 在settings.py文件中添加属性设置: FILES_STORE ,用来设置文件下载下来的存储位置(本地)
# 4. 启动pipeline,在settings.py的ITEM_PIPELINES属性中添加: scrapy.pipelines.files.FilesPipeline:1

## ImagesPipeline: 自动下载图片: from scrapy.pipelines.images import ImagesPipeline
# 1. 定义一个Item,在Item中定义两个属性image_urls和images,image_urls用来存储需要下载的图片的url地址,是一个列表
# 2. 当图片下载完成后,会把图片的相关信息存储到Item的images属性中,如:下载路径,下载url和图片的校验码等
# 3. 在settings.py文件中添加属性设置: IMAGES_STORE ,用来设置图片下载下来的存储位置(本地)
# 4. 启动pipeline,在settings.py的ITEM_PIPELINES属性中添加: scrapy.pipelines.images.ImagesPipeline:1 

## 实现自定义分类下载图片,需要在pipelines.py文件中自定义pipeline类并继承ImagesPipeline
# 核心是重写: get_media_requests(self, item, info) 和 item_completed(self, results, item, info) 这2个方法

```

### 中间件分类: Downloader Middlewares 与 Spider Middlewares
```python
## 下载器中间件: Downloader Middlewares
# 下载器中间件: 是引擎和下载器之间通信的中间件,在这个中间件中科院设置IP代理,更换请求头等来达到反反爬虫的目的
# 下载器中间件核心实现两个方法: process_request, process_response
# process_request(self, request, spider): 
    # 执行时间:在request对象前往downloader的过程中调用
    # 返回值:None,一切正常,继续执行其他中间件链的process_request函数
    # 返回值:Response,停止调用process_request和process_exception函数,也不在继续下载该请求,而是调用process_response函数流程
    # 返回值:Request,停止调用process_request函数,交由调度器重新安排下载
    # 抛出IgnoreRequest异常,process_exception函数会被调用,如果没有此方法,request.errback方法会被调用,如果errback也没有,则会被忽略掉,甚至连日志都没有
# process_response(self, request, response, spider):
    # 执行时间:将下载结果返回给engine引擎的过程中调用
    # 返回值:Response,继续执行其他中间件链的process_response函数
    # 返回值:Request,停止调用process_request函数,交由调度器重新安排下载
    # 抛出IgnoreRequest异常,request.errback方法会被调用,如果errback也没有,则会被忽略掉,甚至连日志都没有 
# process_exception(self, request, exception, spider):
    # 执行时间:在下载过程中出现异常调用,或者在process_request函数抛出IgnoreRequest异常时调用
    # 返回值:None,继续执行其他中间件链的process_exception函数
    # 返回值:Response,开始中间件链的process_response处理流程
    # 返回值:Request,停止调用process_request函数,交由调度器重新安排下载
    # 抛出IgnoreRequest异常,request.errback方法会被调用,如果errback也没有,则会被忽略掉,甚至连日志都没有  

## 爬虫中间件: Spider Middlewares
# process_spider_input(self,response,spider): 接收一个response对象并处理
# process_spider_output(self,response,result,spider): 当Spider处理response返回result时,该方法被调用
# process_spider_exception(self,response,exception,spider): spider出现的异常时被调用
# process_start_requests(self,start_requests,spider): 当spider发出请求时,被调用
```

### 中间件(随机请求头): 随机获取User-Agent
- 第一种固定写法: `settings.py`
```python
USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'
```
- 第二种动态获取: 使用随机请求头中间件方式
```python
# 1.在settings.py文件中注销USER_AGENT:
# USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36' 
# 2.[或]创建一个文件[useragentmiddlewares]编写一个类[UserAgentMiddleware],或者直接在middlewares.py文件中编写一个类: 如 UserAgentMiddleware
from fake_useragent import UserAgent
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent',UserAgent().chrome)
        # request.headers.setdefault(b'User-Agent',UserAgent().random)
        # request.headers['User-Agent'] = UserAgent.random()
# 3.在settings.py中的开启DOWNLOADER_MIDDLEWARES
DOWNLOADER_MIDDLEWARES = {
  # 注:DOWNLOADER_MIDDLEWARES的middleware与上面编写的类一致,如果还是不能动态获取User-Agent,就调他的优先级,数字越小优先级越高
   'ScrapyDemo.middlewares.UserAgentMiddleware': 343, # 数字越小表示优先级越高
}
```
- 第三种动态获取:
```python
# 1.在setting.py中定义一个User-Agent的列表
USER_AGENT = [
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
   "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
   "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
]
# 2.在middlewares.py[文件中的内容可以清空]中编写一个类: UserAgentMiddleware
from ScrapyDemo.settings import USER_AGENT
from random import choice
class UserAgentMiddleware(object):
    def process_request(self, request, spider):
        request.headers.setdefault(b'User-Agent',choice(settings.USER_AGENT))
# 3.在settings.py中的开启DOWNLOADER_MIDDLEWARES
DOWNLOADER_MIDDLEWARES = {
    # 注:DOWNLOADER_MIDDLEWARES的middleware与上面编写的类一致,如果还是不能动态获取User-Agent,就调他的优先级,数字越小优先级越高
   'ScrapyDemo.middlewares.UserAgentMiddleware': 343, # 数字越小表示优先级越高
}
```
### 中间件(动态IP代理):
```python
# 1.创建一个文件[proxymiddlewares]编写一个类[ProxyMiddleware],或者直接在middlewares.py文件中编写一个类[ProxyMiddleware]
class ProxyMiddleware(object):
def process_request(self, request, spider):
    # request.meta['proxy'] = "http://ip:port"
    # request.meta['proxy'] = "http://username:password@ip:port"
    request.meta['proxy'] = "http://175.165.128.214:1133"
# 2.在settings.py中开启中间件
DOWNLOADER_MIDDLEWARES = {
   'ScrapyDemo.proxymiddlewares.Proxy': 343,
   # 或者'ScrapyDemo.middlewares.ProxyMiddleware': 343,
}
```
### 中间件(Scrapy对接selenium + phantomjs):
```python
# 1.创建一个文件[seleniummiddlewares]编写一个类[SeleniumMiddleware],或者直接在middlewares.py文件中编写一个类[SeleniumMiddleware]
from selenium import webdriver
class SeleniumMiddleware(object):
    def __init__(self):
        self.driver = webdriver.PhantomJS()
    def process_request(self, request, spider):
        # 注意：参数为request的url
        self.driver.get(request.url)
        self.driver.find_element_by_id("key").send_keys("爬虫")
        self.driver.save_screenshot("Jd.png")
# 2.在settings.py中开启中间件
DOWNLOADER_MIDDLEWARES = {
   'ScrapyDemo.middlewares.SeleniumMiddleware': 343,
}        
```
### Scrapy-Redis: 分布式爬虫组件
```python
### Scrapy是爬虫框架,但是不支持分布式,scrapy-redis是为了实现Scrapy分布式爬取,而提供以redis为基础的组件
### 将一个Scrapy项目变成一个scrapy-redis分布式项目:
## 1.安装scrapy-redis组件: pip install scrapy-redis
## 2.将Spider爬虫类从scrapy.Spider变成scrapy_redis.spiders.RedisSpider 或 将spider爬虫类从scrapy.CrawlSpider变成scrapy_redis.spiders.RedisCrawlSpider
## 3.将Spider爬虫类中的start_urls删除,增加一个redis_key = "xxx",redis_key是为了以后在redis中控制爬虫启动的,爬虫的第一个url,就是在redis中通过这个发出的
## 4.在settings.py文件中配置如下信息:
# ★指定使用scrapy-redis的调度器(Scheduler),确保request保存到redis
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# ★指定使用scrapy-redis的去重
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 默认情况下,RFPDupeFilter只记录第一个重复请求,将DUPEFILTER_DEBUG设置为True会记录所有重复的请求。
# DUPEFILTER_DEBUG =True
# ★不清理redis队列
SCHEDULER_PERSIST = True
# ★设置redis为item,pipeline
ITEM_PIPELINES = {
	'scrapy_redis.pipelines.RedisPipeline' : 300
}
# ★指定redis数据库的连接参数
# REDIS_URL = 'redis://passwd@localhost:6379'  # 如果设置此项,则此项优先级高于设置的REDIS_HOST 和 REDIS_PORT
REDIS_HOST = '127.0.0.1'
REDIS_PORT = 6379
# 指定排序爬取地址时使用的队列
SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'  # 默认的,按优先级排序
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'  # 可选的,按先进先出排序（FIFO）
# SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'  # 可选的,按后进先出排序（LIFO）
# LOG等级
# LOG_LEVEL = 'DEBUG'
# REDIS_ENCODING = 'utf-8'

### 运行一个爬虫项目步骤:
# 1.在spider爬虫服务器上,进入到爬虫文件所在路径,然后执行: scrapy runspider [爬虫文件].py
# 2.在redis服务器上,推入一个开始的url链接: redis-cli lpush [redis-key] [start_urls链接]
```

### 使用分布式爬虫:
* settings文件添加配置信息:
    * 安装scrapy-rdis: `pip install scrapy-redis`
    * 必须 - 使用了scrapy_redis 的调度器,在redis数据库里分配请求
        `SCHEDULER = "scrapy_redis.scheduler.Scheduler"`
    * 必须 - 使用了scrapy_redis 的去重组件,在redis数据库里做去重
        `DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"`
    * 必须 - 通过配置RedisPipeline将item写入key为 spider.name : items 的redis的list中,供后面的分布式处理item 这个已经由 scrapy-redis 实现，不需要我们写代码，直接使用即可
        `from scrapy_redis.pipelines import RedisPipeline
        ITEM_PIPELINES = {
            'scrapy_redis.pipelines.RedisPipeline': 100 ,
        }`
    * 必须 - 指定redis数据库的连接参数
        `REDIS_HOST = '127.0.0.1'
         REDIS_PORT = 6379`
        `或: REDIS_URL = redis://127.0.0.1:6639`
    * 可选 - 爬虫退出时,不清理redis中的数据
        `SCHEDULER_PERSIST = True`
* spider爬虫文件修改两个地方:
    * 继承类: 由scrapy.Spider更改为scrapy_redis.spiders.RedisSpider
    * start_url删除: 修改为 `redis_key = "项目名:start_urls"` ---> 即`xxx:start_urls`来代替初始化爬取的url
    * 在redis中设置`redis-key`的值: `redis-cli(链接redis) lpush xxx:start_urls http://www.baidu.com`

### scrapy-redis键名介绍: key - value
* "项目名:start_urls" ---> list类型,用于获取spider启动时爬取的`第一个url地址`
* "项目名:requests" ---> zset类型,用于scheduler调度处理requests,内容是`request对象字符串`
* "项目名:dupefilter" ---> set类型,用于爬虫访问的url去重,内容是`url地址的hash值字符串`
* "项目名:items" ---> list类型,保存爬虫获取到的数据item,内容是`json字符串`

### selenium + * 爬虫组合使用:
* 安装: pip install selenium
* selenium + phantomjs: 无界面浏览器(phantomjs下载:https://phantomjs.org/download.html[已弃用])
* selenium + chromedriver: chrome浏览器(chromedriver下载地址:http://chromedriver.storage.googleapis.com/index.html[注:需与chrome浏览器版本对应])
* selenium + geckodriver: firefox浏览器(geckodriver下载地址:https://github.com/mozilla/geckodriver/releases[注:需与firefox浏览器版本对应])
* 配置系统环境变量: path=E:\Installation_Tools\DriverUtils\chromedriver.exe; 或 在创建浏览器对象的时候使用绝对路径 
* 示例使用selenium + chromedriver:  如下
    ```python
    from selenium import webdriver
    # 创建chrome浏览器对象
    driver = webdriver.Chrome(executable_path='E:\Installation_Tools\DriverUtils\chromedriver.exe')
    # 发送请求获取网页信息
    driver.get("https://www.baidu.com")
    # 获取响应的html源码
    html_source = driver.page_source
    
    # 使用lxml库或bs4库作为解析对象:
    from lxml import etree  
    htmlElement = etree.HTML(html_source)  # 使用lxml作为解析对象
    # htmlElement.xpath('xpath语法')  # 使用xpath语法爬取数据
    # from bs4 import BeautifulSoup
    # bs = BeautifulSoup(html_source,'lxml')  # 使用bs4作为解析对象
    # bs.select('标签元素')  # 使用标签元素爬取数据
    # 使用selenium定位标签元素, 如
    # bs.find_element_by_xxx('标签元素')
    
    # 关闭当前页面
    driver.close()
    # 关闭整个浏览器
    driver.quit()
    ```