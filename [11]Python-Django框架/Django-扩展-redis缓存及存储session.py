# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-06 16:27

# django-redis
# 安装: pip install django-redis

### Django默认情况下session是存储在数据库中的,但是当用session保存用户的状态时,用户频繁的访问服务器,会增大数据库的压力,也会降低用户访问的速度
# 解决方式: 将session会话存储到redis中
# Django项目session会话存储到redis中的两种配置方式: 如下


### 第一种配置: 直接将session会话的存储位置配置到redis中
## 1.安装: pip install django-redis-sessions==0.5.6
## 2.在Django项目的settings文件中配置redis作为存储session会话位置
# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_HOST = 'localhost'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 2
# SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'session'


##############################################################################################

### 第二种配置: 将Django项目的缓存设置为Redis,然后将session会话的存储位置设置到Django项目的缓存中
## 1.安装: pip install redis 和 pip install django-redis
## 2.配置Redis数据库作为Django项目的缓存:
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/2",  # 设置redis服务的IP地址与端口号以及哪个数据库
        "LOCATION": "redis://192.168.208.128:6379/2",  # 设置redis服务的IP地址与端口号以及哪个数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "password",  # redis密码,如果redis设置了密码需要加上这一项
            # "SOCKET_CONNECT_TIMEOUT": 5,  # 配置socket建立连接的超时时间(秒)
            # "SOCKET_TIMEOUT": 5,  # 配置连接建立后的读写操作超时时间(秒)
            # "CONNECTION_POOL_KWARGS": {"max_connections": 100},  # 配置连接池的最大连接数量
            # "CONNECTION_POOL_CLASS": "myproj.mypool.MyOwnPool",  # 自己的连接池子类
        }
    }
}


## 3.配置Session的存储方式(引擎): 数据库(默认), 文件, 缓存, 缓存+数据库, 加密cookie ...
# 1.Django默认的session会话存储方式,需要添加django.contrib.sessions到的INSTALLED_APPS中
# SESSION_ENGINE = "django.contrib.sessions.backends.db"

# 2.使用文件方式存储session会话:
SESSION_ENGINE = 'django.contrib.sessions.backends.file'
SESSION_FILE_PATH = None  # 缓存文件存储路径,如果为None,则使用tempfile模块获取一个临时地址tempfile.gettempdir()

# 3.使用缓存方式存储sesison会话: 只存在本地内在中,如果丢失则不能找回,比数据库的方式读写更快
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名(默认内存缓存,也可以是memcache),此处别名依赖缓存的设置

# 4.使用缓存和数据库的方式同时存储session会话: 优先从本地缓存中获取,如果没有则从数据库中获取
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'
SESSION_CACHE_ALIAS = "default"   # 使用的缓存别名(默认内存缓存,也可以是memcache),此处别名依赖缓存的设置

# 5.使用cokie加密方式存储session会话:
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'


## session的其他公用设置项:
# SESSION_COOKIE_NAME ＝ "sessionid"        # Session的cookie保存在浏览器上时的key,即: sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"                # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None              # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False             # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True            # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600              # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False        # 是否每次请求都保存Session，默认修改之后才保存（默认）

