# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-01 17:21

### 字符串str: Python字符串是不可改变的字符序列

## raw 字符串(原始字符串):
# 格式: r"字符串内容"
# 作用: 让转义字符 \ 无效
# 示例:
a = "c:\newfile\test.txt"
print(a)
# c:
# ewfile	est.txt
print(len(a)) # 17
a = r"c:\newfile\test.txt"
print(a)  # c:\newfile\test.txt
print(len(a)) # 19


## in / not in : 判断对象是否在容器中,存在返回True,不在返回Flase

## 字符串文本解析方法: split() 和 join()
# S.split(sep=None)  # 分割: 将字符串使用sep为分隔符进行分割,返回分割后的字符串的列表,当不给定参数时,用空白字符作为分隔符进行分割
# S.join(iterable)   # 拼接: 使用S字符串将iterable可迭代对象中的字符串进行拼接,返回一个新的字符串
# s = 'Beijing is capital'
# L = s.split(' ')  # L = ['Beijing', 'is', 'capital']
# s = '\\'
# L = ['C:', 'Programe files', 'python3']
# s2 = s.join(L)  # s2 = b'C:\Programe files\python3'

## 字符串的索引[index]操作:
# Python序列都可以用索引[index]来访问序列中的对象或元素
# Python序列的正向索引是从0开始,最后一个索引为len(序列) - 1
# Python序列的反向索引是-1表示最后一个,-len(序列)表示第一个


## 字符串的切片操作: 从字符串序列中取出一部分相应的元素重新组成一个字符串
    # 语法: 字符串[ (开始索引start) : (结束索引end) (:(步长s))]   ---> 注: () 内括起的部分代表可以省略
    # 说明: 包头不包尾
        # 1. 开始索引是切片开始切下的位置: 0代表第一个元素，-1代表最后一个元素
        # 2. 结束索引是切片的终止索引: (但不包含终止索引)
        # 3. 步长是: 切片每次获取完当前索引后移动的方向和偏移量
            # 1) 没有步长，相当于取值完成后向后移动一个索引的位置（默认为1)
            # 2) 当步长为正整数时，取正向切片:
                # 步长默认值为1, 开始索引默认值为0, 结束索引的默认值为len(s)
            # 3) 当步长为负整数时，取反向切片:
                # 反向切片时，默认的起始位置为最后一个元素，默认终止位置为第一个元素的前一个位置

## 整数转换为字符串:
# hex(number)  将整数转换为十六进制的字符串
# oct(number)  将整数转换为八进制的字符串
# bin(number)  将整数转换为十进制的字符串


## 字符串的构造(创建)函数: str()
# str(True)   ---> "True"
# str(Flase)   ---> "Flase"
# str(3.14)   ---> "3.14"
# str(None)   ---> "None"


## 字符串str的常用方法:
# S.isdigit()	判断字符串中的字符是否全为数字
# S.isalpha()	判断字符串是否全为英文字母
# S.islower()	判断字符串所有字符是否全为小写英文字母
# S.isupper()	判断字符串所有字符是否全为大写英文字母
# S.isspace()	判断字符串是否全为空白字符
# S.center(width[,fill])	    将原字符串居中，左右默认填充空格
# S.count(sub[, start[,end]])	获取一个字符串中子串的个数
# S.find(sub[, start[,end]])	获取字符串中子串sub的索引,失败返回-1
# S.strip()	    返回去掉左右空白字符的字符串
# S.lstrip()	返回去掉左侧空白字符的字符串
# S.rstrip()	返回去掉右侧空白字符的字符串
# S.upper()	    生成将英文转换为大写的字符串
# S.lower()	    生成将英文转换为小写的字符串
# S.replace(old, new[, count])	        将原字符串的old用new代替，生成一个新的字符串
# S.startswith(prefix[, start[, end]])	返回S是否是以prefix开头，如果以prefix开头返回True,否则返回False,
# S.endswith(suffix[, start[, end]])	返回S是否是以suffix结尾，如果以suffix结尾返回True,否则返回False


## 格式化字符串中的占位符和类型码
# %s	    字符串
# %r	    字符串，使用repr 而不是str
# %c	    整数转为单个字符
# %d	    十进制整数
# %o	    八进制整数
# %x	    十六进制整数(字符a-f小写)
# %X	    十六进制整数(字符A-F大写)
# %e	    指数型浮点数(e小写),如2.9e+10
# %E	    指数型浮点数(E大写),如2.9E+10
# %f, %F	浮点十进制形式
# %g, %G	十进制形式浮点或指数浮点自动转换
# %%	    等同于一个%字符



### 字节串: 存储以字节为单位的数据
# 说明: 字节串是不可变的字节序列,字节是0~255之间的整数
## 字节串的构造函数: bytes()
# bytes()                         生成一个空的字节串 等同于 b''
# bytes(整型可迭代对象)           用可迭代对象初始化一个字节串
# bytes(整数n)                    生成n个值为零的字节串
# bytes(字符串, encoding='utf-8') 用字符串的转换编码生成一个字节串



### 字节数组: 可变的字节序列
## 创建字节数组的构造函数: bytearray()
# bytearray()	                        创建空的字节数组
# bytearray(整数)	                    用可迭代对象初始化一个字节数组
# bytearray(整型可迭代对象)	            生成n个值为0的字节数组
# bytearray(字符串, encoding='utf-8')	用字符串的转换编码生成一个字节数组
# 注: 以上参数等同于字节串

## 字节数组的方法:
# B.clear()                     清空字节数组
# B.append(n)                   追加一个字节(n为0-255的整数)
# B.remove(value)               删除第一个出现的字节，如果没有出现，则产生ValueError错误
# B.reverse()                   字节的顺序进行反转
# B.decode(encoding='utf-8')    解码
# B.find(sub[, start[, end]])   查找


