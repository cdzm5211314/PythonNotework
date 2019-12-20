
### Scrapy框架学习-知识总结:
***
> Windows系统使用Scrapy框架需要依赖pywin32  
> 安装: pip install pywin32  
> 安装: [Twisted下载后安装](https://www.lfd.uci.edu/~gohlke/pythonlibs/)  

### Scrapy常用的基本命令:
* 全局命令:
    * scrapy --help # 查看scrapy的使用命令
    * scrapy view "url地址" # 该命令会将网页document内容下载下来,并且在浏览器显示
    * scrapy fetch "url地址" # 该命令会通过scrapy downloader将网页源码下载下来显示
    * scrapy startproject "工程名" # 创建项目工程
    * scrapy genspider "爬虫名字" "爬虫的域名" # 创建爬虫文件
    * scrapy shell "url地址" # 命令行交互模
    * scrapy runspider "爬虫文件名.py" # 启动爬虫程序
* 项目命令:
    * scrapy list # 列出项目下的爬虫
    * scrapy check # 检查代码是否有错误
    * scrapy crawl "爬虫名字" # 启动弄爬虫程序

### Scrapy项目目录结构:
* 创建Scrapy爬虫项目: `scrapy startproject projectname`
* Scrapy项目目录结构:
    * scrapy.cfg: 项目的配置信息文件
    * items.py: 数据存储模版,用于结构化数据
    * pipelines.py: 数据持久化操作
    * middlewares.py: 中间件文件
    * settings.py: 跟爬虫相关的配置文件
    * spiders: 爬虫目录, 如创建爬虫文件,编写爬虫内容

### 创建爬虫模版及运行爬虫:
* 创建基础爬虫模版: `scrapy genspider [-t basic] spidername spiderdomain`
* 运行爬虫文件:
    * 第一种: 终端命令行执行 `scrapy crawl spidername [--nolog]`
    * 第二种: 在项目根目录创建运行文件, 如 run.py
        ```python3
          from scrapy import cmdline
          # cmdline.execute("scrapy crawl spidername [--nolog]".split())
          cmdline.execute(["scrapy", "crawl", "spidername", "[--nolog]")
        ```
* 创建自动爬虫模版: `scrapy genspider -t crawl spidername spiderdomain`    
    ```python3
    # 注: 自动爬虫模版比基础爬虫模版多个rules的url地址规则自动提取器
    rules = (
        # 定义URL链接匹配规则(正则表达式)
        Rule(LinkExtractor(allow=r'Items/'), callback='parse_item', follow=True),
        # 定义URL链接匹配规则(XPath表达式)
        # Rule(LinkExtractor(restrict_xpaths='//div[@class="bookname"]//a[4]'), callback='parse_item', follow=True),
    )
    # 注: extract_links()为LinkExtractor,用于定义需要提取的URL链接
    ## Rule()的参数详解:
    # LinkExtractor() ---> 定义URL链接自动提取的规则
    # callback ---> 根据提取的URL链接,指定执行哪个回调函数进行数据解析,注: CrawlSpaider使用了parse作为回调函数,因此不要覆盖parse作为回调函数自己的回调函数
    # follow ---> 默认值为True,表示是否跟进继续提取URL链接,当callback为None时,默认值为True
    # process_links ---> 主要用来过滤由extract_links获取到的URL链接
    # process_request ---> 主要用来过滤在rule中提取到request
    # cb_kwargs ---> 传递给回调函数的参数字典
    
    
    ## LinkExtractor()的参数详解: URL链接提取器(根据我们编写的规则自动获取要爬取的URL链接)
    # 作用: 每个LinkExtractor有唯一的公共方法extract_links(response),它接受一个Response对象,并返回一个scrapy.link.Link对象
    # allow=() ---> 允许的url，所有满足这个正则表达式的url都会被提取出来 　
    # deny=() ---> 禁止的url,所有满足这个正则表达式的url都不会被提取出来
    # allowed_domains=() ---> 允许的域名,只有在这个里面指定的域名的url才会被提取
    # deny_domains=() ---> 禁止的域名,所有在这个里面指定的域名的url都不会被提取
    # restrict_xpaths=() ---> 使用xpath表达式提取，和allow共同作用过滤链接
    # restrict_css=()---> 使用css选择器提取,和allow共同作用过滤链接
    
    # tags=('a','area') ---> 接收一个标签(字符串)或一个标签列表,提取指定标签内的链接
    # attrs=('href',) ---> 默认提取tags里的href属性，也就是url链接
    # unique=True ---> 默认值为True,是否应对提取的链接应用重复过滤
    # strip=True ---> 默认值为True,是把地址前后多余的空格删除
    # process_value=None ---> 默认值为None,作用比较强大了,他接受一个函数,可以立即对提取到的地址做加工,优先级要大于allow 
    ```    

### Scrapy的数据提取:
* xpath(): 返回选择器列表,由指定XPath表达式参数选择的节点    
* css(): 返回选择器列表,由指定CSS表达式参数选择的节点 
* re(): 返回unicode字符串列表,当正则表达式被赋予作为参数时提取
* extract(): 返回一个unicode字符串以及所选数据
* extract_first(): 返回第一个unicode字符串以及所选数据

* XPath(特殊)表达式:
    * obj.xpath("string(.)"): 表示获取当前标签下的所有文本内容
    * obj.xpath("string(表达式)"): 表示获取当前标签下的所有文本内容
    * ''.join(obj.xpath("表达式").extract()): 将序列中的元素以指定的字符连接成一个新的字符串

### Scrapy的数据处理: 
* 第一种生成文件格式保存数据: 如 JSON CSV XML
    * return返回提取数据: 如 return xxx
    * 终端命令行执行命令: `scrapy crawl spidername -o xxx.json[xxx.csc, xxx.xml]`
* 第二种使用pipeline保存数据:
    * 使用pipeline文件管道保存数据:
        * 第一步: 在pipelines.py文件中编写爬虫对应的pipeline管道类,如下所示:
            ```python3
            class XxxPipeline(object):
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
                    # item数据类型跟爬虫文件yield推送过来的数据类型一致
                    return item  # 如果开启了其他pipeline类,爬虫数据也会被其他的pipeline类所接受
                    # raise DropItem()  # 抛出异常DropItem表示终止，否则继续交给后续的pipeline处理
                
                def close_spider(self,spider):
                    """关闭爬虫时执行,只执行一次,可省略"""
                    pass
            ```
        * 第二步: 在settings.py文件中开启定义的pipeline类管道
            ```python3
            # 注: 在此为spider爬虫文件开启pipeline,数值越小,优先级越高(同时数据也会存到其他的pipeline中)
            ITEM_PIPELINES = {
               'ScrapyCrawler.pipelines.XxxPipeline': 300,
            }
            ```
    * 注: 爬虫文件中,使用`yeild`只能推送 `字典类型`和`item对象类型` 数据到pipeline
    * 注: 爬虫文件中,使用`return`只能一次性返回 `所有item对象类型` 数据到pipeline
    * 注: 爬虫文件中可以自己单独使用的pipeline,这样数据就不会推送到其他的pipline中
        ```python3
        # 第一种: 直接在爬虫文件类中配置自己的pipeline管道
        custom_settings = {
          "ITEM_PIPELINES": {
              'ScrapyCrawler.pipelines.XxxPipeline': 300,
          }
        }
        
        # 第二种: 在pipeline管道中使用判断爬虫名字,只处理某个爬虫推送过来的数据,如 spider.name
        class PaChongPipeline(object):
            def process_item(self, item, spider):
                if spider.name == "爬虫名字1":
                    print("处理spider1的数据")
                elif spider.name == "爬虫名字2":
                    print("处理spider2的数据")
                else:
                    print("处理其他spiser的数据")      
                # return item
        
        第三种: 在pipeline管道中抛出异常DropItem,就不会把数据传递给后续的pipeline
        from scrapy.exceptions import DropItem
        raise DropItem
        # return item
        ```

### Scrapy的日志信息:
```python3 settings.py
# 日志的级别(从高到低): CRITICAL(严重错误) ERROR(一般错误) WARNING(警告) INFO(一般信息) DEBUG(调试信息)[默认级别]
# LOG_ENABLED = True  # 默认,日志信息的开关状态,设置为False为关闭状态
# LOG_LEVEL = 'DEBUG'  # 默认,日志信息的级别
# LOG_ENCODING = "utf-8"  # 默认,日志信息的编码格式
# LOG_FORMAT = '%(asctime)s [%(name)s] %(levelname)s: %(message)s'  # 默认,日志信息的数据格式
# LOG_DATEFORMAT = '%Y-%m-%d %H:%M:%S'  # 默认,日志信息的日期时间格式
# LOG_STDOUT = 'False'  # 默认,如果设置为True,进程所有的标准输出(及错误)将会被重定向到log中
# LOG_FILE = None  # 默认,日志信息的输出文件名,如果设置为None,则使用标准错误输出(standard error)

# 日志信息文件的目录结构
# import datetime
# CURRENT_TIME = datetime.datetime.now()  # 获取当前时间current_time
# LOG_FILE_PATH = 'logs/scarpy_{}_{}_{}.log'.format(CURRENT_TIME.year,CURRENT_TIME.month,CURRENT_TIME.day)
# LOG_FILE = LOG_FILE_PATH  # 日志信息的存储文件位置,设置后终端不会显示日志信息
```

### Scrapy的Request对象与Response对象
```python3
## Request: 用于发送请求,参数详解如下
# 注: def __init__(self, url, callback=None, method='GET', headers=None, body=None,
                 cookies=None, meta=None, encoding='utf-8', priority=0,
                 dont_filter=False, errback=None, flags=None):
# url: request对象发送请求的url地址
# callback: 在发送请求后,返回响应后执行的回调函数
# method: 默认为GET请求方式,可以设置为POST,PUT,且保证大写
# meta: 比较常用,属性的初始值(字典类型),用于在不同的请求之间传递数据使用
# cookies: 两种方式(dict和list)
# dot_filter: 默认为Flalse,是对URl地址进行过滤去重,设置为True(不去重)
# headers: 请求头信息
# boday: 请求体内容
# encoding: 默认为utf-8编码格式,使用默认就可以了
# errback: 在请求发生错误的时候执行的回调函数

## Response: 由Scrapy自动构建,请求的响应内容,主要用于数据提取,属性详解如下
# xpath(): 数据提取选择器
# css(): 数据提取选择器
# text: 此次请求的响应内容,字符串数据
# body: 此次请求的响应内容,字节数据
# meta: 从其他请求传递过来的meta属性(字典类型),可以用来保持多个请求之间的数据传递
# request: 属性的初始值Response.request,代表Request生成的此次响应
# headers: 此次响应的请求头,dict值可以是字符串(对于单值标头)或列表(对于多值标头)
# url: 此次响应的url地址
# status: 此次响应的状态码,默认200
# encoding: 返回当前字符串编码和解码的格式

# 注: 1.如果请求需要发送数据的时,使用POST请求,并且使用Resquest子类FormRequest类来实现(如,请求表单)
# FormRequest接受参数(formdata)的数据类型为字典(dict)类型
# 注: 2.如果爬虫在开始时就发送POST请求,需要在爬虫类中重写`start_request(self)`方法,并且不在调用start_url列表中的url地址
```

### pipeline下载文件和图片: FilesPipeline, ImagesPipeline
```python3
## FilesPipeline: 自动下载文件: from scrapy.pipelines.files import FilesPipeline
# 1. 定义一个Item,在Item中定义两个字段属性file_urls和files,file_urls用来存储下载文件的url地址,是一个列表
# 2. 当文件下载完成后,会把文件的相关信息存储到Item的files属性中,如:下载路径,下载url和文件的校验码等
# 3. 在settings.py文件中添加属性设置: FILES_STORE ,用来设置文件下载下来的存储位置(本地)
# 4. 在settings.py文件中开启pipeline,如,ITEM_PIPELINES属性添加: 'scrapy.pipelines.files.FilesPipeline': 1

## ImagesPipeline: 自动下载图片: from scrapy.pipelines.images import ImagesPipeline
# 1. 定义一个Item,在Item中定义两个字段属性image_urls和images,image_urls用来存储下载图片的url地址,是一个列表
# 2. 当图片下载完成后,会把图片的相关信息存储到Item的images属性中,如:下载路径,下载url和图片的校验码等
# 3. 在settings.py文件中添加属性设置: IMAGES_STORE ,用来设置图片下载下来的存储位置(本地)
# 4. 在settings.py文件中开启pipeline,如,ITEM_PIPELINES属性添加: 'scrapy.pipelines.images.ImagesPipeline': 1 

### 实现自定义分类图片下载,需要在pipelines.py文件中自定义pipeline类继承ImagesPipeline,并重写如下两个方法
def get_media_requests(self, item, info):
    for image_url in item["image_urls"]:
        yield scrapy.Request(image_url)  # 对各个图片URL返回一个Request
# 注:get_media_requests()默认返回None,表示没有图片可下载

def file_path(self, request, response=None, info=None):
    "" 给下载的图片自定义图片名称 """
    return image_name

def item_completed(self, results, item, info):
    pass
```

### 中间件分类: Downloader Middlewares 与 Spider Middlewares
```python3
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

### 下载中间件示例: 动态User-Agent 
* 第一种固定方式: settings.py  
`USER_AGENT = 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36'`
* 第二种随机方式: 使用fake_useragent模块,编写下载中间件类
    ```python3
    # 1.注销settings.py文件中的USER_AGENT属性
    
    # 2.安装fake_useragent模块: pip install fake_useragent
    
    # 3.另创建一个文件[useragentmiddleware]并编写[UserAgentDownloaderMiddleware]类,或者直接在文件[middlewares]中编写[UserAgentDownloaderMiddleware]类
    from fake_useragent import UserAgent
    class UserAgentDownloaderMiddleware(object):
        def process_request(self, request, spider):
            # 设置随机的获取User-Agent
            # request.headers.setdefault(b'User-Agent', UserAgent().chrome)  # 随机chrome浏览器任意版本
            request.headers.setdefault(b'User-Agent', UserAgent().random)  # 随机任意浏览器任意版本
    
    # 4.开启settings.py文件中的DOWNLOADER_MIDDLEWARES中间件属性
    DOWNLOADER_MIDDLEWARES = {
        # 'SpiderExample.middlewares.SpiderexampleDownloaderMiddleware': 543,
        # 数值越小表示优先级越高,默认543
        'SpiderExample.middlewares.UserAgentDownloaderMiddleware': 343,
    }
    ```

* 第三种随机方式: 提供多个User-Agen列表,编写下载中间类
    ```python3
    # 1.注销settings.py文件中的USER_AGENT属性定义一个USER_AGENTS列表属性,里面存储一些User-Agent值,如
    USER_AGENTS = [
       "Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:61.0) Gecko/20100101 Firefox/61.0",
       "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36",
       "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.80 Safari/537.36"
    ]
    
    # 2.另创建一个文件[useragentmiddleware]并编写[UserAgentDownloaderMiddleware]类,或者直接在文件[middlewares]中编写[UserAgentDownloaderMiddleware]类
    from random import choice
    from SpiderExample.settings import USER_AGENTS
    class UserAgentDownloaderMiddleware(object):
        def process_request(self, request, spider):
            # 设置随机的获取User-Agent
            request.headers.setdefault(b'User-Agent', choice(USER_AGENTS))
    
    # 3.开启settings.py文件中的DOWNLOADER_MIDDLEWARES中间件属性
    DOWNLOADER_MIDDLEWARES = {
        # 'SpiderExample.middlewares.SpiderexampleDownloaderMiddleware': 543,
        # 数值越小表示优先级越高,默认543
        'SpiderExample.middlewares.UserAgentDownloaderMiddleware': 343,
    }
    ```
### 下载中间件示例: 动态代理IP
```python3
# 1.另创建一个文件[proxymiddleware]并编写[ProxyDownloaderMiddleware]类,或者直接在文件[middlewares]中编写[ProxyDownloaderMiddleware]类
class ProxyDownloaderMiddleware(object):
    def process_request(self, request, spider):
        # 设置动态代理IP
        # request.meta['proxy'] = "http://ip:port"
        # request.meta['proxy'] = "http://username:password@ip:port"
        request.meta['proxy'] = "http://61.153.251.150:22222"

# 2.开启settings.py文件中的DOWNLOADER_MIDDLEWARES中间件属性
DOWNLOADER_MIDDLEWARES = {
    # 'SpiderExample.middlewares.SpiderexampleDownloaderMiddleware': 543,
    # 数值越小表示优先级越高,默认543
    'SpiderExample.middlewares.ProxyDownloaderMiddleware': 243,
}
``` 

### Scrapy的登录方式:
* 第一种方式: 使用账号与密码发送POST请求
    ```python3
    # 1.注销爬虫类中的start_urls属性
    # 2.在爬虫类中重写start_requests方法,使用FormRequest发送POST请求
    def start_requests(self):
        login_url = "http://www.renren.com/PLogin.do"
        login_data = {
            "email": "1810376****",
            "password": "ch**123***",
        }
        yield scrapy.FormRequest(login_url, formdata=login_data, callback=self.parse)
    
    # 3.在爬虫类中重新发送爬虫请求
    def parse(self, response):
        # 登录成功后再次发送请求
        info_url = "http://www.renren.com/893394172/profile"
        yield scrapy.Request(info_url, callback=self.parse_info)
    
    # 4.在爬虫类中编写数据提取方法
    def parse_info(self,response):
        # 提取所需要的数据
        author = response.xpath('//h1[@class="avatar_title no_auth"]/text()').extract_first().strip()
        print(author)
    ```
* 第二种方式: 携带cookie的方式(cookie为字典类型和列表类型)
    ```python3
    # 1.在浏览器上手动登录网站,找到cookie值
    # 2.在爬虫类中重写start_requests方法,使用Request携带cookie发送GET请求
    def start_requests(self):
        url = "http://www.renren.com/893394172/profile"
        cookie_str = "anonymid=k456ongu-692yve; depovince=GW; _r01_=1; "
        cookie_dict = {}
        for cookievalue in cookie_str.split("; "):  # 根据"; "进行分割cookie字符串组成一个列表
            key, value = cookievalue.split("=")  # 根据"="进行分割每个cookie的键与值
            cookie_dict[key] = value
        yield scrapy.Request(url, cookies=cookie_dict, callback=self.parse)
    
    # 3.在回调函数中进行解析提取数据
    def parse(self, response):
        # 提取所需要的数据
        author = response.xpath('//h1[@class="avatar_title no_auth"]/text()').extract_first().strip()
        print(author)
    ```
* 第三种方式: 使用账号与密码加上验证码发送POST请求,略...可参考爬虫`cd_11ganjilogin`

### Scrapy中调式测试使用:
* [虚拟环境下]进入项目根目录
* 终端命令行执行: `scrapy shell URL链接` 发送请求
* 然后就可以进行调试(存在response对象)
* 注: PyCharm中调式工具: `Tools ---> HTTP Client ---> test RESTful Web Service` 发送GET,POST,PUT...请求


### Linux-CentOS7.2使用Docker虚拟容器:
* 搜索Splash镜像: `docker search splash`
* 下载Splash镜像: `docker pull scrapinghub/splash`
* 删除Splash镜像: `docker rmi -f scrapinghub/splash`
* 启动Splash容器(终端交互): `docker run -it -p 8050:8050 scrapinghub/splash`
* 启动Splash容器(守护进程): `docker run -d -p 8050:8050 scrapinghub/splash`
* 访问Splash服务: `虚拟机IP:端口号` --- `http://192.168.59.130:8050`
* 退出Splash容器: 容器停止退出(exit) 或 容器不停止退出(ctrl + p + q)
* 停止Splash容器: 停止`docker stop 容器ID/容器名称` 或 `强制停止docker kill 容器ID/容器名称`
* 删除一个或多个已停止的容器: `docker rm 7371c90b7c8d` 或 `docker rm -f $(docker ps -aq)`
* 查看正在运行或历史运行过的容器: `docker ps -a`
* Splash对象属性与方法: 
    ```python3
    function main(splash, args)
      assert(splash:go(args.url))  # 请求URl链接
      assert(splash:wait(0.5))  # 等待加载时间
      return {
        html = splash:html(),  # 获取响应的源代码
        png = splash:png(),  # 获取PNG格式的网页截图
        har = splash:har(),  # 获取页面加载过程HAR信息
      }
    end
    # 注: main()方法的第一个参数splash,类似于Selenium的WebDriver对象
    
    # Splash对象属性:
    splash.js_enabled=true  设置启用或者禁用页面中嵌入的JavaScript代码的执行(默认为true,启用JavaScript执行)
    splash.resource_timeout=0  设置网络请求的默认超时时间,以秒为单位,如设置为0或nil则表示无超时
    splash.images_enabled=true  设置启用或禁用图片加载(默认为true,启动图片加载)
    splashp.lugins_enabled=false  设置启用或禁用浏览器插件(默认为false,禁用浏览器插件)
    splashs.croll_position={x=100, y=100}  控制页面上下或左右滚动
    
    # Splash对象方法:
    ok, reason = splash:go{url}  该方法用于请求某个URL链接
    # 注:如果ok为空则代表网页请求错误,reason变量中会包含错误信息
    go{url, baseurl=nil, headers=nil, http_method="GET", body=nil, formdata=nil}方法参数:
        url: 请求的url链接
        baseurl: 可选参数,默认为空,表示资源加载的相对路径
        headers: 可选参数,默认为空,表示请求头信息
        http_method: 可选参数,默认为GET,同时支持POST
        body: 可选参数,默认为空,发送POST请求时的表单数据,使用的Content-type为application/json
        formdata: 可选参数,默认为空,发送发送POST请求时的表单数据,使用的Content-type为application/x-www-form-urlencoded
    
    ok, reason = splash:wait{time, cancel_on_redirect=false, cancel_on_error=true}  该方法用于控制页面的等待时间
    wait{time, cancel_on_redirect=false, cancel_on_error=true}方法参数:
        time: 等待时间,单位为秒
        cancel_on_redirect: 可选参数,默认为false,表示如果发生重定向就停止等待,并返回重定向结果
        cancel_on_error: 可选参数,默认为false,表示如果发生加载错误,就停止等待
    
    splash:jsfunc() 该方法可以直接调用JavaScript定义的函数,但所调用的函数需要用双中括号包围
    splash.evaljs() 该方法用于在页面上下文中执行JavaScript代码,并返回最后一个语句的结果
    splash:runjs() 该方法用于在页面上下文中执行JavaScript代码,如同evaljs()差不多,但更偏向于执行某系动作或声明函数
    ```

### Splash与Scrapy结合使用:
```python3
# 使用之前需要安装模块: pip install scrapy-splash
# settings.py文件中配置Splash服务地址: 
SPLASH_URL = "http://192.168.59.130:8050/"
# settings.py文件中配置下载中间件属性:DOWNLOADER_MIDDLEWARES,如下所示
DOWNLOADER_MIDDLEWARES = {
    'scrapy_splash.SplashCookiesMiddleware': 723,
    'scrapy_splash.SplashMiddleware': 725,
    'scrapy.downloadermiddlewares.httpcompression.HttpCompressionMiddleware': 810,  # 不配置查不到信息
}
# settings.py文件中配置爬虫中间件属性:SPIDER_MIDDLEWARES,如下所示
SPIDER_MIDDLEWARES = {
   'scrapy_splash.SplashDeduplicateArgsMiddleware': 100,
}
# settings.py文件中配置消息队列所使用的过滤类:
DUPEFILTER_CLASS = "scrapy_splash.SplashAwareDupeFilter"
# settings.py文件中配置消息队列所使用的类:
HTTPCACHE_STORAGE = 'scrapy_splash.SplashAwareFSCacheStorage'
```

### Selenium与Scrapy结合使用:
```python3
# 另创建一个文件[seleniummiddleware]并编写[SeleniumDownloaderMiddleware]类,或者直接在文件[middlewares]中编写[SeleniumDownloaderMiddleware]类
class SeleniumDownloaderMiddleware(object):
    def process_request(self, request, spider):
        url = request.url  # 请求要访问的url链接
        spider.browser.get(url)
        html = spider.browser.page_source
        # print(html)
        # HtmlResponse对象,它是Response的子类,返回之后便顺次调用每个Downloader Middleware的process_response()方法
        # 而在process_response()中我们没有对其做特殊处理,它会被发送给Spider,传给Request的回调函数进行解析
        return HtmlResponse(url, body=html, request=request, encoding="utf-8")
# 爬虫文件类中使用信号监听以便爬虫结束后关闭浏览器:
from scrapy import signals
from selenium import webdriver
class Cd14seleniumScrapySpider(scrapy.Spider):
    @classmethod
    def from_crawler(cls, crawler, *args, **kwargs):
        spider = super(Cd14seleniumScrapySpider, cls).from_crawler(crawler, *args, **kwargs)
        spider.browser = webdriver.Firefox(executable_path="E:\Installation_Tools\Driver\FirefoxDriver\geckodriver.exe")
        crawler.signals.connect(spider.spider_closed, signal=signals.spider_closed)
        return spider

    def spider_closed(self, spider):
        print("爬虫结束了...关闭浏览器")
        spider.browser.quit()  # 关闭浏览器
# settings.py文件中开启编写的Selenium中间件:
DOWNLOADER_MIDDLEWARES = {
   # 'SpiderExample.middlewares.SpiderexampleDownloaderMiddleware': 543,
   # 数值越小表示优先级越高,默认543
   'SpiderExample.middlewares.SeleniumDownloaderMiddleware': 343,  # Selenium+Scrapy结合使用,定义中间件
}
```

### Scrapy-Redis分布式爬虫组件:
> Scrapy是爬虫框架,但是不支持分布式,scrapy-redis是为了实现Scrapy分布式爬取,而提供以redis为基础的组件  
* scrapy-redis组件的安装: `pip install scrapy-redis`
* 如何将一个Scrapy项目变成一个scrapy-redis分布式爬虫项目: 如下所示
* 爬虫类的继承类的修改
    ```python3
    基础类: scrapy.Spider 改成 scrapy_redis.spiders.RedisSpider
    自动类: scrapy.CrawlSpider 改成 scrapy_redis.spiders.RedisCrawlSpider
    ```
* 爬虫类的属性删除与添加
    ```python3
    # start_urls = []  # 注销或删除
    redis_key = "xxx:start_urls"  # 添加属性值,代替初始爬取的URL
    ```
* settings.py文件中配置如下信息
    * 必选-指定redis数据库的连接参数
        ```python3
        # REDIS_URL = 'redis://127.0.0.1:6379'  
        REDIS_HOST = '127.0.0.1'
        REDIS_PORT = 6379
        ```
    * 必选-使用了scrapy-redis的调度器,在redis数据库里分配请求
        ```python3
        SCHEDULER = "scrapy_redis.scheduler.Scheduler"
        ```
    * 必选-使用了scrapy_redis 的去重组件,在redis数据库里做去重
        ```python3
        DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
        ```
    * 必选-使用redis开启pipeline
        ```python3
        ITEM_PIPELINES = {
            'scrapy_redis.pipelines.RedisPipeline' : 300
        }
        ```
    * `DUPEFILTER_DEBUG =True`  # 设置为True,记录所有重复的请求,默认情况下RFPDupeFilter只记录第一个重复请求
    * `SCHEDULER_PERSIST = True`  # 设置为True,爬虫退出时,不清理redis中的数据,暂停后可以继续执行
    * 指定排序爬取地址时使用的队列
        ```python3
        SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderPriorityQueue'  # 默认的,按优先级排序
        SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderQueue'  # 可选的,按先进先出排序（FIFO）
        SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.SpiderStack'  # 可选的,按后进先出排序（LIFO）
        ```
* 启动配置好的分布式爬虫项目:
    ```python3
    # 1.在爬虫服务器上,进入到爬虫文件所在目录,然后执行: scrapy runspider [爬虫文件].py
    # 2.在redis服务器上,推入一个开始的url地址: redis-cli lpush [redis-key] [start_urls链接]
    
    ```
* scrapy-redis键名介绍: key - value
    * "项目名:start_urls" ---> list类型,用于获取spider启动时爬取的第一个url地址
    * "项目名:dupefilter" ---> set类型,用于爬虫访问的url去重,内容是url地址的hash值字符串
    * "项目名:items" ---> list类型,保存爬虫获取到的数据item,内容是json字符串
    * "项目名:requests" ---> zset类型,用于调度器处理requests,内容是request对象字符串

### 分布式爬虫: 从Redis中取出数据导入到MongoDB
```python3
import redis
import pymongo
import json
def main()"
    # redis连接
    redis_client = redis.Redis(host="127.0.0.1", port=6379, db=0)
    # mongodb连接
    mongo_client = pymongo.MongoClient("localhost",27017)
    # 获取数据库
    db = mongo_client.dbname
    # 获取集合
    collection = db.jehename
    while True:
        # 从redis中取出数据
        scource, data = redis_cilent.bloop(["cd_17scrapy_redis:items"])
        # 把Json数据转换为字典类型数据
        item = json.loads(data)
        # 插入数据到mongodb中
        collection.insert(item)
```


