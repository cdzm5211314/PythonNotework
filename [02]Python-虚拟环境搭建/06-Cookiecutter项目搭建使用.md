### CentOS7.2系统Cookiecutter搭建Django项目示例:

* 当前系统Python环境安装: pip3 install cookiecutter

* 搭建Django项目,需要使用cookiecutter-django模版
    ```
    在GitHub中搜索cookiecutter-django: git@github.com:pydanny/cookiecutter-django.git
    ```

* cookiecutter使用cookiecutter-django模版搭建Django项目: 
    ```
    执行命令: cookiecutter git@github.com:pydanny/cookiecutter-django.git  # 可能会报错
    注: 因为不是使用系统默认的Python2版本,所以需要进入安装的Python3的bin目录下
    /usr/local/python3/bin/cookiecutter git@github.com:pydanny/cookiecutter-django.git
    ### 接下来会出现一系列配置选项:
    0.是否重新下载cookiecutter-django: (之前下载过了就选no然后yes)
    1.project_name(填写项目名称): ZanHu
    2.project_slug: 默认跟项目名称一致
    3.description(项目描述): 自己填写一些描述
    4.author_name(作者名字): __cd__
    5.domain_name(项目域名): 使用默认
    6.email(邮箱): 使用默认
    7.version(项目的初始版本号): 使用默认
    8.Choose from 1, 2, 3, 4, 5 [1](是否开源): 选5,不开源
    9.timezone(时区): Asia/Shanghai
    10.windows(开发环境是否为windows): 不是选n, 是就选y
    11.use_pycharm(是否使用Pycharm开发): 是就选y
    12.use_docker(是否使用Docker): 不是选n
    13.Select postgresql_version(选择版本): 默认选择最新版(未集成MySQL)
    14.Select js_task_runner(JS的运行器): 使用默认
    15.Select cloud_provider: 
    16.custom_bootstrap_compilation(是否使用bootstrap压缩): 使用默认
    17.use_compressor(Django中用于压缩js.css静态文件): 选y
    18.use_celery(是否使用Celery异步操作): 选y
    19.use_mailhog(第三方的邮件发送服务): 此项目选择阿里云
    20.use_sentry(监控): 使用默认
    21.use_whitenoise(部署静态文件,也带压缩功能): 使用默认
    22.use_heroku(国外Pass平台): 使用默认
    23.use_travisci(类似与Jenkins持续集成与发布): 此项目选择n
    24.keep_local_envs_in_vcs(是否在本地环境中使用版本控制): 此项目选择n
    25.debug(是否开启DEBUG): 选y
    [SUCCESS]: Project initialized, keep up the good work! ---> 表示项目搭建完成!!!
    ```

* 在模版项目中创建虚拟环境: pipenv --python 3.6

* 开启MysQL,Redis服务并创建MySQL用户:
```
# 创建MySQL数据库:
create database zhanhu charset="utf8";
create database test_zhanhu charset="utf8";
# 创建MySQL用户并授权:
create user 'admin'@'%' identified by 'admin';
grant all on zanhu.* to 'admin'@'%';
grant all on test_zanhu.* to 'admin'@'%';
flush privileges;
```

* 配置PyCharm远程项目目录映射:
```
1. 在本地PyCharm中创建目录: 如zanhu
2. PyCharm菜单栏 ---> Tools ---> Deproyment ---> Configuration... ---> 点击"+"图标 ---> 选择"SFTP"选项,进入到sftp配置页面
3. 随便取个名字(如:CentosServer) ---> 填写好Linux系统的IP地址,用户名和密码 ---> 点击"Test Connection"测试是否连接成功
注: Root path(可省略): 为Linux系统中项目的上一级目录
4. 选项: Advanced ---> 设置远程连接活跃时间(10秒)和设置编码格式utf-8
5. 进入到"Mappings"配置页面: Local path(本地路径) 和 Deproyment path(远程路径), 点击远程路径选择Linux系统远程目录,完成与本地目录的映射
# Local path(本地路径): E:/workspace_PyCharm/zanhu
# Deproyment path(远程路径): /workspace/zanhu
6. OK 完成...
```

* PyCharm中本地与远程文件选项(上传与下载): 项目右键 ---> Deployment
```
选项 Upload to Xxx: 上传本地文件到远程目录
选项 Download from Xxx: 下载远程目录文件到本地目录
选项 Sync with from Xxx: 对比本地目录文件与服务器目录文件
```

* 配置PyCharm远程Python环境解释器:
```
1. 在本地Pycharm中的Settings中找到: Project Insterpreter
2. 在Python解释器中选择添加(远程): SSH Insterpreter ---> Existing server configuration ---> 选择前面添加(命名)的Linux服务器名称,如CentosServer ---> More(选择把IDE的设置Copy拷贝过去还是More移动过去) ---> Next
3. 选择远程服务器的虚拟环境: Interpreter解释器对相应Linux服务器搭建项目时创建的虚拟环境
如: pipenv --py 查看虚拟环境位置,/envs/zanhu-LlVOupKj/bin/python
4. Running code on the remote server ---> Sync folders 同步本地与远程文件夹选项
# Local Path(本地目录): E:/workspace_PyCharm/zanhu
# Remote path(远程目录): /workspace/zanhu
5. Running code on the remote server ---> Automatically upload project files to server 勾选,表示自动将本地文件上传到远程服务器
6. Finish 完成...
```

