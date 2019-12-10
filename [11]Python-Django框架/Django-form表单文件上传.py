# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-11 17:08

html = """ 
<form action="/upload/" method="post" enctype="multipart/form-data">
    {% csrf_token %}
    <input type="file" name="fileupload">
    <input type="submit" value="上传文件">
</form>
"""

### views.py处理文件上传
# from django.shortcuts import render, HttpResponse
# def upload(request):
#     if request.method == "POST":
#         file_obj = request.FILES.get("fileupload")  # fileupload是html中文件上传的name属性值,得到一个文件对象
#         print(file_obj,type(file_obj))
#         with open(file_obj.name, 'wb') as ft:
#             for line in file_obj:
#                 ft.write(line)
#     return render(request,'update.html')


