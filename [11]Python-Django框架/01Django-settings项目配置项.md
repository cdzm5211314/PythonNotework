### Django项目settings.py配置文件:
```
# 注册应用APP配置属性:
INSTALLED_APPS = []

# 如果创建APP总目录应用: 需要设置总应用包的搜索环境路径
import sys
sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

# 数据库连接配置属性: 如 MySQL
# 需要安装: pip install pymysql
# 注:使用MySQL数据库时,需要在项目目录下的__init__py文件中添加以下内容:
import pymysql
pymysql.install_as_MySQLdb()
DATABASES = {
     'default': {
         'ENGINE': 'django.db.backends.mysql',  # MySQL数据库连接的驱动程序
         'NAME': 'dailyfresh',                  # MySQL数据库名称
         'USER': 'root',                        # MySQL数据库用户名
         'PASSWORD': 'root',                    # MySQL数据库密码
         'HOST': 'localhost',                   # MySQL数据库IP地址
         'PORT': '3306',                        # MySQL数据库PORT端口号
     }
}

# 模版文件的存储路径配置属性:
TEMPLATES = [] 

# 静态文件的存储路径配置信息:
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static')
]

# 上传文件的存储路径配置:
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空
# 上传文件的路由配置信息: 根路由
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# Admin后台管理中文设置:
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

# Pyhon脚本调用Django环境:
# 1.加载Django项目的配置信息
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
# 2.导入Django包,并启动Django项目
import django
django.setup()

# Django中的Session配置信息:
# 1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'              # 引擎（默认）
# 2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'           # 引擎
SESSION_CACHE_ALIAS = 'default'                                     # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
# 3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'            # 引擎
SESSION_FILE_PATH = None                                            # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
# 4. 缓存 + 数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'       # 引擎
# 5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎
# 其他公用设置项：
# SESSION_COOKIE_NAME ＝ "sessionid"         # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"                 # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None              # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False             # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True            # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600              # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False   # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False        # 是否每次请求都保存Session，默认修改之后才保存（默认）

# 终端打印SQL语句的配置信息:
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

## 补充: APPEND_SLASH = True  默认为True,其作用就是自动在URl地址结尾加'/'
```




