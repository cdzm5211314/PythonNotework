# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-14 13:13

# 使用Flask-WTF表单扩展，可以帮助进行CSRF验证，帮助我们快速定义表单模板，而且可以帮助我们在视图中验证表的数据
# 安装: pip install Flask-WTF
# 注: 使用Flask-WTF扩展,需要设置 SECRET_KEY 的配置参数

from flask import Flask, render_template, redirect, url_for, session
from flask_wtf import FlaskForm  # 表单类
from wtforms import SubmitField, StringField, PasswordField  # 表单字段类型
from wtforms.validators import DataRequired, EqualTo  # 表单验证器

app = Flask(__name__)

# 设置 SECRET_KEY 的配置参数
app.config['SECRET_KEY'] = 'asdfghjkl_qwertyuiop_zxcvbnm'


# 自定义表单的模型类
class RegisterForm(FlaskForm):
    '''自定义的注册表单模型类'''
    #                           名字          验证器
    user_name = StringField(label='用户名', validators=[DataRequired('用户名不能为空')])
    password = PasswordField(label='密码', validators=[DataRequired('密码不能为空')])
    password2 = PasswordField(label='确认密码', validators=[DataRequired('确认密码不能为空'), EqualTo('password', '两次密码不一致')])
    submit = SubmitField(label='提交')

# html模版中获取自定义表单
'''
<form method="post">
    <!-- 设置csrf_token -->
    {{ registerForm.csrf_token }}

    <p>{{ registerForm.user_name.label }}
    {{ registerForm.user_name }}</p>
    {% for msg in registerForm.user_name.errors %}
        <p>{{ msg }}</p>
    {% endfor %}

    <p>{{ registerForm.password.label }}
    {{ registerForm.password }}</p>
    {% for msg in registerForm.password.errors %}
        <p>{{ msg }}</p>
    {% endfor %}

    <p>{{ registerForm.password2.label }}
    {{ registerForm.password2 }}</p>
    {% for msg in registerForm.password2.errors %}
        <p>{{ msg }}</p>
    {% endfor %}

    {{ registerForm.submit }}
</form>
'''

@app.route('/register', methods=['GET','POST'])
def register():
    # 创建自定义表单模型类对象,如果是post请求,前端发送了数据,flask会把数据在构造registerForm对象的时候,存放到对象中
    registerForm = RegisterForm()
    # 校验registerForm表单传递的数据是否合理
    # 如果registerForm中的数据完全满足所有的验证码规则,则返回True,否则返回Flase
    if registerForm.validate_on_submit():
        # 表示验证合格,提取数据
        uname = registerForm.user_name.data
        pwd = registerForm.password.data
        pwd2 = registerForm.password2.data

        session['username'] = uname  # 把用户名名保存在session中

        print(uname,pwd,pwd2)
        return redirect(url_for('index'))

    # return 'hello'
    # return render_template('form_wtf.html')
    return render_template('form_wtf.html', registerForm=registerForm)

@app.route('/index')
def index():
    username = session.get('username')
    return '用户%s注册成功' %username

if __name__ == '__main__':
    # def run(self, host=None, port=None, debug=None, load_dotenv=True, **options):

    app.run(debug=True)  # 以debug调试模式开启flask程序
