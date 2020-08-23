### Django框架的中间件: middleware
```
# Django框架有默认的中间件: settings.py文件的 MIDDLEWARE = []
# 中间件的执行顺序: 自上而下,全局操作Django项目的请求与响应

### 中间件的常用方法: process_request() 和 process_response()
from django.utils.deprecation import MiddlewareMixin
class MyMiddleware(MiddlewareMixin):

    def process_request(self, request):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 请求从wsgi拿到的时候
        返回值: None或HttpResponse对象
            如果是None,继续执行后续的中间件的process_request方法
            如果是HttpResponse对象,不执行后续的中间件的process_request方法
        """
        pass

    # def process_view(self, request, callback, callback_args, callback_kwargs):
    def process_view(self, request, view_func, view_args, view_kwargs):
        """
        :param request: 浏览器发来的请求对象
        :param view_func: 将要执行的视图函数的名字
        :param view_args: 位置参数
        :param view_kwargs: 关键字参数
        执行顺序: 按照settings.py文件的中间件注册顺序,从上到下
        何时执行: 在urls.py中找到与视图的对应关系后,在执行真正的视图函数之前调用
        返回值:
            如果是None,继续执行后续的中间件的process_view方法
            如果是HttpResponse对象,不执行后续的中间件的process_view方法
        """
        pass
        
    def process_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 请求有响应的时候
        返回值: 必须是HttpResponse对象
        """
        pass

    def process_exception(self, request, exception):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数中抛出异常时执行
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass

    def process_template_response(self, request, response):
        """
        执行顺序: 按照settings.py文件的中间件注册顺序,从下到上
        何时执行: 在视图函数完成后执行,前提是:视图函数返回的对象有一个render()方法(或表明该对象是一个TemplateResponse对象或等价方法)
        返回值:
            如果是None,继续执行后续中间件的process_exception方法
            如果是HttpResponse对象,不执行后续中间件的process_exception方法
        """
        pass
        
## 注:除了process_response()方法必须返回HttpResponse对象,其他几个方法的返回值可以是None或HttpResponse对象:
# 如果是None,则按照Django定义的规则往下执行
# 如果是HttpResponse对象,则直接将该对象返回给用户
## 注: Django调用 注册的中间件里面的五个方法的执行顺序:
# process_request  ---> urls.py ---> process_view ---> view.py ---> process_exception ---> process_template_response ---> process_response

### 自定义中间步骤:
# 1.在项目根目录下创建包目录,如包名称为middleware
# 2.在创建的middleware包目录下创建.py文件,如文件名称为mymiddleware.py
# 3.在创建的mymiddleware.py文件中编写中间件类,并继承MiddlewareMixin基类
from django.utils.deprecation import MiddlewareMixin
class XxxMiddleware(MiddlewareMixin):
    '''然后根据功能需要,重写那五个方法中的某个或多个方法,如下所示'''
    def process_request(self, request):
        print("request路径: ", request.path)
        print("访问服务器的IP地址: ", request.META.get("REMOTE_ADDR"))
# 4.启用(注册)中间件,在settings.py中进行配置,如MIDDLEWARE添加: 包名.文件名.类名
# 如: 'middleware.mymiddleware.XxxMiddleware'


