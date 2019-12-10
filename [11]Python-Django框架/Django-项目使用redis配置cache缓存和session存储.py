# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-06 16:27

# django-redis
# 安装: pip install django-redis

'''
默认情况下session是存储在数据库中的，但是当用session保存用户的状态时，用户频繁的访问服务器，
会增大数据库的压力，也会降低用户访问的速度。为了解决这个问题将session存储到redis中。
'''

### Django框架项目中session存储到redis中的配置(两种方式):
## 第一种配置:直接将session存储的地方配置到redis中
# 1.安装: pip install django-redis-sessions==0.5.6
# 2.在django项目的settings文件中配置redis作为存储session的位置
# SESSION_ENGINE = 'redis_sessions.session'
# SESSION_REDIS_HOST = 'localhost'
# SESSION_REDIS_PORT = 6379
# SESSION_REDIS_DB = 2
# SESSION_REDIS_PASSWORD = ''
# SESSION_REDIS_PREFIX = 'session'

## 第二种配置:将django项目的缓存设置为redis,然后将session的存储地方设置到django项目的缓存中
# 1.安装: pip install django-redis
# 2.配置redis作为django项目的缓存设置:
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        # "LOCATION": "redis://127.0.0.1:6379/2",  # 设置redis服务的IP地址与端口号以及哪个数据库
        "LOCATION": "redis://192.168.208.128:6379/2",  # 设置redis服务的IP地址与端口号以及哪个数据库
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient",
            # "PASSWORD": "password",  # redis密码,如果redis设置了密码需要加上这一项
        }
    }
}
# 3.配置session的存储位置到redis缓存中:
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
# SESSION_ENGINE = "django.contrib.sessions.backends.db"
SESSION_CACHE_ALIAS = "default"


