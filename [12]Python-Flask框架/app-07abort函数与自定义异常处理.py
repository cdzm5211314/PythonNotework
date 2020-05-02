# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)


## abort()函数: 立即终止视图函数的继续执行,并且会把相对应的信息显示在前端中
@app.route('/login/', methods=['GET'])
def login():
    '''abort函数的使用'''
    # name = request.form.get('name')
    # pwd = request.form.get('pwd')

    name = ''
    pwd = ''
    if name == "zhangsan" or pwd == 'admin':
        return 'login success'
    else:
        # 使用abort函数可以立即终止视图函数的继续执行,并且会把相对应的信息显示在前端中
        # 1.传递状态码信息,必须是标准的http状态码(常用)
        abort(400)
        # 2.传递响应体信息,必须为响应体对象Response
        # res = Response('login failed')
        # abort(res)

##############################################################################################

## 自定义异常处理
@app.errorhandler(404)
def handle_404_error(err):
    '''自定义处理错误的函数'''
    # 这个函数的返回值会是前端用户看到的最终结果
    return u'出现了404错误,错误信息: %s' %err


if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序


