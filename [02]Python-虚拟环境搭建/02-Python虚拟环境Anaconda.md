### 注: 本机安装Python解释器与安装Anaconda并不冲突,Python解释器配置环境变量

### Anaconda安装与配置:
- 下载: https://repo.anaconda.com/archive/  注意版本下载
- 安装后配置系统环境变量: path E:\Developer_Tools\Anaconda3;E:\Developer_Tools\Anaconda3\Scripts;

### 查看是否安装成功并更新所有包:
- 验证: conda --version
- 更新: conda upgrade --all

### 创建虚拟环境: (指定Python解释器版本)
- 注: 创建虚拟环境的默认位置: E:\Developer_Tools\Anaconda3\envs (Anaconda安装目录下envs)
- 创建虚拟环境: conda create -n python35 python=3.5
- 创建虚拟环境: conda create --name python37 python=3.7
- 注: 创建虚拟环境并指定位置: E:\Developer_Tools\AnacondaEnvs
- 创建虚拟环境: conda create -n E:\Developer_Tools\AnacondaEnvs\python35 python=3.5
- 创建虚拟环境: conda create --name E:\Developer_Tools\AnacondaEnvs\python35 python=3.5
- 注: 虚拟环境创建后,虚拟环境中只有Python相关的必须项,如Python,pip等,如果需要安装Anaconda集合包,如下操作:
    ```
    conda install anaconda  # 在当前环境下安装Anaconda集合包
    conda create --name envs_name python=3.6.5 anaconda  # 创建虚拟环境时,安装Anaconda集合包 
    ```

### 进入(切换)虚拟环境:
- 默认位置的虚拟环境: conda activate python35
- 指定位置的虚拟环境: conda activate E:\Developer_Tools\AnacondaEnvs\python35

### 退出当前虚拟环境:
- conda deactivate

### 删除虚拟环境:
- 删除默认位置的虚拟环境: conda remove -n python35 --all
- 删除默认位置的虚拟环境: conda remove --name python35 --all
- 删除指定位置的虚拟环境: conda remove --name E:\Developer_Tools\AnacondaEnvs\python35 --all

### 查看所有的虚拟环境:
- conda env list
- conda info -e
- conda info --envs

### 虚拟环境下的命令使用: (进入到虚拟环境)
- 查看虚拟环境下的模块包: conda list 或 pip list 或 conda list --name python37
- 查看虚拟环境下的Python解释器版本: python --version
- 虚拟环境中安装第三方模块包: conda install requests 或 pip install requests
- 虚拟环境中卸载第三方模块包: conda remove requests 或 pip uninstall requests
- 导入导出当前虚拟环境的包信息(.yaml文件):
    - 导出: conda env export > environment.yaml 或 pip freeze > requirements.txt
    - 导入: conda env create -f environment.yaml 或 pip install -r requirements.txt
    - 更新: conda env update -f enviroment.yml 更新目标环境与源环境一致
    - 导入: pip install -r requirements.txt -i https://pypi.douban.com/simple

### conda install xxx 与 pip install xxx 的区别:
```
# 管理器包范围:
conda是通用包管理系统,与语言无关的的跨平台环境管理器;conda在conda环境中按装任何包
pip只是Python语言下的通用包管理器;pip在任何环境中安装Python包

# 安装位置:
conda安装位置: xxx\Anaconda3\pkgs\*
pip: xxx\Anaconda3\envs\虚拟环境\Lib\site-packages\*
# 如果多个虚拟环境时,conda install xxx,对于同一个包只安装一次,由conda集中管理
# 如果多个虚拟环境时,pip install xxx,只会安装在当前使用的虚拟环境中,故会重复安装
```
    
### 修改Anaconda的JupyterNotebook默认工作路径:
- 终端命令行下执行: jupyter notebook --generate-config ---> 生成一个 jupyter_notebook_config.py文件
    - C:\Users\Administrator\.jupyter\jupyter_notebook_config.py
- 修改此文件内容[214行]: c.NotebookApp.notebook_dir = 'E:\WorkSpace_PyCharm\JupyterNotebook' (指定位置)
- 重新启动jupyter: jupyter notebook
- 注: 或者直接执行命令: jupyter notebook E:\WorkSpace_PyCharm\JupyterNotebook


### Anaconda-conda镜像设置:
- 注: 由于anaconda的镜像在国外,所以访问会较慢,我们可以手动将镜像设置成清华TUNA镜像源,添加多个镜像源如下
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
- conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
- 执行生效：conda config --set show_channel_urls yes
- 查看是否生效：conda config --show channels
- "conda config --set show_channel_urls yes" 表示设置搜索时显示通道地址设置完成后,就在用户目录下生成.condarc文件，内容如下:
``` 如: C:\Users\Administrator\.condarc
channels:
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/msys2
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/pro
  - https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/r
  [删除]- defaults
show_channel_urls: true
```
- 添加其他镜镜像源:
```
# 清华
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/menpo/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/pytorch/
# 中科大
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/

conda config --set show_channel_urls yes
```

### pip安装模块包镜像源:
```
中国科技大学: https://pypi.mirrors.ustc.edu.cn/simple/
华中科技大学: http://pypi.hustunique.com/
山东理工大学: http://pypi.sdutlinux.org/
阿里云: http://mirrors.aliyun.com/pypi/simple/
清华: https://pypi.tuna.tsinghua.edu.cn/simple/
豆瓣: http://pypi.douban.com/simple/
```

### Anaconda更新升级命令: 
- 升级conda本身: conda update conda
- 升级Anaconda应用: conda update anaconda
- 升级spyder编辑器：conda update spyder
- 升级Python解释器: conda update python 
- 注:如当前python环境版本是3.6.0,而最新版本是3.6.5,那么就会升级到3.6.5
- 更新所有包: conda update --all
- 更新某个包: conda update packagename

