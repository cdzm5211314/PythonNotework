### Django框架的内置分页功能:
```
### 使用Django框架内置分页器Paginator封装分页实现:
## Paginator分页器对象属性:
# Paginator分页器对象: paginator = Paginator(all_data,num_page)  # all_data数据集,num_page每一页的数据数
# 返回总数量: paginator.count  # 对象总数
# 返回总页数: paginator.num_pages  # 页码总数
# 返回页码列表(即显示页码数): paginator.page_range  # 页码列表,从1开始,如[1,2,3,4,5,...]
# 返回Page对象(即根据页码数值获取第几分页对象): pages = paginator.page(num)  # 如:第一分页的对象paginator.page(1)   第二分页的对象paginator.page(2)

## Page分页对象的属性与方法: 整数,具体的某一个页面
# 分页对象属性(即当前page对象关联的Pagintor对象): paginator 
# 当前页面上的所有数据: object_list
# 当前页的页码值(即第几分页的当前页码值)属性: pages.number
# 是否有上一页: pages.has_previous()
# 上一页的页码: pages.previous_page_number()
# 是否有下一页: pages.has_next()
# 下一页的页码: pages.next_page_number()
# 是否有上一页或下一页: pages.has_other_pages()
# 返回当前页起始的对象序号: pages.start_index()
# 返回当前页结束的对象序号: pages.end_index()

## 视图:views.py
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
## 分页函数: views.py
def paging(request):
    page_num = request.GET.get('page_num',defaule=1)  # 获取url传递过来的页码数值,默认值为1,可自定义
    all_data = Entity.objects.all()  # 数据查询结果集
    paginator = Paginator(all_data,3)  # 创建分页对象,设置每页显示几条数据
    try:
        pages = paginator.page(page_num)  # 获取页码值对应的分页对象
    except PageNotAnInteger:  # 页码不是整数时引发该异常
        pages = paginator.page(1)  # 获取第一页数据返回
    except EmptyPage:  # 页码不在有效范围时(即数据为空,或参数页码值大于或小于页码范围)引发该异常
        # pages = paginator.page(paginator.num_pages)
        if int(page_num) > paginator.num_pages:
            # 参数页码值大于总页码数: 获取最后一页数据返回
            pages = paginator.page(paginator.num_pages)
        else:
        # 参数页码值小于最小页码数: 获取第一页数据返回
            pages = paginator.page(1)

    ## 这部分是为了当有大量数据时,保证所显示的页码数量不超过10
    if page_num < 6:
        if paginator.num_pages <= 10:
            dis_range = range(1, paginator.num_pages + 1)
        else:
            dis_range = range(1, 11)
    elif (page_num >= 6) and (page_num <= paginator.num_pages - 5):
        dis_range = range(page_num - 5, page_num + 5)
    else:
        dis_range = range(paginator.num_pages - 9, paginator.num_pages + 1)

    return render(request,'papgin.html',{'pages':pages,'dis_range': dis_range})


## 模版:templates
# {# 分页显示 #}
# {# 是否有上一页,有就获取上一页的页码值 #}
# {% if pages.has_previous %}
#   <li class="long"><a href="?page_num={{ pages.previous_page_number }} ">上一页</a></li>
# {% endif %}
#
# {# 所有页码值 #}
# {% for num in pages.paginator.page_range %}
#   {# 选中当前页码进行标识 #}
#   <li {% if num == pages.number %} class="active" {% endif %} ><a href="?page_num={{ num }}">{{ num }}</a></li>
# {% endfor %}
#
# {# 是否有下一页,有就获取下一页的页码值 #}
# {% if pages.has_next %}
#   <li class="long"><a href="?page_num={{ pages.next_page_number }}">下一页</a></li>
# {% endif %}
```

