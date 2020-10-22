###Docker服务与镜像加速器:
* Docker更改权限配置使用:
    ```
    # 问题描述: 从0.5.2开始docker的守护进程总是以root用户来运行;从0.5.3开始，创建一个名为docker组，然后将用户加入这个组内
    # 解决方式一: 切换root用户运行docker命令
    sudo su               # 切换到root用户
    service docker start  # 启动docker service
    docker images         # 显示所有images
    docker ps             # 重新运行docker命令
    # 解决方式二: 添加用户到docker用户组
    sudo groupadd docker                # 添加docker用户组
    sudo gpasswd -a myusername docker   # 添加用户到docker用户组
    sudo service docker restart         # 重启docker服务
    docker ps                           # 重新运行docker命令
    ```
* Docker服务的常用命令:
    ```
    开启Docker服务: systemctl start docker
    停止Docker服务: systemctl stop docker
    查看Docker状态: systemctl status docker
    重启Docker服务: systemctl restart docker
    开机自启动Docker服务: systemctl enable docker
    ```
* Docker镜像加速器配置:
    ``` 
    # CentOS7.2系统:
    1.创建目录: mkdir -p /etc/docker
    2.创建文件: vi /etc/docker/daemon.json
    3./etc/docker/daemon.json文件添加如下内容:
    {
        "registry-mirrors": [
            "https://1qlfqh72.mirror.aliyuncs.com"
        ]
    }
    4.重新加载Docker: systemctl daemon-reload
    5.重新启动Docker: systemctl restart docker
    6.查看镜像加速器是否生效: ps -ef | grep dockerd 或 docker info
    ```


### Docker镜像管理操作:
* 搜索镜像: docker search images_name
* 获取镜像: docker pull images_name[:tag]
    > 默认下载tag标签为latest版本的镜像(最新版)  
* 查看镜像: docker images [-q:显示所有镜像ID]
* 删除镜像: docker rmi -f images_name[:tag] / images_id
    > 默认删除tag标签为latest版本的镜像  
* 镜像变更历史: docker history images_name[:tag] / images_id


### Docker基于镜像操作容器:
* 启动容器: docker run --name -it[-d -p -P] -h hostname(容器主机名称)
    * 以终端交互方式创建容器并启动容器:
        > docker run -it -p port:port --name="容器取名字" images_name[:tag] / images_id  
    * 以守护进程方式创建容器并启动容器:
        > docker run -d -p port:port --name="容器取名字" images_name[:tag] / images_id  
* 容器停止退出: exit
* 容器不停止退出: ctrl + p + q 或 ctrl + p , ctrl + q
* 停止容器: docker stop container_id / container_name
* 强制停止容器: docker kill container_id / container_name
* 查看容器: docker ps -aq  
    > -a: 所有正在运行及历史运行过的容器  
    -q: 只显示容器的ID  
    -l: 显示最近创建的容器(即上一个容器)
* 删除一个已停止容器: docker rm container_id / container_name
* 删除多个已停止容器: docker rm -f $(docker ps -aq)


### Docker基于已有容器操作容器:
* 启动容器: docker start container_id / container_name
* 重启容器: docker restart container_id / container_name
* 进入已启动的容器: docker exec | docker attach
    > docker exec -it container_id /bin/bash	进入容器中打开新的终端,并且可以启动新的进程  
    docker exec -it container_id ls -l /tmp	进入容器并执行命令,显示结果(不进入容器的终端)  
    docker attach container_id	重新进入已启动容器的命令行终端,不会启动新的进程  

### Docker容器其他使用命令:
* 查看容器内的内部细节: 
    > 查看容器/镜像元数据: docker inspect container_id / container_name  
    查看容器IP: docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' container_id / container_name       
* 查看容器内运行的进程: docker top container_id / container_name
* 查看容器的日志信息: docker logs -t -f -till num container_id / container_name
    > -t: 是加入时间戳  
    -f: 跟随最新的日志打印  
    --tail num: 数字,显示最后多少条  
* 查看容器的IP地址: ip ad li   
* 查看容器的IP地址: ifconfig 需安装:yum -y install net-tools 


