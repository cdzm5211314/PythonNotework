# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask,current_app


app = Flask(__name__)

# Flask配置参数(三种方式): 即相当于Django框架中的settings.py文件中的配置信息
# 第一种方式: 使用创建文件配置参数,如 config.cfg
# app.config.from_pyfile('config.cfg')  # 使用配置文件的相对路径,以当前文件的所在目录为总目录

# 第二种方式(常用): 使用创建类配置参数,如 Config
class Config(object):
    DEBUG = 'True'  # 开启Flask程序的调试模式
app.config.from_object(Config)

# 第三种方式: 使用直接操作config字典对象配置参数
# app.config["DEBUG"] = "True"


@app.route('/')
def index():
    '''定义视图函数'''
    # 视图函数中获取配置参数信息(两种方式):
    # 第一种方式: 如果在视图函数能直接操作全局对象app情况下获取配置参数
    print(app.config['DEBUG'])      # 直接从全局对象app的config中获取参数
    print(app.config.get('DEBUG'))  # 直接从全局对象app的config中获取参数
    # 第二种方式: 如果是其他模块中的视图函数获取配置参数, 需导入: from flask import current_app
    # current_app相当于全局的app对象
    print(current_app.config['DEBUG'])
    print(current_app.config.get('DEBUG'))

    return 'hello flask'

if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    # app.run()  # 启动flask内置的简易web服务器
    # app.run(host='0.0.0.0', port=5000)
    app.run(debug=True)  # 以debug调试模式开启flask程序


