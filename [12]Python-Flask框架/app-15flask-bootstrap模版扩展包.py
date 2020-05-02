# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator


## 安装: pip install flask-bootstrap

from flask import Flask
from flask_script import Manager
from flask_bootstrap import Bootstrap


app = Flask(__name__)

bt = Bootstrap(app=app)


# http://127.0.0.1:5000/
@app.route('/')
def demo():

    return 'success'



manager = Manager(app=app)

if __name__ == '__main__':
    manager.run()

## 终端命令行启动服务器: 启动服务器的时候开启调试模式并代码变更自动重启服务器
# python app.py runserver -d -r

"""
## xxx.html文件:

# 使用bootstrap扩展
{% extends 'bootstrap/base.html' %}


{% block content %}
    <h3> 来自于bootstrap扩展 </h3>
{% endblock %}

# 未开发者实现: doc, html, head, body, title, styles, navbar, content ...



"""

