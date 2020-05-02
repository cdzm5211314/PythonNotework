### Flask框架内置模块与函数: pip install flask
- from flask import Flask
- from flask import make_response  `返回response对象`
- from flask import render_template  `返回xxx.html模版`
- from flask import redirect  `url重定向`
- from flask import url_for `url反向解析`
- from flask import jsonify  `返回json字符串`
- from flask import request  `获取请求信息`
- from flask import session  `session会话`
- from flask import Blueprint  `蓝图:用于实现单个应用的视图,模版,静态文件的集合`

### Flask框架扩展插件包:
- Flask框架扩展(表单): pip install flask-wtf
    - from flask_wtf import FlaskForm # 页面表单模型类
    - from wtforms import StringField,PasswordField # 表单字段类型
    - from wtforms import SubmitField # 表单提交按钮
    - from wtforms.validators import DataRequired,EqualTo # 表单字段验证器

- Flask框架扩展(脚本命令行): pip install flask-script
    - from flask_script import Manager # 命令行管理工具
    - from flask_script import Shell
    
- Flask框架扩展(ORM): pip install flask-sqlalchemy
    - from flask_sqlalchemy import SQLAlchemy # 强大的关系型数据库框架
        - MySQL数据库 依赖于 flask-sqlalchemy框架
        - MySQL数据库的安装: pip install flask-mysqldb
        
- Flask框架扩展(管理迁移数据库): pip install flask-migrate
    - flask-migrate 依赖于 flask-script 需安装: pip install flask-script
    - from flask-migrate import Migrate # 数据库的迁移,回退...等工具
    - from flask-migrate import MigrateCommand # 数据库执行者命令

- Flask框架扩展(邮件): pip install flask-mail
    - from flask_mail import Mail
    - from flask_mail import Message

- Flask框架扩展(session): pip install flask-session
    - from flask_session import Session

- Flask框架扩展(模版): pip install flask-bootstrap
    - from flask_bootstrap import Bootstrap

- Flask框架扩展(调试工具): pip install flask-debugtoolbar
    - from flask_debugtoolbar import DebugToolbarExtension


### Flask程序部署:
- 安装gunicorn: pip install gunicorn
- 程序部署(守护进程): gunicorn -w 4 -b 127.0.0.1:5000 -D --access-logfiles ./logs/logfile.log 运行文件名称:Flask程序实例名
- 程序部署: gunicorn -w 4 -b 127.0.0.1:5000 --access-logfiles ./logs/logfile.log 运行文件名称:Flask程序实例名




