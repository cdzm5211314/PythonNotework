# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-30 10:50

#  下载工具包地址: https://github.com/twz915/DjangoUeditor3

### DjangoUeditor富文本的使用与配置
## 1. 创建extra_apps包作为放置第三方的app插件应用
## 2. 找到下载包中的DjangoUeditor文件夹,拷贝项目的extra_apps目录下: 如extra_apps/DjangoUeditor
## 3. 将extra_apps ---> mark ---> root_source (即PyCharm中File ---> Make Directory as ---> Sources Root)
## 4. 将extra_apps包在settings.py当中配置好搜索路径并在INSTALLED_APPS属性中注册DjangoUeditor的app应用
# import sys
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps')))
# sys.path.insert(0, os.path.join(BASE_DIR, 'extra_apps')))
# 'DjangoUeditor',
## 5. 找到项目url文件,配置DjangoUeditor路由
# urlpatterns = [
#     # 使用xadmin插件
#     url(r'^xadmin/', xadmin.site.urls),
#     # 使用DjangoUeditor富文本
#     url(r'^ueditor/',include('DjangoUeditor.urls')),
# ]
## 6. 找到app下的models模型类,在需要使用富文本框的字段使用UEditorField,如: apps/orgs/models/OrgInfo类
# 相关参数含义可参考文档:https://github.com/zhangfisher/DjangoUeditor
# from DjangoUeditor.models import UEditorField
# content = UEditorField(verbose_name='机构详情',
#                       width=700,
#                       height=400,
#                       toolbars='full',
#                       imagePath='ueditor/images/',
#                       filePath='ueditor/files/',
#                       upload_settings={'imageMaxSizing':1024000},
#                       default='')



### 在xadmin插件中使用DjangoUeditor富文本编辑器
# 注: 已将xadmin插件文件夹拷贝到extra_apps目录下,如:extra_apps/xadmin
## 1. 在plugins目录下新建ueditor.py文件,如extra_apps/xadmin/plugins/ueditor.py,
## 2. ueditor.py文件中添加如下代码:
# import xadmin
# from xadmin.views import BaseAdminPlugin, CreateAdminView, ModelFormAdminView, UpdateAdminView
# from DjangoUeditor.models import UEditorField
# from DjangoUeditor.widgets import UEditorWidget
# from django.conf import settings
# class XadminUEditorWidget(UEditorWidget):
#     def __init__(self,**kwargs):
#         self.ueditor_options=kwargs
#         self.Media.js = None
#         super(XadminUEditorWidget,self).__init__(kwargs)
# class UeditorPlugin(BaseAdminPlugin):
#
#     def get_field_style(self, attrs, db_field, style, **kwargs):
#         if style == 'ueditor':
#             if isinstance(db_field, UEditorField):
#                 widget = db_field.formfield().widget
#                 param = {}
#                 param.update(widget.ueditor_settings)
#                 param.update(widget.attrs)
#                 return {'widget': XadminUEditorWidget(**param)}
#         return attrs
# def block_extrahead(self, context, nodes):
#     js = '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.config.js")  # 自己的静态目录
#     js += '<script type="text/javascript" src="%s"></script>' % (settings.STATIC_URL + "ueditor/ueditor.all.min.js")  # 自己的静态目录
#     nodes.append(js)
#
# xadmin.site.register_plugin(UeditorPlugin, UpdateAdminView)
# xadmin.site.register_plugin(UeditorPlugin, CreateAdminView)
## 3. 将ueditor插件添加到xadmin/plugins中的__init__.py中的PLUGINS属性中
# PLUGINS = (
#     'ueditor'
# )
## 4. 找到app应用下的adminx.py文件,配置ueditor插件的模型类字段: 如 app/users/adminx.py
# 注:adminx.py文件中是注册的model模型类: 如: 注册apps/orgs/models/OrgInfo类
# class OrgInfoXadmin(object):
#     style_fields = {'content':'ueditor'}  # content为在model中定义的字段名称
# xadmin.site.register(OrgInfo,OrgInfoXadmin)
## 5. 在settings里面配置媒体文件的上传存储路径
# 注: 如果已经配置过就不必再配置
# 第一种:
# MEDIA_URL='/media/'
# MEDIA_ROOT=os.path.join(BASE_DIR,'media')
# 第二种:
# from django.views.static import serve
# 在项目url文件中配置
# url(r'^media/(?P<path>.*)$',serve,{"document_root":settings.MEDIA_ROOT},name='media')

## 注意: template模版页面需要取消转义: 如 safe