# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-12-11 16:32

# 1) _xxx "单下划线" 开始的属性/方法叫做保护属性/方法,意思是只有类的实例对象和子类的实例对象能访问到这些属性/方法
# 注: 需通过类提供的接口进行访问,不能用 from module import * 导入
# 2) __xxx "双下划线" 开始的属性/方法叫做私有属性/方法,意思是只有在类中使用self访问;连子类的实例对象也不能访问到这些属性/方法
# 3) __xxx__ 系统定义名字,前后均有一个"双下划线",代表Python里特殊方法专用的标识,如 __init__()代表类的构造函数


###########################################################################################
# 定义类(类也可以称为类对象)
class Clazz(object):

    # 类属性就是类所拥有的属性,它被此类的所有对象所共有,在内存中只存在一个
    name = "类公有属性值"          # 类公有属性 ---> 所有实例对象共有的类属性
    _number = "类受保护属性值"     # 类受保护属性
    __age = "私有属性值"          # 类私有属性

    def __new__(cls, *args, **kwargs):
        """创建实例对象并返回该实例对象"""
        # 调用父类的(object)的__new__方法,返回一个Student类的实例对象,这个实例对象传递给init的self参数
        return object.__new__(cls)

    # def __init__(self):
    def __init__(self, higth):
        """构造函数-初始化实例对象属性值"""
        self.higth = higth            # 对象公有属性
        self.city = "对象公有属性值"        # 对象公有属性
        self._salary = "对象受保护属性值"   # 对象受保护属性
        self.__marriage = "对象私有属性值"  # 对象私有属性
        self.__gender = "@property函数转属性"  # 对象私有属性

    def __del__(self):
        """析构函数-销毁实例对象"""
        pass

    def __str__(self):

        return "把实例对象变成str字符串"


    # 私有属性-以调用方法的方式在外部进行获取与赋值
    # 使用公有的getXxx和setXxx方法对私有属性进行封装,
    def getMarriage(self):  # get方法获取私有属性值
        return self.__marriage

    def setMarriage(self, vaule):  # set方法给私有属性重新赋值
        self.__marriage = vaule

    # 私有属性-以调用属性的方式在外部进行获取与赋值
    # 使用property装饰器对私有属性进行封装
    # 注: 需要先定义getter,才去定义setter
    @property
    def gender(self):  # Getter装饰器,获取函数属性值(相当于getXxx()方法)
        print('获取函数属性值时执行的代码')
        return self.__gender
        # return "字符串类型数据"

    @gender.setter
    def gender(self,value):  # Setter装饰器,设置函数属性值(相当于setXxx()方法)
        print('设置函数属性值时执行的代码')
        self.__gender = value

    @gender.deleter
    def gender(self):  # Deleter,装饰器删除函数属性值
        print('删除函数属性值时执行的代码')
        del self.__gender


    def ordinaryFunc(self):  # 对象方法 -> 即普通方法
        print("对象公有方法(普通方法): ordinaryFunc()")

    def _protectedFunc(self):  # 受保护对象方法
        print("对象受保护方法: _protectedFunc()")

    def __privateFunc(self):  # 私有对象方法
        print("对象私有方法: __privateFunc()")

    @classmethod
    def clazzFunc(cls):  # 类方法
        print("类方法: clazzFunc()")

    @staticmethod
    def staticFunc():  # 静态方法
        print("静态方法: staticFunc()")


# 子类继承父类,会继承父类的所有属性和方法(除私有属性与私有方法外)
class SubClazz(Clazz):

    # def __init__(self):  # 根据调用父类的方法中是否需要参数,进行传参
    def __init__(self, higth, count):  # 根据调用父类的方法中是否需要参数,进行传参

        # 调用父类的初始化方法
        # 方法一简单直观,但面对多继承问题,只能多次调用每个父类的__init__方法
        # Clazz.__init__(self)
        Clazz.__init__(self, higth=higth)

        # 方法二不太直观,但可以解决多继承问题,会一次性的执行所有的父类的对应方法
        # super(SubClazz, self).__init__()  # super()表示父类对象
        super(SubClazz, self).__init__(higth=higth)  # super()表示父类对象

        # 子类特有的属性
        self.count = count

        # print("子类初始化方法调用成功...")
        print("子类初始化方法调用成功...", higth, count)



