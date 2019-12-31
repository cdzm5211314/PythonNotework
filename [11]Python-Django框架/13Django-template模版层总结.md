### Django框架的模版层: templates
```
将后端的数据传递给模板进行显示,Django中变量传递给模板的数据类型: 字符串,整数,列表,元组,字典,函数,对象
# 变量的语法: {{ 变量名 }} ---> 变量必须要封装到字典中才能传递给模板
```
* 模版中的标签语法: {% 标签内容 %}
    ```
    ### for标签: 
    ## 作用: 循环遍历 列表,字典,元组
    ## 语法: 如下
    # {% for 变量 in 列表|元组|字典 %}
    # {% empty %}  # 可选从句,在给出的组是空的或者没有被找到时，可以有所操作
    # {% endfor %} 
    ## for循环中允许使用 forloop 内置变量来获取循环的信息:
    # forloop.counter:      当前循环遍历的次数
    # forloop.first:        判断是否为第一次循环
    # forloop.last:         判断是否为最后一次循环
    # forloop.parentloop	本层循环的外层循环
    
    ### if标签: 
    ## 作用: 在模板中完成变量的判断操作,支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not 判断
    ## 语法: 如下
    # 第一种格式: if
    # {% if 条件 %}
    #     满足条件时要执行的内容
    # {% endif %}
    
    # 第二种格式: if ... else
    # {% if 条件 %}
    #   满足条件时要执行的内容
    # {% else %}
    #   不满足条件时要执行的内容
    # {% endif %}

    # 第三种格式: if ... elif ... else
    # {% if 条件1 %}
    #   满足条件1时要执行的内容
    # {% elif 条件2 %}
    #   或满足条件2时要执行的内容
    # {% elif 条件3 %}
    #   或满足条件3时要执行的内容
    # {% else %}
    #   或以上条件都不满足时要执行的内容
    # {% endif %}
    ```
    
* 常用内置过滤器: filter
    ```
    # 过滤器的作用: 在变量输出显示之前，对变量进行筛选和过滤
    # 过滤器的语法: {{ 变量|过滤器:参数 }}
    # {{ value|upper }}             ---> 将value变为大写
    # {{ value|add:num }}           ---> 将num值累加到value之后
    # {{ value|default:"nothing" }} ---> 如果一个变量是false或者为空,使用给定的默认值.否则使用变量的值
    # {{ value|length }}            ---> 返回值的长度，作用于字符串和列表
    # {{ value|safe }}              ---> 对value不进行转义
    # {{ value|date:"Y-m-d H:i:s"}} ---> 日期格式化
    # {{ value|truncatechars:n }}   ---> 将value截取保留至n位字符(包含...)
    # {{value|slice:"2:-1"}}        ---> 切片
    # ...等
    ```

* 自定义过滤器: filter {{ 变量|过滤器名称:参数 }}
    ```   
    ## 自定义过滤器: 只是带有一个或两个参数的Python函数
    # 1.在APP应用目录下创建的包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为过滤器文件,如 app01_filters
    # 3.编写自定义过滤器filter,示例代码如下:
    from django import template
    register = template.Library()
    @register.filter(name="cut")  # 为自定义过滤器取个名字
    def cut(value, arg):  # 第一个为变量,第二个是参数
        return value.replace(arg, "")
    @register.filter(name="addSB")  # 为自定义过滤器取个名字
    def add_sb(value):  # value为变量
        return "{} SB".format(value)
    # 4.在模版文件.html中使用自定义过滤器filter
    {# 4.1先导入我们自定义过滤器filter文件 #}
    {% load app01_filters %}
    {# 4.2使用我们自定义过滤器filter #}
    {{ somevariable|cut:"0" }}
    {{ d.name|addSB }}    
    ```
    
* 自定义标签: simple_tag {% 标签名称 参数1 参数2 ... %}
    ```
    ## 自定义标签: 接收更为灵活的参数的Python函数
    # 1.在app应用目录创建的package包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为标签文件,如 app01_tags
    # 3.编写自定义标签tags,示例代码如下:
    from django import template
    register = template.Library()
    @register.simple_tag(name="plus")
    def plus(a, b, c):
        return "{} + {} + {}".format(a, b, c)
    # 4.在模版文件.html中使用自定义标签simple_tag
    # {% load app01_tags %}
    # {% plus "1" "2" "abc" %}   
    ```

* 自定义标签和自定义过滤器的区别:
```
1.标签:是为了做一些功能, 过滤器:是对斜杠前面的数据做过滤。
2.标签可以写任意个形参,而过滤器最大只能写2个形参,如果过滤器需要接收多个参数,需要将参数存放在列表,元组,字典等数据中
3.过滤器可以用在if等语句后,标签不可以
```

* 模版的继承:
```
## 继承母版: 在子页面最上方使用 {% extends '父模板名称.html' %}
## 块(block): 在父模板中要标识出哪些内容在子模板中允许被修改
# 1.在父模板中正常显示
# 2.在子模板中，如果不修改的话则按父模板的显示,要是修改的话则按照子模板的内容显示
# {% block xxx %}
# {% endblock %}
## 组件: 将常用的页面内容如导航条,页尾信息等页面保存在单独的文件中,然后在需要使用的地方按如下语法导入即可
# {% include 'navbar.html' %}
```


