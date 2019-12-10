# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-10-05 14:59

# hashlib是一种算法,该算法接受传入的内容，经过运算得到一串hash值（不同的hash算法只是复杂度不一样）
# Python3.x 主要提供 SHA1, SHA224, SHA256, SHA384, SHA512 ，MD5 算法

import hashlib

## 使用sha256算法加密(括号内可以接受传值,类型要求是bytes类型)
# 加密方式一
s = "sha256算法"
hash_sha256 = hashlib.sha256(s.encode('utf-8'))
print(hash_sha256.hexdigest())
# 5d0c00a952909ec44a90fde3ebf0943a4f57c52c598412a0537e84d136b7408e

# 加密方式二
hash_sha256 = hashlib.sha256()
hash_sha256.update(s.encode('utf-8'))
print(hash_sha256.hexdigest())
# 5d0c00a952909ec44a90fde3ebf0943a4f57c52c598412a0537e84d136b7408e


## 使用md5算法加密(括号内可以接受传值,类型要求是bytes类型)
# 加密方式一
s = "md5算法"
hash_md5 = hashlib.md5(s.encode("utf-8"))  # s.encode("utf-8")编码
print(hash_md5.hexdigest())
# 获取16进制的算法数据: 124756ef340daf80196b4124686d651c

# 加密方式二
hash_md5 = hashlib.md5()
hash_md5.update(s.encode('utf-8'))
print(hash_md5.hexdigest())  # 124756ef340daf80196b4124686d651c


