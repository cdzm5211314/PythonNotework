# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-03 17:10

## 文件操作的作用:
# 读取内容,写入内容,备份内容
# 把一些内容(数据)存储存放起来,可以让程序下一次执行的时候直接使用,而不必重新制作一份,省时省力

## 文件操作的流程:
# 注:任何的操作系统,一个应用程序同时打开文件的数量有最大数限制
# 1.打开文件
# 2.读写文件
# 3.关闭文件

## 文件的打开函数: open(file, mode)
# file: 表示要打开的目标文件名的字符串(可以包含文件所在的具体路径)
# mode: 表示设置打开目标文件的模式(访问模式),如:只读,写入,追加
# ft = open(file, mode='r') 用于打开文件,返回此文件对应的文件流对象,如打开失败,则触发OSError错误

## 文件的关闭方法: close()
# ft.close()  关闭,释放系统资源

## 文件的访问模式(字符的含义):
# 'r'  只读,若文件存在,文件的指针将会放在文件的开头;若文件不存在,则报错
# 'w'  只写,若文件存在,则清空文件内容再写入内容;若文件不存在,则先创建该文件再写入内容
# 'a'  追加(只写),若文件存在,则在文件末尾追加写入内容并且只能在文本末尾追加;若文件不存在,则先创建该文件再写入内容
# 'r+' 读写,若文件存在,文件的指针将会放在文件的开头;若文件不存在,则报错
# 'w+' 读写,若文件存在,则清空文件内容再写入内容;若文件不存在,则先创建该文件再写入内容
# 'a+' 追加(读写),若文件存在,则在文件末尾追加写入内容并且只能在文本末尾追加;若文件不存在,则先创建该文件再写入内容

# 通常文件以文本方式打开,读写文件的字符串都会被特定的编码方式(默认是UTF-8)进行编码
# 注: 访问模式后面加'b'字符,表示以二进制格式打开文件(字节的方式)进行读取或写入,文件指针放在文件的开头
# 如 rb,wb,ab,rb+,wb+,ab+

## Python文件操作的常用方法:
# 文本文件的操作方法:
# F.close()	                    关闭文件,释放系统资源
# F.read(num)	                从文件中读取数据的长度(单位字节),如果num未传入,表示读取文件所有数据
# F.readline()	                一次读取一行数据
# F.readlines()	                按照行的方式把整个文件中的内容进行一次性读取,并返回一个列表,每行数据为一个元素
# F.seek(偏移量,起始位置)          用来改变文件的指针(起始位置:0表示文件开头,1表示当前位置,2表示文件结尾)
# F.write(text)	                写一个字符串到文件流中,返回写入的字符数
# F.writelines(lines)	        每行字符串的列表
# F.flush()	                    把写入文件对象的缓存内容写入到磁盘

# 二进制文件操作方法:
# F.tell()	                    返回当前文件流的绝对位置
# F.seek(offset, whence=0)	    改变数据流的位置，返回新的绝对位置
# F.readable()	                判断这个文件是否可读,可读返回True,否则返回False
# F.writable()	                判断这个文件是否可写,可写返回True,否则返回False
# F.seekable()	                返回这个文件对象是否支持随机定位
# F.truncate(pos = None)	    剪掉 自pos位置之后的数据，返回新的文件长度(字节为单位)

## 文件的备份示例
old_name = input("请输入你要备份的文件名: ")  # 接受用户输入的目标文件名
index = old_name.rfind(".")  # 提取目标文件后缀名.的下标
# 判断是否有效文件名,
if index > 0:
    postfix = old_name[index:]  # 提取后缀名
# new_name = old_name[:index] + "[备份]" + old_name[index:]  # 组织备份的文件名
new_name = old_name[:index] + "[备份]" + postfix  # 组织备份的文件名
# 打开源文件与备份文件
ft1 = open(old_name, 'rb')
ft2 = open(new_name, 'wb')
# 源文件读取,备份文件写入
# 如果不确定文件大小,循环读取写入,当读取出来的数据没有了就终止循环
while True:
    result = ft1.read(1024)
    if len(result) == 0:
        # 表示读取完成了
        break
    ft2.write(result)
# 关闭源文件与备份文件
ft1.close()
ft2.close()

## 文件的另一种打开方式
"""
with 语句实质是上下文管理
1、上下文管理协议.包含方法__enter__() 和 __exit__().支持该协议对象要实现这两个方法
2、上下文管理器,定义执行with语句时要建立的运行时上下文,负责执行with语句块上下文中的进入与退出操作
3、进入上下文的时候执行__enter__方法,如果设置as var语句,var变量接受__enter__()方法返回值
4、如果运行时发生了异常,就退出上下文管理器,调用管理器__exit__方法
"""
with open("foo.txt") as file:
    data = file.read()


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






