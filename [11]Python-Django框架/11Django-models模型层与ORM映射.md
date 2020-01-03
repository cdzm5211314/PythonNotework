### Django框架的模型层: models
* 模型字段类型: models.字段类型()
    ```
    # 自增长字段,int类型:
        AutoField:
        BigAutoField:
    # 字符串类型:
        CharField: 字符串类型字段
        TextField: 文本字段
    # 布尔型:
        BooleanField: 不允许为空
        NullBooleanField: 允许为空
    # 二进制数据
        BinaryField:
    # 日期时间:
        DateField: # 年月日
        DateTimeField: # 年月日时分秒
    # 整型:
        SmallIntegerField: 6个字节整数
        IntegerField: 11个字节整数
        BigIntegerField: 20个字节整数
        PositiveSmallIntegerField: 5个字节正整数
        PositiveIntegerField: 10个字节正整数
    # 浮点型:
        FloatField: 
        DecimalField: 
    # 其他类型:
        UUIDField: uuid为通用唯一标识符
        ImageField: 图片字段(保存和处理上传的图片),依赖宇Pillow组件
        FileField: 文件字段(保存和处理上传的文件),Imagefield继承于FileField
        FilePathField: 文件路径字段
        EmailField: Email字段,检查Email的合法性
        URLField: URL地址字段,检查URL合法性
        IPAddressField: IP字段,十进制表示的IP地址
        GenericIPAddressField: IP字段,IPv4和IPv6地址表示,检查IP地址合法性
    # 关系字段类型:
        OneToOneField: 一对一
        ForeignKey: 一对多
        ManyToManyField: 多对多
    ...等字段类型
    ```
    
* 模型字段选项: models.字典类型(字段选项)
    ```
    primary_key: 设置主键,对AutoField设置主键后,就会代替原来的自增 id 列
    max_length: 字符串最大长度
    unique=True: 字段值唯一,不允许重复,默认为Flase
    null=True: 数据库中字段允许为空,默认False
    blank=True: 在admin后台提交表单允许为空,默认Flase,当设置为True时,null属性值必须为True
    verbose_name: 在admin后台的显示字段名称
    editable=True: 在admin后台中是否可编辑,默认为True
    default: 为字段设置默认值(数据库与admin后台)
    auto_now=True: 自动创建--->无论添加或修改,都是当前操作的时间
    auto_now_add=True: 自动创建--->永远是创建时的时间
    choices: 轻量级的配置字段可选属性的定义(首先在模型类中定义一个列表或元组提供选择)
    db_column: 在数据库中的字段名称,默认和变量同名
    db_index = True: 在数据库中是否设置为索引,默认为False  
    upload_to="upload/images/": 文件上传功能;指定文件上传的目录位置,相对项目根目录
    ...等字段选项
    ```
    
* 模型元数据: class Meta
    ```
    class Meta:
        db_table = "table_name"  # 指定数据库表名
        ordering = ['order_date']  # 指定返回结果集按照哪个或哪些字段排序
        verbose_name = "student"   # 给模型类起一个可读的名字
        verbose_name_plural = verbose_name  # 模型的复数形式
        abstract = True/False    # 是否作为一个抽象类,默认为False
        unique_together = ("address", "note")  # 联合唯一健,还可以用二维元组((), ())
        app_label = 'app_name'  # 模型类属于哪一个应用
        ...等元数据属性
    ```
    