* 配置PyCharm项目的Django Server服务:
```
1. 右上角的Add Configuration ---> 选择"+"号 ---> Django server 
2. 填写配置信息,如 Configuration 和 Logs
## Configuration信息:
# Name: 随意取名字
# Host: 远程服务器的IP地址,和Django运行的端口号8000
# Run browser: 勾选后会在每次运行项目时自定打开浏览器
# Custom run command: 自定义运行命令,可不选
# Test server: 测试服务器,可不选
# No reload: 勾选后,后端代码修改后不会自动重启项目,可选
# Python insterpreter: 选择远程服务器上的Python解释器
# Working directory: 项目在本地的目录
# Path mapping: 项目本地到远程服务器的映射,可不填
## Logs信息: 勾选下面两项后,终端输出会在PyCharm中输出
Show ... output stream
Show ... error stream
3. 启动对Django的支持: 
Settings中搜索Django 或 Settings ---> Languages & Frameworks ---> Django ---> Enable Django Support(勾选)
# Django project root: 指定Django在本地的路径
# Settings: 指定项目的settings文件,此项目选config/settingslocal.py本地开发文件
4. Ok 完成...
```
### 删除部分文件完成项目的初始模版:
```
1. 删除docs与utility目录下的所有文件及目录

2. 修改./requirements/base.txt 文件
# 修改包版本: 把Django版本改成2.1.7
# 添加数据库包: mysqlclient==1.4.2.post1
3. 修改./requirements/production.txt 文件 ---> 注释以下两行内容,本项目使用阿里云
# django-storages[boto3]==1.8  # https://github.com/jschneier/django-storages
# django-anymail[mailgun]==7.0.0  # https://github.com/anymail/django-anymail

4. 修改安装包源信息: /zanhu/Pipfile 文件
豆瓣: https://pypi.douban.com/simple/
阿里云: https://mirrors.aliyun.com/pypi/simple/
5. 安装开发环境所需要的包: pipenv install -r requirements/local.txt

6. 修改./config/settings/base.py 文件
[14]READ_DOT_ENV_FILE = env.bool("DJANGO_READ_DOT_ENV_FILE", default=False)  # 开发阶段改成True,读取.env文件
[29]LANGUAGE_CODE = "en-us"  # 改成中文:zh-Hans
[48]DATABASES["default"]["ATOMIC_REQUESTS"] = True  # 将http请求中对数据库的操作封装成事务
[66]"django.contrib.humanize",  # 开启
[67]# "django.contrib.admin",  # 此项目不做后台管理,可删除
[211]CSRF_COOKIE_HTTPONLY = True  # 是否只允许http来获取csrf_token,改成False,此项目后期会使用JS来获取csrf_token
[209]Email邮件配置: 开发和部署都适用同样的email,在env中定义
EMAIL_HOST = env('DJANGO_EMAIL_HOST')
EMAIL_USE_SSL = env('DJANGO_EMAIL_USE_SSL', default=True)
EMAIL_PORT = env('DJANGO_EMAIL_PORT', default=465)
EMAIL_HOST_USER = env('DJANGO_EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = env('DJANGO_EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = env('DJANGO_DEFAULT_FROM_EMAIL')
[257] Celery的任务配置:
CELERY_RESULT_BACKEND = env('CELERY_BROKER_URL')  # 在env中定义
CELERY_ACCEPT_CONTENT = ["json","msgpack"]  # 指定接收的内容类型
CELERY_TASK_SERIALIZER = "msgpack"  # 任务序列化与反序列化,msgpack是二进制的序列化方案
CELERY_RESULT_SERIALIZER = 'json'  # 读取任务结果一般性能要求不高,所以使用了可读性更好的json
CELERYD_TASK_TIME_LIMIT = 5 * 60  # 单个任务的最大运行时间5分钟
CELERYD_TASK_SOFT_TIME_LIMIT = 60  # 任务的软时间限制,超时候SoftTimeLimitExceeded异常将会被抛出
7. 在/zanhu/根目录下新建.env文件,编写内容

8. 修改./config/settings/local.py 文件
[14] ALLOWED_HOSTS = ["*"]  # 改成*,允许所有访问
[25] 删除Email相关配置信息: 因为已在./config/settings/base.py文件中做过配置

9. 修改./config/settings/production.py 文件
[57-78] STORAGES 系项目用不到亚马孙的S3存储,删除
[79-98] STAIC和MEDIA 静态文件与媒体文件也用不到,删除
[101] endregion 用不到,删除
[118-146] EMAIL和ADMIN及Anymail 邮箱和后台也用不到,删除

10. 修改./config/wsgi.py 文件
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")  # 修改为开发环境

11.删除/zanhu/users/admin.py 文件

12. 修改./config/urls.py 文件
[4] # from django.contrib import admin  # 后台模块包
[14] # path(settings.ADMIN_URL, admin.site.urls),  # 关于后台的url

13. 生成数据库表,启动项目
pipenv run python manage.py migrate  # 生成数据库表
```