### Docker容器端口号映射:
* 随机映射端口: docker run -P(大写)
* 指定映射端口: docker run -p(小写)
    * -p hostPort:containerPort
    * -p ip:hostPort:containerPort
    * -p ip::containerPort
    * -p hostPort:containerPort -p hostPort:containerPort


### Docker容器数据管理操作:
* 数据卷管理:(-v) 容器与宿主机之间数据共享 
    * 对容器可读可写: docker run -itd -v container_path images_name / images_id
        > 查看映射到宿主机的路径: docker inspect -f "{{.Volumes}}" container_name / container_id
    * 对容器可读可写: docker run -it -v host_path:container_path images_name / images_id
    
    * 对容器可读不可写: docker run -it -v host_path:container_path images_name:ro / images_id
    * Docker挂载宿主机目录访问时出现问题: cannot open directory .: Permission denied
        > 解决办法: 在挂载目录后多加一个 --privileged=true 参数即可  
* 数据卷容器管理:(--volumes-from) 容器与容器之间数据共享 
    * 启动一个容器(别名为volume-test1),作为父容器:
        > 注:父容器需要完成与宿主机目录的挂载映射...  
        docker run -it --name volume-test1 -v host_path:container_path centos  
    * 启动两个容器(别名分别为volume-test2,volume-test3),继承父容器: 
        > docker run -it --name volume-test2 --volumes-from volume-test1 centos  
       docker run -it --name volume-test3 --volumes-from volume-test1 centos
    * 此时就完成了容器之间的数据共享

### Docker数据卷的备份与还原:
* 数据卷备份:
    ``` 宿主机
    # backup_container_name 要备份的数据卷的容器名称
    # host_path_dir 数据卷备份后的文件存放在宿主机的哪个目录
    # container_path_dir 数据卷备份后的文件存放在容器的哪个目录
    # new_container_name 新创建(启动)容器的名称
    # images_name/images_id 基于哪个镜像创建的容器
    # tar cvf ... 以哪种方式备份数据卷数据
    # new_container_path_dir 数据卷备份后的文件在新容器中的哪个目录及文件名字
    # backup_container_data_volumes 要备份的数据卷数据
    
    docker run --volumes-from backup_container_name -v host_path_dir:container_path_dir --name new_container_name images_name/images_id tar cvf /new_container_path_dir/xxx.tar  /backup_container_data_volumes
    ```
* 数据卷还原:
    ```
    # 创建一个带有空数据卷的容器1:
    docker run -d -v host_path_dir:container_path_dir --name container_name1 images_name/images_id
    # 再次创建一个新容器2,挂载容器1容器卷中的数据卷,并使用tar解压备份文件到挂载的容器卷中
    docker run --volumes-from container_name1 -v host_path_dir:/new_container_path_dir --name new_container_name2 images_name/images_id tar xvf /backup/backup.tar
    
    # 或者: docker run -v host_path_dir:/new_container_path_dir --name new_container_name images_name/images_id tar xvf /backup/xxx.tar
    ```

### Docker镜像的自定义构建:
* 第一种方式:使用容器构建自定义镜像:
    > docker commit -a="作者" -m="描述信息" container_id new_images_prefix/new_images_name:set_tag  
* Dockerfile构建镜像指令:
    ```
    FROM        基础镜像,当前构建的新镜像是基于哪个镜像
    MAINTAINER  构建镜像的维护者信息(姓名或邮箱)
    RUN         构建镜像时需要执行的命令(需要安装的软件)
    ADD         将宿主机目录下文件拷贝进镜像目录中,且ADD命令会自动处理URL和自动解压缩包
    COPY        类似于COPY指令,只是拷贝文件
    WORKDIR     创建容器时,终端默认登录进来时的工作目录
    VOLUME      数据卷容器挂载目录["容器挂载目录"]
    ENV         构建镜像过程中设置环境变量   
    EXPOSE      运行容器时对外暴露的端口,可以有多个端口
    CMD         启动容器时运行的命令,如果有多个CMD命令,只有最后一个生效,CMD命令会被 docker run 之后的参数覆盖 
    ENTRYPOINT  启动容器时运行的命令,docker run 之后的参数会被当做参数传递给 ENTRYPOINT 命令(即追加),形成新的命令组合
    ONBUILD     当构建父镜像后,且子镜像继承父镜像后,父镜像中的onbuild信息被触发
    ```
