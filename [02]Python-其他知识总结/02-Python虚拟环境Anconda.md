### 注: 本机安装Python解释器与安装Anaconda并不冲突,Python解释器配置环境变量

### Anaconda安装与配置:
- 下载: https://repo.anaconda.com/archive/  注意版本下载
- 安装后配置系统环境变量: path E:\Developer_Tools\Anaconda3;E:\Developer_Tools\Anaconda3\Scripts;

### 查看是否安装成功:
- 验证: conda --version
- 升级: conda upgrade --all

### 创建虚拟环境: (指定Python解释器版本)
- 注: 创建虚拟环境的默认位置: E:\Developer_Tools\Anaconda3\envs (Anaconda安装目录下envs)
- 创建虚拟环境: conda create -n python35 python=3.5
- 创建虚拟环境: conda create --name python37 python=3.7
- 注: 创建虚拟环境并指定位置: E:\Developer_Tools\AnacondaEnvs
- 创建虚拟环境: conda create -n E:\Developer_Tools\AnacondaEnvs\python35 python=3.5
- 创建虚拟环境: conda create --name E:\Developer_Tools\AnacondaEnvs\python35 python=3.5

### 进入(切换)虚拟环境:
- 默认位置的虚拟环境: activate python35
- 指定位置的虚拟环境: activate E:\Developer_Tools\AnacondaEnvs\python35

### 删除虚拟环境:
- 删除默认位置的虚拟环境: conda remove -n python35 --all
- 删除默认位置的虚拟环境: conda remove --name python35 --all
- 删除指定位置的虚拟环境: conda remove --name E:\Developer_Tools\AnacondaEnvs\python35 --all

### 退出虚拟环境:
- deactivate

### 查看所有的虚拟环境:
- conda env list
- conda info --envs
- conda info -e

### 虚拟环境下的命令使用: (进入到虚拟环境)
- 查看虚拟环境下的模块包: conda list 或 conda list --name python37
- 查看虚拟环境下的Python解释器版本: python --version
- 虚拟环境中安装第三方模块包: conda install requests 或 pip install requests
- 虚拟环境中卸载第三方模块包: conda remove requests 或 pip uninstall requests
- 导入导出当前虚拟环境的包信息(.yaml文件):
    - 导出: conda env export > environment.yaml
    - 导入: conda env create -f environment.yaml

### 修改Anaconda的JupyterNotebook默认工作路径:
- 终端命令行下执行: jupyter notebook --generate-config ---> 生成一个 jupyter_notebook_config.py文件
    - C:\Users\Administrator\.jupyter\jupyter_notebook_config.py
- 修改此文件内容[214行]: c.NotebookApp.notebook_dir = 'E:\WorkSpace_PyCharm\JupyterNotebook' (指定位置)
- 重新启动jupyter: jupyter notebook

- 注: 或者直接执行命令: jupyter notebook E:\WorkSpace_PyCharm\JupyterNotebook


