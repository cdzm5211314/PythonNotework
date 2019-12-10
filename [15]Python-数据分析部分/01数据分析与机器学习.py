# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-24 14:46

# 搭建开发环境(两种方式): jupyter浏览器开发工具 与 PyCharm开发工具类似
# 第一种: Python + 手动安装包   ---> 搭建集成开发环境
# 1.下载Python.exe解释器并安装
# 2.配置Python环境变量,如 E:\Developer_Tools\Python\Python36;E:\Developer_Tools\Python\Python36\Scripts
# 3.数据分析与机器学习需要一些库(jupyter,numpy,pandas,matplotlib): pip install jupyter
# 4.启动开发工具: (终端)jupyter notebook   ---> 浏览器访问:http://localhost:8888/tree
# 5.后续需要安装其他库: pip install xxx


# 第二种: Anaconda   ---> 集成好的开发环境
# 1.下载地址: https://repo.anaconda.com/archive/
# 2.下载对应版本的Anaconda.exe并安装
# 3.配置Anaconda环境变量,如 E:\Developer_Tools\Anaconda3;E:\Developer_Tools\Anaconda3\Scripts;
# 4.启动开发工具: (终端)jupyter notebook   ---> 浏览器访问:http://localhost:8888/tree
# 4.后续通过 pip install xxx 扩展Anaconda集成环境


## jupyter notebook 快捷键使用:
# b 在一个代码单元下面插入一行
# a 在一个代码单元上面插入一行
# dd 选中一个单元格进行删除单元格
# Shift+Tab: 查看方法的属性和注释
# tab: 代码的自动补全

# 运行代码单元:
# Ctrl+Enter(运行输出结果)
# Alt+Enter(运行输出结果并插入一行)
# Shift+Enter(运行输出结果并插入一行,如果有下一行就不插入)


###################################################################################

### 数据分析相关模块的简介与安装:
# numpy模块:          基础数值算法;提供数组支持,很多模块依赖它.如: pandas, scipy, matplotlib
# pandas模块:         序列高级函数;主要用于进行数据探索和数据分析
# scipy模块:          科学计算;主要进行数值计算,比如: 积分, 傅里叶变换, 微分方程求解...
# matplotlib模块:     主要用于作图,解决数据可视化

# statsmodels模块:    主要用于数据分析
# gensim模块:         主要用于文本挖掘

# sklearn模块:        用于机器学习
# keras模块:          用于深度学习

## 相关模块的安装顺序与方式:
# 模块下载地址: https://www.lfd.uci.edu/~gohlke/pythonlibs/
# numpy,mkl(下载安装):   numpy-1.16.2+mkl-cp36-cp36m-win_amd64.whl
# pandas(网络安装):      pip install pandas
# matplotlib(网络安装):  pip install matplotlib
# scipy(下载安装):       scipy-1.2.1-cp36-cp36m-win_amd64.whl

# statsmodels(网络安装): pip install statsmodels
# gensim(网络安装):      pip install gensim


