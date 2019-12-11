# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-01 12:56

### Python的基本数据类型:
# 数字number: (整型int,浮点型float,复数complex,布尔型bool)
# 字符串str: ""
# 列表list: []
# 元组tuple: ()
# 集合set: {}
# 字典dict: {key:value}

### None 表示一个不存在的特殊对象

## 二进制表示方式: 0b开头,后跟0~1
## 八进制表示方式: 0o开头,后跟0~7
## 十六进制表示方式: 0x开头,后跟0~9,A~F,a~f

### 进制之间的转换:
dec = int(input('10进制数为：'))
print("转换为二进制为：", bin(dec))
print("转换为八进制为：", oct(dec))
print("转换为十六进制为：", hex(dec))

string1 = '01'
print('二进制字符串转换成十进制数为：', int(string1, 2))
string2 = '7'
print('八进制字符串转换成十进制数为：', int(string2, 8))
string3 = 'F'
print('十六进制字符串转换成十进制数为：', int(string3, 16))
