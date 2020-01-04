# CentOS7.2(最小系统) - 安装服务 #

### 安装上传与下载服务:
- 安装wget服务: sudo yum -y install wget
- 安装lrzsz服务: sudo yum install lrzsz
- 本地文件上传到服务器: rz
- 服务器文件下载到本地: sz test.tar



### Docker服务安装: 2375
- 安装前的准备依赖  
```
yum -y install gcc  
yum -y install gcc-c++
yum install -y yum-utils device-mapper-persistent-data lvm2
# yum-config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo
yum-config-manager --add-repo http://mirrors.aliyun.com/docker-ce/linux/centos/docker-ce.repo
yum makecache fast
```
- 安装Docker服务
```
yum -y install docker-ce
```
- 启动Docker服务
```
systemctl start docker
```
- 测试安装成功
```
docker version 
```
- 配置镜像加速器
```
1.创建目录: mkdir -p /etc/docker
2.创建文件: vi /etc/docker/daemon.json
3.添加如下内容:
# 网易云
{
"registry-mirrors": ["http://hub-mirror.c.163.com"]
 }
# 阿里云
{
"registry-mirrors": ["https://1qlfqh72.mirror.aliyuncs.com"]
}
4.重新加载: systemctl daemon-reload

```
- Docker基本命令
```
启动: systemctl start docker
停止: systemctl stop docker
重启: systemctl restart docker
运行状态: systemctl status docker
开机自启动: systemctl enable docker
```
- 卸载Docker服务
```
停止: systemctl stop docker 
卸载: yum -y remove docker-ce
删除: rm -rf /var/lib/docker
```
- 测试运行
```
docker run hello-world
```



### Nginx服务安装: 80
- 安装 pcre openssl zlib gcc 依赖: 
```
直接安装: yum -y install gcc zlib zlib-devel pcre-devel openssl openssl-devel
```
- 下载Nginx压缩包并安装
```
http://nginx.org ---> nginx-1.12.2.tar.gz
解压压缩文件执行: tar -xvf nginx-1.12.2.tar.gz
进入解压目录执行: ./configure 
进入解压目录执行: make && make install 
```
- Nginx安装位置与配置文件
```
nginx安装位置: /usr/local/nginx
nginx配置文件: /usr/local/nginx/conf/nginx.conf
```
-  Nginx环境变量与自启动
```
# 环境变量
编辑文件: vi /etc/profile
添加内容: export PATH=$PATH:/usr/local/nginx/sbin
立即生效: source /etc/profile

# 开机自启动
进入到: cd /lib/systemd/system/
创建文件: vi nginx.service
添加内容如下:
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

加入开机自启动: systemctl enable nginx

# nginx基本命令
取消自启动: systemctl disable nginx
启动nginx服务: systemctl start nginx
停止nginx服务: systemctl stop nginx
重启nginx服务: systemctl restart nginx
查询nginx状态: systemctl status nginx
```
- 常见的一个错误
```
Warning: nginx.service changed on disk. Run 'systemctl daemon-reload' to reload units.
问题解决: systemctl daemon-reload
```



### MySQL5.6服务安装: 3306
- 安装前的准备工作
```
查看是否安装了MySQL服务: rpm -qa | grep mysql ---> 空值表示未安装
查看是否安装了Mariadb数据库: rpm -qa | grep -i mariadb
卸载已经安装的Mariadb数据库: rpm -qa|grep mariadb|xargs rpm -e --nodeps
```
- 下载安装包文件并安装
```
1.下载安装包: wget http://repo.mysql.com/mysql-community-release-el7-5.noarch.rpm
提示问题: -bash: wget: 未找到命令
解决问题: yum -y install wget
2.安装下载文件: rpm -ivh mysql-community-release-el7-5.noarch.rpm
安装完成之后,会在/etc/yum.repos.d/目录下新增mysql-community.repo mysql-community-source.repo 两个yum源文件
3.查看可用的 mysql 安装文件: yum repolist all | grep mysql 
```
- 安装MySQL服务
```
1.安装MySQL服务: yum install mysql-server
2.检测是否安装成功: rpm -qa | grep mysql
```
- MySQL服务基本命令
```
启动MySQL服务: systemctl start mysqld
停止MySQL服务: systemctl stop mysqld
重启MySQL服务: systemctl restart mysqld
开机自启动MySQL服务: systemctl enable mysqld
```
- MySQL服务基本设置
```
# 设置MySQL的密码(默认为空):
mysql -u root -p
use mysql;
update user set password=PASSWORD("这里输入root用户密码") where User='root';
flush privileges;
# 设置MySQL远程登陆:
GRANT ALL PRIVILEGES ON *.* TO 'your username'@'%' IDENTIFIED BY 'your password';
```



