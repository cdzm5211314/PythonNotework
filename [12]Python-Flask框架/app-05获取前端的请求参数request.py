# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# request表示当前Flask请求的对象,request对象中保存了一次HTTP请求的一切信息
# request对象的常用属性:
# data: 记录请求的数据,并转换为字符串
# form: 记录请求中的表单数据
# args: 记录请求中的查询参数
# cookies: 记录请求中的cookie信息
# headers: 记录请求中的报文头
# method: 记录请求使用的http方法(GET/POST)
# url: 记录请求的url地址
# files: 记录请求上传的文件

from flask import Flask,request

app = Flask(__name__)

# http://127.0.0.1:5000/index?city=henan
@app.route('/index', methods=['GET','POST'])
def index():

    # form和data是用来提取请求体中的数据
    # 通过request.form可以直接提取请求体中的表单格式的数据,是一个类字典的对象
    # 通过get方法只能拿到多个重名参数的第一个
    name = request.form.get('name')
    name_list = request.form.getlist('name')
    age = request.form.get('age')
    print(request.data)

    # args是用来提取url中的参数(查询字符串)
    city = request.args.get('city')

    return 'hello name=%s, age=%s, city=%s, name_list=%s' % (name, age, city, name_list)

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


