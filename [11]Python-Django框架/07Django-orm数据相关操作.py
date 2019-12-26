# -*- coding:utf-8 -*-
# @Desc : 模型类的CRUD操作
# @Author : Administrator
# @Date : 2019-07-15 15:31

### 增加数据操作 ###
## 1. Entity.objects.create(属性=值,属性=值)  # 返回值：创建好的实体对象
## 2. 创建一个 Entity 对象，并通过 save() 进行保存
# obj = Entity(属性=值,属性=值)
# obj.属性 = 值
# obj.save()
## 3. 使用字典构建对象，并通过 save() 进行保存
# dic = {
#     '属性1':'值1',
#     '属性2':'值2',
# }
# obj=Entity(**dic)
# obj.save()



### 修改数据操作 ###
## 修改单个实体:
# 1.查: 通过 get() 得到要修改的实体对象
# 2.改: 通过对象的属性修改对象的值
# 3.保存: 通过对象的 save() 保存回数据库
## 批量修改数据:
# 调用QuerySet的update(属性=值,属性=值)实现批量修改



### 删除数据操作 ###
## 删除单个对象:
# au = Author.objects.get(id=1)
# au.delete()
## 删除多个对象:
# auList = Author.objects.filter(isActive=False)
# auList.delete()



### 查询数据操作 ###
## 查询所有数据: all()
# Entity.objects.all()  # 返回值：QuerySet(查询结果集,是一个封装了若干对象的列表)

## 只查询一条数据: get(条件)
# Entity.objects.get(条件)
# 注: 该方法只能查询一条数据,查询多于一条数据或没查询出结果的话那么都会抛异常

## 查询返回指定列: values() 与 values('列1','列2',...)
# 作用: 查询一个QuerySet中的部分列，并封装成字典，再放到列表中
# Entity.objects.values()
# Entity.objects.values('列1','列2')
# Entity.objects.all().values()
# Entity.objects.filter().values()

## 查询返回指定列: values_list() 与 values_list('列1','列2')
# 作用: 查询一个QuerySet中的部分列，并封装成元组，再放到列表中
# Entity.objects.values_list()
# Entity.objects.values_list('列1','列2')
# Entity.objects.all().values_list()
# Entity.objects.filter().values_list()

# 总结: values()和values_list()里面写什么字段,就相当于select查询什么字段

## 根据条件查询部分行数据: filter(条件)
# 语法: Entity.objects.filter(条件)
# 1.构建等值条件:
# 示例: Author.objects.filter(id=1)
# 示例: Author.objects.filter(id=1,name='隔壁老王')
# 2.构建不等值条件: __gt, __lt, __contains,__startswith,__endswith, __in, __range, __date, ...
# Entity.objects.filter(属性__查询谓词=值)
# 即: ### 单表查询的双下划线操作 ###
# 示例: Entity.objects.filter(id__gt=5)              # 获取id大于5的数据
# 示例: Entity.objects.filter(id__lt=10, id__gt=1)   # 获取id大于1 且 小于10的数据
# 示例: Entity.objects.filter(id__in=[11, 22, 33])   # 获取id等于11、22、33的数据
# 示例: Entity.objects.exclude(id__in=[11, 22, 33])  # not in
# 示例: Entity.objects.filter(name__contains="ven")  # 获取name字段包含"ven"的
# 示例: Entity.objects.filter(id__range=[1, 3])      # id范围是1到3的，等价于SQL的bettwen and

## 对条件取反: exclude(条件)
# Entity.objects.exclude(条件)
# 示例: Author.objects.exclude(id=1)             # select * from index_author where not(id=1)
# 示例: Author.objects.exclude(id=1,age__lt=30)  # select * from index_author where  not (id=1 and age < 30)

## 排序查询: order_by()
# Entity.objects.order_by('列1','-列2')
# 注: 默认是升序排序，列名前加 - 则表示降序排序

## reverse()  # 对查询结果反向排序,通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)
## distinct()  # 从返回结果中剔除重复纪录(注意只有在PostgreSQL中支持按字段去重)
## count()  # 返回数据库中匹配查询(QuerySet)的对象数量。
## first()  # 返回第一条记录
## last()  # 返回最后一条记录
## exists()  # 如果QuerySet包含数据，就返回True，否则返回False


### 基本查询方法总结:
## 返回QuerySet对象的方法: all(), filter(), exclude(), order_by(), reverse(), distinct()
## 返回特殊的QuerySet对象的方法有:
# values()      返回一个可迭代的字典序列
# values_list() 返回一个可迭代的元祖序列
## 返回具体对象的方法: get(), first(), last()
## 返回布尔值的方法：exists()
## 返回数值的方法: count()


## 聚合函数：
# 1.Avg():   平均值
# 2.Count(): 数量
# 3.Sum():   求和
# 4.Min():   最小值
# 5.Max():   最大值

## 聚合查询(不带分组): aggregate()
# Entity.objects.all().aggregate(别名=聚合函数('列'))
# 示例: Author.objects.all().aggregate(avg=Avg('age'))
# 示例: Book.objects.aggregate(average_price=Avg('price'))

