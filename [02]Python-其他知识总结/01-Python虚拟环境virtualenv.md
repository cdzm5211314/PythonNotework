"""
Python项目中必须包含一个requirements.txt文件，用于记录项目的所有依赖包以及其精确的版本号，以便在新环境（其他项目）中进行部署操作。  
如有两个项目： pythonproject1【虚拟环境project1】 和 pythonproject2【虚拟环境project2】  
1、在project1虚拟环境下执行 pip freeze > requirements.txt 命令生成pythonproject1项目所依赖的包及包的版本号  
2、如果想在pythonproject2项目中使用pythonproject1项目的相同版本号的依赖包，可以把pythonproject1项目中生成的requirements.txt文件拷贝到pythonproject2项目中，
   并在pythonproject2项目的project2虚拟环境下执行pip install -r requirements.txt 命令  
"""

### 系统环境与Python版本:
- Windows7 Python3.6.5

### 虚拟环境的安装:
- 配置Python解释器的系统环境变量
    - path E:\Developer_Tools\Python\Python36;E:\Developer_Tools\Python\Python36\Scripts;
- 安装virtualenv: pip install virtualenv
- 安装virtualenvwrapper-win: pip install virtualenvwrapper-win
- 查看是否安装成功: workon

### 配置虚拟环境位置:
- 新建系统变量: WORKON_HOME
- 指定虚拟环境位置: E:\Developer_Tools\PythonEnvs

### 虚拟环境的使用命令:
- 创建虚拟环境: mkvirtualenv "虚拟环境名称"
- 创建指定版本的虚拟环境: mkvirtualenv --python = E:\Developer_Tools\Python\Python36\python.exe “虚拟环境名称”
- 列出所有的虚拟环境: workon
- 启动/切换虚拟环境: workon "虚拟环境名称"
- 退出(离开)虚拟环境: deactivate
- 删除虚拟环境: rmvirtualenv "虚拟环境名称"

### 虚拟环境中安装模块包:
- 首先进入到虚拟环境中: workon "虚拟环境名称"
- 然后在虚拟环境中安装模块包: 
    - pip install 模块名/包名
    - pip install django==1.11.23  指定版本安装
    - pip install -i https://pypi.douban.com/simple 模块名/包名

### 导出/导入虚拟环境模块包:
- 导出: pip freeze > requirements.txt
- 导入: pip install -r requirements.txt
- 导入: pip install -r requirements.txt -i https://pypi.douban.com/simple


