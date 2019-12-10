# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 14:42

### 在Python脚本中调用Django环境:
if __name__ == '__main__':
    # 1. 加载Django项目的配置信息
    import os
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
    # 2.导入Django,并启动Django项目
    import django
    django.setup()

    # 3. 数据操作
    from app01 import models
    books = models.Book.objects.all()
    print(books)


### 配置数据库:
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 指定要连接的数据库的驱动程序
        "NAME": "你的数据库名称",              # 指定要连接到的数据库的名称,需要手动创建:
        "USER": "数据库用户名",                # 指定登录到数据库管理系统的用户名
        "PASSWORD": "数据库密码",              # 指定登录到数据库管理系统的密码
        "HOST": "数据库IP",                    # 指定要连接到的主机地址
        "POST": 3306                           # 指定端口号
    }
}
# 注:使用MySQL数据库时,需要在项目目录下的__init__py文件中添加以下内容:
# import pymysql
# pymysql.install_as_MySQLdb()


### 设置静态文件的存储路径:
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR,'static'),
# )

### 用户上传的文件为: media文件
# settings.py:
import os
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join('BASE_DIR','media')
# 路由url配置:
# from django.views.static import serve
# urlpatterns = [
#     # media相关的路由设置
#     url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
# ]


### Django终端打印SQL语句:
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console':{
            'level':'DEBUG',
            'class':'logging.StreamHandler',
        },
    },
    'loggers': {
        'django.db.backends': {
            'handlers': ['console'],
            'propagate': True,
            'level':'DEBUG',
        },
    }
}


### Django中的Session配置信息:
# 1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'     # 引擎（默认）
# 2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'                            # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
# 3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'   # 引擎
SESSION_FILE_PATH = None                                   # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
# 4. 缓存 + 数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # 引擎
# 5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎
# 其他公用设置项：
# SESSION_COOKIE_NAME ＝ "sessionid"                       # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"                               # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None                             # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False                            # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True                           # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600                             # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False                  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False                       # 是否每次请求都保存Session，默认修改之后才保存（默认）


