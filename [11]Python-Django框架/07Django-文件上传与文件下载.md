### 文件的上传与下载:
```
### 第一种方式文件的上传: 上传文件到本地目录(原生方式)
# 1.xxx.html文件:
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="fileupload">
    <input type="submit" value="上传文件">
</form>

# 2.urls.py:  
urlpatterns = [
    url(r'^upload/', view=upload_file, name='upload'),
]

# 3.views.py文件:
from django.shortcuts import HttpResponse
def upload_file(request):
    if request.method == "POST":
        # file_obj根据xxx.html中文件上传的name属性值,得到一个文件对象
        file_obj = request.FILES.get("fileupload", None)  
        import os
        if not os.path.exists('media'):  # 判断文件存放目录是否存在
            os.makedirs("media")  # 创建文件存放目录
        with open(os.path.join(os.getcwd(), 'media', file_obj.name), 'wb') as ft:
                # ft.write(file_obj.read())      # 一次性读取文件内容然后写入数据保存
                for chunk in file_obj.chunks():  # 分块读取文件内容然后写入数据保存
                    ft.writer(chunk)
        return HttpResponse("上传文件成功...")


### 第二种方式文件的上传: 上传文件到本地目录(admin后台上传文件)
# 1. settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    # 注:文件上传路径信息:MEDIA + upload_to ---> /media/images/文件
    # 注:数据库im字段信息: images/文件 
    im = models.ImageField(upload_to="images")  

# 3.admin.py文件: 注册模型类
from .models import UploadModel
admin.site.register(UploadModel)

# 4.创建超级管理员账户,访问: http://127.0.0.1:8000/admin 上传文件


### 第三种方式文件的上传: 上传文件到本地目录(信息写入数据库)
# 1.xxx.html文件:
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="fileupload">
    <input type="submit" value="上传文件">
</form>

# 2.urls.py:  
urlpatterns = [
    url(r'^upload/', view=upload_file, name='upload'),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    # 注:文件上传路径信息:MEDIA + upload_to ---> /media/images/文件
    # 注:数据库im字段信息: images/文件 
    im = models.ImageField(upload_to="images")  

# 4.views.py文件:
from django.shortcuts import HttpResponse
from .models import UploadModel
def upload_file(request):
    if request.method == "POST":
        file_obj = request.FILES.get("fileupload", None)  
        # 上传文件信息写入数据库
        UploadModel.objects.create(im=file_obj)
        return HttpResponse("上传文件成功...")


### 上传图片文件后的图片显示: 即图片文件的读取
# 1.settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.urls.py文件: 项目根路由,文件读取的配置信息
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    im = models.ImageField(upload_to="images") 

# 4.views.py文件: 
from .models import UploadModel
from django.shortcuts import render
def show_image(request):
    upall = UploadModel.objects.all()
    return render(request, 'show.html', {'uploadall':upall})

# 5.show.html文件:
{% for file in uploadall %} 
    <image src="/media/{{ file.im }}" />  # 显示图片
    <image src="{{ MEDIA_URL }}{{ file.im }}" />  # 显示图片
    # 注: 使用MEDIA_URL模版上下文变量需要在settings.py文件中的变量TEMPLATES中配置如下内容
    # 'django.template.context_processors.media'
{% endfor%} 
```

    
### 文件的下载: URL地址预览(图片)和文件下载
```
# 1.settings.py文件: 上传文件的存储路径配置
MEDIA_URL = '/media/'  # 指定上传文件的存储相对路径(读取文件),默认为空
MEDIA_ROOT = os.path.join('BASE_DIR','media')  # 指定上传文件的存储绝对路径(存储文件),默认为空

# 2.urls.py文件: 项目根路由,文件读取的配置信息
from django.views.static import serve
from 根项目名 import settings
urlpatterns = [
    # media相关的路由设置
    url(r'^media/(?P<path>.*)$', serve, {'document_root':settings.MEDIA_ROOT}),
]

# 3.models.py文件: 定义模型类
from django.db import models
class UploadModel(models.Model):
    im = models.ImageField(upload_to="images") 
    
# 4.xxx.html文件
<a href="/download/?file={{ file.im }}">下载</a>

# 5. urls.py文件:
url(r'^download/$',views.download_file),

# 6.views.py文件
def download_file(request):
    # 获取请求参数,图片的存储位置
    fi = request.GET.get('file', '')
    # 获取文件名
    # file_name = fi.split("/")[-1]      # 字符串分割,取列表最后一个元素
    file_name = fi.[fi.rindex("/")+1:]   # 进行字符串切片分割
    import os
    from django.shortcuts import HttpResponse
    # 获取文件的绝对路径
    file_path = os.path.join(os.getcwd(), 'media', fi.replace('/', '\\'))
    with open(file_path, 'rb') as ft:
        
        ## 默认预览图片: 
        response = HttpResponse(ft.read())  # 读取文件内容写入到页面
        response["Content-Type"] = "image/png"
        response["Content-Disposition"] = "inline;filename=" + file_name
        
        ## 第一种文件下载方式: from django.shortcuts import HttpResponse
        response = HttpResponse(ft.read())  # 读取文件内容写入到页面
        response['Content-Type'] = 'application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
        ## 第二种文件下载方式: from django.http import StreamingHttpResponse
        response =StreamingHttpResponse(ft)  # 传入文件句柄对象
        response['Content-Type']='application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
        ## 第三种文件下载方式[推荐使用]: from django.http import FileResponse
        # FileResponse是StreamingHttpResponse的子类,内部使用迭代器进行数据流传输
        response =FileResponse(ft)  # 传入文件句柄对象
        response['Content-Type']='application/octet-stream'  # 设置头信息,告诉浏览器这是个文件
        response["Content-Disposition"] = "attachment;filename=" + file_name
        
    return response
```