### Redis服务安装: 6379
- 下载安装Redis
```
安装依赖: yum install -y gcc
安装依赖: yum install -y epel-release
下载redis安装包: wget http://download.redis.io/releases/redis-4.0.13.tar.gz
解压包文件: tar -zxvf redis-4.0.13.tar.gz
执行命令: make MALLOC=libc
进入解压目录,指定目录安装redis服务: make && make PREFIX=/usr/local/redis install
复制配置文件redis.conf到redis安装目录的bin目录下: cp redis.conf /usr/local/redis/bin
```
- 将redis添加到系统服务
```
创建文件: vi /usr/lib/systemd/system/redis.service
添加如下内容:
[Unit]
Description=The redis-server Process Manager
After=syslog.target network.target
 
[Service]
Type=simple
PIDFile=/var/run/redis.pid
ExecStart=/usr/local/redis/bin/redis-server /usr/local/redis/bin/redis.conf
ExecReload=/bin/kill -s HUP $MAINPID
ExecStop=/bin/kill -s QUIT $MAINPID
 
[Install]
WantedBy=multi-user.target
```
- redis基本命令
```
启动redis服务: systemctl start redis
停止redis服务: systemctl stop redis
开机自启动redis服务: systemctl enable redis
```
- 链接redis并修改配置文件
```
# 配置redis系统环境变量: vi /etc/profile ---> export PATH=/usr/local/redis/bin:$PATH ---> source /etc/profile
# 配置环境变量后本地链接redis: redis-cli
# 修改redis.conf配置文件: vi /usr/local/redis/bin/redis.conf
设置密码[500行]: requirepass password
设置远程访问[69行]: #bind 127.0.0.1

```



### MongoDB服务安装: 27017
- 配置mongodb的yum源:
```
1.编辑文件: vi /etc/yum.repos.d/mongodb-org-4.0.repo
2.添加如下内容:
[mongodb-org-4.0]
name=MongoDB Repository
baseurl=https://repo.mongodb.org/yum/redhat/$releasever/mongodb-org/4.0/x86_64/
gpgcheck=1
enabled=1
gpgkey=https://www.mongodb.org/static/pgp/server-4.0.asc
3.执行: yum makecache
```
- 安装mongodb服务
```
安装mongo服务: yum -y install mongodb-org
```
- mongo服务基本命令
```
启动mongo服务: systemctl start mongod
停止mongo服务: systemctl stop mongod
查看mongo服务状态: systemctl status mongod
开机自启动mongo服务: systemctl enable mongod
```
- 修改配置文件
```
查看mongo安装信息: whereis mongod
默认数据位置: /var/lib/mongo
默认日志位置: /var/log/mongodb/mongod.log
默认配置文件位置: /etc/mongod.conf
数据: storage.dbPath
日志: systemLog.path 
设置远程访问: vi /etc/mongod.conf
修改 bindIp: 127.0.0.1 ---> bindIp: 0.0.0.0 

```


### Python3.6.5安装:
- 下载压缩文件解压,并进入到解压目录
```
wget https://www.python.org/ftp/python/3.7.2/Python-3.7.2.tgz
tar -xf Python-3.6.5.tgz
cd ./Python-3.6.5
```
- 准备编译环境并安装依赖包
```
yum install -y gcc
yum install -y zlib* openssl*
```
- 安装Python3.6.5
```
# 预编译,--enable-optimizations配置项用于提高Python安装后的性能,但是会导致安装慢
./configure --prefix=/usr/local/python3 --enable-optimizations
# 安装
make install
```
- 配置环境变量
```
vi /etc/profile
export PATH=$PATH:/usr/local/python3/bin
source /etc/profile
```
- 解释器: `python(pip)执行Python2` 和 `python3(pip3)指向Python3`
- 安装外部库测试
```
pip3 install pipenv
```

