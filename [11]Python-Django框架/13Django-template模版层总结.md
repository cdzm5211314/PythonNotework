### Django框架的模版层: templates
```
将后端的数据传递给模板进行显示,Django中变量传递给模板的数据类型: 字符串,整数,列表,元组,字典,函数,对象
# 变量标签: {{ 变量名 }} ---> 变量必须要封装到字典中才能传递给模板
# 块标签: 如 {% for %}{{ endfor }}, {% if %}{{ endif }} ...
```
* 模版中的标签语法: {% 标签内容 %}
    ```
    ### for标签: 
    ## 作用: 循环遍历 列表,字典,元组
    ## 语法: 如下
    {% for 变量 in 列表|元组|字典 %}  # 循环取值reversed倒序: {% for 变量 in 列表 reversed %}
    {% empty %}  # 可选从句,未获取到数据时,执行的内容
    {% endfor %}
    ## for循环中允许使用 forloop 内置变量来获取循环的信息:
    forloop.counter:      当前循环遍历的次数,从1开始
    forloop.counter0:     当前循环遍历的次数,从0开始
    forloop.revcounter:   当前循环遍历的次数,序号倒序
    forloop.first:        判断是否为第一次循环
    forloop.last:         判断是否为最后一次循环
    forloop.parentloop	本层循环的外层循环
    
    ### if标签: 
    ## 作用: 在模板中完成变量的判断操作,支持 and 、or、==、>、<、!=、<=、>=、in、not in、is、is not 判断
    ## 语法: 如下
    # 第一种格式: if
    {% if 条件 %}
        满足条件时要执行的内容
    {% endif %}
    
    # 第二种格式: if ... else
    {% if 条件 %}
      满足条件时要执行的内容
    {% else %}
      不满足条件时要执行的内容
    {% endif %}

    # 第三种格式: if ... elif ... else
    {% if 条件1 %}
      满足条件1时要执行的内容
    {% elif 条件2 %}
      或满足条件2时要执行的内容
    {% else %}
      或以上条件都不满足时要执行的内容
    {% endif %}
    ```
* 模版常用内置标签:
    ````
    {# 单行注释 #%}
    {% comment %} 多行注释 {% endcomment %}
    {% autoescape off %} 解析标签内容 {% endautoescape %}
    {% autoescape on %} 自动转义为普通字符串(默认) {% endautoescape %}
    {% debug %} 输出整个调试信息,包括当前上下文和导入的模块
    {% block %} 定义可以被子模板覆盖的块,为模板继承时使用 {% endblock %} 
    {% extends "xxx.html" %} 带引号,作为父模板的名称来扩展
    {% extends variable %} 使用的变量variable;如果变量的计算结果为字符串,Django将使用该字符串作为父模板的名称,如果变量评估为一个Template对象,Django将使用该对象作为父模板
    {% include "xxx.html" %} 模版中包含使用某个组件(.html)
    ...等
    ````    
    
* 模版常用内置过滤器:
    ```
    # 过滤器的作用: 在变量输出显示之前,对变量进行筛选和过滤
    # 过滤器的语法: {{ 变量|过滤器 }} 或 {{ 变量|过滤器1|过滤器2 }} 或 {{ 变量|过滤器:参数 }}
    {{ variable|upper }}             ---> 将variable变为大写
    {{ variable|add:num }}           ---> 将num值累加到variable之后
    {{ variable|default:"nothing" }} ---> 如果一个变量是false或者为空,使用给定的默认值,否则使用变量的值
    {{ variable|length }}            ---> 返回值的长度,作用于字符串和列表
    {{ variable|safe }}              ---> 对variable不进行转义
    {{ variable|date:"Y-m-d H:i:s"}} ---> 日期格式化
    {{ variable|truncatechars:n }}   ---> 将variable截取保留至n位字符(包含...)
    {{ variable|slice:"2:-1"}}       ---> 切片
    ...等
    ```
    
* 自定义过滤器: filter 
    ```  
    ## 语法样式: {{ 变量|过滤器名称:参数 }}
    ## 自定义过滤器步骤: 过滤器本质就是带有一个或两个参数的Python函数
    # 1.在APP应用目录下创建包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为过滤器文件,如 app01_filters.py
    # 3.编写自定义过滤器filter,示例代码如下:
    from django import template
    register = template.Library()
    # 如果未设置name属性值,默认会使用函数名作为过滤器名字
    @register.filter(name="get1")  # name属性值为自定义过滤器名字
    def get1_filter(variable):  # variable为使用过滤器的变量
        return "{} SB".format(variable)
    @register.filter(name="get2")  # name属性值为自定义过滤器名字
    def get2_filter(variable, arg):  # variable为使用过滤器的变量,arg为传递的参数
        return variable.replace(arg, "")
    # 4.在模版文件.html中使用自定义过滤器filter
    {# 4.1 导入自定义过滤器filters文件 #}
    {% load app01_filters %}
    {# 4.2 使用自定义过滤器filter #}
    {{ variable|get1 }}    
    {{ variable|get2:"0" }}
    ```
    
* 自定义标签: simple_tag 
    ```
    ## 语法样式: {% 标签名称 参数1 参数2 ... %}
    ## 自定义标签步骤: 标签本质就是带有多个参数的Python函数
    # 1.在APP应用目录下创建包目录名称必须为: templatetags
    # 2.在templatetags目录下创建一个名称任意的.py文件作为标签文件,如 app01_tags.py
    # 3.编写自定义标签tag,示例代码如下:
    from django import template
    register = template.Library()
    @register.simple_tag(name="plus")  # name属性值为自定义标签名字
    def plus_tag(a, b, c):  # a,b,c为传递给标签的参数(形参)
        return "{} + {} + {}".format(a, b, c)
    # 4.在模版文件.html中使用自定义标签simple_tag
    {# 4.1 导入自定义标签tags文件 #}
    # {% load app01_tags %}
    {# 4.2 使用自定义标签tag #}
    # {% plus "1" "2" "abc" %} # 1,2,abc为传递给标签的参数(实参)  
    ```

* 自定义标签和自定义过滤器的区别:
```
1.标签:是为了做一些功能;过滤器:是对斜杠前面的数据做过滤
2.标签可以写任意个形参,而过滤器最大只能写2个形参,如果过滤器需要接收多个参数,需要将参数存放在列表,元组,字典等数据中
3.过滤器可以用在if等语句后,标签不可以
```

* 模版的继承:
```
## 继承父模版(extends): 在子模版的第一行使用 {% extends '父模板名称.html' %}
## 预留块(block): 在父模板中要标识出哪些内容在子模板中允许被修改,被填充
# 1.在父模板中正常显示
# 2.在子模板中,如果不修改的话则按父模板的显示,要是修改的话则按照子模板的内容显示
# {% block xxx %}
# {% endblock %}
## 组件(页面): 将常用的页面内容如导航条,页尾信息等页面保存在单独的.html文件中,然后在需要使用的地方按如下语法导入即可
# {% include 'navbar.html' %}
```