* 第二种方式:使用Dockerfile文件构建自定义镜像: 示例如下
    * 1.编辑Dockerfile文件: vi Dockerfile
        ``` 
        FROM centos
        MAINTAINER author
        ADD pcre-8.37.tar.gz /usr/local/src
        ADD nginx-1.16.1.tar.gz /usr/local/src
        RUN yum install -y wget gcc gcc-c++ make openssl-devel 
        RUN useradd -s /sbin/nologin -M www
        WORKDIR /usr/local/src/nginx-1.16.1
        RUN ./configure --prefix=/usr/local/nginx --user=www --group=www --with-http_ssl_module --with-http_stub_status_module --with-pcre=/usr/local/src/pcre-8.37 && make && make install 
        RUN echo "dameon off;" >> /usr/local/nginx/conf/nginx.conf
        ENV PATH /usr/local/nginx/sbin:$PATH
        EXPOSE 80
        CMD ["nginx"]
        RUN echo "father image onbuild ... 886"
        ```
    * 2.构建自定义镜像: docker build -f Dockerfile -t new_images_prefix/new_images_name:set_tag .
    * 3.创建新镜像容器运行: docker run -it new_images_prefix/new_images_name:set_tag
    
### Dockerfile镜像构建文件: JDK8 + Tomcat8
````
# 1.创建宿主机与容器之间的挂载目录:
mkdir -p /workspace/cdtomcat/logs
mkdir -p /workspace/cdtomcat/webapps

# 2.下载准备JDK8与Tomcat8压缩包文件:
apache-tomcat-8.5.21.tar.gz  
https://archive.apache.org/dist/tomcat/tomcat-8/v8.5.21/bin/apache-tomcat-8.5.21.tar.gz
jdk-8u231-linux-x64.tar.gz  
https://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html

# 3.自定义Dockerfile构建文件:
FROM centos:7.2
MAINTAINER author author@163.com
ADD apache-tomcat-8.5.21.tar.gz /usr/local/
ADD jdk-8u231-linux-x64.tar.gz /usr/local/
WORKDIR /usr/local
ENV JAVA_HOME /usr/local/jdk1.8.0_231
ENV CLASSPATH $JAVA_HOME/lib/dt.jar:$JAVA_HOME/lib/tools.jar
ENV CATALINA_HOME /usr/local/apache-tomcat-8.5.21
ENV CATALINA_BASE /usr/local/apache-tomcat-8.5.21
ENV PATH $PATH:$JAVA_HOME/bin:$CATALINA_HOME/lib:$CATALINA_HOME/bin
EXPOSE 8080
# CMD ["/usr/local/apache-tomcat-8.5.47/bin/catalina.sh","run"]
CMD /usr/local/apache-tomcat-8.5.47/bin/startup.sh && tail -F /usr/local/apache-tomcat-8.5.47/bin/logs/catalina.out

# 4.构建新的镜像文件:
docker build -f /workspace/cdtomcat/Dockerfile -t author/tomcat8 .

# 5.运行新容器: 挂载宿主机目录与容器卷目录关系
docker run -d -p 8080:8080 --name tomcat8 -v /workspace/cdtomcat/webapps/:/usr/local/apache-tomcat-8.5.47/webapps/ -v /workspace/cdtomcat/logs/:/usr/local/apache-tomcat-8.5.47/logs/ --privileged=true author/tomcat8
````
     
### 将新镜像推送到阿里云仓库:
* 创建阿里云账号,开通Registry仓库,创建镜像仓库(本地仓库):
    > 命名空间: 镜像的前缀, 仓库名称: 镜像名称  
* 登录阿里云仓库,需输入Registry仓库密码: 
    > docker login --username=阿里云账号 registry.cn-beijing.aliyuncs.com  
    当出现"Login Succeeded",即登录成功
* 将镜像推送到阿里云仓库: docker tag 命名镜像
    > docker tag [image_id] registry.cn-beijing.aliyuncs.com/命名空间/仓库名称:[镜像版本号]  
    docker push registry.cn-beijing.aliyuncs.com/命名空间/仓库名称:[镜像版本号]  
* 从阿里云仓库拉取到镜像: 
    > docker pull registry.cn-beijing.aliyuncs.com/命名空间/仓库名称:[镜像版本号]  
 
 
 
