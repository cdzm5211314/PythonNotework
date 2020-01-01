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
菜单栏选择 ---> Tools ---> HTTP Client ---> Test RESTful Web Service
```

### PyCharm工具使用: 部署文件到Linux系统(ContOS7.2)
```
# 1.首先使用PyCharm打开一个文件夹,这个文件夹就是我们要映射到远程Linux系统的文件夹,如: E:\WorkSpace
# 2.菜单栏Tools ---> Deproyment ---> Configuration... 
或 菜单栏File ---> settings ---> Build,Execution,Deployment ---> Deproyment
---> 点击"+"图标添加,"name"名字随便取 
---> 选择"SFTP"模式,进入到sftp配置页面
# 3.随便取个名字(如:CentosServer) 
---> 填写好Linux系统的IP地址,用户名和密码 
---> 点击"Test Connection"测试是否连接成功
---> Advanced: 设置远程连接活跃时间(10秒)和设置编码格式utf-8
注: Root path(可省略): 为Linux系统中项目的上一级目录
# 4.进入到"Mappings"配置页面: 
---> Local path: 本地目录路径
---> Deproyment path: 远程目录路径
---> Ok, 完成本地目录与远程目录的映射
# 5.右键PyCharm项目目录 ---> 然后右键文件 ---> Deployment 
---> Upload to Xxx: 上传本地目录文件到远程目录
---> Download from Xxx: 下载远程目录文件到本地目录
---> Sync with from Xxx: 对比本地目录文件与服务器目录文件
```

### PyCharm工具使用: 配置远程Python环境解释器(ContOS7.2)
```
# 1. 菜单栏File ---> settings ---> Project Insterpreter 
---> Add(添加Python解释器) 
---> SSH Insterpreter(远程服务)
# 2. 配置远程Python解释器: 
---> Existing server configuration 配置信息
---> Deproyment configuration (选择之前添加的远程服务名称) 
---> More(选择把IDE的设置Copy拷贝过去还是More移动过去) 
---> Next 
---> Interpreter(选择远程Python解释的pyhon位置路径)
# 3. Finish, 完成远程Python解释器配置
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
# 4.打开PyCharm中的Docker连接窗口: 菜单栏View ---> Tool Windows ---> Docker
或 菜单栏View ---> Tool Windows ---> Services ---> Add Service(第一次) ---> Docker Connection
或 菜单栏File ---> settings ---> Build,Execution,Deployment ---> Docker
---> 点击"+"图标添加,"name"名字随便取
---> TCP scoket模式: 配置信息
---> Engine API URL: 远程服务的IP地址,如tcp://localhost:2375
---> 当下方出现"Connection successful"表示连接成功,然后就可以远程对Docker进行管理和信息显示
---> Path mappings: 可以进行本地目录与远程服务目录的映射
# 5.当出现"Connection successful"表示连接成功
# 6.Ok, 然后就可以远程对Docker进行管理和信息显示
```







