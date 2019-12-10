# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-05 13:18


# Python2.x 默认都是经典类,只有显示的继承了object,才是新式类
# Python3.x 默认都是新式类,经典类被废除,不必显示的继承object

# 注意:为了保证编写代码能在同时在Python2.x和Python3.x上运行!!!
# 在定义类时,如果没有父类,建议统一继承自object
class Clazz(object):
    pass

### 继承后方法的调用顺序(广度优先与深度优先)
# 经典类: 深度优先 DD ---> BB ---> AA ---> object ---> CC
# 新式类: 广度优先 DD ---> BB ---> CC ---> AA ---> object

class AA():
    def test(self):
        print("AA 的test方法")

class BB(AA):
    def test(self):
        print("BB 的test方法")
    # pass

class CC(AA):
    def test(self):
        print("CC 的test方法")

class DD(BB,CC):
    pass

d = DD()
d.test()
