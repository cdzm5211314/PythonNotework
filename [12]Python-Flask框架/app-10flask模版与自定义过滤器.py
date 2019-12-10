# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/index')
def index():
    data = {
        'name':'张三',
        'age':21,
        'param_dict':{'city':'henan','country':'china'},
        'param_list': [1,4,7,2,5,8,3,6,9],
    }
    # return render_template('filter.html', course='Python')  # course传递给模版的变量
    return render_template('filter.html', **data)  # course传递给模版的变量



# 自定义模版过滤器(两种方式)
# 注: 自定义的过滤器名称如果和内置的过滤器重名,会覆盖内置的过滤器
# 第一种方式
# 1.定义过滤器函数
def list_step_2(list):
    '''取列表步长2的列表元素'''
    return list[1::2]
# 2.注册过滤器(第一个参数为自定义过滤器函数的名字,第二个参数为过滤器的名字,以方便模版使用)
app.add_template_filter(list_step_2, 'double_2')

# 第二种方式:
@app.template_filter('list_reverse')
def list_reverse(li):
    '''列表元素的反转'''
    return list(reversed(li))



if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序

# 模版中使用变量及过滤器
'''
<p>模版中使用视图函数传递过来变量</p>

<p>变量name = {{ course }}</p>

<p>变量name = {{ name }}</p>
<p>变量name = {{ age }}</p>

<p>字典变量 param_dict: city = {{ param_dict }}</p>
<p>字典变量获取键的值 param_dict: city = {{ param_dict['city'] }}</p>
<p>字典变量获取键的值 param_dict: city = {{ param_dict.country }}</p>

<p>列表变量: param_list: {{ param_list }}</p>
<p>列表变量获取元素: param_list: {{ param_list[2] }}</p>

<p>列表变量中元素运算: param_list[1] + param_list[2] = {{ param_list[1] + param_list[2] }}</p>

<p>字符串的运算: {{ 'hello ' + 'Python' }}</p>

<hr>
<p>模版中使用内置过滤器 - 字符串过滤器</p>
<p>safe：禁用转义,默认是开启的 ---> {{ '<em>hello</em>' | safe }}</p>
<p>capitalize：把变量值的首字母转成大写，其余字母转小写 ---> {{ 'helloword' | capitalize}}</p>
<p>lower：把值转成小写 ---> {{ 'HELLO' | lower }}</p>
<p>upper：把值转成大写 ---> {{ 'hello' | upper }}</p>
<p>title：把值中的每个单词的首字母都转成大写 ---> {{ 'hello' | title }}</p>
<p>trim：把值的首尾空格去掉 ---> {{ '  hello flask      ' | trim}}</p>
<p>reverse:字符串反转 ---> {{ 'olleh' | reverse }}</p>
<p>format:格式化输出 ---> {{ '%s is %d' | format('name',17) }}</p>
<p>striptags：渲染之前把值中所有的HTML标签都删掉 ---> {{ '<em>hello</em>' | striptags }}</p>
<p>支持链式使用过滤器: {{ '  hello flask      ' | trim | upper}}</p>

<hr>
<p>模版中使用内置过滤器 - 列表过滤器</p>
<p>first：取第一个元素 ---> {{ [1,2,3,4,5,6] | first }}</p>
<p>last：取最后一个元素 ---> {{ [1,2,3,4,5,6] | last }}</p>
<p>length：获取列表长度 ---> {{ [1,2,3,4,5,6] | length }}</p>
<p>sum：列表求和 ---> {{ [1,2,3,4,5,6] | sum }}</p>
<p>sort：列表排序 ---> {{ [6,2,3,1,5,4] | sort }}</p>

<hr>
<p>模版中使用自定义过滤器(两种自定义过滤器方式)</p>
<p>需求: 取出列表[1,2,3,4,5,6,7,8,9]中下标为1,3,5,7,9的元素</p>
<p>自定义过滤器使用: {{ [1,2,3,4,5,6,7,8,9] | double_2 }}</p>
<p>自定义过滤器使用: {{ [1,2,3,4,5,6,7,8,9] | list_reverse }}</p>

'''