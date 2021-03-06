### Django框架后台管理: Admin
```
# 后台管理访问: http://localhost:8000/admin

# 使用Admin后台系统管理模型类(即数据库数据)
0.Admin后台管理页面中文设置: settings.py
LANGUAGE_CODE = 'zh-Hans'
TIME_ZONE = 'Asia/Shanghai'

1.创建超级管理员用户: python manage.py createsuperuser
# python manage.py createsuperuser
# Username: 输入用户名,默认为系统账户名
# Email Address: 电子邮件
# Password: 密码(8位)
# Password(agian): 重复密码

2.在APP应用下的admin.py文件中使用内置方式注册模型类
from .models import Student
admin.site.register(Student)

3.在APP应用下的admin.py文件中使用自定义方式注册模型类
from .models import Student
@admin.register(Student)  # 简写注册,等同于: admin.site.register(Student, StudentAdmin)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["name", "author",deletes]  # 定制显示的列: 即admin后台显示的模型字段名称或自定义函数名称
    list_display_link = ["author"]  # 定制列可以点击跳转: 点击哪个字段进入编辑页面
    list_filter = ["author"]  # 定制右侧快速过滤查询: 根据字段过滤
    search_fields = ["name"]  # 定制快速搜索框: 根据字段搜索
    raw_id_fields = ["关联字段"]  # 后台显示关联字段所属的信息
    ordering = ["排序字段"]
    list_per_page = 10  # 默认为100条
    actions_on_top = True  # 显示顶部的选项
    actions_on_bottom = True  # 显示底部的选项
# admin.site.register(Student, StudentAdmin)  # 自定义方式注册模型类


### 定制信息字段详情:
## list_display : 定义在 列表页 上显示的字段们
# 取值：由属性名组成的元组或列表
## 2.list_display_links : 定义在列表页中也能够连接到详情页的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须要出现在list_display中
## 3.list_editable : 定义在列表页中就允许修改的字段们
# 取值：由属性名组成的元组或列表
# 注意：取值必须出现在list_display中但不能出现在list_display_links中
## 4.search_fields : 添加允许被搜索的字段们
# 取值：由属性名组成的元组或列表
## 5.list_filter : 列表页的右侧增加过滤器，实现快速筛选
# 取值：由属性名组成的元组或列表
## 6.date_hierarchy : 列表页的顶部增加时间选择器，取值必须是DateField 或 DateTimeField的列名
## 7.fields : 在详情页中，指定显示哪些字段并按照什么样的顺序显示
# 取值：由属性名组成的元组或列表
## 8.fieldsets : 在详情页面中，对字段们进行分组显示的
# 注意：fieldsets 与 fields 是不能共存的
# 取值：
# fieldsets = (
#     #分组1
#     ('分组名称',{
#         'fields':('属性1','属性2'),
#         'classes':('collapse',)
#     }),
#     #分组2
#     ()
# )


### 编辑关联对象:
## 在一对多的关系中，可以在一端的编辑页面中编辑多端的对象，嵌入多端对象的方式包括表格、块两种
# 类型InlineModelAdmin：表示在模型的编辑页面嵌入关联模型的编辑
# 子类TabularInline：以表格的形式嵌入
# 子类StackedInline：以块的形式嵌入
## 在app01/admin.py文件中添加如下代码：
class AreaStackedInline(admin.StackedInline):
    model = AreaInfo    # 关联子对象（多类对象）
 
class AreaAdmin(admin.ModelAdmin):
    inlines = [AreaStackedInline]
```


