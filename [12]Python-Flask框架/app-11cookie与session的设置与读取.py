# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13


### 会话技术: 会话是浏览器和服务器之间的多次请求和响应
## 跨域请求传递数据
## web开发中使用的短连接
## cookie
    # 客户端会话技术
    # 数据都是存储在浏览器中
    # 支持过期
    # 不能跨域名
        # frame标签
        # 可以直接加载整个网站
    # 不能跨浏览器
    # cookie是通过Response来进行操作
    # flask中的cookie可以直接支持中文
        # flask对cookie中的内容做了编码
## session
    # 服务端会话技术
    # 对数据进行数据安全操作
    # 默认在内存中
        # 不容易管理
        # 容易丢失
        # 不能多台电脑协作
## token


from flask import Flask,make_response,request,session


app = Flask(__name__)

# 设置cookie信息
@app.route('/set_cookie')
def set_cookie():

    # 创建response对象
    # response = Response(response="响应信息")
    # 设置cookie信息
    # response.set_cookie("key1","value1")
    # return response

    # 创建response对象
    resp = make_response('success')
    # 设置cookie信息,有效期默认浏览器关闭就失效
    resp.set_cookie('cookiekey','cookievalue')
    resp.set_cookie('cookiekey2','cookievalue2')
    # 设置cookie的有效期时间,单位为秒
    resp.set_cookie('cookiekey3','cookievalue3',max_age=60)
    return resp

# 获取cookie信息
@app.route('/get_cookie')
def get_cookie():
    cookie = request.cookies.get('cookiekey')
    return cookie

# 删除cookie
@app.route('/del_cookie')
def del_cookie():
    # 创建response对象
    # resp = make_response('del success')
    # 删除cookie
    # resp.delete_cookie('cookiekey2')

    # 创建response对象
    resp = redirect(url_for("login"))
    # 删除cookie
    resp.delete_cookie('cookiekey2')

    return resp


############################################################################################

# Flask框架中session需要用到秘钥字符串,所以需要提前配置参数信息
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


