# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

from flask import Flask, redirect, url_for
from werkzeug.routing import BaseConverter

app = Flask(__name__)


# 转换器指定按照哪个类型接受参数: 如 string(默认接受字符串) int(接受整数) float(接受浮点数) path(和默认相似,但也接受斜线)
# @app.route('/goods/<int:goods_id>')  # 设置转换器以整数类型的方式去提取url路由参数
@app.route('/goods/<goods_id>')  # 默认转换器以字符串类型方式提取url路由参数(除了/的字符以外)
def goods_detail(goods_id):
    '''定义视图函数'''
    print(goods_id)
    return 'goods detail page %s' % goods_id


# 自定义转换器的使用步骤:
# 1.自定义自己的转换器类,需要继承 from werkzeug.routing import BaseConverter
class RegexConverter(BaseConverter):
    '''自定路由转换器'''

    # 普通转换器
    def __init__(self, url_map):  # url_map是固定参数,表示当前app对像的路由映射列表
        super(RegexConverter, self).__init__(url_map)  # 调用父类的初始化方法
        self.regex = r"1[34578]\d{9}"  # 定义正则表达式

    # 万能转换器
    # def __init__(self, url_map, regex):  # url_map是固定参数,表示当前app对像的路由映射列表
    #     # 调用父类的初始化方法
    #     super(RegexConverter, self).__init__(url_map)
    #     # 将正则表达式的参数保存到对象的属性中,Flask会使用这个属性来进行路由的正则匹配
    #     # self.regex = regex  # regex为url路由传递过来的正则表达式参数, 即 (r"1[34578]\d{9}")

    def to_python(self, value):  # 一般不需要重写父类的to_python方法
        '''可以对提取的路由参数进行进一步的处理,value = 提取的路由参数'''
        # value值默认是提取的路由参数,也可以是进一步处理后的数据,并且返回的是什么数据,视图函数的参数就是这个返回的数据
        # return 'data'
        # return value
        pass

    def to_url(self, value):  # 一般不需要重写父类的to_url方法
        pass


# 2.将自定义的转换器添加到Flask的应用中
app.url_map.converters['re'] = RegexConverter


# 3.直接在路由中使用自定义的转换器
@app.route('/send/<re:mobile>')  # 普通的自定义转换器
# @app.route('/send/<re(r"1[34578]\d{9}"):mobile>')  # 设置万能转换器,参数正则表达式
def send_sms(mobile):
    print(mobile)
    return 'send sms to %s' %mobile  # 调用父类的to_python方法

@app.route('/index')
def index():
    url = url_for('index', mobile="18622223333")  # 调用父类的to_url方法
    return redirect(url)


if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序
