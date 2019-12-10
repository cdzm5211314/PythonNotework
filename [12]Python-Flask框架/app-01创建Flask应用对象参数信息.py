# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask

# __name__ 表示当前模块的名字,Python中一个文件就表示以个模块
# print(__name__)  # __main__

# 创建Flask的应用对象
# 模块名,Flask以这个模块所在的目录为项目总目录,默认这个目录中的static为静态目录,templates为模版目录
# 参数: static_url_path = "/python3"      # 访问静态资源的url前缀,默认值为static  --->
# 参数: static_folder = "static"          # 静态文件的目录,默认就是static
# 参数: template_folder = "templates"     # 模版文件的目录,默认就是templates

# 访问静态资源的url前缀设置:
# 默认访问: http://127.0.0.1:5000/static/index.html
# 修改访问: http://127.0.0.1:5000/python/index.html
# app = Flask(__name__, static_url_path="/python")

app = Flask(__name__)  #  app = Flask('__main__')

@app.route('/')
def index():
    '''定义视图函数'''
    return 'hello flask'

if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    app.run()  # 启动flask内置的简易web服务器