#########################################################################################
# print(" ----- 类属性(类公有属性,类受保护属性,类私有属性) begin -----> ")
# 创建实例对象
# c = Clazz()
# print(Clazz.name)       # 类名可以在外部直接访问类公有属性
# print(Clazz._number)    # 类名可以在外部直接访问类受保护属性
# print(Clazz.__age)      # 报错,无法在外部直接访问类私有属性
# print(c.name)           # 实例对象可以在外部直接访问类公有属性(但首先找的是实例对象的对象属性,如果没有才找类属性)
# print(c._number)        # 实例对象可以在外部直接访问类受保护属性
# print(c.__age)          # 报错,无法在外部直接访问类私有属性

# 注: 实例对象想给类属性重新赋值,其实并不是给类属性赋值,而是给实例对象定义了一个与类属性同名的对象属性,并给其赋值
# c.name = "张三"

# print(" ----- 类属性(类公有属性,类受保护属性,类私有属性) end ----- ")

#########################################################################################
# print(" ----- 对象属性(对象公有属性,对象受保护属性,对象私有属性) begin -----> ")

# 创建实例对象
# c = Clazz()

# print(Clazz.city)           # 报错,类名无法在外部直接访问对象公有属性
# print(Clazz._salary)        # 报错,类名无法在外部直接访问对象受保护属性
# print(Clazz.__marriage)     # 报错,类名无法在外部直接访问对象私有属性
# print(c.city)               # 实例对象可以在外部直接访问对象公有属性
# print(c._salary)            # 实例对象可以在外部直接访问对象受保护属性
# print(c.__marriage)         # 报错,实例对象无法在外部直接访问对象私有属性

# print(" ----- 对象属性(对象公有属性,对象受保护属性,对象私有属性) end ----- ")

#########################################################################################
# print(" ----- 对象方法(对象普通[公有]方法,对象受保护方法,对象私有方法) begin -----> ")

# 创建实例对象
# c = Clazz()
# print(Clazz.ordinaryFunc())         # 报错,类名无法在外部直接访问对象普通方法
# print(Clazz._protectedFunc())       # 报错,类名无法在外部直接访问对象受保护方法
# print(Clazz.__privateFunc())        # 报错,类名无法在外部直接访问对象私有类方法
# print(c.ordinaryFunc())             # 实例对象可以在外部直接访问对象普通方法
# print(c._protectedFunc())           # 实例对象可以在外部直接访问对象受保护方法
# print(c.__privateFunc())            # 报错,实例对象无法在外部直接访问对象私有方法

# print(" ----- 对象方法(对象普通[公有]方法,对象受保护方法,对象私有方法) end ----- ")

#########################################################################################
# print(" ----- 类方法(@classmethod) 与 静态方法(@classmethod) begin -----> ")
# 创建实例对象
# c = Clazz()
#
# Clazz.clazzFunc()   # 类名可以直接访问类方法
# Clazz.staticFunc()  # 类名可以直接访问静态方法
# c.clazzFunc()       # 实例对象可以直接访问类方法
# c.staticFunc()      # 实例对象可以直接访问静态方法

# print(" ----- 类方法(@classmethod) 与 静态方法(@classmethod) end ----- ")

#########################################################################################
# print(" ----- 魔术方法(前后双下划线) begin -----> ")

# def __new__(cls, *args, **kwargs):  # 创建实例对象并返回该实例对象

# def __init__(self):  # 构造函数,给实例对象设置属性值

# def __del__(self):   # 析构函数,当类的所有引用都被删除后,该类就会被系统从内存中删除

# def __str__(self):   # 把实例对象变成str字符串并返回

# 实例对象.__dict__:     # 将实例对象内部的所有对象属性名与所有对象属性值组成一个dict字典

# print(" ----- 魔术方法(前后双下划线) end ----- ")

#########################################################################################
# print(" ----- 继承:子类(子类对象)调用继承父类后的属性 begin -----> ")

