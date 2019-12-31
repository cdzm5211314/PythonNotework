### Cookie与Session:
```
## Cookie的操作: 存, 取, 删
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/', domain=None, secure=None, httponly=False)
# 注:参数解释,key:cookie的名字, value:cookie的值, max_age:cookie存在时间,秒为单位, expires:具体的时间为单位
# 注: cookie不设置过期时间的话,默认关闭浏览器就失效

response = HttpResponse('保存cookie')
response.set_cookie('username', username,)  # 设置cookie的键与值
response.set_signed_cookie('username', username, salt='asdasd') # 设置cookie的键与值,加盐

cookies = request.COOKIES  # 获取所有的cookie信息
username = request.COOKIES.get('username')  # 获取指定cookie的值
username = request.get_signed_cookie('username', salt='asdasd') # 获取cookie的值,注:如果加盐,盐要相同否则取不到值

response = HttpResponse('删除cookie')
response.delete_cookie('username')  # 删除指定的cookie

request.COOKIES.has_key("username")  # 判断所有cookie信息是否存在某个cookie,存在返回True
```

### Session的操作:
```
request.session['username'] = username  # 设置session的键与值
username = request.session.get('username')  # 获取session的值
del request.session['username']  # 删除指定的session的值
request.session.flush()  # 清空所有session并删除数据库session表中的数据
request.session.clear()  # 清空所有session但并不删除数据库session表中的数据
request.session.logout() # 退出登陆,清空所有session并删除数据库session表中的数据

## 获取session中所有的键,值,键值对
# request.session.keys()
# request.session.values()
# request.session.items()
# request.session.iterkeys()
# request.session.itervalues()
# request.session.iteritems()

# request.session.session_key               # 用户session的随机字符串
# request.session.exists("session_key")     # 检查用户session的随机字符串在数据库session表中中是否存在
# request.session.clear_expired()           # 将所有session失效日期小于当前日期的数据删除
# request.session.delete()                  # 删除当前会话的所有session数据
# request.session.flush()                   # 删除当前的会话数据并删除会话的Cookie。

request.session.set_expiry(value)  # 设置会话Session和Cookie的超时时间
* 如果value是个整数,session会在多少秒数后失效
* 如果value是个datetime或timedate，session就会在这个时间后失效
* 如果value是0,用户关闭浏览器session就会失效
* 如果value是None,session会依赖全局session失效策略


### Django中默认支持Session,其内部提供了5种类型的Session配置
## 1. 数据库: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
## 2. 缓存: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存,也可以是memcache）,此处别名依赖缓存的设置
## 3. 文件: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎
SESSION_FILE_PATH = None  # 缓存文件路径,如果为None,则使用tempfile模块获取一个临时地址tempfile.gettempdir()
## 4. 缓存 + 数据库: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # 引擎
## 5. 加密Cookie: Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎

## settings.py配置文件中设置默认操作(通用配置)
# SESSION_COOKIE_NAME ＝ "sessionid"  # Session的cookie保存在浏览器上时的key,即:sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"          # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None        # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False       # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True      # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600        # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False       # 是否每次请求都保存Session，默认修改之后才保存（默认）
```
