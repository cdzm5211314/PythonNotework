# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-11 17:30

### 正则表达式动机:
# 1. 文本处理已经成为计算机的常见工作之一
# 2. 对文本内容的搜索，定位，提取是逻辑比较复杂的工作
# 3. 为了快速解决上述问题，产生了正则表达式技术

## 定义:即文本的高级匹配模式，提供搜索，替代等功能。其本质是一系列由特殊符号组成的字串，这个字串即正则表达式。
## 匹配原理:由普通字符和特殊符号组成字符串，通过描述字符的重复和位置等行为，达到匹配某一类字符串的目的



### 元字符的使用:
## 普通字符: a b c
# 匹配规则: 每个字符匹配对应的字符
In [15]: re.findall("hello","hello world")
Out[15]: ['hello']

## 或: |
# 匹配规则: 匹配 | 两边任意一个正则表达式
In [21]: re.findall("ab|cd","abcdefghialkjasbab")
Out[21]: ['ab', 'cd', 'ab']

## 匹配单个字符: .
# 匹配规则: 匹配除换行外的任意字符
In [24]: re.findall("f.o","foo is not fao")
Out[24]: ['foo', 'fao']

## 匹配开始位置: ^
# 匹配规则: 匹配目标字符串的开头位置
In [30]: re.findall("^Tom","Tom is a boy")
Out[30]: ['Tom']

## 匹配结束位置: $
# 匹配规则: 匹配字符串的结束位置
In [32]: re.findall("Tom$","hi Tom")
Out[32]: ['Tom']

## 匹配重复: *  --->  fo* -> fooooooooo  f  fo
# 匹配规则: 匹配前面的字符出现0次或多次
In [33]: re.findall("fo*","fadsfafoooafo")
Out[33]: ['f', 'f', 'fooo', 'fo']

## 匹配重复: +  ---> fo+ -> fo  fooooo
# 匹配规则: 匹配前面的字符出现1次或多次
In [36]: re.findall("fo+","fadsfafoooafo")
Out[36]: ['fooo', 'fo']

## 匹配重复: ?  ---> fo? ->  f   fo
# 匹配规则: 匹配前面的字符出现0次或1次
In [42]: re.findall("fo?","fasdffoafooooo")
Out[42]: ['f', 'f', 'fo', 'fo']

## 匹配重复: {n}    ---> fo{3} -> fooo
# 匹配规则:匹配指定的重复次数
In [43]: re.findall("fo{2}","fasdffoafooooo")
Out[43]: ['foo']

## 匹配重复: {m,n}  ---> fo{2,4} -> foo  fooo  foooo
# 匹配规则: 匹配前面的正则表达式 m--n次
In [46]: re.findall("fo{2,4}","fasdfofoooafooooo")
Out[46]: ['fooo', 'foooo']

## 匹配字符集合: [字符集]
# 匹配规则: 匹配任意一个字符集中的字符
In [51]: re.findall("^[A-Z][a-z]*","Boy")
Out[51]: ['Boy']

## 匹配字符集: [^...]    ---> [^abc] -> 除a b  c之外任意字符
# 匹配规则: 字符集取非，除列出的字符之外任意一个字符
In [54]: re.findall("[^ ]+","a little boy")
Out[54]: ['a', 'little', 'boy']

## 匹配任意(非)数字字符: \d   \D
# 匹配规则: \d匹配任意数字字符[0-9]    \D匹配任意非数字字符[^0-9]
In [57]: re.findall("1\d{10}","18888886666")
Out[57]: ['18888886666']

## 匹配任意(非)普通字符: \w   \W
# 匹配规则: \w匹配普通字符[_0-9a-zA-Z],也能匹配普通汉字   \W匹配非普通字符
re.findall("\w+","hello#nihao%asdf@adsgdfg!df&")
Out[60]: ['hello', 'nihao', 'asdf', 'adsgdfg', 'df']
re.findall("\W+","hello#nihao%asdf@adsgdfg!df&")
Out[63]: ['#', '%', '@', '!', '&']

## 匹配任意(非)空字符: \s   \S
# 匹配规则: \s匹配任意空字符[ \r\t\n\v\f]   \S匹配任意非空字符
In [65]: re.findall("\w+\s+\w+","hello   world")
Out[65]: ['hello   world']
In [66]: re.findall("\S+","hello this is tom")
Out[66]: ['hello', 'this', 'is', 'tom']

## 匹配字符串位置: \A   \Z
# 匹配规则: \A匹配字符串开头位置^    \Z匹配字符串结尾位置$


### 绝对匹配: 正则表达式要完全匹配目标字符串内容
## 在正则表达式开始和结束位置加上^ $ (或者\A \Z),这样正则表达式必须匹配整个目标字符串才会有结果
In [75]: re.findall("\A\d+\Z","123445")
Out[75]: ['123445']

## 匹配(非)单词边界: \b   \B
# 匹配规则: \b匹配单词边界位置,普通字符和非普通字符交界认为是单词边界  \B匹配非单词边界位置
In [81]: re.findall(r"num\b","num#asdf#")
Out[81]: ['num']
In [82]: re.findall(r"num\b","numasdf#")
Out[82]: []


### 元字符总结:
# 匹配单个字符: a   .   \d  \D  \w  \W  \s  \S [...]  [^...]
# 匹配重复: *   +  ?  {n}  {m,n}
# 匹配位置: ^  $  \A  \Z   \b  \B
# 正则中的特殊符号：.  *  +  ?  ^  $  []  {}   ()  |  \
# 其他: |  () \
# 正则表达式转义: \   ---> 正则表达式如果匹配特殊字符需要加 \ 表达转义
"""
         正则          目标字符串
e.g.     \$\d+  ---->     $10
         pattern        string
python  "\\$\\d+"        "$10"
raw      r"\$\d+"        "$10"
"""
## raw字符串: 原始字符串对内容不解释转义，就表达内容原本意义,如: r"\$\d+" ---> "$10"

