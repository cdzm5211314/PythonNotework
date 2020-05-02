# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, redirect, url_for, render_template


app = Flask(__name__)


## Flask路由参数说明: 关键字参数
# 默认标识是尖括号<name>
# name需要和对应的视图函数的参数名字保持也一直
# 参数允许有默认值:
    # 如果有默认值,那么路由中,不传输参数也是可以的
    # 如果没有默认值,参数在路由中必须传递
# 默认参数类型: 字符串
# 参数语法: <converter:var>
    # converter: 参数类型,如:
        # string: 默认类型,会将斜杠认为是参数分隔符
        # int: 约束,限制参数的类型,只能是纯数字
        # float:
        # path: 接受到的数据格式是字符串,特性: 会将斜杠认为是一个字符
        # uuid: 接受uuid类型数据,xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    # var: 参数名称


# 访问: http://127.0.0.1:5000
@app.route('/')
def index():
    '''定义视图函数'''
    return 'hello flask'

# 访问: http://127.0.0.1:5000/hello
@app.route("/hello/")
def hello():
    '''定义视图函数'''
    return render_template("hello.html")

# 访问: http://127.0.0.1:5000/param/123
@app.route("/param/<args>/")  # 默认接受string类型数据
def param1(args):
    print(type(args), args)  # <class 'str'> 123
    return "success"

# 访问: http://127.0.0.1:5000/param/zhangsan
@app.route("/param/<string:name>/")  # 接受string类型数据
def param2(name):
    print(type(name), name)  # <class 'str'> zhangsan
    return "success"

# 访问: http://127.0.0.1:5000/param/123
@app.route("/param/<int:nid>/")  # 接受int类型数据,只能是纯数字
def param3(nid):
    print(type(nid), nid)  # <class 'int'> 123
    return "success"

# 访问: http://127.0.0.1:5000/param/xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
@app.route("/param/<uuid:name>/")  # 接受uuid类型数据
def param4(name):
    print(type(name), name)  # <class 'uuid.UUID'> xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx
    return "success"

# 访问: http://127.0.0.1:5000/param/abc
# 访问: http://127.0.0.1:5000/param/abc/def
@app.route("/param/<path:name>")
def param(name):
    print(type(name), name)  # <class 'str'> abc 或 <class 'str'> abc/def
    return "success"


############################################################################################

## Flask请求方法说明:
# 常用的方法有5个,请求方式默认为GET,可以在路由参数中设置,如下所示
# method = ["GET", "POST", "DELETE", "PUT", "HEAD"]
# methods参数限定视图函的访问方式


# 访问: http://127.0.0.1:5000/demo
@app.route('/demo/',)  # 默认GET请求方式
def demo1():
    '''定义视图函数'''
    return 'demo1'

# 访问: http://127.0.0.1:5000/demo
@app.route('/demo/', methods=['GET'])  # 限定GET请求方式,访问视图函数
def demo2():
    '''定义视图函数'''
    return 'demo2'

# 访问: http://127.0.0.1:5000/demo
@app.route('/demo/', methods=['POST'])  # 限定POST请求方式,访问视图函数
def demo3():
    '''定义视图函数'''
    return 'demo3'

# 访问: http://127.0.0.1:5000/demo
@app.route('/demo/', methods=['GET','POST'])  # 限定GET,POST两种请求方式,访问视图函数
def demo4():
    '''定义视图函数'''
    return 'demo4'

##########################################################################################

## 1.当同一视图函数分别由两个路由装饰时,访问任意一个路由,都可以访问到此视图函数
# 访问: http://127.0.0.1:5000/test1 ---> 视图函数: test
# 访问: http://127.0.0.1:5000/test2 ---> 视图函数: test
@app.route('/test1/')
@app.route('/test2/')
def test():
    return 'success'

## 2.当同一路由装饰两个视图函数时,上面的视图函数会覆盖下面的视图函数
# 访问: http://127.0.0.1:5000/hello ---> 视图函数: demo1
@app.route('/hello/')
def demo1():
    return 'hello'

@app.route('/hello/')
def demo2():
    return 'hello 2'

# 如果路由想要分别访问两个视图函数,可以根据methods限定视图的访问方式
# 访问: http://127.0.0.1:5000/hello ---> GET请求方式 ---> 访问视图函数: demo3
@app.route('/hello/', methods=["GET"])
def demo3():
    return 'hello'
# 访问: http://127.0.0.1:5000/hello ---> POST请求方式 ---> 访问视图函数: demo4
@app.route('/hello/', methods=["POST"])
def demo4():
    return 'hello 2'


##########################################################################################

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


