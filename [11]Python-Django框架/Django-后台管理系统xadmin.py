# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-29 15:39

# 第三方插件Xadmin(基于Bootstrap3): 官网 http://sshwsfc.github.io/xadmin/
# GitHub下载地址: https://github.com/sshwsfc/xadmin

### Xadmin的安装与配置:
## 1、将下载好的xadmin-master解压，复制里面的xadmin文件夹到我们的项目根目录当中
## 2、创建extra_apps包作为放置第三方的app插件应用，然后将xadmin文件夹移动到extra_apps包下
## 3、将extra_apps ---> mark ---> root_source (即PyCharm中File ---> Make Directory as ---> Sources Root)
## 4、将extra_apps包在settings.py当中配置好搜索路径:
# import sys
# sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps')))
## 5、安装xadmin依赖包: 打开cmd，进入虚拟环境，安装xadmin依赖包，依赖包的版本在xadmin文件夹下：requirements.txt，在其中有一个包版本改成2.1 django-formtools==2.1，否则版本太低，拉不起来
# pip install -r requirements.txt -i https://pypi.douban.com/simple/
## 6、依赖包装完之后，再去settings.py中的INSTALLED_APPS当中添加上xadmin插件应用app
# 'xadmin',
# 'crispy_forms',
## 7、将项目本来的admin注释掉改为xadmin:
# import xadmin
# url(r'^xadmin/', xadmin.site.urls),
## 8、再次执行迁移同步，目的是为了生成xadmin所依赖的表:
# python manage.py migrate
## 11、创建超级管理员，去验证xadmin是否安装成功
# python manage.py createsuperuser
# Username: chendong
# Email address: configureadmin@163.com
# Password: 密码
# Password (again): 密码
# Superuser created successfully.


### Xadmin的后台注册文件: 注册model模型类(数据表)到xadmin后台管理系统中
## 在app应用下创建adminx.py文件,xadmin的数据表注册是到app应用下的adminx.py文件中查找:
# 如创建 apps.courses.xadmin.py
# import xadmin
# from course.models import CourseInfo
# class CourseInfoXadmin(object):
#     list_display = []  # 展示字段
#     list_filter = []  # 过滤字段
#     search_fields = []  # 搜索字段
# xadmin.site.register(CourseInfo,CourseInfoXadmin)  # 注册



### Xadmin全局-配置后台管理主题样式: 找到任意app应用下的adminx.py文件 apps.courses.xadmin.py
# from xadmin views import views
# class BaseXadminSetting(object):
#     enable_themes = True
#     use_bootswatch = True
# xadmin.site.register(views.BaseAdminView,BaseXadminSetting)

### Xadmin全局-配置后台管理系统名称: 找到任意app应用下的adminx.py文件 apps.courses.xadmin.py
# from xadmin import views
# class CommXadminSetting(object):
#     site_title = 'xx后台管理系统'
#     site_footer = '版权所有'
#     menu_style = 'accordion'  # 设置伸缩
# xadmin.site.register(views.CommAdminView,CommXadminSetting)

### Xadmin应用-配置后台管理导航栏app应用(英文)名称为中文名称:
# 第一种: 找到app应用下的apps.py文件: 如 apps.courses.app.py
# class CoursesConfig(AppConfig):
#     name = 'courses'       # 当前app英文名称
#     verbose_name = "课程"  # 设置app中文名称
# 第二种: 找到app应用下的__init__.py文件,配置app中文名称设置类的路径: 如 apps.courses.__init__.py
# default_app_config = 'courses.apps.CoursesConfig'


### 修改xadmin后台管理页面左侧栏的图标显示样式:
# 1.在项目目录下找到extra_apps/xadmin/pulgins/auth.py文件 ---> model_icon = 'fa fa-user'
# 2.把model_icon = 'fa fa-user'添加到每个app应用下的adminx.py文件中的模型注册类中
# 注: 图标样式使用的是xadmin插件下的extra_apps/xadmin/static/xadmin/vendor/font-awesome/css和font
# 3.使用最新第三方插件: 如下载font-awesome-4.7.0.zip,解压文件并复制css和font文件夹进行覆盖
# 4.修改adminx.py文件,根据http://fontawesome.dashgame.com/提供的图标样式名称修改model_icon的值





