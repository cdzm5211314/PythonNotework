# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-30 10:51

### admin后台集成富文本编辑器步骤: 富文本方式一
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


### admin后台集成富文本编辑器步骤: 富文本方式二
## 1.安装模块包: pip install django-ckeditor
## 2.配置第三方应用: settings ---> INSTALLED_APPS
INSTALLED_APPS = [
    'ckeditor',           # 富文本编辑器
    'ckeditor_uploader',  # 富文本编辑器上传图片模块
]
## 3.配置MEDIA映射路径: settings
# 富文本编辑器ckeditor配置
# CKEDITOR_CONFIGS = {
#     'default': {
#         'toolbar': 'full',  # 工具条功能
#         'height': 300,  # 编辑器高度
#         'width': 300,  # 编辑器宽
#     },
# }
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR,'media')
CKEDITOR_UPLOAD_PATH = 'upload/'
# 上传图片保存路径,如果没有图片存储或者使用自定义存储位置,那么则直接写' ';
# 如果是使用django本身的存储方式,那么你就指名一个目录用来存储即可

## 4.配置URL映射路径: 根路由
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),  # Admin后台富文本编辑器
]

from Blog.settings import DEBUG, MEDIA_ROOT
from django.views.static import serve
if DEBUG:
    urlpatterns += url(r'^media/(?P<path>.*)/$', serve, {"document_root":MEDIA_ROOT})

## 5.配置模型类字段: models.py文件
# ckeditor.fields.RichTextField 不支持上传文件的富文本字段
# ckeditor_uploader.fields.RichTextUploadingField 支持上传文件的富文本字段
# 哪个模型类字段使用富文本编辑器,就修改哪个字段属性
from ckeditor_uploader.fields import RichTextUploadingField
content = RichTextUploadingField(null=True, blank=True)  # 帖子内容,使用富文本编辑器

## 6.重新生成迁移文件并执行
python manage.py makemigrations
python manage.py migrate

## 7.注册模型类: admin.py文件
# admin.site.register(Post)  # 原始注册方式
@admin.register(Post)  # 自定义方式注册模型类
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "created"]
# admin.site.register(Post, PostAdmin)  # 自定义方式注册模型类

