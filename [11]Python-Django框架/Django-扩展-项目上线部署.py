# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-08-29 13:22

### 通过 nginx + uwsgi 将django项目部署在Ubuntu服务器上


### Ubuntu服务器部署前的工作:
# 注: 安装之前最好更新下源: sudo apt-get update
## 1. 安装Python3的pip包管理工具
# sudo apt-get install python3-pip

## 2. 安装虚拟环境和虚拟环境管理包
# sudo pip3 install virtualenv  # (报错的话需要把pip也安装一下)
# sudo pip3 install virtualenvwrapper

## 3. 修改~/.bashrc 文件,添加以下内容: sudo vim ~/.bashrc
# export WORKON_HOME=~/Envs  # 指定以后创建的虚拟环境位置
# source /usr/local/bin/virtualenvwrapper.sh
# VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3

## 4. 使文件生效: source ~/.bashrc

## 5. 创建虚拟环境: mkvirtualenv projectenvs -p /usr/bin/python3

## 6. 虚拟环境中安装项目所依赖的包
# 6.1 使用pip freeze > requirements.txt将windows的虚拟环境安装包相应信息导出来,然后拷贝到Ubuntu服务器
# 6.2 使用pip3 install -r requirements.txt -i https://pypi.douban.com/simple  # 注: 在安装过程中mysqlclient会报错，按照下面两步走
# 6.3 sudo apt-get install libmysqlclient-dev
# 6.4 pip3 install mysqlclient
# 6.5 再次使用pip3 install -r requirements.txt -i https://pypi.douban.com/simple安装

## 7. 安装MySQL数据库
# sudo apt-get install mysql-server
# 创建项目对象的数据库,并导入数据:windown--->ubuntu: 使用NavicatPremium客户端的数据传输功能
# 将项目放入虚拟环境中,进入项目使用 python manage.py runserver 保证能拉起项目
# 注: [settings中配置成开发阶段: DEBUG = True 和 ALLOWED_HOSTS = []]

### Ubuntu服务器开始部署配置:
## 8. 安装uwsgi: pip3 install uwsgi  或  pip3 install uwsgi -i https://pipy.douban.com/simple/
## 9. 测试uwsgi: 在项目根目录下执行 uwsgi --http :8000 --module GuLiEdu.wsgi ---> https://UbuntuIP:8000
# 注: [settings中配置成上线阶段: DEBUG = False 和 ALLOWED_HOSTS = ['*'] 以及 注释掉静态文件存储路径STATICFILES_DIRS属性,然后配置STATIC_ROOT = os.path.join(BASE_DIR,'static')]
# 注: 然后执行: python manage.py collectstatic --->  [yes] ---> 把静态文件收集到 STATIC_ROOT 目录中
# 问题: 上线阶段访问获取不到静态文件及media媒体上传文件 ---> 结合nginx使用

## 10. 安装nginx: sudo apt-get install nginx
# 注: 安装完成会自动启动nginx的服务，我们在外部windows浏览器直接访问Ubuntu服务器IP地址会进入到nginx的环境界面
# 10.1 在项目 根目录下新建文件夹config: mkdir config
# 10.2 在config文件夹下新建文件guli_nginx.conf: vi guliedu_nginx.conf  ---> 添加以下内容:
"""
# the upstream component nginx needs to connect to
upstream django {
    # server unix:///path/to/your/mysite/mysite.sock; # for a file socket
    server 127.0.0.1:8000; # for a web port socket (we'll use this first)
}
# configuration of the server
server {
    # the port your site will be served on
    listen 80;  # 监听端口
    # the domain name it will serve for
    server_name 10.0.244.102; # 你的Ubuntu服务器IP地址
    charset utf-8;

    # max upload size
    client_max_body_size 75M;   # adjust to taste

    # Django media
    location /media  {
        alias /home/chendong/桌面/GuLiEdu/static/media;  # 指向django项目的media目录
    }
    # Django static
    location /static {
        alias /home/chendong/桌面/GuLiEdu/static; # 指向django项目的static目录
    }

    # Finally, send all non-media requests to the Django server.
    location / {
        uwsgi_pass django;
        include /etc/nginx/uwsgi_params; # the uwsgi_params file you installed
    }
}
"""
## [有问题]11. 将刚创建的配置文件guliedu_nginx.conf加入到nginx的启动配置文件夹中
# sudo cp /home/chendong/桌面/GuLiEdu/config/guliedu_nginx.conf /etc/nginx/conf.d/
# 注: 在/usr/local/nginx/conf目录下创建conf.d目录,然后拷贝guliedu_nginx.conf文件
# sudo cp /home/chendong/桌面/GuLiEdu/config/guliedu_nginx.conf /usr/local/nginx/conf/conf.d/

## 12. 拉取所有需要的staticfile到同一个目录:
# 12.1 settings中注释掉配置的STATICFILES_DIRS属性,在上线阶段,这个配置失效
# 12.2 settings中配置另一个属性: STATIC_ROOT = os.path.join(BASE_DIR, "static")
# 12.3 在项目根目录下执行: python manage.py collectstatic --->  [yes] ---> 把静态文件收集到 STATIC_ROOT 目录中

## 13. 重启nginx服务: sudo service nginx restart
# 问题: 访问项目,未找到静态文件...

