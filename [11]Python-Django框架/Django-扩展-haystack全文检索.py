# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-12 11:18

### Django全文搜索类库:
# django-haystack(容器): 支持whoosh、solr、Xapian、Elasticsearc四种检索引擎
# whoosh(具体搜索引擎): 纯Python编写的全文搜索引擎,虽然性能比不上sphinx、xapian、Elasticsearc等,但是无二进制包,程序不会莫名其妙的崩溃,对于小型的站点,whoosh已经足够使用
# jieba: 一款免费的中文分词包, pip install jieb


## 检索流程: 用户 ---> 全文检索框架(haystack) ---> 搜索引擎(whoosh)

### Django项目全文检索实现步骤:
## 1.安装模块
# pip install django-haystack
# pip install whoosh

## 2.在settings.py文件中添加应用,如: haystack
INSTALLED_APPS = [
    'haystack',  # 注: 需要加在所有的自定义APP应用前面
]

## 3.在项settings.py文件中配置生成索引文件路径,如
HAYSTACK_CONNECTIONS = {
    'default': {
        # whoosh默认搜索引擎默认配置
        'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 指定生成的索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}
# 3.1对搜索结果进行分页(默认为20),设置每页显示结果为10
HAYSTACK_SEARCH_RESULTS_PER_PAGE = 10
# 3.2当添加、修改、删除数据时,自动生成索引文件
HAYSTACK_SIGNAL_PROCESSOR = 'haystack.signals.RealtimeSignalProcessor'


## 4.在APP应用包下创建search_indexes.py文件,如
# 定义模型索引类: 模型类名 + Index
# 指定对于某个模型类的某些数据建立索引
from haystack import indexes  # 定义索引类
from .models import Post      # 导入模型类
# 模型索引类格式: 模型类名 + Index
class PostIndex(indexes.SearchIndex, indexes.Indexable):
    # document=True,每个索引里面有且只有一个,haystack和搜索引擎使用此字段的内容作为索引进行检索
    # use_template=True,允许使用数据模板去建立搜索引擎索引的文件,即索引里面存放了模型类的哪些字段属性
    text = indexes.CharField(document=True, use_template=True)  # 可以当做默认设置

    # 给模型类的的哪些字段设置索引
    # title,content代表全文搜索框的字段名称
    # model_attr选项对应了模型类的字段属性
    title = indexes.NgramField(model_attr='title')
    content = indexes.NgramField(model_attr='content')

    # 重写父类方法,根据哪个模型类属性字段搜索,就返回哪个模型类
    def get_model(self):
        return Post  # 搜索的模型类

    def index_queryset(self, using=None):
        return self.get_model().objects.all()  # 此处表示所有数据

## 5.在项目的templates目录下创建搜索引擎模版:
# 如: project/templates/search/indexes/APP应用名称/模型类名小写_text.txt
# 即: project/templates/search/indexes/post/post_text.txt
# 注: search/indexes两个目录是固定写法
# 注: post表示之前定义的模型索引类所在app应用的名字
# 注: post_text.txt中的post表示建立索引的模型类的小写名称
# 5.1 编辑post_text.txt文件,指定根据表中的哪些字段建立索引
{{ object.title }}      # object表示检索的Post模型类对象,title为模型字段属性
{{ object.content }}    # object表示检索的Post模型类对象,title为模型字段属性

## 6.执行命令生成索引文件,在settings.py文件设置过PATH路径
# python manage.py rebuild_index
# 注: 生成的索引文件就在项目根目录的whoosh_index目录中: 即 project/whoosh_index/*

## 7.编辑搜索框请求信息: form表单
<form method = "get" action = "/search/" >
    <input type="text" name="q" placeholder="搜索" >
</form>
# 注: 必须为get请求方式,搜索框的name属性值必须为q,action属性值与项目的url路由需要一致

## 8.在urls.py根路由文件中配置搜索URL路由,如
# 注: 需要跟搜素框form表单的action属性值一致
urlpatterns = [
    url(r'search/', include('haystack.urls')),
]

## 9.在项目的templates/search目录下创建html文件: 如 project/templates/search/search.html
# Djang项目启动时会查找search.html文件,如果查找不到就会报错
# 注: 在项目启动后进行全文检索时会给search.html传递几个变量,如
# query: 搜索关键字,可用于判断是否有搜索结果
# page: 当前页对象page ---> 遍历page对象,获取到的是SearchResult类的实例对象,对象的属性object才是模型类的对象
# 即: 模型类对象_list = [ result.object for result in page.object_list ]
# paginator: 分页器对象paginator
# HAYSTACK_SEARCH_RESULTS_PER_PAGE = 2  # 指定搜索结果每页的显示数据条数(在settings中进行配置)

# 示例如下:
# {% extends 'base.html' %}
# {% block title %}
#     搜索结果列表
# {% endblock %}
# {% block left %}
#     <div id="main">
#         <div class="archives">
#             {% if query %}
#                 {% for searchResult in page.object_list %}

#                     <article class="archive-article archive-type-post">
#                         <div class="archive-article-inner">
#                             <header class="archive-article-header">
#                                 <a href="#" class="archive-article-date">
#                                     <time>{{ searchResult.object.created|date:'Y-m' }}</time>
#                                 </a>
#                                 <h1 itemprop="name">
#                                     <a class="archive-article-title" target="_blank"
#                                        href="/post/{{ searchResult.object.id }}">{{ searchResult.object.title }}</a>
#                                 </h1>
#                             </header>
#                         </div>
#                     </article>

#                    <div class="pagenation">
#                        {% if page.has_previous %}
#                            <a href="/search?q={{ query }}&page={{ page.previous_page_number }}">上一页</a>
#                        {% endif %}
#                        {% for pindex in paginator.page_range %}
#                            {% if pindex == page.number %}
#                                <a href="/search?q={{ query }}&page={{ pindex }}" class="active">{{ pindex }}</a>
#                            {% else %}
#                                <a href="/search?q={{ query }}&page={{ pindex }}">{{ pindex }}</a>
#                            {% endif %}
#                        {% endfor %}
#                        {% if spage.has_next %}
#                            <a href="/search?q={{ query }}&page={{ page.next_page_number }}">下一页</a>
#                        {% endif %}
#                    </div>

#                 {% empty %}
#                     未搜索到数据...
#                 {% endfor %}
#             {% endif %}

#         </div>
#     </div>
# {% endblock %}


# 如上方式无法使用中文进行搜索
## 10.改变分词方式: 如 jiebe中文分词包
# 10.1安装: pip install jieba
# 10.2在App应用包下创建tokenizer.py文件,添加如下内容
import jieba
from whoosh.analysis import Tokenizer, Token
class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):

        t = Token(positions, chars, removestops=removestops, mode=mode,
                  **kwargs)
        seglist = jieba.cut(value, cut_all=False)  # 精确模式: 使用结巴分词库进行分词
        # seglist = jieba.cut_for_search(value)    # 搜索引擎模式: 使用结巴分词库进行分词
        for w in seglist:
            t.original = t.text = w
            t.boost = 1.0
            if positions:
                t.pos = start_pos + value.find(w)
            if chars:
                t.startchar = start_char + value.find(w)
                t.endchar = start_char + value.find(w) + len(w)
            yield t  # 通过生成器返回每个分词的结果token
def ChineseAnalyzer():
    return ChineseTokenizer()

# 10.3进入到安装了全文检索工具包的虚拟环境中:
# 先复制,即: 虚拟环境名称\Lib\site-packages\haystack\backends\whoosh_backend.py
# 后拷贝,即: 项目根目录\APP应用包目录\whoosh_backend.py
# 再改名,即: 项目根目录\APP应用包目录\whoosh_cn_backend.py
# 最后编辑whoosh_cn_backend.py,添加如下内容
# 搜索[132行]build_schema函数,修改else下内容[162行]:
else:
    from 应用名称.tokenizer import ChineseAnalyzer  # 导入中文分析器
    schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer(),
                                                  field_boost=field_class.boost, sortable=True)

