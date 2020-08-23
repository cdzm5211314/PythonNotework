# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @DateTime: 2020/8/23 12:18


# 发送邮件
def util_send_mail(request, email):
    # 根据email获取到用户的信息
    user = UserProfile.objects.filter(email=email).first()
    # print(user, email)
    random_code = str(uuid.uuid4())  # 获得一个随机码
    request.session[random_code] = user.id  # 把用户的id信息保存到session中

    # 发送邮件的标题
    subject = "个人博客找回密码"
    # 发送邮件的正文内容
    # message = """
    # 可爱的用户:
    #      你好!此链接用于找回密码,请点击链接: <a href='http://127.0.0.1:8000/blog/updatepasswd/?c=%s'>修改密码</a>,
    #      如果链接不能点击,请复制:
    #      http://127.0.0.1:8000/blog/updatepasswd/?c=%s
    #
    # """ % (random_code, random_code)
    # 发件人邮箱
    # from_email = EMAIL_HOST_USER
    # 收件人列表
    # recipient_list = [email]
    # 发送邮件的正文内容,会覆盖message的内容
    html_message = """
    可爱的用户: <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;你好!此链接用于找回密码,请点击链接: <a href='http://127.0.0.1:8000/blog/updatepasswd/?c=%s'>修改密码</a>, <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;如果链接不能点击,请复制: <br />
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;http://127.0.0.1:8000/blog/updatepasswd/?c=%s <br />

    """ % (random_code, random_code)

    result = send_mail(subject, "", EMAIL_HOST_USER, [email,], html_message=html_message)

    return result

