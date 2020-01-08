### Django项目settings.py配置文件:
```
# 查看Django全局的默认配置信息: django/conf/global_settings.py

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
TEMPLATES = [
   # 如果配置了目录,则优先按照写好的路径去找模板文件,如果找不到才会到app应用下的templates目录中查找模版文件
   'DIRS': [os.path.join(BASE_DIR, 'templates')],
   # 'DIRS': [ ],  # 如果未配置目录,则会自动的到每个应用中查找templates的目录来作为模板文件的存放目录
   'APP_DIRS': True,  # 默认True表示搜索应用中的 templates 目录
   # 如果不想每次在模版文件中加载静态文件时都使用{% load static %},那么就把static标签变成Django内置标签
   'builtins': ['django.templatetags.static'],
] 

# 静态文件的存储路径配置信息:
STATIC_URL = '/static/'
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
LANGUAGE_CODE = 'zh-Hans'       # 设置中文,默认为en-us
TIME_ZONE = 'Asia/Shanghai'     # 设置时区,默认为UTC
# USE_I18N = True                 # 是否启动自动翻译,默认为True
# USE_L10N = True                 # 设置以本地格式化显示数字和时间,默认为False
USE_TZ = False                  # 设置使用本地时间,默认为True

# Pyhon脚本调用Django环境:
# 1.加载Django项目的配置信息
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
# 2.导入Django包,并启动Django项目
import django
django.setup()

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




