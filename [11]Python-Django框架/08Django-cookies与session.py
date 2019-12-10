# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-17 11:21

### cookies ###

## 设置cookies的值:
# 响应对象.set_cookie(key,value,expires)  # key:cookie的名字, value:cookie的值, expires:保存时间,以s为单位
# 响应对象.set_signed_cookie(key,value,salt='加密盐', max_age=None, ...)
# 示例: 响应对象.set_cookie('uname','tom',60*60*24*365)

## 响应对象:
# 1.HttpResponse
#   resp = HttpResponse("给客户端的一句话")
#   resp.set_cookie('key','value',expires)
#   return resp
# 2.render()
#   resp = render(request,'xxx.html',locals())
#   resp.set_cookie('key','value',expires)
#   return resp
# 3.HttpResponseRedirect / redirect
#   resp = redirect('/地址/')
#   resp.set_cookie('key','value',expires)
#   return resp

## 获取cookies的值: request.COOKIES 获取当前站点下所有的cookies的信息
# request.COOKIES           # 获取所有的cookies值信息
# request.COOKIES['key']    # 根据cookie的key获取value值
# request.get_signed_cookie(key, default=RAISE_ERROR, salt='', max_age=None)

## 删除coookies的值
# 响应对象.delete_cookie("user")  # 删除用户浏览器上之前设置的usercookie值


### session ###
## 设置 session 的值:
# request.session['key'] = value
# request.session.setdefault('k1',123) # 存在则不设置
## 获取 session 的值:
# value = request.session[key]
# value = request.session.get('key')
# value = request.session.get('k1',None)
## 删除 session 的值:
# del request.session['key']


## # 所有 键、值、键值对
# request.session.keys()
# request.session.values()
# request.session.items()
# request.session.iterkeys()
# request.session.itervalues()
# request.session.iteritems()

# request.session.session_key               # 会话session的key
# request.session.clear_expired()           # 将所有Session失效日期小于当前日期的数据删除
# request.session.exists("session_key")     # 检查会话session的key在数据库中是否存在
# request.session.delete()                  # 删除当前会话的所有Session数据
# request.session.flush()                   # 删除当前的会话数据并删除会话的Cookie。
# 注: flush()用于确保前面的会话数据不可以再次被用户的浏览器访问,例如，django.contrib.auth.logout() 函数中就会调用它
# request.session.set_expiry(value)         # 设置会话Session和Cookie的超时时间
# * 如果value是个整数，session会在些秒数后失效
# * 如果value是个datatime或timedelta，session就会在这个时间后失效
# * 如果value是0,用户关闭浏览器session就会失效
# * 如果value是None,session会依赖全局session失效策略


### Django中的Session配置: Django中默认支持Session，其内部提供了5种类型的Session
## 1. 数据库Session
SESSION_ENGINE = 'django.contrib.sessions.backends.db'   # 引擎（默认）
## 2. 缓存Session
SESSION_ENGINE = 'django.contrib.sessions.backends.cache'  # 引擎
SESSION_CACHE_ALIAS = 'default'  # 使用的缓存别名（默认内存缓存，也可以是memcache），此处别名依赖缓存的设置
## 3. 文件Session
SESSION_ENGINE = 'django.contrib.sessions.backends.file'  # 引擎
SESSION_FILE_PATH = None  # 缓存文件路径，如果为None，则使用tempfile模块获取一个临时地址tempfile.gettempdir()
## 4. 缓存 + 数据库
SESSION_ENGINE = 'django.contrib.sessions.backends.cached_db'  # 引擎
## 5. 加密Cookie Session
SESSION_ENGINE = 'django.contrib.sessions.backends.signed_cookies'  # 引擎

## 其他公用设置项：
# SESSION_COOKIE_NAME ＝ "sessionid"  # Session的cookie保存在浏览器上时的key，即：sessionid＝随机字符串（默认）
# SESSION_COOKIE_PATH ＝ "/"  # Session的cookie保存的路径（默认）
# SESSION_COOKIE_DOMAIN = None  # Session的cookie保存的域名（默认）
# SESSION_COOKIE_SECURE = False  # 是否Https传输cookie（默认）
# SESSION_COOKIE_HTTPONLY = True  # 是否Session的cookie只支持http传输（默认）
# SESSION_COOKIE_AGE = 1209600  # Session的cookie失效日期（2周）（默认）
# SESSION_EXPIRE_AT_BROWSER_CLOSE = False  # 是否关闭浏览器使得Session过期（默认）
# SESSION_SAVE_EVERY_REQUEST = False  # 是否每次请求都保存Session，默认修改之后才保存（默认）

