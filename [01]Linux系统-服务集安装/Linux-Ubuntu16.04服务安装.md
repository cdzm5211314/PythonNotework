# Ubuntu16.04(桌面系统)- 安装服务 #

### Ubuntu初始化状态配置:
```
# 问题1: 安装VMwareTools解决全屏问题:
复制文件: cp vmware****.tar.gz 到home下的桌面目录下
解压文件: tar -zxvf vmware****.tar.gz 
计入解压目录安装: sudo ./vmware-install.pl
# 问题2: 安装openssh-server服务解决远程连接问题:
安装: sudo apt-get install openssh-server
开启: sudo /etc/init.d/ssh start
# 问题3: 设置root账号的密码: sudo passwd root
# 问题4: ssh服务器拒绝密码,请再试一次
安装vim: sudo apt-get install vim
编辑文件: vim /etc/ssh/ssd_config
修改内容: PermitRootLogin yes  
重启ssh服务: service sshd restart
```

### 安装上传与下载服务:
* 安装wget服务: `sudo apt-get install wget`
* 安装lrzsz服务: `sudo apt-get install lrzsz`
* 本地文件上传到服务器: `rz`
* 服务器文件下载到本地: `sz test.tar`

### 开机提示"检测到系统程序出现问题":
* 打开文件: `vim /etc/default/apport`
* 修改内容: `enable = 1 ---> enable = 0`

### 安装Notepad++记事本:
```
# 服务安装:
sudo add-apt-repository ppa:notepadqq-team/notepadqq
sudo apt-get update
sudo apt-get install notepadqq
# 服务卸载:
sudo apt-get remove notepadqq
sudo add-apt-repository --removeppa:notepadqq-team/notepadqq
```

### 安装搜狗输入法:
```
下载并上传: https://pinyin.sogou.com/linux/?r=pinyin
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
sudo apt-get -f install
sudo apt-get update --fix-missing
sudo dpkg -i sogoupinyin_2.2.0.0108_amd64.deb
安装好后进行配置: im-config
重启Ubuntu系统后: fcitx-config-gtk3
```

### 设置Firefox浏览器中文:
```
# 第一种方式:
火狐浏览器输入: http://ftp.mozilla.org
语言包在xpi目录下，简体中文（zh-CN.xpi）/繁体（zh-TW.xpi）
如: http://ftp.mozilla.org/pub/firefox/releases/65.0.1/linux-x86_64/xpi/zh-CN.xpi
# 第二种方式: [通过]
sudo apt-get install firefox
sudo apt-get install firefox-locale-zh-hans
```

### 安装Google浏览器:
```
wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo dpkg -i google-chrome-stable_current_amd64.deb
```
***

### 升级Python3.5 ---> Python3.6: 未升级
```
sudo add-apt-repository ppa:jonathonf/python-3.6
sudo apt-get update
sudo apt-get install python3.6
# 期间需要输入Yes,调整Python3的优先级,使得3.6优先级较高
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.5 1
sudo update-alternatives --install /usr/bin/python3 python3 /usr/bin/python3.6 2
# 现在输入python系统默认为Python2,需要修改为Python3
[可略]sudo update-alternatives --install /usr/bin/python python /usr/bin/python2 100
[可略]sudo update-alternatives --install /usr/bin/python python /usr/bin/python3 150

修复Python3.5 升级 Python3.6后,终端terminal无法启动的问题:
cd /usr/lib/python3/dist-packages/gi/
sudo cp _gi.cpython-35m-x86_64-linux-gnu.so _gi.cpython-36m-x86_64-linux-gnu.so
sudo cp _gi_cairo.cpython-35m-x86_64-linux-gnu.so _gi_cairo.cpython-36m-x86_64-linux-gnu.so
```

### Python虚拟环境搭建: pipenv 或 virtualenv
```
sudo apt-get install python-pip  # 指向Python2
sudo apt-get install python3-pip # 指向Python3
sudo apt-get install virtualenv  # 会同时安装python-virtualenv和python3-virtualenv
sudo apt-get install virtualenvwrapper
# 或者已安装pip: 执行下面命令
sudo pip3 install pipenv
sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper
# 配置virtualwrapper环境变量: 
编辑文件: sudo vim ~/.bashrc 
添加内容: export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
添加内容: export WORKON_HOME=/envs
添加内容: source /usr/local/bin/virtualenvwrapper.sh
执行生效: source ~/.bashrc

# 注:查找virtualenvwrapper.sh: sudo find / -name virtualenvwrapper.sh
# 注:因为ubuntu默认使用Python2版本,所以需要配置: VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
```

