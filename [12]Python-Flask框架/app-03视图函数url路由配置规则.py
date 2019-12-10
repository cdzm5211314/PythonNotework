# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route('/')
def index():
    '''定义视图函数'''
    return 'hello flask'



# 通过methods限定视图函的访问方式
@app.route('/post_onlt', methods=['GET','POST'])
def post_only():
    '''定义视图函数'''
    return 'post only'



# 当同一路由装饰两个视图函数时,上面的视图函数会覆盖下面的视图函数
# 如果路由想要分别访问两个视图函数,可以根据methods限定视图的访问方式
@app.route('/hello')
def hello():
    return 'hello'
@app.route('/hello')
def hello2():
    return 'hello 2'

# 当同一视图函数分别由两个路由装饰时,访问任意一个路由,都可以指定到此视图函数
@app.route('/hi1')
@app.route('/hi2')
def hi():
    return 'hi'



@app.route('/login')
def login():
    '''视图函数中使用路由反向重定向'''
    # url = '/'  # 固定写死路由访问路径
    # url = url_for('index')  # 通过url_for函数,通过视图函数的名字找到视图函数对应的路由url路径
    # return redirect(url)  # 路由重定向
    return redirect(url_for('index'))  # 路由反向跳转



if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    print(app.url_map)  # 通过url_map可以查看整个Flask程序中路由信息
    # Map([< Rule '/' (OPTIONS, HEAD, GET) -> index >,< Rule '/static/<filename>' (OPTIONS, HEAD, GET) -> static >])
    app.run(debug=True)  # 以debug调试模式开启flask程序


