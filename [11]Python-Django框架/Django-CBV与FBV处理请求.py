# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-06-27 9:40

### CBV(class base views): 就是在视图里使用类处理请求
### FBV(function base views): 就是在视图里使用函数处理请求



## CBV ---> views.py
from django.shortcuts import render, HttpResponse
from django.views import View

class LoginView(View):

    def dispatch(self, request, *args, **kwargs):  # 请求来了进行分发
        print("DISPATCH")

        # 执行父类View的dispatch方法
        # super().dispatch(request, *args, **kwargs)
        # super(LoginView, self).dispatch(request, *args, **kwargs)
        # return HttpResponse("dispatch ...")
        # """
        # 后台输出: DISPATCH GET
        # 前端页面: dispatch ...
        # """

        # 执行父类View的dispatch方法
        # result = super().dispatch(request, *args, **kwargs)
        result = super(LoginView, self).dispatch(request, *args, **kwargs)
        return result
        # """
        # 后台输出: DISPATCH GET
        # 前端页面: get ...
        # """

    def get(self, request):
        print("GET")
        return HttpResponse("get ...")

    def post(self, request):
        print("POST")
        return HttpResponse("post ...")

## CBV ---> urls.py
from django.conf.urls import url
# from app01 import LoginView

urlpatterns = [
    url(r'^login/', LoginView.as_view()),  # view(request) ---> dispatch() ---> self.get() 或 self.post() ...
]

# *************** #

## FBV ---> views.py
# from django.shortcuts import render, HttpResponse
# def logout(request):
#     if request.Method == "GET":  #  if request.Method = "POST":
#         return HttpResponse("OK")

## CBV ---> urls.py
# from django.conf.urls import url
# from app01 import views
#
# urlpatterns = [
#     url(r'^logout/', views.logout),
# ]





