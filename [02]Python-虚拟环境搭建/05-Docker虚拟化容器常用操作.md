### Docker虚拟化容器常用命令
___

### 配置Docker服务镜像加速器:
```
# 如: CentOS7.2
# 创建目录: mkdir -p /etc/docker
# 创建文件: vi /etc/docker/daemon.json  添加内容如下:
{
    "registry-mirrors": ["https://1qlfqh72.mirror.aliyuncs.com"]
}
# 
重新加载: systemctl daemon-reload
重新启动: systemctl restart docker
检查镜像加速是否生效: ps -ef | grep docker
```


### Docker服务开启停止以及状态:
```
systemctl start docker
systemctl stop docker
systemctl restart docker
systemctl status docker
```

### Docker镜像的常用命令:
```
# 查找某个镜像: docker search images_name
# 下载某个镜像: docker pull images_name[:tag]  # 默认下载tag标签为latest版本的镜像(最新版)
# 列出本机镜像: docker images
# 删除某个镜像: docker rmi -f images_name[:tag]/images_id  # 默认删除tag标签为latest版本的镜像
# 查看镜像变更历史: docker history images_name[:tag]/images_id
```

### Docker容器的常用命令:
* 以终端交互方式创建容器并启动容器: 
    ```
    docker run -it -p port:port images_name[:tag]/images_id
    docker run -it -p port:port --name="容器取名字" images_name[:tag]/images_id
    ```
* 以守护进程方式创建容器并启动容器: 
    ```
    docker run -d -p port:port images_name[:tag]/images_id
    docker run -d -p port:port --name="容器取名字" images_name[:tag]/images_id
    ```
* 查看当前正在运行的容器: `docker ps [-aq]`  # -a:所有正在运行及历史运行过的容器 -q:只显示容器的ID
* 退出停止(或不停止)容器: `exit` 或 `ctrl+p+q`
* 启动容器: `docker start container_id/container_namme`
* 停止容器: `docker stop container_id/container_name`
* 强制停止容器: `docker kill container_id/container_name`
* 重启容器: `docker restart container_id/container_namme`
* 删除一个已停止容器: `docker rm container_id`
* 删除多个已停止容器: `docker rm -f $(docker ps -aq)`
* 查看容器的日志信息: `docker logs -t -f -till num container_id/container_name`
* 进入正在运行的容器并一终端交互:
    ```
    docker exec -it container_id/container_namme  # 进入容器中打开新的终端,并且可以启动新的进程
    docker exec -it container_id/container_namme ls -l /tmp	 # 进入容器并执行命令,显示结果(不进入容器的终端)
    docker attach container_id/container_namme	# attach重新进入已启动容器的命令行终端,不会启动新的进程
    ```
* 从容器内拷贝文件到宿主机目录中: `docker cp container_id/container_namme:container_path host_path`
* 把一个容器副本制作为一个新的镜像: 
    ```
    docker commit -a="提交的镜像作者" -m="提交的镜像说明" container_id/container_name new_images_name:tag
    ```

### Docker容器数据卷添加方式:
```
# 第一种方式: 可读可写
docker run -it -v /host_path:/container_path images_name[:tag]/images_id
# 第二种方式: 可读不可写(容器)
docker run -it -v /host_path:/container_path:ro images_name[:tag]/images_id
注: Docker挂载宿主机目录,Docker访问出现cannot open directory .: Permission denied???
解决办法:在挂载目录后多加一个--privileged=true参数即可
```

### 新镜像的两种制作方式:
```
# 第一种方式: 使用容器副本
docker commit -a="提交的镜像作者" -m="提交的镜像说明" container_id/container_name new_images_name:tag
# 第二种方式: 使用Dockerfile文件
docker build -f Dockerfile_path -t new_images_name:tag .
```

