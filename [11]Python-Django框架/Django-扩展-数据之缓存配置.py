# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2020-01-08 11:20

## 缓存是一类可以更快的读取数据的介质统称,也指其它可以加快数据读取的存储方式
## 由Django的生命周期知各级缓存的优先级: 中间件应用的全局缓存 > 视图函数缓存 > 模板渲染下的局部视图使用缓存

## Django settings 中 cache 默认为: 本地内存缓存
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'unique-snowflake',
    }
}
## 缓存其他参数说明:
# TIMEOUT: 缓存过期时间(默认300秒, None表示永不过期, 0表示立即过期)
# OPTIONS: 可选参数列表
#     MAX_ENTRIES: 最大缓存个数(默认300个)
#     CULL_FREQUENCY: 缓存到达最大个数之后,剔除缓存个数的比例
# KEY_PREFIX: 缓存key的前缀(默认为空)
# VERSION: 缓存key的版本(默认为1)
# KEY_FUNCTION:"func_name"  # 生成key的函数(默认函数会生成为:【前缀:版本:key】)


## Django其他的内建缓存配置方式:
'django.core.cache.backends.dummy.DummyCache'  # 开发调式
'django.core.cache.backends.db.DatabaseCache'  # 数据库
'django.core.cache.backends.filebased.FileBasedCache'  # 文件
'django.core.cache.backends.locmem.LocMemCache'  # 本地内存
'django.core.cache.backends.memcached.MemcachedCache' # python-memcached模块
'django.core.cache.backends.memcached.PyLibMCCache'  # pylibmc模块

## 还有使用Redis数据库作为Django项目缓存:
# pip install redis
# pip install django-redis
# 配置Redis缓存: 与内置的缓存配置基本一致
CACHES = {
    'default':{
        'BACKEND': 'django_redis.cache.RedisCache',  # 使用Redis数据库缓存引擎
        'LOCATION':'redis://127.0.0.1:6379/12',  # 配置Redis主机地址、端口号、数据库
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 指定连接Redis的客户端类
            # 'PASSWORD': 'mysecret',  # Redis数据库密码
            # "PICKLE_VERSION": -1  # django-redis使pickle来序列化对象
            # "SOCKET_CONNECT_TIMEOUT": 5,  # 配置socket建立连接的超时时间(秒)
            # "SOCKET_TIMEOUT": 5,  # 配置连接建立后的读写操作超时时间(秒)
            # "CONNECTION_POOL_KWARGS": {"max_connections": 100},  # 配置连接池的最大连接数量
            # "CONNECTION_POOL_CLASS": "myproj.mypool.MyOwnPool",  # 自己的连接池子类
        }
    }
}



###############################################################################################

### 在settings.py文件中配置缓存: 分为数据库缓存, 文件缓存, 本地内存缓存 Memcache缓存 等...
# 注: from django.core.cache import cache  # 指向settings中配置的CACHES的缓存对象(即默认的default)
# 注: from django.core.cache import caches # 指向settings中配置的CACHES的缓存对象(如果配置多个缓存)
# 获取缓存对象: cache_obj = caches['default']
## 使用Django内置的缓存API(底层): 导入from django.core.cache import cache
# 设置缓存: cache.set(key, value, timeout)  # key表示缓存的名称,value表示缓存的数据类型,timeout缓存过期时间
# 获取缓存: cache.get(key)  # 根据缓存的名称获取数据
# 删除缓存: cache.delete(key)  # 根据缓存的名称删除缓存

## 开发调试使用(实际内部不做任何操作)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache', # 引擎-开发调试
    }
}

## 数据库缓存:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',  # 引擎-使用数据库缓存
        'LOCATION': 'my_cache_table',  # 用于保存缓存数据的数据库表名字
    }
}
# 创建缓存表命令: python manage.py createcachetable