* 自定义模型类管理器
    ```
    # 注: 模型类可以定义使用多个管理器
    # 1.在models.py文件中定义一个类并继承Manager类
    from django.db.models.manager import Manager
    class ModelClazzManager(Manager):
        # 应用1.改变原有查询的结果集: 如all()
        # 应用2.封装方法:用户操作模型类对应的数据表(增删改查)
        # self.model: 获取self对象所在的模型类(即ModelClazz模型类)
        pass
        
    # 2.在models.py文件中模型类中定义管理器类对象属性
    from django.db import models
    class ModelClazz(models.Model):
        name = models.CharField(max_length=32)
        # 自定义一个模型器管理类对象(...)
        manages = ModelClazzManager()
        # objects = ModelClazzManager()  # 可以使用原有的管理器对象名称
        # 注: 模型类也可以重写(增删改查)操作数据方法,实现逻辑操作
        
    # 3.如果重新定义的管理器为manages,就不能使用原有的管理器objects了
    # 如,是: ModelClazz.manages.all() 而不是: ModelClazz.objects.all()
    ```
    
### 关系字段类型: 一对一, 一对多, 多对多
* 关系字段中的属性设置值:
    ```
    ## to: 要关联的表名
    注: to='ModelName'  # 加引号,这个表能找到就可以,不用引号,类必须在此模型类上面定义
    ## to_filed: 要关联的表中的字段名称
    ## related_name: 给模型类主表定义一个属性
    ## on_delete: 当删除关联表中的数据时，当前表与其关联的行的行为
    # 1. models.CASCADE: 将定义有外键的模型对象同时删除,django模板的默认操作
    # 2. model.PROTECT: 阻止上面的删除操作,但是弹出ProtectedError异常
    # 3. models.SET_NULL: 将外键字段设为null,只有当字段设置了null=True时,方可使用该值
    # 4. models.SET_DEFAULT: 将外键字段设为默认值,只有当字段设置了default参数时,方可使用
    # 5. models.DO_NOTHING: 什么也不做
    # 6. models.SET: 设置为一个传递给SET()的值或者一个回调函数的返回值,注意大小写
    ```
    
* OneToOneField: 一对一关系,将关系字段定义在任意一端中,如: 学生与学生证
    ```
    # 注: 关系字段定义在哪个模型类中,哪个模型类对应的表就是子表
    class Student(models.Model):  # 学生模型类
        # sno = models.AutoField(primary_key=True)  # 学生学号
        sno = models.CharField(max_length=20)  # 学生学号
        sname = models.CharField(max_length=32)  # 学生姓名
        class Meta:
            db_table = "t_student"  # 数据库表
    # 数据库表(t_student即主表)字段: id, sno, sname  
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    
    class Card(models.Model):  # 学生证模型类
        cno = models.CharField(max_length=20)  # 学生证编号
        cmajor = models.CharField(max_length=32)  # 学生证专业
        # student = models.OneToOneField(Student, primary_key=True) # 关联另一个模型类,设置外键属性
        student = models.OneToOneField(Student)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性student后,会在关联的模型类中增加一个隐式的属性: card
        class Meta:
            db_table = "t_card"  # 数据库表
    # 数据库表(t_card即子表)字段: id, cno, cmajor, student_id
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    # student_id表示在模型类中设置了外键属性student后,在数据库表中指向关联数据库表的主键ID
    
    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如查询: Card.objects.first().student
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如查询: Student.objects.first().card
    ```
    
* ForeignKey: 一对多关系,将关系字段定义在多的一端中,如: 作者和书籍
    ```
    # 注: 关系字段定义在哪个模型类中,哪个模型类对应的表就是子表
    class Author(models.Model):  # 作者
        aname = models.CharField(max_length=32)  # 作者姓名
    class Meta:
        db_table = "t_author"
    # 数据库表(t_author即主表)字段: id aname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段

    class Book(models.Model):  # 书籍
        bname = models.CharField(max_length=32)  # 书籍名称
        author = models.ForeignKey(Author)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性author后,会在关联的模型类中增加一个隐式的属性: book_set
    class Meta:
        db_table = "t_book"
    # 数据库表(t_book即为子表)字段: id bname author_id
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    # author_id表示在模型类中设置了外键属性author后,在数据库表中指向关联数据库表的主键ID

    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如(跨表)对象查询 - 对象.关联字段.字段: Book.objects.first().author.aname
    # 如(跨表)字段查询 - 关联字段__字段: Book.objects.values_list("author__aname")
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如(跨表)对象查询 - 对象.隐式属性: Author.objects.first().book_set.all()
    # 如(跨表)对象查询 - 对象.隐式属性: Author.objects.first().book_set.all().values_list("bname")
    # 如(跨表)字段查询 - 表名__字段: Author.objects.values_list("book__bname")
    ```

