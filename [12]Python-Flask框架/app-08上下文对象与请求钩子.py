# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# 请求上下文对象: request session
# 应用上下文对象: current_app g
# g: 处理请求时,用于临时存储的对象,每次请求都会重设这个变量

# 请求钩子是通过装饰器的形式实现,Flask支持如下四种请求钩子:
# before_first_request: 在处理第一个请求前运行
# before_request: 在每次请求前运行
# after_request(response): 如果没有未处理的异常抛出,在每次请求后运行
# teardown_request(response): 在每次请求后运行,即使有未处理的异常抛出

# 钩子的理解: 可以相当于Django框架中的中间件

from flask import Flask, request, url_for

app = Flask(__name__)


@app.route('/index')
def index():
    print('index 被执行')
    num = 1 / 0
    return 'index page'


@app.route('/hello')
def hello():
    print('hello 被执行')
    return 'hello page'


@app.before_first_request
def handle_before_first_request():
    '''在第一次请求处理之前先被执行'''
    print('在第一次请求处理之前先被执行 handle_before_first_request')


@app.before_request
def handle_before_request():
    '''在每次请求处理之前都被执行'''
    print('在每次请求处理之前都被执行 handle_before_request')


@app.after_request
def handle_after_request(response):
    '''在每次请求处理(视图函数处理)之后都被执行,前提是视图函数没有出现异常'''
    print('在每次请求处理之后都被执行,前提是视图函数没有出现异常 handle_after_request')
    return response


@app.teardown_request
def handle_teardown_request(response):
    '''在每次请求处理(视图函数处理)之后都被执行,不管视图函数是否出现异常,注意程序在非调式模式下,即DEBUG=False'''
    path = request.path  # 请求的url路径
    if path == url_for('index'):
        print('在请求钩子中判断请求的视图逻辑: index')
    elif path == url_for('hello'):
        print('在请求钩子中判断请求的视图逻辑: hello')
    print('在每次请求处理之后都被执行,不管视图函数是否出现异常 handle_teardown_request')
    return response


if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    # app.run(debug=True)  # 以debug调试模式开启flask程序
    app.run(debug=False)  # 以debug调试模式开启flask程序
