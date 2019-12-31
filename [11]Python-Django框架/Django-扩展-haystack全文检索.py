# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-12 11:18

# haystack: 全文检索框架,支持whoosh、solr、Xapian、Elasticsearc四种全文检索引擎
# whoosh: 纯Python编写的全文搜索引擎，虽然性能比不上sphinx、xapian、Elasticsearc等，但是无二进制包，程序不会莫名其妙的崩溃，对于小型的站点，whoosh已经足够使用
# jieba: 一款免费的中文分词包
# 流程: 用户 ---> 全文检索框架(haystack) ---> 搜索引擎(whoosh)

### haystack全文检索框架的使用步骤:
## 一. 安装与配置
# 1.1在虚拟环境依次安装模块包
# pip install django-haystack
# pip install whoosh
# pip install jieb

## 1.2在项目的settings中注册haystack应用,如:
# INSTALLED_APPS = [
#     ...,
#     'haystack',
# ]

## 1.3在项目的settings中配置搜索引擎,如
# 全文检索框架的配置
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎: 位置,虚拟环境名称/lib/python3.x/site-packages/haystack/backends/
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',  # 默认的whoosh搜索引擎默认配置
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 当添加、修改、删除数据时，自动生成索引文件
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'

## 二. 生成索引文件: 即对表中的某些字段进行关键词分析,建立关键词对应的索引数据
# 2.1在app应用下建立一个search_indexes.py文件,在其中定义一个模型索引类,如: 建立goods应用下的GoodsSKU模型类的索引类
from haystack import indexes  # 定义索引类
from goods.models import GoodsSKU  # 导入你的模型类
# 指定对于某个类的某些数据建立索引
# 索引类名格式: 模型类名 + Index
class GoodsSKUIndex(indexes.SearchIndex, indexes.Indexable):
    # 索引字段 use_template=True 指定根据表中的哪些字段建立索引文件,把说明放在一个文件中
    text = indexes.CharField(document=True, use_template=True)
    def get_model(self):
        # 返回你的模型类
        return GoodsSKU
    # 建立索引的数据
    def index_queryset(self, using=None):
        return self.get_model().objects.all()  # 此处表示所有数据

# 2.2在templates模版目录下建立目录,如 templates/search/indexes/goods/goodssuk_text.txt
# 注: search/indexes两个目录是固定写法,goods表示之前定义的模型类的索引类所在app应用的名字
# 注: 文件名称为之前定义的模型类名字的小写 + _text.txt
# goodssuk_text.txt文件中指定根据表中的哪些字段建立索引
{{ object.name }}  # 根据商品的名称建立索引
{{ object.desc }}  # 根据商品的简介建立索引
{{ object.goods.detail }}  # 根据商品的详情建立索引

# 2.3使用命令生成索引文件
# python manage.py rebuild_index
# 注: 此时建立好的索引文件就存放在上述第三步settings中配置的whoosh_index目录下

## 三. 全文检索的使用
# 3.1在项目的urls中添加搜索的配置,如
urlpatterns = [
    url(r'^search/', include('haystack.urls')),
]

# 3.2表单的搜索框设置为form表单,如
# <form method = "get" action = "/search" >
#     <input type="text" class="input_text fl" name="q" placeholder="搜索商品" >
#     <input type="submit" class="input_btn fr" name="" value="搜索" >
# </form>
# 注: form表单的method必须为get方式,搜索框的name属性值必须为q, form表单的action需要与项目的urls路由设置的一致

# 3.3在templates/search/下创建search.html文件,如 templates/search/search.html
# 此时启动项目进行搜索,程序报错,说找不到search.html文件, 所以需要创建search.html文件
# 注: 再次启动项目进行搜索会给search.html模型传递几个变量,如:
# query: 搜索关键字
# page: 当前页的page对象 ->遍历page对象，获取到的是SearchResult类的实例对象，对象的属性object才是模型类的对象。
# paginator: 分页paginator对象
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2  # 指定搜索结果每页的显示数据条数(在settings中进行配置)
# 示例如下:
# {% extends 'base_detail_list.html' %}
# {% block title %}搜索结果列表{% endblock title %}
# {% block main_content %}
# 	<div class="breadcrumb">
# 		<a href="#">{{ query }}</a>
# 		<span>></span>
# 		<a href="#">搜索结果如下:</a>
# 	</div>
# 	<div class="main_wrap clearfix">
#         <ul class="goods_type_list clearfix">
#             {% for item in page %}
#             <li>
#                 <a href="{% url 'goods:detail' item.object.id %}"><img src="{{ item.object.image.url }}"></a>
#                 <h4><a href="{% url 'goods:detail' item.object.id %}">{{ item.object.name }}</a></h4>
#                 <div class="operate">
#                     <span class="prize">￥{{ item.object.price }}</span>
#                     <span class="unit">{{ item.object.price}}/{{ item.object.unite }}</span>
#                     <a href="#" class="add_goods" title="加入购物车"></a>
#                 </div>
#             </li>
#             {% endfor %}
#         </ul>
#         <div class="pagenation">
#                 {% if page.has_previous %}
# 				<a href="/search?q={{ query }}&page={{ page.previous_page_number }}"><上一页</a>
#                 {% endif %}
#                 {% for pindex in paginator.page_range %}
#                     {% if pindex == page.number %}
# 				        <a href="/search?q={{ query }}&page={{ pindex }}" class="active">{{ pindex }}</a>
#                     {% else %}
# 				        <a href="/search?q={{ query }}&page={{ pindex }}">{{ pindex }}</a>
#                     {% endif %}
# 				{% endfor %}
#                 {% if spage.has_next %}
# 				<a href="/search?q={{ query }}&page={{ page.next_page_number }}">下一页></a>
#                 {% endif %}
# 			</div>
# 	</div>
# {% endblock main_content %}


## 四. 改变分词方式: 如 jiebe中文分词包
# 4.1.在虚拟环境中安装分词模块: pip install jieba
# 4.2.进入到安装haystack模块目录下: 如 虚拟环境名称/lib/python3.x/site-packages/haystack/backends/
# 4.3.在上述目录下创建ChineseAnalyzer.py文件,添加如下内容
import jieba
from whoosh.analysis import Tokenizer, Token
class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode, **kwargs)
        seglist = jieba.cut(value, cut_all=True)  # 对一个语句进行中文分词处理
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t

def ChineseAnalyzer():
    return ChineseTokenizer()

# 4.4复制虚拟环境目录下的 /lib/python3.x/site-packages/haystack/backends/whoosh_backend.py文件，改为如下名称
# whoosh_cn_backend.py  # 即 虚拟环境/lib/python3.x/site-packages/haystack/backends/whoosh_cn_backend.py
# 4.5编辑复制出来的新文件whoosh_cn_backend.py,引入中文分析类,内部采用jieba分词,并修改内容,如下
# from .ChineseAnalyzer import ChineseAnalyzer
# 更改词语分析类
# 查找: analyzer=StemmingAnalyzer()
# 改为: analyzer=ChineseAnalyzer()
# 4.6修改settings.py文件中的搜索引擎配置项,如
HAYSTACK_CONNECTIONS = {
    'default': {
        # 使用whoosh引擎: 位置,虚拟环境名称/lib/python3.x/site-packages/haystack/backends/
        #'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',  # 默认的whoosh搜索引擎默认配置
        'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 4.7重新生成索引文件
# 执行命令: python manage.py rebuild_index


