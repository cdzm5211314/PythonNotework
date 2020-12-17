# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-31 16:01

### random : 取随机数
import random
# print(random.random())  # 默认随机取0-1之间的浮点数 0.0 <= x < 1.0
# print(random.uniform(1.5,10.0))  # 随机取区间内的浮点数 1.5 <= x < 10.0

# print(random.randint(1,7))  # 随机取1-7之间的整数,包头也包尾
# print(random.randrange(1,7))  # 随机取1-7之间的整数,包头不包尾
# print(random.randrange(0, 101, 2))  # 返回0-100的偶数
# print(random.choice("hello"))  # 随机取序列的一个元素
# print(random.choice(["java","c++","php","python"]))  # 随机取序列的一个元素
# print(random.sample(["张三","李四","王五","徐六","柳七"],3))  # 随机取序列的多个元素

# item = [1,2,3,4,5,6,7]
# item = (1,2,3,4,5,6,7)
# item = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
# random.shuffle(item)  # 随机打乱列表的顺序(只能打乱列表)
# print(item)

### 生成随机数
checkcode = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
check = random.sample(checkcode,4)
yzm = ''
for i in  check:
    yzm += str(i)
print(type(yzm),yzm)
yzm = "".join(check)

# 随机一个浮点数
# print(random.random())
# 随机取出一个任意范围内的浮点数
# print(random.uniform(1,3))

# 随机一个整数
# print(random.randint(1,5)) # 包1 - 包5
# print(random.randrange(1,5)) # 包1 - 不包5

# 随机取出列表中的一个元素
# print(random.choice([11,22,33,44,55]))

# 随机取出列表中的多个元素
# print(random.sample([11,22,33,44,55],3))

# 打乱顺序
# li = [1,2,3,4,5,6,7]
# random.shuffle(li)
# print(li)

# 验证码示例
# chr():可以将数字转换成对应的ascii码：A - 65, Z - 96，a - 97, z - 122
def v_code():
    res = ""
    for i in  range(5): # range(5) 取出：1 - 4
        # 随机取出0-9的数字
        num = random.randint(0,9)
        # 随机取出A-Z，a-z
        alf = chr(random.randint(65,122))
        # 随机取出两个元素中的一个，并转换成字符串
        s = str(random.choice([num,alf]))
        res += s
    return res

print(v_code())