###Docker-Dockerfile自定义镜像:
```
# Dockerfile保留字指令,注:注释内容不能与保留字指令在同一行
FROM(from): 基础镜像,当前构建的新镜像是基于哪个镜像的
MAINTAINER(maintainer): 新镜像维护者的姓名和邮箱地址
RUN(run): 容器构建时需要运行的命令
EXPOSE(expose): 容器运行时对外暴露的端口
WORKDIR(workdir): 容器创建后,终端默认登陆的进来工作目录路径,一个落脚点
ENV(env): 构建镜像过程中设置环境变量
ADD(add): 将宿主机目录下的文件拷贝进镜像且ADD命令会自动处理URL和解压缩tar包
COPY(copy): 类似ADD,将宿主机目录下的文件拷贝文件和目录到镜像中;将从构建上下文目录中<源路径>的文件/目录复制到新的一层的镜像内的<目标路径>位置;COPY src dest 或 COPY ["src", "dest"]
VOLUME(volume): 容器数据卷,用于数据保存和持久化工作
CMD(cmd): 指定一个启动时要运行的命令;Dockerfile中可以有多个 CMD 指令,但只有最后一个生效,CMD会被 docker run 之后的参数覆盖
ENTRYPOINT(entrypoint): 指定一个容器启动时要运行的命令;docker run之后的参数会当做参数传递给ENTRYPOINT保留字指令(即追加),形成新的命令组合
ONBUILD(onbulid): 当构建一个被继承的Dockerfile时运行命令,父镜像在被子继承后父镜像的onbuild被触发


自定义示例如下: JDK8 + Tomcat8
# 1.创建宿主机与容器卷目录:
mkdir -p /workspace/cdtomcat/conf
mkdir -p /workspace/cdtomcat/logs
mkdir -p /workspace/cdtomcat/webapps

# 2.准备tomcat与jdk压缩包:
apache-tomcat-8.5.47.tar.gz
jdk-8u201-linux-x64.tar.gz

# 3.编辑Dockerfile文件:
FROM centos
# 新镜像的维护者姓名
MAINTAINER chen<cdzm5211314@163.com>
# 把java8与tomcat8安装压缩包文件添加到容器中
ADD apache-tomcat-8.5.47.tar.gz /usr/local/
ADD jdk-8u201-linux-x64.tar.gz /usr/local/
# 设置工作访问时候的WORKDIR路径,登录落脚点
ENV MYPATH /usr/local
WORKDIR $MYPATH
# 配置java8与tomcat8环境变量
ENV JAVA_HOME /usr/local/jdk1.8.0_201
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-8.5.47
ENV CATALINA_BASE /usr/local/apache-tomcat-8.5.47
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
# 容器运行时监听的端口
EXPOSE 8080
# 启动时运行tomcat
# ENTRYPOINT ["/usr/local/apache-tomcat-8.5.47/bin/startup.sh" ]
# CMD ["/usr/local/apache-tomcat-8.5.47/bin/catalina.sh","run"]
CMD /usr/local/apache-tomcat-8.5.47/bin/startup.sh && tail -F /usr/local/apache-tomcat-8.5.47/bin/logs/catalina.out

# 4.构建新的镜像文件:
docker build -f /workspace/cdtomcat/Dockerfile -t chen/tomcat8 .

# 5.运行新容器: 挂载宿主机目录与容器卷目录关系
docker run -d -p 8080:8080 --name mytomcat8 -v /workspace/cdtomcat/webapps/:/usr/local/apache-tomcat-8.5.47/webapps/ -v /workspace/cdtomcat/logs/:/usr/local/apache-tomcat-8.5.47/logs/ --privileged=true chen/tomcat8
```

### Docker常用服务容器:
```
# 如,MySQL数据库:
docker run -d -p 3306:3306 --name mymysql5 -v /workspace/cdmysql/conf:/etc/mysql/conf.d -v /workspace/cdmysql/logs:/logs -v /workspace/cdmysql/data:/var/lib/mysql -e MYSQL_ROOT_PASSWORD=root mysql:5.7
命令参数说明:
-d : 守护式进程开启容器(后台运行)
-p 3306:3306 :将宿主机的3306端口映射到docker容器的3306端口
--name mymysql5 :为运行的容器取个名称
-v /workspace/cdmysql/conf:/etc/mysql/conf.d :将宿主机/workspace/cdmysql/conf目录下的conf/my.cnf 挂载到容器的 /etc/mysql/conf.d
-v /workspace/cdmysql/logs:/logs :将宿主机/workspace/cdmysql/logs目录挂载到容器的/logs目录
-v /workspace/cdmysql/data:/var/lib/mysql :将宿主机/workspace/cdmysql/data目录挂载到容器的/var/lib/mysql目录
-e MYSQL_ROOT_PASSWORD=123456 :初始化 root 用户的密码
```

