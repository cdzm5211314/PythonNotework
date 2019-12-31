### Django框架处理请求方式: FBV 与 CBV
* FBV(function base views): 使用视图函数处理请求
    ```
    # url路由: 
    url(r'^index/$', views.index_view, name='index'),
    # views视图:
    def index_view(request):
       if request.method == "GET":  # 处理get请求
            pass
       else:  # 处理post请求
            pass
    ```
* CBV(class base views): 使用视图类处理请求
    ```
    # url路由:    
    url(r'^index/$', IndexView.as_view(), name='index'),
    # views视图:
    from django.views import View
    class IndexView(View):
        def get(self, resuest):  # 处理get请求
            pass    
        def post(self, request):  # 处理post请求
            pass
    ```
    
    
    