### Python虚拟坏境常用命令: virtualenv
```
# 虚拟环境位置根据环境变量中的配置指定
创建Python3环境: mkvirtualenv -p /usr/bin/python3 envs_name
进入/切换虚拟环境: workon envs_name
退出虚拟环境: deactivate
删除已虚拟环境: rmvirtualenv envs_name
虚拟环境中安装模块包: pip3 install package_name
```

### Python虚拟环境常用命令: pipenv
```
# 创建虚拟环境: pipenv --three
# 创建虚拟环境: pipenv --python python3
# 进入虚拟环境: pipenv shell
# 退出虚拟环境: exit
# 删除虚拟环境[项目根目录]: `pipenv --rm` 
# 查看虚拟环境包列表: pip list
# 查看项目的根目录: `pipenv --where` 
# 查看虚拟环境目录: `pipenv --venv` 
# 查看Pytho解释器位置: `pipenv --py`
```

### 安装JDK服务:
```
下载JDK并上传到/opt/目录下: jdk-7u79-linux-x64.gz
解压文件: sudo tar -zxvf jdk-7u79-linux-x64.gz
# 添加Java_JDK环境变量:
编辑文件: sudo vim /etc/profile
添加内容: JAVA_HOME=/opt/jdk1.7.0_79
添加内容: PATH=/opt/jdk1.7.0_79/bin:$PATH
添加内容: export JAVA_HOME PATH
执行生效: source /etc/profile
查看是否成功: java -version 或 javac
```

### 安装Tomcat服务: 8080
```
下载Tomcat并上传到/opt/目录下: apache-tomcat-7.0.75.tar.gz
解压文件: sudo tar -zxvf apache-tomcat-7.0.75.tar.gz
编辑Tomcat启动脚本: sudo vim /opt/apache-tomcat-7.0.75/bin/startup.sh ---> 添加如下内容
JAVA_HOME=/opt/jdk1.7.0_79
JRE_HOME=/opt/jdk1.7.0_79/jre
PATH=$JAVA_HOME/bin:$JRE_HOME:$PATH
CLASSPATH=.:$JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
TOMCAT_HOME=/opt/apache-tomcat-7.0.75
进入到Tomcat服务的bin目录下启动Tomcat服务: sudo ./startup.sh
# 设置开机Tomcat自启动:
sudo vim /etc/rc.local ---> 添加如下内容
export JAVA_HOME=/opt/jdk1.7.0_79
/opt/apache-tomcat-7.0.75/bin/startup.sh start
修改文件权限: sudo chmod 777 /etc/rc.local
```

### 安装MySQL服务: 3306
```
# 开始安装MySQL服务:
sudo apt-get install mysql-server ---> 安装过程中需要设置MySQL服务root账号的密码:root
sudo apt install mysql-client
sudo apt install libmysqlclient-dev
# 查看是否成功安装并启动MySQL服务
sudo netstat -tap | grep mysql
# 测试登陆访问MySQL服务:
mysql -uroot -p  # 本机访问
mysql -h IP -u root -p  # 远程访问
# 设置MySQL允许远程访问: 修改配置文件
编辑文件: sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
注释内容: bind-address = 127.0.0.1:
本机登陆访问: mysql -uroot -p ---> 输入密码 
# 设置MySQL允许远程访问: 执行授权命令
mysql -uroot -p
grant all on *.* to root@'%' identified by '你的密码' with grant option;
flush privileges;
quit
重启MySQL服务: sudo service mysql restart
# 添加开机自启动: 
安装服务: sudo apt-get install sysv-rc-conf
设置自启动: sudo sysv-rc-conf --level 2345 mysql on
```

### 安装Redis服务: 6379
```
安装服务: sudo apt-get install redis-server
查看Redis服务系统进程: sudo ps -aux | grep redis
# 修改Redis配置信息: sudo vi /etc/redis/redis.conf
设置Redis服务密码: requirepass password
设置Redis允许远程访问: 注释[69行]: bind 127.0.0.1
重启Redis服务: sudo service redis restart
# 访问Redis服务:
redis-cli  ---> auth password  # 本机访问
redis-cli -a password  # 本机访问
redis-cli -h IP  # 远程访问
redis-cli -a password -h IP  # 远程访问
设置自启动: sudo sysv-rc-conf --level 2345 redis on
```