## 文件缓存:
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.filebased.FileBasedCache',  # 引擎-使用文件缓存
        'LOCATION': '/var/tmp/django_cache',  # Linux,缓存文件的存储目录
        # 'LOCATION': 'c:\foo\bar',  # Windows,缓存文件的存储目录
    }
}

## 本地内存缓存:(默认)
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 引擎-使用本地内存缓存
        'LOCATION': 'unique-snowflake'  # 如果你只有一个本地内存缓存,你可以忽略这个
    }
}

## Memcache缓存: python-memcached模块 + pylibmc模块
# 1.此缓存使用 python-memcached模块 连接memcache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.MemcachedCache',
        'LOCATION': '127.0.0.1:11211',   # 使用本机指定11211端口为Memcache缓存服务器
        'LOCATION': 'unix:/tmp/memcached.sock', # 指定局域网内的主机名加socket套接字为Memcache缓存服务器
        # 指定多台主机IP地址和Port端口为Memcache缓存服务器集群
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
            # 设置权重
            # ('172.19.26.240:11211',10),
            # ('172.19.26.242:11211',20),
        ]

    }
}

# 2.此缓存使用 pylibmc模块 连接memcache
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.memcached.PyLibMCCache',
        'LOCATION': '127.0.0.1:11211',  # 使用本机指定11211端口为Memcache缓存服务器
        'LOCATION': '/tmp/memcached.sock',  # 指定某个路径为缓存目录
        # 分布式缓存,在多台服务器上运行Memcached进程,程序会把多台服务器当作一个单独的缓存,而不会在每台服务器上复制缓存值
        'LOCATION': [
            '172.19.26.240:11211',
            '172.19.26.242:11211',
        ]
    }
}


##############################################################################################

### Django项目中如何使用Cache缓存:
## 全站缓存配置: settings ---> MIDDLEWARE(中间件,先UpdateMiddleware后FetchFormCacheMiddleware)
MIDDLEWARE = [
    # 服务端响应response时作用;查看是否有缓存,如果没有则写入缓存,如果有直接返回给客户端
    'django.middleware.cache.UpdateMiddleware',  # 即设置缓存,放在第一位
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # 客户端请求request时作用;查看是否有缓存,如果有不经过views直接返回,如果没有直接进入views视图执行函数获取缓存
    'django.middleware.cache.FetchFormCacheMiddleware',  # 即获取缓存,放在最后一位
]


## 在视图views中使用: 使用装饰器用于对视图函数的输出进行缓存
from django.views.decorators.cache import cache_page
# @cache_page(timeout = 60 * 15)  # timeout表示缓存的过期时间
@cache_page(60 * 15)  # 缓存的过期时间
def func(request):
    pass

## 在路由URL中使用:
from django.views.decorators.cache import cache_page
urlpatterns = [
    url(r'^foo/(\d+)/$', cache_page(60 * 15)(my_view)),
    url(r'^foo/(\d+)/$', cache_page(my_view, 60 * 15)),
]


## 在模板template中使用: 缓存时间(豪秒),给缓存的key值(取缓存的时候,需要根据key值取)
{% load cache %}
{% cache 500 'sunk' %}  # sunk: 缓存的key
    pass  # 缓存内容
{% endcache %}


###############################################################################################

### 缓存示例: 使用Redis数据库缓存
# 1.安装插件: pip install django-redis
# 2.settings.py文件: 配置信息
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',  # 使用本地内存缓存引擎
    },
    'redis': {
        'BACKEND': 'django_redis.cache.RedisCache',  # 使用Redis数据库缓存引擎
        'LOCATION': 'redis://127.0.0.1:6379/9',  # 配置Redis主机地址、端口号、数据库
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',  # 指定连接Redis的客户端类
        }
    }
}

# 3.views.py文件: 使用缓存
from django.views.decorators.cache import cache_page
from django.core.cache import caches
# 获取缓存对象: cache_obj = caches['defaule']
from django_redis import get_redis_connection
# 连接池中获取连接: conn = get_redis_connection("redis")


