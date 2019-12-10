### FBV(function base views): 就是在视图里使用函数处理请求
### CBV(class base views): 就是在视图里使用类处理请求

### CBV中加装饰器:
# 1. 登陆装饰器
from functools import wraps
def check_login(func):
    @wraps(func)
    def inner(request, *args, **kwargs):
        next_url = request.get_full_path()
        if request.session.get("user"):
            return func(request, *args, **kwargs)
        else:
            return redirect("/login/?next={}".format(next_url))
    return inner

# 2. CBV登陆视图类
class LoginView(View):

    def get(self, request):
        """ 处理GET请求 """
        return render(request, 'login.html')

    def post(self, request):
        """ 处理POST请求 """
        user = request.POST.get('user')
        pwd = request.POST.get('pwd')
        if user == 'alex' and pwd == "alex1234":
            next_url = request.GET.get("next")
            # 生成随机字符串
            # 写浏览器cookie -> session_id: 随机字符串
            # 写到服务端session：
            # {
            #     "随机字符串": {'user':'alex'}
            # }
            request.session['user'] = user
            if next_url:
                return redirect(next_url)
            else:
                return redirect('/index/')
        return render(request, 'login.html')

# 3. 在CBV视图类中加入装饰器(三种方式)

# 1).加在CBV视图类的get和post方法上
from django.utils.decorators import method_decorator
class HomeView(View):

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "home.html")
    
    @method_decorator(check_login)
    def post(self, request):
        print("Home View POST method...")
        return redirect("/index/")
		
# 2).加在dispatch方法上
from django.utils.decorators import method_decorator
class HomeView(View):
	
	# 因为CBV中首先执行的就是dispatch方法，所以这么写相当于给get和post方法都加上了登录校验
    @method_decorator(check_login)
    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        print("Home View POST method...")
        return redirect("/index/")
# 3).直接加在视图类上，但method_decorator必须传 name 关键字参数
# 如果get方法和post方法都需要登录校验的话就写两个装饰器
from django.utils.decorators import method_decorator

@method_decorator(check_login, name="get")
@method_decorator(check_login, name="post")
class HomeView(View):

    def dispatch(self, request, *args, **kwargs):
        return super(HomeView, self).dispatch(request, *args, **kwargs)

    def get(self, request):
        return render(request, "home.html")

    def post(self, request):
        print("Home View POST method...")
        return redirect("/index/")



		