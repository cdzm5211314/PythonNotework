# -*- coding:utf-8 -*-
# @Desc: 
# @Author: Administrator
# @Date: 2018-04-29 13:23

### 工厂模式: 最常用的实例化对象模式,可以给系统带来更大的扩展和减少代码的修改量(可维护性)

class Person(object):
    def __init__(self,name):
        self.name = name
    # def work(self,axe_type):
    def work(self):
        print(self.name + "开始工作了...")
        # axe = Factory.creat_axe(axe_type)
        # axe.cut_tree()
        factory = Stone_Axe_Factory()
        print(type(factory))
        axe = factory.create_axe()
        print(type(axe))
        axe.cut_tree()

class Axe(object):
    def __init__(self,name):
        self.name = name
    def cut_tree(self):
        print("使用%s砍树..."%self.name)
class StoneAxe(Axe):
    def cut_tree(self):
        print("使用花岗石做成的斧头砍树...")
class SteelAxe(Axe):
    def cut_tree(self):
        print("使用精钢做成的斧头砍树...")

# 工厂类
class Factory(object):
    def create_axe(self):
        pass
class Stone_Axe_Factory(Factory):
    def create_axe(self):
        return StoneAxe("花岗石斧头")
class Steel_Axe_Factory(Factory):
    def create_axe(self):
        return ("精钢斧头")
# class Factory(object):
#     # 生产斧头,根据用户指定的类型来生产
#     @staticmethod
#     def creat_axe(type):
#         if type == "stone":
#             return StoneAxe("花岗石斧头")
#         elif type == "steel":
#             return SteelAxe("精钢斧头")
#         else:
#             print("传递的类型不对...")

per = Person("张三")
per.work()