* ManyToManyField: 多对多关系,将关系字段定义在任意一端中,如: 课程与教师
    ```
    class Course(models.Model):  # 课程
        cname = models.CharField(max_length=32)  # 课程名称
    class Meta:
        db_table = "t_course"
    # 数据库表(t_course)字段: id cname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段

    class Teacher(models.Model):  # 教师
        tname = models.CharField(max_length=32)  # 教师姓名
        course = models.ManyToManyField(Course)  # 关联另一个模型类,设置外键属性
        # 注: 此处设置了外键属性course后,会在关联的模型类中增加一个隐式的属性:teacher_set
    class Meta:
        db_table = "t_teacher"

    # 数据库表(t_teacher)字段: id tname
    # id字段是在模型类中未设置主键时,django默认添加的自增字段
    
    ## 注:多对多关系中,Django默认会自动生成第三张(中间)表:
    # 数据库表(t_teacher_course)字段: id teacher_id course_id
    # teacher_id: 指向模型类对应数据库表(即t_teacher)主键
    # course_id: 指向模型类对应数据库表(即t_course)主键
    
    ### 正向操作: 子表 ---> 通过外键属性 ---> 主表
    # 如: Teacher.objects.first().course.all()
    ### 反向操作: 主表 ---> 通过隐式属性 ---> 子表
    # 如: Course.objects.first().teacher_set.all()
    
    # 注:可以自定义第三张表,不使用Django默认生成
    class Teacher_Course(models.Model):
        teacher = models.ForeignKey(Teacher)  # 关联另一个模型类,设置外键属性
        course = models.ForeignKey(Course)    # 关联另一个模型类,设置外键属性
    ```
### Django定义完模型类生成数据库表:
```
# 生成迁移文件: python manage.py makemigrations
# 执行迁移文件: python manage.py migrate

# 注:当模型类发生变更后需要重新生成数据库表
# 1.删除数据库表: 删除该模型类对应的数据表
# 2.删除数据库表信息: 删除django_migrations表中关于该模型类的迁移记录信息
# 3.删除APP应用文件: 删除./app_dir/migrations/迁移文件
# 4.再次生成迁移文件及执行迁移文件,生成对应的模型类数据库表
```

### Django框架ORM: 对象关系映射
* 添加数据: 
    ```
    # 1. Entity.objects.create(属性=值,属性=值)  # 返回值:创建好的实体对象
    
    # 2. 创建一个 Entity 对象，并通过 save() 进行保存
    obj = Entity(属性=值,属性=值)
    obj.save()
    
    # 3. 使用字典构建对象，并通过 save() 进行保存
    dic = {
        '属性1':'值1',
        '属性2':'值2',
    }
    obj=Entity(**dic)
    obj.save()
    ```
* 删除数据:
    ```
    # 删除一条或多条数据: 先查询后删除
    auList = Author.objects.filter(mid="1001)
    auList.delete()
    ```
* 修改数据:
    ```
    ## 修改单个对象: 可以对对象的全部属性值进行修改
    # 1.查: 通过查询得到要修改的实体对象
    # 2.改: 通过对象的属性修改对象的值
    # 3.保存: 通过对象的 save() 保存回数据库
    ## 批量修改数据: 推荐使用
    # 调用QuerySet对象的update(属性=值,属性=值)实现批量修改
    # 如: Entity.objects.filter(sname="王五").update(spasswd="555555")
    # SQL语句: UPDATE `stu` SET `spasswd` = '555555' WHERE `stu`.`sname` = '王五'
    ```  