### 安装MongoDB服务: 27017 
```
### 默认安装是2.x版本
安装服务: sudo apt-get install mongodb
查看mongodb是否安装成功: mongo -version
查看mongodb服务运行状态: sudo service mongodb status
查看MongoDB服务默认安装位置: locate mongo
# MongoDB配置文件信息: sudo vim /etc/mongodb.conf
dbpath=/var/lib/mongodb               # 存放数据库文件的地方
logpath=/var/log/mongodb/mongodb.log  # 存放log的地方
#bind_ip = 127.0.0.1                  # 设置可以远程访问  mongo 10.0.244.100:27017/demo
# 关闭与启动MongoDB
sudo service mongodb stop 　　
sudo service mongodb restart
设置MongoDB开机自启动: sudo pgrep mongo -l  # 注: -l是英文字母l,不是阿拉伯数字1
# 设置密码访问: 略...
# 注: navicat武炼远程连接mongodb,需要升级到3.x版本

### 升级MongoDB2.x到3.x
导入包管理系统所需的key: sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv EA312927
# 官方提供无效: echo "deb http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
创建mongodb列表文件: echo "deb http://mirrors.aliyun.com/mongodb/apt/ubuntu xenial/mongodb-org/3.2 multiverse" | sudo tee /etc/apt/sources.list.d/mongodb-org-3.2.list
更新本地包数据库: sudo apt-get update
安装mongodb包: sudo apt-get install -y mongodb-org
# 未通过验证: sudo apt-get install -y mongodb-org --allow-unauthenticated
开启mongodb: sudo service mongod start
# MongoDB配置文件位置: sudo vim /etc/mongodb.conf
设置远程访问: 修改内容 bindIp: 0.0.0.0
开机自启动: sudo systemctl enable mongod
# 注: 升级后记得删除2.x版本的配置文件: /etc/mongodb.conf
```

### 安装Nginx服务: 80
```
预先安装GCC: sudo apt-get install gcc
预先安装PCRE: sudo apt-get install libpcre3 libpcre3-dev
预先安装zlib: sudo apt-get install zlib1g zlib1g-dev
预先安装OpenSSL: sudo apt-get install openssl openssl-dev
下在文件: wget http://nginx.org/download/nginx-1.13.6.tar.gz
解压文件: sudo tar -zxvf nginx-1.13.6.tar.gz
进入到解压目录: cd nginx-1.13.6
预编译: sudo ./configure --prefix=/usr/local/nginx 
安装Nginx服务:  make && make install 
启动Nginx服务: sudo /usr/local/nginx/sbin/nginx
浏览器访问测试: http://IP
# nginx安装位置: /usr/local/nginx
# nginx配置文件: /usr/local/nginx/conf/nginx.conf

### 设置Nginx开机自启动服务:
# 设置环境变量: vim /etc/profile
添加内容: export PATH=$PATH:/usr/local/nginx/sbin
内容生效: source /etc/profile
# 开机自启动脚本: vim /lib/systemd/system/nginx.service  ---> 添加内容如下
[Unit]
Description=nginx service
After=network.target 
[Service] 
Type=forking 
ExecStart=/usr/local/nginx/sbin/nginx
ExecReload=/usr/local/nginx/sbin/nginx -s reload
ExecStop=/usr/local/nginx/sbin/nginx -s quit
PrivateTmp=true 
[Install] 
WantedBy=multi-user.target
加入开机自启动命令: systemctl enable nginx

### Nginx命令:
取消自启动: systemctl disable nginx
停止nginx服务: systemctl stop nginx
重启nginx服务: systemctl restart nginx
```

### 安装Docker服务: 2375
```
# 安装http相关软件包:
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common
# 设置apt仓库地址:
curl -fsSL https://mirrors.aliyun.com/docker-ce/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository "deb [arch=amd64] https://mirrors.aliyun.com/docker-ce/linux/ubuntu $(lsb_release -cs) stable"
# 安装Docker软件:
sudo apt-get update
sudo apt-get install docker-ce  # 安装最新版的docker
sudo apt-get install docker-ce=18.03.0~ce-0~ubuntu  # 安装指定版本的docker
检查是否安装成功: docker --version
查看Docker的状态: sudo service docker status
添加开机自启动: systemctl enable docker 

### 配置Docker镜像加速源: 阿里云
编辑文件: vim /etc/docker/daemon.json
添加内容: {"registry-mirrors": ["https://1qlfqh72.mirror.aliyuncs.com"]}
重新加载: systemctl daemon-reload
重新启动: systemctl restart docker
```


