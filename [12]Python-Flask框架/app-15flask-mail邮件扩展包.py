# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# Flask-Mail通过包装了Python内置的smtplib包,可以用在Flask程序中发送邮件
# Flask-Mail连接到简单邮件协议（Simple Mail Transfer Protocol,SMTP）服务器,并把邮件交给服务器发送
# 安装: pip install flask-mail

from flask import Flask
from flask_mail import Mail, Message

app = Flask(__name__)

# 配置邮件: 服务器 / 端口 / 传输层安全协议 / 邮箱地址 / 密码
# 注: 如果之前配置了参数信息,使用update会覆盖之前设置的参数
app.config.update(
    DEBUG=True,
    MAIL_SERVER='smtp.qq.com',
    MAIL_PROT=465,
    MAIL_USE_TLS=True,
    MAIL_USERNAME='371673381@qq.com',
    MAIL_PASSWORD='goyubxohbtzfbidd',
)
mail = Mail(app)


@app.route('/')
def index():
    # 参数说明: 第一个参数表示发送的邮件标题,sender发送方(邮箱地址), recipients接受方(邮箱地址列表)
    msg = Message("This is a test ", sender='371673381@qq.com', recipients=['shengjun@163.com', '371673381@qq.com'])
    # 邮件内容
    msg.body = "Flask test mail"
    # 发送邮件
    mail.send(msg)
    return 'send success'


if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):
    app.run(debug=True)  # 以debug调试模式开启flask程序
