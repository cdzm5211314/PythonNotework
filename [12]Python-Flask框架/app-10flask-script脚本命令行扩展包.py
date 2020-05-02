# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13


# 安装: pip install flask-script
# flask-script: 实现命令行参数接受

from flask import Flask
from flask_script import Manager  # 脚本启动命令的管理类

# 创建Flask的应用对象
app = Flask(__name__)

# 创建脚本启动命令的管理类对象
manager = Manager(app=app)

@app.route('/')
def index():

    return 'index page'


if __name__ == '__main__':
    # app.run(debug=True)  # 以debug调试模式开启flask服务器
    # 通过脚本启动命令的管理类对象启动flask服务器
    manager.run()


## 通过终端命令行去执行命令: 如 runserver, shell
# 启动flask脚本程序命令: python 脚本文件.py runserver
# 参数说明: -h(指定主机), -p(指定端口), -d(调试模式), -r(自动重新加载文件), --threaded(多线程)
# 如: python app-10flask-script脚本命令行扩展包.py runserver -h 0.0.0.0 -p 8000
# 如: python app-10flask-script脚本命令行扩展包.py runserver -d -r -h 0.0.0.0 -p 8000
# 进入flask环境交互命令: python 脚本文件.py shell
# 如: python app-10flask-script脚本命令行扩展包.py shell


