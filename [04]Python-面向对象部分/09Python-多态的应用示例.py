# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

### 多态的实现步骤:
# 定义父类,并提供公共方法
# 定义子类,并重写父类方法
# 传递子类对象给调用者,实现不同子类执行效果不同

class Dog(object):  # 父类

    def work(self):
        print("指哪打哪...")

class ArmyDog(Dog):  # 继承Dog类

    def work(self):  # 子类重写父类同名方法
        print("追击敌人...")

class DrugDog(Dog):  # 继承Dog类

    def work(self):  # 子类重写父类同名方法
        print("追查毒品...")


class Person(object):

    def work_with_dog(self, dog):  # 传入不同的对象,执行不同的代码,实现不同的效果
        dog.work()

p = Person()
ad = ArmyDog()
dd = DrugDog()

p.work_with_dog(ad)  # 追击敌人...
p.work_with_dog(dd)  # 追查毒品...