##############################################################################################################
### 不使用Django框架内置分页器封装分页类实现
```
分页显示封装类: mypage.py
class Page():
    def __init__(self, page_num, total_count, url_prefix, per_page=10, max_page=11):
        """
        :param page_num: 当前页码数
        :param total_count: 总数据
        :param url_prefix: a标签href的前缀
        :param per_page: 每页显示多少条数据
        :param max_page: 页面最多显示页码数
        """
        self.url_prefix = url_prefix
        self.max_page = max_page
        # 每一页显示多少条数据
        # 总共需要多少页码来展示
        total_page, m = divmod(total_count, per_page)
        if m:
            total_page += 1
        self.total_page = total_page

        try:
            page_num = int(page_num)
            # 如果输入的页码数超过了最大的页码数，默认返回最后一页
            if page_num > total_page:
                page_num = total_page
        except Exception as e:
            # 当输入的页码不是正经数字的时候 默认返回第一页的数据
            page_num = 1
        self.page_num = page_num

        # 定义两个变量保存数据从哪儿取到哪儿
        self.data_start = (page_num - 1) * 10
        self.data_end = page_num * 10

        # 页面上总共展示多少页码
        if total_page < self.max_page:
            self.max_page = total_page

        half_max_page = self.max_page // 2
        # 页面上展示的页码从哪儿开始
        page_start = page_num - half_max_page
        # 页面上展示的页码到哪儿结束
        page_end = page_num + half_max_page
        # 如果当前页减一半 比1还小
        if page_start <= 1:
            page_start = 1
            page_end = self.max_page
        # 如果 当前页 加 一半 比总页码数还大
        if page_end >= total_page:
            page_end = total_page
            page_start = total_page - self.max_page + 1
        self.page_start = page_start
        self.page_end = page_end

    @property
    def start(self):
        return self.data_start

    @property
    def end(self):
        return self.data_end

    def page_html(self):
        # 自己拼接分页的HTML代码
        html_str_list = []
        # 加上第一页
        html_str_list.append('<li><a href="{}?page=1">首页</a></li>'.format( self.url_prefix))
        # 判断一下 如果是第一页，就没有上一页
        if self.page_num <= 1:
            html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(self.page_num-1))
        else:
            # 加一个上一页的标签
            html_str_list.append('<li><a href="{}?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format( self.url_prefix, self.page_num-1))
        for i in range(self.page_start, self.page_end+1):
            # 如果是当前页就加一个active样式类
            if i == self.page_num:
                tmp = '<li class="active"><a href="{0}?page={1}">{1}</a></li>'.format(self.url_prefix, i)
            else:
                tmp = '<li><a href="{0}?page={1}">{1}</a></li>'.format( self.url_prefix, i)
            html_str_list.append(tmp)

        # 加一个下一页的按钮
        # 判断，如果是最后一页，就没有下一页
        if self.page_num >= self.total_page:
            html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
        else:
            html_str_list.append('<li><a href="{}?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format( self.url_prefix, self.page_num+1))
        # 加最后一页
        html_str_list.append('<li><a href="{}?page={}">尾页</a></li>'.format( self.url_prefix, self.total_page))

        page_html = "".join(html_str_list)
        return page_html


### 代码测试: views.py
from django.shortcuts import render
## 分页显示测试代码1
def books(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Book.objects.all().count()
    # 导入分页显示封装类进行测试测试
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/books/", max_page=9,)
    ret = models.Book.objects.all()[page_obj.start:page_obj.end]
    page_html = page_obj.page_html()
    return render(request, "books.html", {"books": ret, "page_html": page_html})


## 分页显示测试代码2
def depts(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Dept.objects.all().count()
	# 导入分页显示封装类进行测试测试
    from utils.mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/depts/", max_page=11, )
    ret = models.Dept.objects.all()[page_obj.start:page_obj.end]
    print(ret)
    page_html = page_obj.page_html()
    return render(request, "dept.html", {"depts": ret, "page_html": page_html})		
```
		
### 原始分页显示
```
# 每一页显示多少条数据
per_page = 10
# 总共需要多少页码来展示
total_page, m = divmod(total_count, per_page)
if m:
    total_page += 1
try:
    page_num = int(page_num)
    # 如果输入的页码数超过了最大的页码数，默认返回最后一页
    if page_num > total_page:
        page_num = total_page
except Exception as e:
    # 当输入的页码不是正经数字的时候 默认返回第一页的数据
    page_num = 1

# 定义两个变量保存数据从哪儿取到哪儿
data_start = (page_num-1)*10
data_end = page_num*10

# 页面上总共展示多少页码
max_page = 11
if total_page < max_page:
    max_page = total_page

half_max_page = max_page // 2
# 页面上展示的页码从哪儿开始
page_start = page_num - half_max_page
# 页面上展示的页码到哪儿结束
page_end = page_num + half_max_page
# 如果当前页减一半 比1还小
if page_start <= 1:
    page_start = 1
    page_end = max_page
# 如果 当前页 加 一半 比总页码数还大
if page_end >= total_page:
    page_end = total_page
    page_start = total_page - max_page +1

all_book = models.Book.objects.all()[data_start:data_end]
# 自己拼接分页的HTML代码
html_str_list = []
# 加上第一页
html_str_list.append('<li><a href="/books/?page=1">首页</a></li>')

# 判断一下 如果是第一页，就没有上一页
if page_num <= 1:
    html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))
else:
    # 加一个上一页的标签
    html_str_list.append('<li><a href="/books/?page={}"><span aria-hidden="true">&laquo;</span></a></li>'.format(page_num-1))

for i in range(page_start, page_end+1):
    # 如果是当前页就加一个active样式类
    if i == page_num:
        tmp = '<li class="active"><a href="/books/?page={0}">{0}</a></li>'.format(i)
    else:
        tmp = '<li><a href="/books/?page={0}">{0}</a></li>'.format(i)

    html_str_list.append(tmp)

# 加一个下一页的按钮
# 判断，如果是最后一页，就没有下一页
if page_num >= total_page:
    html_str_list.append('<li class="disabled"><a href="#"><span aria-hidden="true">&raquo;</span></a></li>')
else:
    html_str_list.append('<li><a href="/books/?page={}"><span aria-hidden="true">&raquo;</span></a></li>'.format(page_num+1))
# 加最后一页
html_str_list.append('<li><a href="/books/?page={}">尾页</a></li>'.format(total_page))
page_html = "".join(html_str_list)
```

