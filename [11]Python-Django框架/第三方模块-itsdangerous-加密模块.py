# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-09-05 16:18

# itsdangerous : 加密模块,并且可以设置过期时间
# 安装: pip install itsdangerous

from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from itsdangerous import SignatureExpired  # 过期时间异常

# 对数据进行加密
serializer = Serializer('asdfghjkl',3600)  # 创建Serializer加密对象,第一个参数为加密的秘钥secret_key,第二个参数过期时间(秒)
info = {'data':1}  # 需要加密的数据
result = serializer.dumps(info)  # 给数据加密,加密后数据为bytes类型数据
print(result)  # 加密后的数据
print(result.decode('utf8'))  # bytes类型数据转换为字符串类型数据

# 对加密的数据进行解密
serializer = Serializer('asdfghjkl',3600)  # 创建Serializer解密对象,参数需要与创建加密对象的参数一致
res = serializer.loads(result)
print(res)




