# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13


from flask import Flask, redirect, url_for, render_template, make_response, jsonify


app = Flask(__name__)

## 视图函数的返回值的集中形式:


@app.route('/test/')
def test():
    return "success"  # 返回一个字符串


@app.route('/test/')
def test():
    # 设置响应信息(一): 返回元组时,顺序依次是: 返回内容,返回状态码,返回响应头信息
    # return 'hello world', 200  # 返回元组数据
    # return 'index page', 666, {'name': 'lisi', 'age': '20'}  # 状态码可以任意填写, UNKNOWN
    # return 'index page', '666 flask status', {'name':'lisi','age':'20'}  # 第二个位置可以是字符串形式,状态码 空格分开 + 描述信息
    return 'hello world', 200, {'Locateion':'www.baidu.com'}  # 返回元组数据


@app.route('/test/')
def test():
    # 设置响应信息(二): 使用make_response构造响应信息
    from flask import make_response
    # response = make_response(data, code)  # data返回的数据内容,code状态码

    # response = make_response('hello')
    # response.status = '999 flask status'  # 设置状态码
    # response.headers['name'] = 'wangwu'   # 设置响应头信息
    # return response  # 返回make_response

    response = make_response('hello', 200)
    response.headers = {'Location': 'abc'}  # 设置响应头信息
    return response  # 返回make_response


@app.route('/test/')
def test():
    from flask import render_template
    return render_template("test.html")  # 返回模版文件


@app.route('/test/')
def test():
    from flask import jsonify

    import json
    # json_str = json.dumps(data)           # python字典类型转换成json字符串类型
    # python_dict = json.loads(json_str)    # json字符串类型转换成python字典类型
    # return json_str, 200, {'Content-Type':'application/json'}  # 使用原始的方式设置响应头信息,返回json字符串格式数据

    # jsonify函数帮助转为数据为json字符串,并设置响应头 Content-Type 为 application/json
    return jsonify({'name': '张三', 'age': 25})       # 返回json字符串数据
    # return jsonify(city='henan', country='China')  # 返回json字符串数据


## 反向解析: 根据视图函数的名字获取访问路径
@app.route('/test/')
def test():
    from flask import redirect
    # 访问: http://127.0.0.1:5000/hello
    return redirect("/hello")  # 固定写死路由,进行路由反向跳转

@app.route('/test/')
def test():
    from flask import redirect, url_for
    # url = url_for('index')  # 通过url_for函数,通过视图函数的名字找到视图函数对应的路由url路径
    # return redirect(url)    # 路由重定向
    # url_for("函数名",参数名=value)
    return redirect(url_for('index'))  # 动态获取路由,进行路由反向跳转

## 反向解析: url_for()
# 在app中使用: url_for("函数名")
# 在蓝图中使用: url_for("蓝图名.函数名")
# 在模版中获取静态资源路径: url_for("静态资源", filename="相对于资源的相对路径")


if __name__ == '__main__':

    print(app.url_map)  # 通过url_map可以查看整个Flask程序中路由信息
    # Map([< Rule '/' (OPTIONS, HEAD, GET) -> index >,< Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static >])
    app.run(debug=True)  # 以debug调试模式开启flask程序


