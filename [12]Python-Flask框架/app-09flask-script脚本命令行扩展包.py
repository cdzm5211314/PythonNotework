# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# Flask-Script扩展命令行
# 安装: pip install Flask-Script

from flask import Flask
from flask_script import Manager  # 脚本启动命令的管理类

app = Flask(__name__)

# 创建脚本启动命令管理类对象
manager = Manager(app)

@app.route('/')
def index():

    return 'index page'



if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    # app.run(debug=True)  # 以debug调试模式开启flask程序
    # 通过管理类对象启动flask程序
    manager.run()


# 通过终端命令行去执行命令: 如 runserver, shell
# 启动脚本程序命令: python 脚本文件.py runserver
# 如: python app-09flask-script脚本命令行扩展包.py runserver -h 0.0.0.0 -p 8000
# 启动flask程序交互命令: python 脚本文件.py shell
# 如: python app-09flask-script脚本命令行扩展包.py shell