- 创建Python软链接(未使用)
```
第一种:
# 默认python指向Python2,这里创建python3指向Python3
ln -s /usr/local/python3/bin/python3.6 /usr/bin/python3
# 保留pip指向Pip2,这里创建pip3指向Pip3
ln -s /usr/local/python3/bin/pip3 /usr/bin/pip3
升级Pip3: pip3 install --upgrade pip
# 如果pip3无法使用,需要添加环境变量
vi /etc/profile
export PATH=$PATH:/usr/local/python3/bin
source /etc/profile

第二种: (使用此种方式)
# 默认python指向Python2,这里创建python3指向Python3
备份原文件为python2: sudo mv /usr/bin/python /usr/bin/python2
创建Python3软链接: sudo ln -s /usr/local/python3/bin/python3.6 /usr/bin/python
备份源文件为pip2: sudo mv /usr/bin/pip /usr/bin/pip2
创建Python3的pip软链接: sudo ln -s /usr/local/python3/bin/pip3 /usr/bin/pip
# 终端测试: python  ---> 输出: python3.6.5
注:在Centos中,yum源使用的是Python2.7,替换为Python3以后,yum源无法正常工作,所以我们需要修改yum配置文件
更改权限: sudo chmod 777 /usr/bin/yum
修改内容: vi /usr/bin/yum
将 #!/usr/bin/python 改为 #!/usr/bin/python2.7
sudo yum search pip ---> 用于测试yum是否正常工作
```

* 安装Scrapy框架(下载Twisted模块包)
```
下载: wget https://twistedmatrix.com/Releases/Twisted/19.10/Twisted-19.10.0.tar.bz2
解压: tar -xf Twisted-19.10.0.tar.bz2
进入解压目录: cd Twisted-19.10.0
安装: python3 setup.py installl
然后就可以安装scrapy: pip3 install scrapy
```

### 安装Python虚拟环境: virtualenv
- 安装虚拟环境
```
# 创建存放虚拟环境的隐藏目录: sudo mkdir -p /envs
pip3 install virtualenv
pip3 install virtualenvwrapper
```
- 配置环境变量
```
编辑文件: vi ~/.bashrc ---> 添加如下两行内容
export WORKON_HOME=/envs 
export VIRTUALENVWRAPPER_PYTHON=/usr/local/python3/bin/python3
source /usr/local/python3/bin/virtualenvwrapper.sh 
立即生效: source ~/.bashrc 
```
- 虚拟环境相关命令
```
# 创建虚拟环境: mkvirtualenv my_django115
# 创建虚拟环境: mkvirtualenv -p python3 虚拟环境名称
# 查看虚拟环境: workon
# 进入虚拟环境: workon my_django115
# 退出虚拟环境: deactivate
# 删除虚拟环境需要先退出虚拟环境: rmvirtualenv my_django115
```

### 安装Python虚拟环境: pipenv
- 安装虚拟环境
```
# 创建存放虚拟环境的隐藏目录: sudo mkdir -p /envs
pip3 install pipenv
```
- 配置环境变量
```
编辑文件: vi ~/.bashrc ---> 添加如下两行内容
export WORKON_HOME=/envs 
# source /usr/local/python3/bin/pipenv 
立即生效: source ~/.bashrc 
```
- 虚拟环境相关命令
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

### 安装Git:
* 移除旧版本: yum remove git
* 安装依赖包:
```
yum -y install curl-devel expat-devel gettext-devel openssl-devel zlib-devel
yum -y install gcc perl-ExtUtils-MakeMaker
```
* 下载安装包: wget https://www.kernel.org/pub/software/scm/git/git-2.21.1.tar.gz
* 解压下载包: tar -xf git-2.21.1.tar.gz
* 编译和安装: 
```
进入解压后的git目录：cd git-2.21.1
./configure --prefix=/usr/local/git
make prefix=/usr/local/git all      # 不指定路径的话默认安装在/usr/bin
make prefix=/usr/local/git install  # 执行安装
```
* 配置环境变量:
```
编辑文件: vi ~/.bashrc ---> 添加如下内容
export PATH=$PATH:/usr/local/git/bin 
立即生效: source ~/.bashrc 

```
* 检测是否安装成功: git --version
* Git的使用配置: GitHub
```
生成SSH秘钥: ssh-keygen -t rsa -C "your email address"
生成的秘钥文件: cat root/.ssh/id_ras.pub
添加密钥到GitHub: 点击自己的头像 ---> settings ---> SSH And GPG Keys ---> New SSH key
将CentOS本地 id_rsa.pub 中的内容粘贴到 Key 文本框中,随意输入一个 title(不要有中文),点击 Add Key 即可
测试验证是否成功: ssh git@github.com
```


