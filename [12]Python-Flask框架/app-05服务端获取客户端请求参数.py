# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13


## 服务端在接受客户端请求后,会自动创建Request对象,此对象由Flask框架创建,Request对象不可修改
# request表示当前Flask请求的对象,request对象中保存了一次HTTP请求的一切信息

## request对象的常用属性:
# url: 请求完整的URL地址
# base_url: 去掉GET参数的URL地址
# host_url: 只有主机和端口号的地址
# path: 路由中的路径
# method: 请求的使用方法(GET/POST...)
# remote_addr: 请求的客户端地址
# args: GET请求参数,类字典类型数据
# form: POST请求参数(即表单数据参数),类字典类型数据
# files: 文件上传,类字典类型数据
# data: 请求的数据,并转换为字符串
# cookies: 请求中的cookie信息
# headers: 请求中的报文头信息
# user_agent: 浏览器身份


from flask import Flask,request

app = Flask(__name__)


# 访问: http://127.0.0.1:5000/hello/zhangsan?pid=2
@app.route('/hello/<param>')
def hello_world(param):
    print(request.url)          # http://127.0.0.1:5000/hello/zhangsan?pid=2
    print(request.base_url)     # http://127.0.0.1:5000/hello/zhangsan
    print(request.host_url)     # http://127.0.0.1:5000/
    print(request.path)         # /hello/zhangsan
    print(request.method)       # GET
    print(request.remote_addr)  # 127.0.0.1
    print(request.args)         # ImmutableMultiDict([('pid', '2')])
    print(request.data)         # b''
    print(request.form)         # ImmutableMultiDict([])
    print(request.user_agent)   # Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
    # print(request.cookies)      # {}
    # print(request.headers)
    """
    Host: 127.0.0.1:5000
    Connection: keep-alive
    Upgrade-Insecure-Requests: 1
    User-Agent: Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36
    Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
    Accept-Encoding: gzip, deflate, br
    Accept-Language: zh-CN,zh;q=0.9


    """

    return 'Hello World!'

############################################################################################

## 获取请求参数: GET请求 args属性用来提取url中的数据(查询字符串)

@app.route("/test1/")
def test1():

    # 访问: http://127.0.0.1:5000/test1/?username=zhangsan&password=123456
    param = request.args  # ImmutableMultiDict([('username', 'zhangsan'), ('password', '123456')])

    # 访问: http://127.0.0.1:5000/test1/?password=123456
    # print(request.args["username"])  # zhangsan 注:如参数不存在,会报错
    print(request.args.get("username"))  # zhangsan 注:如果参数不存在,不会报错,会返回None

    # 访问: http://127.0.0.1:5000/test1/?password=123456&password=789
    print(request.args.get("password"))  # 123456 注:多个参数同名,会获取第一次出现的参数的值
    print(request.args.getlist("password"))  # ['123456', '789'] 注:多个参数同名,获取参数值的列表

    return "success"


## 获取请求参数: POST请求 form属性用来提取请求体中的数据
# http://127.0.0.1:5000/index?city=henan
@app.route('/index', methods=['GET','POST'])
def index():

    # form和data是用来提取请求体中的数据
    # 通过request.form可以直接提取请求体中的表单格式的数据,是一个类字典的对象
    name = request.form.get('age')  # 只能获取多个同名参数的第一个数据
    name_list = request.form.getlist('name')  # 获取多个同名参数数据的一个列表

    print(request.data)

    return 'success'

##
@app.route('/upload', methods=['POST'])
def uploadfile():
    '''接受前端传送过来的文件'''
    file_obj = request.files.get('pic')  # 文件上传的标签的name属性值
    if file_obj is None:  # 表示没有上传文件
        return '没有上传文件'

    # 将文件保存在本地(即程序所运行的目录中)
    # 使用原始操作保存文件:
    # f = open('./demo.jpg','wb')   # 1.创建一个文件
    # data = file_obj.read()        # 2.读取上传文件的内容
    # f.write(data)                 # 3.向新建的文件中写入刚才读取的文件内容
    # f.close()                     # 4.关闭文件

    # 使用with操作保存文件:
    # with open('test1.jpg', 'wb') as ft:
    #     ft.write(file_obj.read())

    # 使用flask操作保存文件:直接使用上传的文件对象进行保存
    file_obj.save('./test.jpg')

    return '上传成功'


if __name__ == '__main__':

    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    app.run(debug=True)  # 以debug调试模式开启flask程序