# 创建子类实例对象
# sc = SubClazz()
# sc = SubClazz(175, 10)

# print(SubClazz.name)        # 子类类名可以直接访问父类的类公有属性
# print(SubClazz._number)     # 子类类名可以直接访问父类的类受保护属性
# print(SubClazz.__age)       # 报错,子类类名无法直接访问父类的类私有属性
# print(sc.city)              # 子类实例对象可以直接访问父类的对象公有属性
# print(sc._salary)           # 子类实例对象可以直接访问父类的对象受保护属性
# print(sc.__marriage)        # 报错,子类实例对象无法直接访问父类的对象私有属性

# print(" ----- 继承:子类(子类对象)调用继承父类后的属性 end ----- ")

#########################################################################################
# print(" ----- 继承:子类(子类对象)调用继承父类后的方法 begin -----> ")

# 创建子类实例对象
# sc = SubClazz()

# SubClazz.ordinaryFunc()      # 报错,子类类名无法直接访问父类的对象普通方法
# SubClazz._protectedFunc()    # 报错,子类类名无法直接访问父类的对象受保护方法
# SubClazz.__privateFunc()     # 报错,子类类名无法直接访问父类的对象私有方法
# sc.ordinaryFunc()            # 子类实例对象可以直接访问父类的对象普通方法
# sc._protectedFunc()          # 子类实例对象可以直接访问父类的对象受保护方法
# sc.__privateFunc()           # 报错,子类实例对象无法直接访问父类的对象私有方法

# print(" ----- 继承:子类(子类对象)调用继承父类后的方法 end ----- ")

#########################################################################################
# print(" ----- 继承:子类(子类对象)调用继承父类后的 类方法(@classmethod) 和 静态方法(@staticmethod) begin -----> ")

# 创建子类实例对象
# sc = SubClazz()

# SubClazz.clazzFunc()     # 子类类名可以直接访问父类的类方法
# SubClazz.staticFunc()    # 子类类名可以直接访问父类的静态方法
# sc.clazzFunc()           # 子类实例对象可以直接访问父类的类方法
# sc.staticFunc()          # 子类实例对象可以直接访问父类的静态方法

# print(" ----- 继承:子类(子类对象)调用继承父类后的 类方法(@classmethod) 和 静态方法(@staticmethod) end ----- ")

#########################################################################################
# print(" ----- @property装饰器函数 begin -----> ")

# property工具,它把方法包装成属性,让方法可以以属性的形式被访问和调用
# 注: getter() 定义在 setter() 之前

# 创建实例对象
# c = Clazz()

# print(c.gender)     # 获取函数属性值

# c.gender = "男"      # 设置函数属性值

# print(c.gender)     # 再次获取函数属性值

# print(" ----- @property装饰器函数 end ----- ")

#########################################################################################
print(" -----  begin 继承 -----> ")
# is a      # 代表类之间的继承关系
# has a     # 代表对象与它的成员之间的从属关系
class Fu(object):
    def __init__(self, name, age):
        self.name = name
        self.__age = age
        print("父类的init方法...", name, age)

    def fufunc(self):
        print("父类的普通方法...")

class Zi(Fu):

    # def __init__(self, name, age):
    def __init__(self, name, age, salary):
        # Fu.__init__()  # 调用父类的init方法

        # super()表示父类对象
        super(Zi, self).__init__(name=name, age=age)  # 调用父类的init方法,有参数传递

        # 子类自己的属性
        self.salary = salary

        # print("子类的init方法...", name, age)
        print("子类的init方法...", name, age, salary)

    def zifunc(self):
        print("子类的普通方法...")

# f = Fu("张三",21)
# print(f)

print("**************************************************************")

# 子类继承父类,子类拥有自己的__init__方法,未定义自己的属性,且调用父类的__init__方法
# z = Zi("李四",30)
# print(z)

print("**************************************************************")

# 子类继承父类,子类拥有自己的__init__方法,并定义自己的属性,且调用父类的__init__方法
# z = Zi("王五",25,3500)
# print(z)


print(" -----  end 继承 ----- ")

#########################################################################################



