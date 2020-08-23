# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-31 14:53

from django.core.mail import send_mail
from django.conf import settings

### settings.py:发送邮件配置
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.163.com'  # smpt服务地址
EMAIL_PORT = 25  # 端口号
EMAIL_HOST_USER = 'config***@163.com'  # 发送邮件的邮箱地址即发件人
EMAIL_HOST_PASSWORD = 'asd*****'  # 发送邮件的邮箱[即发件人]中设置的客户端授权密码
EMAIL_FROM = '天天生鲜<configure@163.com>'  # 收件人看到的发件人


### views.py代码: send_mail(subject, message, from_email, recipient_list, html_message=html_message)
## subject = '天天生鲜欢迎信息'  # 邮件标题信息
## message = '邮件正文内容'
## html_message = '<h1>%s,欢迎你成为天天生鲜注册会员,</h1>请点击下面链接激活你的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
# 注: 邮件正文内容,message不能解析html信息,所以使用:html_message
## from_email = settings.EMAIL_FROM  # 发件人邮箱
## recipient_list = [email]  # 收件人邮箱列表

## send_mail(subject, message, from_email, recipient_list, html_message=html_message)

##########################################################################################################
### 发送邮件验证码代码封装: utils/send_mail_utils
from django.core.mail import send_mail
from django.conf import settings
import string
import random
# 生成验证码(随机字符串)
def get_random_code(slen):
    return ''.join(random.sample(string.ascii_letters + string.digits, slen))

def send_mail_code(email,send_type):
    pass
    ## 1.获取验证码: get_random_code(6)

    ## 2.settings配置邮件信息
    # EMAIL_HOST = 'smtp.163.com'                      # smpt服务地址
    # EMAIL_PORT = 25                                  # 端口号
    # EMAIL_HOST_USER = 'configureadmin@163.com'       # 发送邮件的邮箱地址即发件人
    # EMAIL_HOST_PASSWORD = 'asdfghjkl123456'          # 发送邮件的邮箱[即发件人]中设置的客户端授权密码
    # EMAIL_FROM = '谷粒教育<configureadmin@163.com>'  # 收件人看到的发件人

    ## 3.发送邮件的具体内容信息
    # subject = '天天生鲜欢迎信息'      # 邮件标题信息
    # message = ''                      # 邮件正文内容
    # html_message = '<h1>%s,欢迎你成为天天生鲜注册会员,</h1>请点击下面链接激活你的账户<br/><a href="http://127.0.0.1:8000/user/active/%s">http://127.0.0.1:8000/user/active/%s</a>' % (username, token, token)
    # 注: 邮件正文内容,message不能解析html信息,所以使用:html_message
    # from_email = settings.EMAIL_FROM  # 邮件发件人邮箱
    # recipient_list = [email]          # 邮件收件人邮箱列表

    # send_mail(subject,message,from_email,recipient_list)