* 显示底层的SQL语句: 测试
    ```
    # 1.Movie.objects.all().query.__str__()  # 针对select查询
    # 2.自定义函数
    from django.db import connection
    def showsql():
        query = connection.queries  # 打印所有底层执行过的SQL语句
        print(query[-1]['sql'])     # 取出最后一条SQL语句
    ```    
* 查询数据:
    * 基本查询方法: 13个基本方法
        ```
        ## 返回QuerySet对象的方法: all(), filter(), exclude(), order_by(), reverse(), distinct()
        ## 返回特殊的QuerySet对象的方法有: values(), values_list()
        # values()      返回一个可迭代的字典序列
        # values_list() 返回一个可迭代的元祖序列
        ## 返回具体对象的方法: get(), first(), last()
        ## 返回布尔值的方法：exists()
        ## 返回计数值的方法: count()
        
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
        ```
    * 聚合函数总结: 
        ```
        ## 聚合函数: 
        # 1.Avg():   平均值
        # 2.Min():   最小值
        # 3.Max():   最大值
        # 4.Sum():   求和
        # 5.Count(): 计数

        ## 聚合查询(不带分组): aggregate()
        # Entity.objects.all().aggregate(别名=聚合函数('列'))
        # 示例: Author.objects.all().aggregate(avg=Avg('age'))
        # 示例: Book.objects.aggregate(average_price=Avg('price'))
        
        ## 聚合查询(带分组): annotate() ---> annotate()前面的values("列1","列2")表示按照哪个列进行分组
        # Entity.objects.all().values('分组列1','分组列2').annotate(别名=聚合函数('列')).values('查询列1','查询列2','查询列3')
        # Entity.objects.filter(条件).values('分组列').annotate(别名=聚合函数('列')).filter(条件)
        # 示例: Employee.objects.values("dept").annotate(avg=Avg("salary").values(dept, "avg")
        ```
    
    * F查询与Q查询:
        ```
        ## F(): 在执行中获取某列的值
        # from django.db.models import F
        # 示例: Author.objects.all().update(age=F('age')+10)  # update author set age=age+10
        # 示例: Book.objects.filter(commnet_num__gt=F('keep_num'))
        
        ## Q(): 在查询条件中可以完成 |(OR) 和 &(AND) 和 ~(非) 操作
        # from django.db.models import Q
        # 示例: Author.objects.filter(Q(id=1)|Q(age=48))  # select * from author where id=1 or age=48
        # 示例: Book.objects.filter(Q(authors__name="小仙女")|Q(authors__name="小魔女"))
        ```
        
    * SQL原生查询:
        ```
        # 第一种包含主键:
        # Manager.raw(raw_query, params=None, translations=None)
        # raw_query: 执行的sql语句
        # params: 需要格式化的参数,类型:列表
        # translations: 值为字典,将查出来的数据键值对化,根据模型属性声明查询出来的键,如:{模型属性:键}
            Person.objects.raw('SELECT * FROM myapp_person LIMIT 1')[0]
            Person.objects.raw('SELECT * FROM myapp_person WHERE last_name = %s', [lname])
            
        # 第二种不包含主键:
            # 若你同时使用不止一个数据库,你可以使用 django.db.connections 获取指定数据库的连接(和指针)
            # from django.db import connections 是一个类字典对象,它允许你通过连接别名获取指定数据库连接
            # 如: connections['my_db_alias'].cursor()
            
            from django.db import connection  # 代表默认数据库连接
            cursor = connection.cursor()  # 获取指针对象
            # 1.调用 cursor.execute(sql, [params]) 方法执行该SQL语句
            # 2.调用 cursor.fetchone() 或 cursor.fetchall() 方法获取结果数据
        ```
        
    * ForeignKey查询: 多表查询
        ```
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
        ```


