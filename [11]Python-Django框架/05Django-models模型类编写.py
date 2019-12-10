# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-09 15:24

### 数据库的配置: settings.py
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",  # 指定要连接的数据库的驱动程序
        "NAME": "你的数据库名称",              # 指定要连接到的数据库的名称,需要手动创建:
        "USER": "数据库用户名",                # 指定登录到数据库管理系统的用户名
        "PASSWORD": "数据库密码",              # 指定登录到数据库管理系统的密码
        "HOST": "数据库IP",                    # 指定要连接到的主机地址
        "POST": 3306                           # 指定端口号
    }
}
# 注:使用MySQL数据库时,需要在项目目录下的__init__py文件中添加以下内容:
# import pymysql
# pymysql.install_as_MySQLdb()

### 数据库的同步操作:
## python manage.py makemigrations  # 生成迁移文件
## python manage.py migrate         # 执行迁移文件

### 自定义模型管理器类:
class ModelClazzManager(models.Manager):
    # 应用1.改变原有查询的结果集: 如all()
    # 应用2.封装方法:用户操作模型类对应的数据表(增删改查)
    # self.model:获取self对象所在的模型类(即ModelClazz模型类)
    pass

### 模型类字段类型:
from django.db import models
class ModelClazz(models.Model):
    auto = models.AutoField(primary_key=True)  # 自增长字段，int型,必须填入参数 primary_key=True
    name = models.CharField(max_length=32)     # 字符类型，必须提供max_length参数， max_length表示字符长度
    id = models.IntegerField()  # 整数类型
    date1 = models.DateField(auto_now_add=True)  # 日期字段，日期格式  YYYY-MM-DD，相当于Python中的datetime.date()实例
    date2 = models.DateTimeField(auto_now=True)  # 日期时间字段，格式 YYYY-MM-DD HH:MM[:ss[.uuuuuu]][TZ]，相当于Python中的datetime.datetime()实例

    # 自定义一个模型器管理类对象
    objects = ModelClazzManager()
    
    class Meta:
        db_table = "addressinfo"            # 表的名称
        verbose_name = "省市县地址信息"     # admin后台信息显示
        verbose_name_plural = verbose_name  # 复数
        # ordering                          # 指定数据在后台管理中的排序方式，取值是一个列表，将排序的列表示在列表，默认升序，降序使用-


## 其他字段类型
# EmailField()  # 字符串类型，Django Admin以及ModelForm中提供验证机制
# BooleanField()  # 布尔值类型
# NullBooleanField()  # 可以为空的布尔值
# TextField()  # 文本类型
# GenericIPAddressField()  # 字符串类型，Django Admin以及ModelForm中提供验证 Ipv4和Ipv6
# URLField()  # 字符串类型，Django Admin以及ModelForm中提供验证 URL
# UUIDField()  # 字符串类型，Django Admin以及ModelForm中提供对UUID格式的验证
# FilePathField()  # 字符串，Django Admin以及ModelForm中提供读取文件夹下文件的功能
# FileField()  # 字符串，路径保存在数据库，文件上传到指定目录
# ImageField()  # 字符串，路径保存在数据库，文件上传到指定目录
# BinaryField()  # 二进制类型
# FloatField()  # 浮点型



### 模型类字段选项:
# primary_key  # 主键
# unique  # 如果设置为unique=True 则该字段在此表中必须是唯一的
# null  # 表示某个字段可以为空
# blank  # 提交表单可以为空，默认False，此参数为True，null参数必须为True
# choices  # 元组值，一个用来选择值的2维元组。第一个值是实际存储的值，第二个用来方便进行选择
# db_column  # 在数据库中的字段名称，默认和变量同名
# db_index  # 如果db_index=True 则代表着为此字段设置数据库索引
# default  # 为该字段设置默认值
# help_text  # 表单帮助信息
# verbose_name  # admin后台显示名称
# editable  # 该字段是否可编辑，默认为True
# auto_now_add  # 配置auto_now_add=True，创建数据记录的时候会把当前时间添加到数据库
# auto_now  # 配置上auto_now=True，每次更新数据记录的时候会更新该字段

#########################################################################################################################
# 一对多关系映射:
# 学生: 多
class Student(models.Model):  # 数据表: 应用名字_student, 即 app02_student
    s_name = models.CharField(max_length=32)
    s_age = models.IntegerField()
    grade = models.ForeignKey("Grade")
    # 此处关联的模型类最好加上单引或双引号,如果不加引号,且Grade模型类定义在后面,在生成迁移文件的时候会报错
# 班级: 一
class Grade(models.Model):  # 数据表: 应用名字_grade, 即 app02_grade
    g_name = models.CharField(max_length=32)

# 班级与学生是: 一对多的关系, 所以定义两者之间的关系需要在多(学生)的一方引用一(班级)的一方的主键为外键
# 即模型类: grade = models.ForeignKey('Grade')
# 即数据表: app02_student表中多了一个字段,字段名为: 关联属性_id  ---> grade_id


#########################################################################################################################

### 关系字段:
## OneToOneField: 一对一，将字段定义在任意一端中(Author,Wife)
# 属性 = models.ForeignKey(Entry)
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
# 属性 = models.ForeignKey(Entry)
# 示例: publisher = models.ForeignKey(Publisher)
# 正向查询: 通过Book查询Publisher
# book = Book.objects.get(id=1)
# publisher = book.publisher
# 反向查询: Django默认会在Publisher中增加book_set属性，来表示对应的所有书籍的查询对象
# pub = Publisher.objects.get(id=1)
# books = pub.book_set.all()

## ManyToManyField: 多对多，将字段定义在任意一端中(Author,Book)
# 属性 = models.ManyToManyField(Entry)
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



