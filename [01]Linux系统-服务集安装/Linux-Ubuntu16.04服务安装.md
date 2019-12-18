# Ubuntu16.04(桌面系统)- 安装服务 #

### 安装上传与下载服务:
* 安装wget服务: `sudo yum -y install wget`
* 安装lrzsz服务: `sudo yum install lrzsz`
* 本地文件上传到服务器: `rz`
* 服务器文件下载到本地: `sz test.tar`

### 开机提示"检测到系统程序出现问题":
* 安装gksu: `sudo apt install gksu`
* 打开文件: `gksu gedit /etc/default/apport`
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

### 升级Python3.5 ---> Python3.6:
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
```

### Python虚拟环境搭建:
```
sudo apt-get install python-virtualenv
sudo apt-get install virtualenvwrapper
# 或者已安装pip: 执行下面命令
sudo pip3 install virtualenv
sudo pip3 install virtualenvwrapper
# 配置virtualwrapper环境变量: 
编辑文件: sudo vim ~/.bashrc 
添加内容: export WORKON_HOME=$HOME/.virtualenvs
添加内容: source /usr/share/virtualenvwrapper/virtualenvwrapper.sh
执行生效: source ~/.bashrc
```

### Python虚拟坏境常用命令:
```
# 虚拟环境位置根据环境变量中的配置指定
创建Python3环境: mkvirtualenv -p /usr/bin/python3.6 envs_name
进入/切换虚拟环境: workon envs_name
退出虚拟环境: deactivate
删除已虚拟环境: rmvirtualenv envs_name
虚拟环境中安装模块包: pip3 install package_name
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
# 查看系统是否安装过MySQL服务:
sudo netstat -tap | grep mysql
# 开始安装MySQL服务:
sudo apt-get install mysql-server ---> 安装过程中需要设置MySQL服务root账号的密码:root
sudo apt install mysql-client
sudo apt install libmysqlclient-dev
# 查看是否成功安装并启动MySQL服务
sudo netstat -tap | grep mysql
# 测试登陆访问MySQL服务:
mysql -uroot -p  # 本地访问
mysql -h IP -u root -p  # 远程访问
# 设置MySQL允许远程访问:
编辑文件: sudo vim /etc/mysql/mysql.conf.d/mysqld.cnf
注释内容: bind-address = 127.0.0.1:
本机登陆访问: mysql -uroot -p ---> 输入密码 
# 设置允许远程访问:
grant all on *.* to root@'%' identified by '你的密码' with grant option;
flush privileges;
quit
重启MySQL服务: sudo service mysql restart
```

### 安装Redis服务: 6379
```
安装服务: sudo apt-get install redis-server
查看Redis服务系统进程: sudo ps -aux | grep redis
修改Redis配置信息: sudo vi /etc/redis/redis.conf
设置Redis服务密码: requirepass password
设置Redis允许远程访问: 注释[69行]: bind 127.0.0.1
重启Redis服务: sudo /etc/init.d/redis-server restart
# 访问Redis服务:
redis-cli  ---> auth password  # 本机访问
redis-cli -a password  # 本机访问
redis-cli -a password -h IP  # 远程访问
```

### 安装MongoDB服务: 27017 
```
安装服务: sudo apt-get install mongodb
查看mongodb是否安装成功: mongo -version
查看mongodb服务运行状态: systemctl status mongodb.service
查看MongoDB服务默认安装位置: locate mongo
# MongoDB配置文件信息: sudo vi /etc/mongodb.conf
dbpath=/var/lib/mongodb               # 存放数据库文件的地方
logpath=/var/log/mongodb/mongodb.log  # 存放log的地方
#bind_ip = 127.0.0.1                  # 设置可以远程访问  mongo 10.0.244.100:27017/demo
# 关闭与启动MongoDB
sudo service mongodb stop 　　
sudo service mongodb start
设置MongoDB开机自启动: pgrep mongo -l  # 注: -l是英文字母l,不是阿拉伯数字1
# 设置密码访问: 略...
```

### 安装Nginx服务: 80
```
解压文件: sudo tar -zxvf nginx-1.8.1.tar.gz
进入到解压目录: cd nginx-1.8.1
预编译: sudo ./configure
安装Nginx服务:  make && make install 
启动Nginx服务: sudo /usr/local/nginx/sbin/nginx
浏览器访问测试: http://IP
# 设置Ngnix开机自启动: sudo vim /etc/rc.local
添加内容: /usr/local/nginx/sbin/nginx
# nginx安装位置: /usr/local/nginx
# nginx配置文件: /usr/local/nginx/conf/nginx.conf
```



