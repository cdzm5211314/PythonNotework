# -*- coding:utf-8 -*-
# @Desc:
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 单例模式: 保证创建的实例对象的只有一个
# 1.定义一个类属性，初始值为None，用于记录单例对象的引用
# 2.重写父类的__new__方法
# 3.如果类属性为None，就调用父类方法分配空间，并在类属性中记录结果
# 4.返回类属性中保存的对象引用
### 代码有问题，虽然对象只有一个了，但是初始化方法__init__方法执行了多次
# 1.定义一个类属性init_flag标记是否执行过初始化方法，类属性初始值为False
# 2.在__init__方法中判断init_flag值是否为False，如果为False就执行初始化操作
# 3.然后将init_flag值设置为True
# 4.这样再次自动调用__init__方法时,,初始化方法就不会再执行了

class MusicPlayer(object):
    # 1.定义类属性:记录第一个被创建对象的引用
    instance = None
    # 2.重写__new__ 方法:(静态方法)
    def __new__(cls, *args, **kwargs):
        # 3.如果类属性 is None,就调用父类方法分配空间,并在类属性中记录结果
        # 判断类属性是否是空对象
        if cls.instance is None:
            # 调用父类方法,为第一个对象分配空间
            cls.instance = super().__new__(cls)
        # 4.返回类属性中第一次保存的对象引用
        return cls.instance

    def __init__(self):
        print("对象实例初始化...")

# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)


# 单例模式 ---> 目的:让类创建对象,系统中只有 唯一的一个实例
# 1.定义一个类属性,初始值为None,用于记录单例对象的引用
# 2.重写父类的__new__ 方法
# 3.如果类属性 is None,就调用父类方法分配空间,并在类属性中记录结果
# 4.返回类属性中保存的对象引用






