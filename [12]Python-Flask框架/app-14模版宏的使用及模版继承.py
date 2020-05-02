# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('hong_extends.html')

if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序

# 模版宏类似于python中的函数,宏的作用就是在模板中重复利用代码,避免代码冗余
'''
<h2>不带参数宏的定义与使用</h2>
<p>定义:</p>
{% macro input() %}
    <input type="text" name="username" value="请填写用户名" size="30"/>
{% endmacro %}
<p>使用:</p>
{{ input() }}

<hr>
<h2>带参数宏的定义与使用</h2>
<p>定义:</p>
{% macro input(name,value='',type='text',size=20) %}
    <input name="{{ name }}" value="{{ value }}" type="{{ type }}" size="{{ size }}"/>
{% endmacro %}
<p>使用:</p>
{{ input(name='user', value='name',type='password',size=40)}}

<hr>
<h2>将宏单独封装在html文件中</h2>
<p>文件名可以自定义macro.html</p>
<!--{% macro input() %}-->
    <!--<input type="text" name="username" placeholde="Username">-->
    <!--<input type="password" name="password" placeholde="Password">-->
    <!--<input type="submit">-->
<!--{% endmacro %}-->
<p>在其它模板文件中先导入，再调用</p>
<!--{% import 'macro.html' as func %}-->
<!--{{ func.input() }}-->

<hr>
<h2>模版的继承,填充与包含(与Django框架一致)</h2>
<p>继承:extends ---> {% extends 'xxx.html' %}</p>
<p>填充:block ---> {% block mycontent' %}需要填充的内容{% endblock mycontent %}</p>
<p>包含:include ---> {% include 'yyy.html' %}</p>

<hr>
<h2>模版中的特殊变量与方法(可以直接访问)</h2>
<p>config对象: 就是Flask的config配置参数对象,也就是 app.config 对象</p>
<p>request对象: 表示当前请求的 request 对象,request对象中保存了一次HTTP请求的一切信息</p>
<p>url_for方法: 就是Flask的config配置参数对象,也就是 app.config 对象</p>
<p>get_flashed_messages方法(闪现): 返回之前在Flask中通过 flash() 传入的信息列表,把字符串对象表示的消息加入到一个消息队列中,然后通过调用 get_flashed_messages() 方法取出</p>

'''