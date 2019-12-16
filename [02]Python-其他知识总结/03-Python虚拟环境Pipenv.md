### Pipenv安装虚拟环境及使用
***

```python3
### Pipfile的基本理念:
# Pipfile 文件是 TOML 格式而不是 requirements.txt 这样的纯文本
# 一个项目对应一个 Pipfile,支持开发环境与正式环境区分.默认提供 default 和 development 区分
# 提供版本锁支持,存为 Pipfile.lock

# 安装虚拟环境时只需在 Pipfile 和 Pipfile.lock 所在的目录下运行 pipenv install
# 注: pipenv 创建的虚拟环境必须与每个项目的文件夹绑定在一起

Pipenv集成了pip,virtualenv两者的功能,且完善了两者的一些缺陷
```

### 虚拟环境的创建及讲解:
* 安装Pipen工具: `pip install pipenv`
* 查看Pipenv安装是否成功: `pipenv --version`
* 配置虚拟环境位置的系统环境变量:
```python3
WORKON_HOME E:\Developer_Tools\PythonEnvs
```
* 创建虚拟环境(如系统已安装了Python2,Python3):
```python3
# 即进入到项目根目录下执行如下命名
pipenv --two    # 会使用当前系统的Python2创建虚拟环境
pipenv --three  # 会使用当前系统的Python3创建虚拟环境
pipenv --python python3.6  # 指定某一Python版本创建虚拟环境
pipenv --python=E:\Developer_Tools\Python\Python27\python2.exe  # 指定某一Python版本创建虚拟环境
# 注: 初始化好虚拟环境后,会在项目根目录下生成两个文件: Pipfile 和 Pipfile.lock
```

* 更新源信息(Pipfile):
```python3
# 豆瓣源: https://pypi.douban.com/simple
# 清华源: https://pypi.tuna.tsinghua.edu.cn/simple
# 阿里云源: https://mirrors.aliyun.com/pipy/simple
```

* pipenv install 多重作用:
```python3
# 1.如果虚拟环境已存在,则安装Pipfile中的依赖包
# 2.如果虚拟环境不存在,但Pipfile存在,则根据Pipfile中Python版本创建虚拟环境并安装依赖包(pipenv install --dev)
# 3.如果虚拟环境和Pipfile都不存在,则根据系统默认Python版本创建虚拟环境,并生成Pipfile和Pipfile.lock
```

* 激活虚拟环境: 
```python3
pipenv shell  # 进入虚拟环境
# 注:如果虚拟环境不存在会使用当前系统默认版本的Python创建虚拟环境并进入
```

* 在虚拟环境中安装模块包: `pipenv install packagename`
* 在虚拟环境中安装模块包的指定版本: `pipenv install packagename==1.1.1`
* 在虚拟环境中安装模块包到开发环境: `pipenv install packagename --dev`
* 在虚拟环境中安装模块包(不加锁加快速度): `pipenv install packagename --skip-lock`
* 在虚拟环境中删除模块包: `pipenv uninstall  packagename` 
* 在虚拟环境中删除所有模块包: `pipenv install --all`
* 在虚拟环境中更新所有模块包: `pipenv update`
* 在虚拟环境中查看安装模块包列表: `pip list`
* 在虚拟环境中查看安装模块包依赖关系: `pipenv graph`
* 在虚拟环境中查看项目的根目录: `pipenv --where` 
* 在虚拟环境中查看虚拟环境目录: `pipenv --venv` 
* 在虚拟环境中查看Pytho解释器位置: `pipenv --py` 
* 退出当前虚拟环境: `exit` 或 `ctrl + d`
* 生成lockfile文件[项目根目录]: `pipenv lock` 
* 删除虚拟环境[项目根目录]: `pipenv --rm` 
* 检查安全漏洞: `pipenv check`
* 运行py文件: `pipenv run python [pyfile]`

* 虚拟环境中模块包信息导入导出:
```python3
# 导出: pip freeze > requirements.txt
# 导出: pipenv lock -r > requirements.txt  # 默认只导出生产环境的依赖包
# 导出: pipenv lock -r --dev > requirements.txt  # 只导出开发环境的依赖包

# 导入: pip freeze -r requirements.txt
# 导入: pipenv install -r requirements.txt  # 默安装所有依赖包到生产包环境
# 导入: pipenv install -r requirements.txt --dev  # 安装所有依赖包到开发环境
```


