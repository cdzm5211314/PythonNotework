# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, request, abort, Response, make_response, jsonify
import json

app = Flask(__name__)

# 使用abort函数
@app.route('/login', methods=['GET'])
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

@app.errorhandler(404)
def handle_404_error(err):
    '''自定义处理错误的函数'''
    # 这个函数的返回值会是前端用户看到的最终结果
    return u'出现了404错误,错误信息: %s' %err



# 设置响应信息的方法(两种)
@app.route('/index')
def index():

    # 第一种: 使用元组,返回自定义的响应信息
    #         响应体    状态码            响应头
    # return 'index page', 400, [('name','zhangsan'),('age','18')]
    # return 'index page', 400, {'name':'lisi','age':'20'}
    # return 'index page', 666, {'name':'lisi','age':'20'}  # 状态码可以任意填写, UNKNOWN
    # return 'index page', '666 flask status', {'name':'lisi','age':'20'}  # 第二个位置可以是字符串形式,状态码 空格分开 + 描述信息

    # 第二种: 使用make_response构造响应信息
    resp = make_response('index page response')
    resp.status = '999 flask status'  # 设置状态码
    resp.headers['name'] = 'wangwu'  # 设置响应头
    resp.headers['age'] = '25'  # 设置响应头
    return resp



# 返回json数据的方法
@app.route('/json')
def jsonfunc():

    # json: 就是字符串
    data = {'name':'张三','age':25}

    # json_str = json.dumps(data)           # python字典类型转换成json字符串类型
    # python_dict = json.loads(json_str)    # json字符串类型转换成python字典类型
    # return json_str, 200, {'Content-Type':'application/json'}  # 使用原始的方式设置响应头信息,返回json字符串格式数据

    # jsonify函数帮助转为数据为json字符串,并设置响应头 Content-Type 为 application/json
    return jsonify(data)                            # 返回json字符串数据
    # return jsonify(city='henan',country='China')  # 返回json字符串数据


if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序


