# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-30 10:51

### 富文本编辑器配置:
## 1.安装: pip install django-tinymce
## 2.settings.py中配置(样式与高宽)
TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',  # 主题模式:高级
    'width': 600,         # 富文本宽度
    'height': 400,        # 富文本高度
}

## 3.在settings.py中配置app
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'apps',     # 配置apps总应用包, sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))
    'tinymce',  # 富文本编辑器
]

## 4.项目urls.py文件中配置路由
from django.conf.urls import url,include
from django.contrib import admin
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/',include('tinymce.urls')),  # 富文本编辑器
]

## 5.项目app应用的model模型中定义
from tinymce.models import HTMLField
class Blog(models.Model):
    '''论坛'''
    # 富文本类型:带有格式的文本
    content = HTMLField(blank=True, verbose_name='评论')