## 14. 通过配置文件启动uwsgi
# 14.1 在项目根目录下的config目录下新建 uwsgi.ini 配置文件,内容如下:
"""
# mysite_uwsgi.ini file
[uwsgi]
# Django-related settings
# the base directory (full path)
# chdir表示需要操作的目录,也就是项目的目录
chdir = /home/chendong/桌面/GuLiEdu
# Django's wsgi file
# module表示项目下的wsgi文件的路径
module = GuLiEdu.wsgi
# the virtualenv (full path)
# process-related settings
# master
master = true
# maximum number of worker processes
# processes表示进程数
processes = 10
# the socket (use the full path to be safe
socket = 127.0.0.1:8000
# ... with appropriate permissions - may be needed
# chmod-socket    = 664
# clear environment on exit
vacuum = true
# virtualenv表示使用的虚拟环境的目录
virtualenv = /home/chendong/.virtualenvs/guliedu
# logto表示日志文件
logto = /tmp/mylog.log
"""
# 14.2 进入虚拟环境,执行: uwsgi -i /home/chendong/桌面/GuLiEdu/config/uwsgi.ini &

## 15. 浏览器访问Ubuntu部署的Django项目: http://UbuntuIP



#################################################################################################################
### DailyFresh项目示例部署: Ubuntu
## uwsgi安装与配置部署项目:
# 注: windows系统不支持安装uwsgi
# 1.在Python虚拟环境下安装: pip install uwsgi 或 pip install uwsgi -i https://pipy.douban.com/simple
# 2.修改项目下的settings文件,内容如下
"""
DEBUG=FALSE
ALLOWED_HOSTS=[‘*’]
"""
# 3.在项目根目录下创建uwsgi.ini文件,内容如下
"""
[uwsgi]
# 使用nginx连接时使用
# socket=127.0.0.1:8080
# 直接使用uwsgi作为web服务器使用: 相当于 python manage.py run IP:PORT
http=127.0.0.1:8080
# chdir指定项目的目录路径
chdir=/home/chendong/桌面/DailyFresh
# wsgi-file指定项目中的wsgi.py文件路径,相对于项目目录
wsgi-file=dailyfresh/wsgi.py
# 指定启动的工作进程数以及指定工作进程中的线程数
processes=4
threads=2
# 主进程
master=True
# 保存启动后主进程的pid号
pidfile=uwsgi.pid
# daemonize指定uwsgi后台运行时,保存日志信息的文件
daemonize=uwsgi.log
# virtualenv指定项目使用的Python虚拟环境的路径
virtualenv=/home/chendong/.virtualenvs/dailyfresh
"""
# 4.uwsgi的启动与停止:
"""
启动:uwsgi --ini 配置文件路径       例如:uwsgi --ini uwsgi.ini
停止:uwsgi --stop uwsgi.pid路径     例如:uwsgi --stop uwsgi.pid
"""



## nginx + uwsgi 安装与配置部署项目:
# 1.首先是uwsgi安装与配置: 项目根根目录下创建uwsgi.ini文件,添加内容如下
"""
[uwsgi]
# 使用nginx+uwsgi作为web服务器使用:
# socket=127.0.0.1:8000
# 直接使用uwsgi作为web服务器使用: 相当于 python manage.py run IP:PORT
# http=127.0.0.1:8000
# chdir指定项目的目录路径
chdir=/home/chendong/桌面/DailyFresh
# wsgi-file指定项目中的wsgi.py文件路径,相对于项目目录
wsgi-file=DailyFresh/wsgi.py
# 指定启动的工作进程数以及指定工作进程中的线程数
processes=4
threads=2
# 主进程
master=True
# 保存启动后主进程的pid号
pidfile=uwsgi.pid
# daemonize指定uwsgi后台运行时,保存日志信息的文件
daemonize=uwsgi.log
# virtualenv指定项目使用的Python虚拟环境的路径
virtualenv=/home/chendong/.virtualenvs/dailyfresh
"""
# 2.nginx配置-请求转发给uwsgi
""" 修改nginx服务的配置文件: /usr/local/nginx/conf/nginx.conf
location / {
	include uwsgi_params;  # 包含uwsgi的请求参数
	uwsgi_pass uwsgi服务器的ip:port;  # 请求转交给uwsgi
}
"""
# 3.nginx配置-处理静态文件:
# 3.1项目中settings设置收集静态文件路径
"""
STATIC_ROOT='收集的静态文件路径' 例如:/home/chendong/桌面/DailyFresh/static/,最好在其他位置新建一个目录
"""
# 3.2收集静态文件的命令: python manage.py collectstatic
# 3.3收集完静态文件之后,让nginx提供静态文件,配置信息如下
""" 修改nginx服务的配置文件: /usr/local/nginx/conf/nginx.conf
location /static {
	alias /home/chendong/桌面/DailyFresh/static/; # 指定项目静态文件存放的目录,如settings中的STATIC_ROOT配置的路径一致
}
"""
# 4.nginx配置-请求转发给另外地址:
# 在location 对应的配置项中增加 proxy_pass 转发的服务器地址。
# 如当用户访问127.0.0.1时，在nginx中配置把这个请求转发给172.16.179.131:80(nginx)服务器，让这台服务器提供静态首页。
# 配置如下:
# location = /{
#     proxy_pass http://172.16.179.131;
# }
# 5.nginx配置-upstream实现负载均衡:
# ngnix 配置负载均衡时，在server配置的前面增加upstream配置项。
# upstream dailyfresh {
#     server 127.0.0.1:8080;
#     server 127.0.0.1:8081;
# }






