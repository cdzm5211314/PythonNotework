# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-30 11:03

### 一个项目中可有多个app应用,所以创建一个总应用目录进行管理

## 1.在项目根目录下创建一个包: 如apps (如果是第三方插件应用可有创建extra_apps)
## 2.把之前创建的app应用复制粘贴到apps总应用包下
## 3.将apps ---> mark ---> root_source (即PyCharm中File ---> Make Directory as ---> Sources Root)
## 4.在settings.py设置apps总应用包的搜寻环境变量
# import sys
# sys.path.insert(0, os.path.join(BASE_DIR, 'apps')))
## 5.在setting.py中配置INSTALLED_APPS:
INSTALLED_APPS = [
    'django.contrib.staticfiles',
    # 配置app单个应用
    'users.apps.UsersConfig',
    'courses.apps.CoursesConfig',
    'orgs.apps.OrgsConfig',
    'operations.apps.OperationsConfig',
]
# 或者
# INSTALLED_APPS = [
#     'django.contrib.staticfiles',
#     # 配置apps总应用,也可以不添加
#     'apps',
#     # 配置app单个应用
#     'user.apps.UserConfig',      # 用户模块
#     'goods.apps.GoodsConfig',    # 商品模块
#     'order.apps.OrderConfig',    # 订单模块
#     'cart.apps.CartConfig',      # 购物车模块
# ]

# INSTALLED_APPS = [
#     'django.contrib.staticfiles',
#     'apps',     # 总应用包
#     'user',     # 用户模块
#     'goods',    # 商品模块
#     'order',    # 订单模块
#     'cart',     # 购物车模块
# ]
