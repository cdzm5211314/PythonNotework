# 代码有问题,虽然对象只有一个了,但是初始化方法 __init__方法执行了多次
# 解决方法:
# 1.定义一个 类属性 init_flag 标记是否执行过初始化方法,类属性初始值为False
# 2.在__init__方法中判断init_flag值是否为False,如果为False就执行初始化操作
# 3.然后将init_flag值设置为True
# 4.这样 再次自动调用 __init__方法时,,初始化方法就不会再执行了

class MusicPlayer(object):
    instance = None
    # 1.定义类属性:初始值为False
    init_falg = False
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        # 2.在init方法中判断init_falg的值是否为False,值为False,执行__init__方法
        if  MusicPlayer.init_falg:
            return
        # 3.修改init_falg的值为True
        print("对象实例初始化...")
        MusicPlayer.init_falg = True


# 创建多个对象
player1 = MusicPlayer()
print(player1)
player2 = MusicPlayer()
print(player2)