# 10.2与10.3也可以进行如下操作:
# 创建文件: 在虚拟环境名称/lib/python3.x/site-packages/haystack/backends/目录下创建tokenizer.py文件
# 文件内容: 如下
import jieba
from whoosh.analysis import Tokenizer, Token
class ChineseTokenizer(Tokenizer):
    def __call__(self, value, positions=False, chars=False,
                 keeporiginal=False, removestops=True,
                 start_pos=0, start_char=0, mode='', **kwargs):
        t = Token(positions, chars, removestops=removestops, mode=mode, **kwargs)
        seglist = jieba.cut(value, cut_all=False)  # 精确模式: 使用结巴分词库进行分词
        # seglist = jieba.cut_for_search(value)    # 搜索引擎模式: 使用结巴分词库进行分词
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
# 先复制,即: 虚拟环境名称\Lib\site-packages\haystack\backends\whoosh_backend.py
# 后改名,即: 虚拟环境名称\Lib\site-packages\haystack\backends\whoosh_cn_backend.py
# 最后编辑whoosh_cn_backend.py,添加如下内容
# 搜索[132行]build_schema函数,修改else下内容[162行]:
else:
    from .tokenizer import ChineseAnalyzer  # 导入中文分析器
    schema_fields[field_class.index_fieldname] = TEXT(stored=True, analyzer=ChineseAnalyzer(),
                                                  field_boost=field_class.boost, sortable=True)

## 11.在settings.py文件中的搜索引擎配置项,如
HAYSTACK_CONNECTIONS = {
    'default': {
        # whoosh默认搜索引擎默认配置
        # 'ENGINE': 'haystack.backends.whoosh_backend.WhooshEngine',
        # 使用中文分词引擎,文件在APP应用目录下
        'ENGINE': 'post.whoosh_cn_backend.WhooshEngine',
        # # 使用中文分词引擎,文件在Python虚拟环境的安装库目录下
        # 'ENGINE': 'haystack.backends.whoosh_cn_backend.WhooshEngine',
        # 索引文件路径
        'PATH': os.path.join(BASE_DIR, 'whoosh_index'),
    }
}

## 12.重新生成索引文件:
# 执行命令: python manage.py rebuild_index


