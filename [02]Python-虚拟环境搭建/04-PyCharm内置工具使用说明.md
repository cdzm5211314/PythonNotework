### 代码自动补全内容提示说明:
```
# F ---> Function   函数     模块
# v ---> Variable   变量     模块
# c ---> Class      类       模块
# m ---> Method     方法     类中定义
# f ---> Field      属性     类中定义
# p ---> Paramter   参数     模块.函数, 实例对象(类).方法
# p ---> Property
```

### PyCharm工具使用: 模拟发送请求响应数据
```
选择 ---> Tools ---> HTTP Client ---> Test RESTful Web Service
```

### PyCharm工具使用: 部署文件到Linux系统
```
# 1.首先使用PyCharm打开一个文件夹,这个文件夹就是我们要映射到远程Linux系统的文件夹,如: E:\WorkSpace
# 2.选择 ---> Tools ---> Deproyment ---> Configuration... ---> 点击"+"图标 ---> 选择"SFTP"选项,进入到sftp配置页面
# 3.随便取个名字(如:CentosServer) ---> 填写好Linux系统的IP地址,用户名和密码 ---> 点击"Test Connection"测试是否连接成功
# 4.进入到"Mappings"配置页面: Local path(本地路径) 和 Deproyment path(远程路径), 点击远程路径选择Linux系统远程目录,完成与本地目录的映射
# 5.在PyCharm项目目录下新建文件"test.py",然后右键文件 ---> Deployment ---> Upload to,上传文件到远程目录
# 6.右键PyCharm项目目录 ---> Deployment ---> Download from,下载远程目录文件到本地文件夹
```