### cookiecutter-django模版项目目录结构说明:
```
zanhu  # 项目根目录
├── config  # Django项目的配置文件目录
│   ├── settings
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── production.py
│   │   └── test.py
│   ├── __init__.py
│   ├── celery_app.py
│   ├── urls.py  # 根路由
│   └── wsgi.py  # wsgi服务
├── docs  # 项目文档目录,目录下内容可删除
│   ├── pycharm
│   │   ├── images
│   │   │   ├── 1.png
│   │   │   ├── 2.png
│   │   │   ├── 3.png
│   │   │   ├── 4.png
│   │   │   ├── 7.png
│   │   │   ├── 8.png
│   │   │   ├── f1.png
│   │   │   ├── f2.png
│   │   │   ├── f3.png
│   │   │   ├── f4.png
│   │   │   ├── issue1.png
│   │   │   └── issue2.png
│   │   └── configuration.rst
│   ├── Makefile
│   ├── __init__.py
│   ├── conf.py
│   ├── index.rst
│   └── make.bat
├── locale  # Django使用国际化生成文件的目录
│   └── README.rst
├── requirements  # 项目需要安装的包目录
│   ├── base.txt
│   ├── local.txt
│   └── production.txt
├── utility  # 项目中使用的脚本与工具目录,目录下内容可删除,需要自己搭建环境
│   ├── install_os_dependencies.sh
│   ├── install_python_dependencies.sh
│   ├── requirements-bionic.apt
│   ├── requirements-jessie.apt
│   ├── requirements-stretch.apt
│   ├── requirements-trusty.apt
│   └── requirements-xenial.apt
├── zanhu  # 右键 ---> Mark directory as ---> Resource Root 选项
│   ├── contrib  # 数据库的生成文件目录,根据migrations中文件生成对应的数据库表
│   │   ├── sites
│   │   │   ├── migrations
│   │   │   │   ├── 0001_initial.py
│   │   │   │   ├── 0002_alter_domain_unique.py
│   │   │   │   ├── 0003_set_site_domain_and_name.py
│   │   │   │   └── __init__.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   ├── static  # Django项目的静态文件
│   │   ├── css
│   │   │   └── project.css
│   │   ├── fonts
│   │   │   └── .gitkeep
│   │   ├── images
│   │   │   └── favicons
│   │   │       └── favicon.ico
│   │   ├── js
│   │   │   └── project.js
│   │   └── sass
│   │       ├── custom_bootstrap_vars.scss
│   │       └── project.scss
│   ├── taskapp  # Celery任务目录
│   │   ├── __init__.py
│   │   ├── celery.py
│   ├── templates  # Django项目的模版文件
│   │   ├── account
│   │   │   ├── account_inactive.html
│   │   │   ├── base.html
│   │   │   ├── email.html
│   │   │   ├── email_confirm.html
│   │   │   ├── login.html
│   │   │   ├── logout.html
│   │   │   ├── password_change.html
│   │   │   ├── password_reset.html
│   │   │   ├── password_reset_done.html
│   │   │   ├── password_reset_from_key.html
│   │   │   ├── password_reset_from_key_done.html
│   │   │   ├── password_set.html
│   │   │   ├── signup.html
│   │   │   ├── signup_closed.html
│   │   │   ├── verification_sent.html
│   │   │   └── verified_email_required.html
│   │   ├── pages
│   │   │   ├── about.html
│   │   │   └── home.html
│   │   ├── users
│   │   │   ├── user_detail.html
│   │   │   └── user_form.html
│   │   ├── 403.html
│   │   ├── 404.html
│   │   ├── 500.html
│   │   └── base.html
│   ├── users  # 用户应用APP,完成了登录,注册,找回密码等功能
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   └── __init__.py
│   │   ├── tests
│   │   │   ├── __init__.py
│   │   │   ├── factories.py
│   │   │   ├── test_forms.py
│   │   │   ├── test_models.py
│   │   │   ├── test_tasks.py
│   │   │   ├── test_urls.py
│   │   │   └── test_views.py
│   │   ├── __init__.py
│   │   ├── adapters.py  # 集成第三方登录功能使用的文件
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── context_processors.py
│   ├── __init__.py
│   └── conftest.py  # 项目测试使用的文件
├── .coveragerc  # 生成项目的测试覆盖度报告文件
├── .editorconfig  # 编辑器的配置
├── .gitattributes
├── .gitignore
├── .pre-commit-config.yaml
├── .pylintrc  # 规范Python代码格式
├── README.rst  # 项目的文档
├── manage.py  # Django项目的文件
├── pytest.ini  
├── setup.cfg  # 项目相关的配置
└── Pipfile  # 使用Pipenv生成的文件
```
