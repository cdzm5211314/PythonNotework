### 静态文件与模版文件的访问:
```
### 静态文件设置(settings.py): 在Django中,不被解释器所动态解析的文件就是静态文件
## 设置静态文件的访问路径: 在浏览器中通过哪个地址能够找到静态文件
# STATIC_URL = '/static/'
#  ---> 如果访问路径是 http://localhost:8000/static/...,那么就到静态文件存储路径中找文件而不走路由(urls.py)
## 设置静态文件的存储路径: 指定静态文件存储在服务器上的哪个位置处
# STATICFILES_DIRS = (os.path.join(BASE_DIR,'static'),)
# 静态文件目录的存放位置：
# 1.在项目的根目录处创建一个 static 目录，用于保存静态文件
# 2.每个应用中也可以创建一个 static 目录，用于保存静态文件

### 如何访问静态文件:
# 1. 直接使用静态文件访问路径进行访问 ---> http://localhost:8000/static/..
# 如: <img src="/static/images/a.jpg">
# 如: <img src="http://localhost:8000/static/images/a.jpg">
# 2. 使用 {% static "xxx" %} 访问静态资源路径
# 2.1.在模板最顶层增加: {% load static %} 或 {% load staticfiles %}
# 2.2.在使用静态资源时:
# <img src="{% static 'images/a.jpg'%}">
# <script src="{% static "mytest.js" %}"></script>

# 或者如果不想每次在模版文件中加载静态文件时都使用{% load static %},那么就把static标签变成Django内置标签:
# 在settings.py文件中属性TEMPLATES/OPTIONS同级下添加: 'builtins':['django.templatetags.static']

## 获取静态文件的前缀: {% get_static_prefix %}   ---> /static/
# {% load static %}
# <img src="{% get_static_prefix %}images/hi.jpg" />   ---> /static/images/hi.jpg

### 模板(Templates)的设置: 在 settings.py 中有一个 TEMPLATES 变量
# 1. BACKEND：指定使用的模板的引擎
# 2. DIRS: 指定模板的存放路径
# 2.1 如果写东西: 则按照写好的路径去找模板
# 2.2 如果未写东西: 那么Django会自动的到每个应用中搜索一个叫templates的目录来作为模板的存放目录
# 3. APP_DIRS: 是否自动搜索应用中的目录,设置为True: 表示搜索应用中的 templates 目录
```

