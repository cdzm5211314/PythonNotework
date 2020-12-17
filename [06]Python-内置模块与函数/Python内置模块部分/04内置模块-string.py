# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-23 8:11

import string

# result = string.ascii_letters  # 大小写字母常数
# 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
# result = string.letters
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

# result = string.ascii_lowercase  # 小写字母常数
# 'abcdefghijklmnopqrstuvwxyz'
# result = string.lowercase
# 'abcdefghijklmnopqrstuvwxyz'

# result = string.ascii_uppercase  # 大写字母常数
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# result = string.uppercase
# 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# result = string.digits  # 十进制数字常数
# '0123456789'

# result = string.hexdigits  # 十六进制数字常数
# '0123456789abcdefABCDEF'

# result = string.octdigits  # 八进制数字常数
# '01234567'

# result = string.punctuation  # ASCII字符串，在C语言环境中被视为标点字符
# '!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

# result = string.printable  # 能够被打印的ASCII字符串
# '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~ \t\n\r\x0b\x0c'

# result = string.whitespace  # 包含所有被视为空格的ASCII字符的字符串,字符空间，制表符，换行符，返回页面，换页符和垂直选项卡
# '\t\n\x0b\x0c\r

#  使用string模块生成随机字符串
import random,string
def genRandomString(slen=10):
    return ''.join(random.sample(string.punctuation + string.ascii_letters + string.digits, slen))

res = genRandomString()
print(res)
print(''.join(random.sample(string.printable,10)))

# 使用random模块生成随机的数字与字母的字符串
tmp_list = []
for i in range(5):
    u = chr(random.randint(65, 90))  # 生成大写字母
    l = chr(random.randint(97, 122))  # 生成小写字母
    n = str(random.randint(0, 9))  # 生成数字，注意要转换成字符串类型

    tmp = random.choice([u, l, n])
    tmp_list.append(tmp)

print("".join(tmp_list))





