# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:10

# 文件是数据存储的单位
# 文件通常用来长期存储数据
# 文件中的数据是以字节为单位进行顺序存储的

## 文件的操作流程: (注:任何的操作系统，一个应用程序同时打开文件的数量有最大数限制)
# 1.打开文件
# 2.读写文件
# 3.关闭文件

## 文件的打开函数: open()
# open(file, mode='rt') 用于打开一个文件，返回此文件对应的文件流对象，如果打开失败，则会触发OSError错误！

## 文件的关闭方法: close()
# F.close()  关闭，释放系统资源

## mode 模式字符的含义:
# 'r'	只读,若文件不存在,则返回IOError错误
# 'w'	只写,若文件存在,则清空文件内容再写;若文件不存在,则创建该文件
# 'a'	只写,若文件存在,则在文件末尾追加内容,并且只能在文本末尾追加;若文件不存在,则创建该文件
# 'r+'	读写,读的时候和r一样,但是在写操作的时候,从最前面开始改写（不是插入）
# 'w+'	读写,创建文件对象的时候会清空文件,之后执行读操作的时候,读出来的为空;写的时候和w模式一样,无论之前是否存在写的操作,读的时候均为空
# 'a+'  读写,创建文件对象的时候不会清空文件,文件写的时候直接在文件尾部写,读的时候在直接从最开始读
# 通常文件以文本方式打开,读写文件的字符串都会被特定的编码方式（默认是UTF-8）编码
# 注: 模式后面加'b'，读写文件都以字节方式(二进制)读写,如 rb,wb,ab,rb+,wb+,ab+

## Python文件操作的常用方法:
# 文本文件的操作方法:
# F.close()	                    关闭文件(关闭后文件不能再读写会发生ValueError错误)
# F.readline()	                读取一行数据, 如果到达文件尾则返回空行
# F.readlines(max_chars=-1)	    返回每行字符串的列表,max_chars为最大字符(或字节)数
# F.writelines(lines)	        每行字符串的列表
# F.flush()	                    把写入文件对象的缓存内容写入到磁盘
# F.read(size = -1)	            从一个文件流中最多读取size个字符
# F.write(text)	                写一个字符串到文件流中，返回写入的字符数

# 二进制文件操作方法:
# F.tell()	                    返回当前文件流的绝对位置
# F.seek(offset, whence=0)	    改变数据流的位置，返回新的绝对位置
# F.readable()	                判断这个文件是否可读,可读返回True,否则返回False
# F.writable()	                判断这个文件是否可写,可写返回True,否则返回False
# F.seekable()	                返回这个文件对象是否支持随机定位
# F.truncate(pos = None)	    剪掉 自pos位置之后的数据，返回新的文件长度(字节为单位)


### 示例: 目录的递归操作
import os
# 从某个目录(E:/Work_PyCharm/Python3_shangxuetang/[02]Python-函数操作/test/)下查找包含hello的py文件有哪些?
file_list = []
# 递归函数---使用绝对路径:parent_dir:文件所在父目录的绝对路径,file_name:当前你要处理的文件或目录
def find_hello(parent_dir,file_name):
    # 拼接你当前处理的文件或目录的绝对路径
    file_abspath = os.path.join(parent_dir,file_name)
    # 首先判断是否是一个目录
    if os.path.isdir(file_abspath):  # 如果传入的是一个目录
        for f in os.listdir(file_abspath):  # 进入目录,列表该目录下的所有文件列表
            find_hello(file_abspath,f)  # 递归调用自己本身的函数
    else:
        # 如果传入的是一个文件,判断文件名是否是以.py结尾
        if file_abspath.endswith(".py"):
            # 读取该.py结尾的文件,查看内容中是否含有hello
            if read_and_find_hello(file_abspath):
                file_list.append(file_abspath)

# 读取.py结尾的文件,查看内容是否有hello
def read_and_find_hello(py_file):
    flag = False
    # 打开文件
    file = open(py_file)
    while True:
        # 查看文件内容是否含有hello
        line = file.readline()
        if line == "":  # 如果文件读取完成(最后一行),退出循环
            break
        elif "hello" in line:  # 查找到
            flag = True
            break
    # 关闭文件
    file.close()
    return flag

# print(read_and_find_hello("test/file2.py"))
find_hello("E:/Work_PyCharm/Python3_shangxuetang/[02]Python-函数操作","test")
print(file_list)


# 文件的另一种打开方式
"""
with 语句实质是上下文管理
1、上下文管理协议。包含方法__enter__() 和 __exit__()，支持该协议对象要实现这两个方法。
2、上下文管理器，定义执行with语句时要建立的运行时上下文，负责执行with语句块上下文中的进入与退出操作。
3、进入上下文的时候执行__enter__方法，如果设置as var语句，var变量接受__enter__()方法返回值。
4、如果运行时发生了异常，就退出上下文管理器。调用管理器__exit__方法。
"""
with open("foo.txt") as file:
    data = file.read()



