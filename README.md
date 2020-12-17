### 导出/导入虚拟环境模块包:
- 导出: pip freeze > requirements.txt
- 导入: pip install -r requirements.txt
- 导入: pip install -r requirements.txt -i https://pypi.douban.com/simple  

### Python虚拟环境: virtualenv
- 创建默认版本虚拟环境: mkvirtualenv [虚拟环境名称]
- 创建指定版本虚拟环境: mkvirtualenv --python=python2 [虚拟环境名称]
- 列出所有的虚拟环境：workon
- 进入(切换)虚拟环境：workon [虚拟环境名称]
- 退出(离开)虚拟环境：deactivate
- 删除虚拟环境：rmvirtualenv [虚拟环境名称]
- 安装模块包: pip install package_name -i https://pypi.douban.com/simple 

### Python虚拟环境: Pipenv
- 使用默认版本创建虚拟环境: pipenv install 
- 创建指定版本虚拟环境: pipenv --python python3.6
- 列出所有的虚拟环境: workon
- 进入虚拟环境：pipenv shell 
- 退出(离开)虚拟环境：exit
- 删除虚拟环境：pipenv --rm
- 生成lockfile文件: pipenv lock
- 修改源配置信息(Pipfile): https://pypi.tuna.tsinghua.edu.cn/simple
- 安装模块包(生产): pipenv install packagename 
- 安装模块包(开发): pipenv install packagename --dev
- 安装模块包(加速): pipenv install packagename --skip-lock

### Python虚拟环境: Anaconda
- 创建指定版本虚拟环境: conda create --name python36 python=3.6
- 列出所有的虚拟环境：conda env list
- 进入(切换)虚拟环境：conda activate [虚拟环境名称]
- 退出(离开)虚拟环境：conda deactivate
- 删除虚拟环境：conda remove --name python35 --all
- 安装模块包: pip install package_name -i http://mirrors.aliyun.com/pypi/simple
- 安装模块包: conda install package_name -i http://mirrors.aliyun.com/pypi/simple

### Pip源镜像加速配置: 
- Windows系统配置: C:\Users\Administrator 用户目录下创建pip目录,并在此目录创建pip.ini文件,添加如下内容
    ```
    [global]
        index-url = https://pypi.douban.com/simple
        index-url = https://mirrors.aliyun.com/pypi/simple	
    [install]
        trusted-host = pypi.douban.com
        trusted-host = mirrors.aliyun.com
    ```
- Linux系统配置: /home/用户目录下创建.pip目录,并在此目录下创建pip.conf文件,添加如下内容
    ```
    [global]
        index-url = http://pypi.douban.com/simple
        trusted-host =  pypi.douban.com
    ```

### 使用Python-IDEL[虚拟环境]
- 1.首先终端进入到虚拟环境: activate envs_name
- 2.终端下的虚拟环境中执行命令: python -m idlelib.idle

### Shell交互工具[虚拟环境]
- 1.首先终端进入到虚拟环境: activate envs_name
- 2.安装Ipython工具: pip install ipython
- 3.终端下的虚拟环境中执行命令: ipython


