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

### PyCharm ---> Settings ---> Build,Execution,Deployment(构建,执行,发布)

### PyCharm工具使用: 模拟发送请求响应数据
```
选择 ---> Tools ---> HTTP Client ---> Test RESTful Web Service
```

### PyCharm工具使用: 部署文件到Linux系统(ContOS7.2)
```
# 1.首先使用PyCharm打开一个文件夹,这个文件夹就是我们要映射到远程Linux系统的文件夹,如: E:\WorkSpace
# 2.选择 ---> Tools ---> Deproyment ---> Configuration... ---> 点击"+"图标 ---> 选择"SFTP"选项,进入到sftp配置页面
# 3.随便取个名字(如:CentosServer) ---> 填写好Linux系统的IP地址,用户名和密码 ---> 点击"Test Connection"测试是否连接成功
# 4.进入到"Mappings"配置页面: Local path(本地路径) 和 Deproyment path(远程路径), 点击远程路径选择Linux系统远程目录,完成与本地目录的映射
# 5.在PyCharm项目目录下新建文件"test.py",然后右键文件 ---> Deployment ---> Upload to,上传文件到远程目录
# 6.右键PyCharm项目目录 ---> Deployment ---> Download from,下载远程目录文件到本地文件夹
```

### PyCharm工具使用: 远程连接及管理Docker(ContOS7.2)
```
使远端服务器上的Docker能与本机PyCharm进行连接和通信,进行如下设置
# 1.开放远端连接: vi /lib/systemd/system/docker.service
ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock  # 注释或删除
ExecStart=/usr/bin/dockerd -H tcp://0.0.0.0:2375 -H unix:///var/run/docker.sock   # 添加
# 2.添加到环境变量: vi /etc/profile
添加: export DOCKER_HOST=tcp://0.0.0.0:2375
生效: source /etc/profile
# 3.重启服务: systemctl daemon-reload && systemctl restart docker
# 4.打开PyCharm中的Docker连接窗口: View ---> Tool Windows ---> Docker
# 5.在弹出的窗口中选择"configure" ---> 点击"+"图标,然后填写连接信息:(名字随便取),TCP模式,IP地址为远端的IP地址
# 6.当下方出现"Connection successful"表示连接成功,然后就可以远程对Docker进行管理和信息显示
```