## 贪婪与非贪婪
# 贪婪模式: 正则表达式的重复匹配总是尽可能多的向后匹配更多内容   *   +   ？  {m,n}
# 非贪婪(懒惰模式): 尽可能少的匹配内容  贪婪 ---> 非贪婪  *？  +？  ??  {m,n}?
In [106]: re.findall(r"ab+?","abbbbbbbb")
Out[106]: ['ab']
In [107]: re.findall(r"ab??","abbbbbbbb")
Out[107]: ['a']

### 正则表达式的子组:
# 可以使用()为正则表达式建立子组，子组可以看做是正则表达式内部操作的一个整体
# 子组是在正则表达式整体匹配到内容的前提下才会发挥作用，它不影响正则表达式整体去匹配目标内容这一原则
## 子组的使用:
# 1.作为内部整体可以改变某些元字符的行为
re.search(r"(ab)+\d+","ababab1234").group()
'ababab1234'
re.search(r"\w+@\w+\.(com|cn)","abc@123.com").group()
'abc@123.com'
# 2.子组在某些操作中可以单独提取出匹配内容
re.search(r"(https|http|ftp)://\S+","https://www.baidu.com").group(1)
'https'

### 捕获组和非捕获组: 可以通过组名更方便获取某组内容
# 格式: (?P<name>pattern)
re.search(r"(?P<dog>ab)cdef",'abcdefghti').group('dog')
'ab'



### Python内置模块: re
import re
## 生成正则表达式对象
regex = compile(pattern,flags = 0)
# 参数说明:
# pattern   正则表达式
# flags     功能标志位，丰富正则表达式的匹配功能
# 返回值: 回正则表达式对象

## 从目标字符串查找正则匹配内容
regex.findall(string,pos,endpos)
# 参数说明:
# string  目标字符串
# pos     匹配目标的起始位置
# endpos  匹配目标的终止位置
# 返回值: 返回匹配到的内容,如果正则表达式有子组则只返回子组对应内容


## 从目标字符串查找正则匹配内容
re.findall(pattern,string,flags)
# 参数说明:
# pattern  正则表达式
# string   目标字符串
# flags    标志位
# 返回值: 返回匹配到的内容,如果正则表达式有子组则只返回子组对应内容

## 根据正则匹配内容切割字符串
re.split(pattern,string,flags = 0)
# 参数: pattern  string  flags
# 返回值: 返回列表，列表中为切割的内容

## 替换正则匹配到的目标子串部分
re.sub(pattern,replaceStr,string,max,flags)
# 参数：
# pattern     正则表达式
# replaceStr  要替换的内容
# string
# max         最多替换几处 默认全部替换
# flags
# 返回值: 返回替换后的字符串

## 替换正则匹配到的目标子串部分
re.subn(pattern,replaceStr,string,max,flags)
# 参数：
# pattern
# replaceStr  要替换的内容
# string
# max   最多替换几处 默认全部替换
# flags
# 返回值: 返回一个元组，为实际替换了几处和替换后的字符串

## 使用正则表达式匹配目标字符串
re.finditer(pattern,string,flags)
# 参数: pattern  string flags
# 返回值: 返回一个迭代对象，迭代到的内容是一个match对象

## 完全匹配目标字符串
re.fullmatch(pattern,string,flags)
# 参数: pattern,string,flags
# 返回值: 返回匹配到的match对象,如果没匹配成功返回None

## 从起始位置开始匹配目标字符串
re.match(pattern,string,flags)
# 参数: pattern,string,flags
# 返回值: 返回匹配到的match对象,如果没匹配成功返回None

## 正则表达式匹配目标字符串，只匹配第一处
re.search(pattern,string,flags)
# 参数: pattern,string,flags
# 返回值: 返回匹配到的match对象,如果没匹配成功返回None


#####小示例#####
# 验证手机号: 以1开头,第二位3,5,6,7,8后面9位就随意数字
result = re.match("1[35678]\d+","18103763930")
# print(result.group())
result = re.match("1[35678]\d{9}","18103763930")
# print(result.group())
# 验证邮箱: 邮箱名称是由a-z,A-Z,0-9,_组成的,然后是@符号,后面是域名
result = re.match("\w+@[a-z0-9]+\.[a-z]+","configrueadmin@163.com")
# print(result.group())
# 验证URL: 规则是前面https或http或ftp,后面是冒号+双斜杠,再后面就是任意非空白字符
result = re.match("(https|http|ftp)://[^\s]+","https://www.baidu.com")
# print(result.group())
# 验证身份证: 身份证是18位,前17位是数字,最后一个可能是数字也可能是字符
result = re.match("\d{17}[a-zA-Z0-9]","41152119890312123x")
# print(result.group())


# 示例: findall(), sub()
result = re.findall("\$\d+","abc $99def  $123xyz")  # 获取价格信息
# print(result)  # ['$99', '$123']
result = re.findall('a(.*?)b','aa456bb')  # 能够返回括号中的内容,括号前后的内容起到定位于过滤的作用
# print(result)  # 'a456'
result = re.sub("\$","#","abc $99def  $123xyz")  # 把字符串中$替换成#
# print(result)  # abc #99def  #123xyz

# 示例: split()
result = re.split("-","abc-def-ghj")
print(result)  # ['abc', 'def', 'ghj']
result = re.split("-","abc-def-ghj-")
print(result)  # ['abc', 'def', 'ghj', '']

