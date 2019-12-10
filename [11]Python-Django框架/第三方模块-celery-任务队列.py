# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-06 14:10

# celery : 任务队列,异步操作,如发送邮件
# 安装: pip install celery

# 任务发出者,中间人,任务处理者可以在同一台电脑,也可以不在同一台电脑上

### 任务发出者: 项目代码
## 一般使用celery做异步操作,通常会在项目目录下新建一个包,专门存放任务,如: celery_tasks
# 1.在包下新建一个文件,如: tasks.py
from celery import Celery
from django.conf import settings
from django.core.mail import send_mail
# 2.创建一个Celery类的对象,broker指定中间人,使用redis数据库
app = Celery('celery_tasks.tasks',broker='redis://192.168.208.128:6379/3')  # 第一个参数随便写,一般会写成此文件的路径,如:celery_tasks.tasks
# app = Celery('celery_tasks.tasks',broker='redis://:password@192.168.208.128:6379/3')  # redis有密码
# 3.定义任务函数
@app.task
def send_register_active_email(to_email,username,token):
    '''发送注册用户激活邮件'''
    subject = '天天生鲜欢迎信息'  # 邮件主题信息
    message = ''  # 邮件正文内容,message不能解析html信息,所以需要使用:html_message
    from_email = settings.EMAIL_FROM  # 发件人邮箱
    recipient_list = [to_email]  # 收件人邮箱列表
    html_message = '<h1>%s,欢迎你成为天天生鲜注册会员,</h1>请点击下面链接激活你的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (
        username, token, token)
    send_mail(subject, message, from_email, recipient_list, html_message=html_message)
# 4.在项目代码中发送任务
from celery_tasks.tasks import send_register_active_email
send_register_active_email.delay(to_email,username,token)



### 任务列队(中间人-broker): 使用redis



### 任务处理者(worker): 也需要任务代码(拷贝一份项目代码)
# 执行命令: celery -A 'celery任务文件路径' worker -l info
# 如: (dailyfresh) chendong@UbuntuServer:~/桌面/DailyFresh$ celery -A celery_tasks.tasks worker -l info
## 报错:因为是django项目,tasks.py文件有django的启动配置信息,所以需要在 项目目录下/celery_tasks/tasks.py文件中添加如下信息
""""
# 加载django项目的配置信息:
# import os
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "DailyFresh.settings")
# 导入django,并启动django项目
# import django
# django.setup()
"""
# Celery启动: (dailyfresh) chendong@UbuntuServer:~/桌面/DailyFresh$ celery -A celery_tasks.tasks worker -l info


