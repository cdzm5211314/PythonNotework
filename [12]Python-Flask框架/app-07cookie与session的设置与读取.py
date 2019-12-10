# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask,make_response,request,session

app = Flask(__name__)

# 设置cookkie信息
@app.route('/set_cookie')
def set_cookie():
    resp = make_response('success')
    # cookie有效期默认浏览器关闭就失效
    resp.set_cookie('cookiekey','cookievalue')
    resp.set_cookie('cookiekey2','cookievalue2')
    resp.set_cookie('cookiekey3','cookievalue3',max_age=60)  # 有效期时间单位为秒
    return resp

# 获取cookie信息
@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('cookiekey')
    return cookie

# 删除cookie
@app.route('/del_cookie')
def del_cookie():
    resp = make_response('del success')
    resp.delete_cookie('cookiekey2')
    return resp

###################################################################################
# Flask的session需要用到秘钥字符串,所以需要提前配置参数信息
# Flask默认把session保存到了cookie中
app.config['SECRET_KEY'] = 'qw4654sfswzzvswwt56'

session_dict = {}

# 设置session信息
@app.route('/userlogin')
def userlogin():
    # 把session保存到程序运行的内存中
    global session_dict  # 声明为全局变量
    session_dict['1']['username'] = 'Python'
    # flask默认把session保存到cookie中
    session['username'] = 'python'
    return 'userlogin set session success'

# 获取session信息
@app.route('/index')
def index():
    username = session.get('username')
    return 'index get session success: %s' %username



if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序


