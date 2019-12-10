# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23


class MusicPlayer(object):

    def __new__(cls, *args, **kwargs):
        # 创建对象时,new方法会自动调用
        print("创建对象,分配内存空间...")

        # 1.为对象分配空间
        # 注意:new方法是静态方法,调用的时候需要传递cls参数
        instance = super().__new__(cls)
        # 2.返回对象的引用
        return instance

    def __init__(self):
        print("初始化...")

# 创建播放器对象
player = MusicPlayer()
print(player)

# 总结:__new__()方法的作用
# 1,在内存中为对象 分配空间
# 2,返回 对象的引用

# 注意: 重写__new__方法一定要返回 return super().__new__(cls)
# 否则Python解释器 得不到 分配了内存空间的 对应引用,就不会调用对象的初始化方法:__init__方法