## 聚合查询(带分组): annotate() ---> annotate()前面的values("列1","列2")表示按照哪个列进行分组
# Entity.objects.all().values('分组列1','分组列2').annotate(别名=聚合函数('列')).values('查询列1','查询列2','查询列3')
# Entity.objects.filter(条件).values('分组列').annotate(别名=聚合函数('列')).filter(条件)
# 示例: Employee.objects.values("dept").annotate(avg=Avg("salary").values(dept, "avg")


### ForeignKey数据操作 ###



### F 查询和 Q 查询 ###
## F(): 在执行中获取某列的值
# from django.db.models import F
# 示例: Author.objects.all().update(age=F('age')+10)  # update author set age=age+10
# 示例: Book.objects.filter(commnet_num__gt=F('keep_num'))
## Q(): 在查询条件中可以完成 |（OR）和 &（AND）操作
# from django.db.models import Q
# 示例: Author.objects.filter(Q(id=1)|Q(age=48))  # select * from author where id=1 or age=48
# 示例: Book.objects.filter(Q(authors__name="小仙女")|Q(authors__name="小魔女"))


### 原生的数据库操作方法 ###
## 查询: raw(sql语句)
# Entity.objects.raw(sql)  ---> 返回: QuerySet
## 增删改: connection.cursor().execute(sql语句)
from django.db import connection
def doSQL(request):
    with connection.cursor() as cursor:
        sql = 'delete from ...'
        cursor.execute(sql)
        return ''


### 关系字段:
## OneToOneField: 一对一，将字段定义在任意一端中(Author,Wife)
# 属性 = models.ForeignKey(Entity)
# 示例: author = models.OneToOneField(Author)
# 数据库中: 在Wife对应表中(wife)生成一个外键(author_id),引用自Author对应表(author)的主键
# 在Author模型类中: 会增加一个隐式属性叫wife
# 正向查询: 直接通过关联属性查询即可(通过 wife 找 author)
# wife = Wife.objects.get(id=1)
# author = wife.author
# 反向查询: 通过反向引用属性查询(通过 author 找 wife)
# author = Author.objects.get(id=1)
# wife = author.wife

## ForeignKey: 一对多，将字段定义在多的一端端中(Publisher,Book)
# 属性 = models.ForeignKey(Entity)
# 示例: publisher = models.ForeignKey(Publisher)
# 正向查询: 通过Book查询Publisher
# book = Book.objects.get(id=1)
# publisher = book.publisher
# 反向查询: Django默认会在Publisher中增加book_set属性，来表示对应的所有书籍的查询对象
# pub = Publisher.objects.get(id=1)
# books = pub.book_set.all()

## ManyToManyField: 多对多，将字段定义在任意一端中(Author,Book)
# 属性 = models.ManyToManyField(Entity)
# 示例: authors = models.ManyToManyField(Author)


### ForeignKey操作:
## 正向查找: 对象查找(跨表)  ---> 对象.关联字段.字段
# book_obj = Book.objects.first()   # 第一本书对象
# book_obj.publisher                # 获取这本书关联的出版社的对象
# book_obj.publisher.name           # 获取这本书关联的出版社的名称
## 正向查找: 字段查找(跨表) ---> 关联字段__字段
# Book.objects.values_list("publisher__name")

## 反向查找: 对象查找(跨表)  ---> obj.表名_set
# publisher_obj = Publisher.objects.first()     # 第一个出版社对象
# books = publisher_obj.book_set.all()          # 获取这个出版社出版过的所有书的对象
# titles = books.values_list("title")           # 再获取这个出版社出版过的所有书的书名
## 反向查找: 字段查找(跨表) ---> 表名__字段
# titles = Publisher.objects.values_list("book__title")


########################################################################################
### 一般操作: 必知必会13条
# all():         查询所有结果
# filter():      它包含了与所给筛选条件相匹配的对象
# get():         返回与所给筛选条件相匹配的对象，返回结果有且只有一个，如果超过一个或者没有都会抛出错误。
# exclude():     它包含了与所给筛选条件不匹配的对象
# values():      返回一个特殊的QuerySet，并不是一系列model的实例化对象，而是一个可迭代的字典序列
# values_list(): 它与values()非常相似，它返回的是一个元组序列，values返回的是一个字典序列
# order_by():    对查询结果排序
# reverse():     对查询结果反向排序，请注意reverse()通常只能在具有已定义顺序的QuerySet上调用(在model类的Meta中指定ordering或调用order_by()方法)。
# distinct():    从返回结果中剔除重复纪录(如果你查询跨越多个表，可能在计算QuerySet时得到重复的结果。此时可以使用distinct()，注意只有在PostgreSQL中支持按字段去重。)
# count():       返回数据库中匹配查询(QuerySet)的对象数量。
# first():       返回第一条记录
# last():        返回最后一条记录
# exists():      如果QuerySet包含数据，就返回True，否则返回False


### 返回QuerySet对象的方法有: all(), filter(), exclude(), order_by(), reverse(), distinct()
### 返回特殊的QuerySet对象的方法有:
# values()      返回一个可迭代的字典序列
# values_list() 返回一个可迭代的元祖序列
### 返回具体对象的方法: get(), first(), last()
### 返回布尔值的方法：exists()
### 返回数字的方法: count()



### 模型关系与级联操作:
## 主表-从表:
# 关系声明在哪个模型类中,此模型对应的表就是从表,反之就是主表
## 级联操作:
# 主表查从表,隐式属性 模型类_set
# 从表查主表,显示属性 设置的属性


