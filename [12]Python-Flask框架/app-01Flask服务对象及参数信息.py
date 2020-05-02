# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask

# __name__ 表示当前模块的名字,Python中一个文件就表示一个模块
# print(__name__)  # __main__,表示当前模块为主运行模块


# 创建Flask服务对象
# 模块名,Flask以这个模块所在的目录为项目总目录,默认这个目录中的static为静态目录,templates为模版目录
# 参数: static_url_path = "/python"       # 访问静态资源的url前缀,默认值为static --->
# 参数: static_folder = "static"          # 静态文件的目录,默认就是static
# 参数: template_folder = "templates"     # 模版文件的目录,默认就是templates

# 访问静态资源的url前缀设置:
# 默认访问: http://127.0.0.1:5000/static/index.html
# 修改访问: http://127.0.0.1:5000/python/index.html
# app = Flask(__name__, static_url_path="/python")

app = Flask(__name__)  # app = Flask('__main__')

@app.route('/')
def index():
    '''定义视图函数'''
    return 'hello flask'



if __name__ == '__main__':
    # Flask服务启动时候添加参数说明:
    # debug=True: 开启调式模式,开启后如果修改Python代码会自动重启
    # threaded=True: 开始多线程
    # port: 启动时指定服务器端口号
    # host: 默认是127.0.0.1,指定为0.0.0.0代表本机可以被所有IP访问
    app.run(debug=True, host="0.0.0.0")  # 启动flask内置的简易web服务器


