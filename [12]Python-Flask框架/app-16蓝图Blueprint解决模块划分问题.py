# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# 蓝图用于实现单个应用的视图、模板、静态文件的集合,蓝图就是模块化处理的类
# 简单来说:蓝图就是一个存储操作路由映射方法的容器,主要用来实现客户端请求和URL相互关联的功能
# Flask中使用蓝图可以帮助我们实现模块化应用的功能


##############################################################################################################
# app.py文件: 程序实例文件,即程序的入口模块文件
from flask import Flask
# from 模块名 import 模块中的蓝图对象  # 文件形式创建蓝图对象
# from 包名 import 模块中的蓝图对象    # 包文件形式创建蓝图对象

app = Flask(__name__)

# 3.在程序实例中注册某个模块应用的蓝图对象
# 第一个参数是蓝图对象,url_prefix参数默认值是根路由,如果指定:会在蓝图注册的路由url中添加前缀
app.register_blueprint(app_goods,url_prefix='/goods')
app.register_blueprint(app_order,url_prefix='/order')

# ---------------------------------------------------- #
# 蓝图的模块应用分离使用:
# 模块应用一: 分文件形式与包(目录)文件形式
# 文件形式: 如 goods.py  ---> 蓝图对象就创建在此文件中
# 包文件形式: 如 goods/*.py ---> 蓝图对象就创建在包下的__init__.py文件中,顺便把视图加载进来,让蓝图与应用程序知道有视图的存在 from .views import 视图函数名字
from flask import Blueprint
# 1.创建一个蓝图的对象,蓝图对象就是一个小模块的抽象概念
# Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
app_goods = Blueprint('app_goods',__name__)  # 注: 蓝图的名字与蓝图对象的名字不一定需要一致

# 2.使用蓝图对象注册蓝图路由
@app_goods.route('/index')  # http:127.0.0.0:5000/goods/index
# from . import app_goods  # 如是包文件形式创建的蓝图对象,需要在使用蓝图的地方进行导入蓝图对象
def goods_index():
    return 'goods_index'

# 3.在程序实例中注册该蓝图,即把该蓝图添加到程序入口模块文件中(app.py)
# 第一个参数是蓝图对象,url_prefix参数默认值是根路由,如果指定:会在蓝图注册的路由url中添加前缀
# app.register_blueprint(app_goods,url_prefix='/admin')

# ------------------------------------------------------------------------------------------------------------ #
# 蓝图的模块应用分离使用:
# 模块应用二: 分文件形式与包(目录)文件形式
# 文件形式: 如 order.py  ---> 蓝图对象就创建在此文件中
# 包文件形式: 如 order/*.py ---> 蓝图对象就创建在包下的__init__.py文件中,顺便把视图加载进来,让蓝图与应用程序知道有视图的存在 from .views import 视图函数名字
from flask import Blueprint
# 1.创建一个蓝图的对象,蓝图对象就是一个小模块的抽象概念
# Blueprint必须指定两个参数，admin表示蓝图的名称，__name__表示蓝图所在模块
app_order = Blueprint('app_order',__name__)  # 注: 蓝图的名字与蓝图对象的名字不一定需要一致

# 2.使用蓝图对象注册蓝图路由
@app_order.route('/index')  # http:127.0.0.0:5000/order/index
# from . import app_order  # 如是包文件形式创建的蓝图对象,需要在使用蓝图的地方进行导入蓝图对象
def order_index():
    return 'order_index'

# 3.在程序实例中注册该蓝图,即把该蓝图添加到程序入口模块文件中(app.py)
# 第一个参数是蓝图对象,url_prefix参数默认值是根路由,如果指定:会在蓝图注册的路由url中添加前缀
# app.register_blueprint(app_order,url_prefix='/admin')


################################################################################################################
# 蓝图中模版目录的处理:
# 视图函数中返回的模版文件默认是到程序根目录下的templates目录查找
# 如果应用模块中的视图函数想要查到应用模块包下指定的目录(如 static和templates)下的模版文件,
# 需要在应用模块包下的__init__.py文件中创建蓝图对象时,添加两个属性(static_folder和template_folder), 如下
# app = Blueprint('app_goods', __name__, static_folder='static', template_folder='templates')

# 模版文件的查找顺序: 先查找模版文件总目录,再查找应用模块下的模版文件目录


################################################################################################################
if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    print(app.url_map)
    app.run(debug=True)  # 以debug调试模式开启flask程序

