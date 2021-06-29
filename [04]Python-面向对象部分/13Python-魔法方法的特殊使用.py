# -*- coding:utf-8 -*-


### 面向对象 - with上下文管理器： __enter__() 和 __exit__()
# with 语句后面的结果对象，需要重写 __enter__() 和 __exit__()方法
# 当进入到with代码时，会自动调用 __enter__() 方法中的代码
# 当执行完with代码时，会自动调用 __exit__() 方法中的代码
class ExampleDemo1(object):

    def __enter__(self):  # with 拿到一个对象，触发该方法
        print("__enter__方法被调用1...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):  # with执行完毕后，执行该方法
        # exc_type 异常的类型
        # exc_val 异常的值
        # exc_tb 异常的内存地址
        print("__exit__方法被调用2...")
        return True


### 面向对象 - 对象后面加括号，触发执行： __call__()
# 注：__init__()方法的执行是由创建对象时触发的，即：对象 = 类名()
# 注：__call__()方法的执行是由对象后加括号触发的，即：对象() 或者 类名()()
class ExampleDemo2(object):

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("__init__方法被调用1！！！")

    def __call__(self, *args, **kwargs):
        print('__call__方法被调用2！！！')


### 面向对象 - 实现迭代器类： __iter__() 和 __next__()
class ExampleDemo3(object):

    def __init__(self,start):
        self.start = start

    def __iter__(self):  # 可迭代方法，将对象变成迭代器，故返回其自己
        print("__iter__方法被调用1---")
        return self

    def __next__(self):  # 对迭代器取值
        print("__next__方法被调用2---")
        if self.start > 10:
            raise StopIteration
        result = self.start
        self.start += 1
        return result


if __name__ == '__main__':
    # 上下文管理器
    with ExampleDemo1() as obj:  # obj是创建对象后调用__enter__方法的返回结果
        print(obj)


    ed1 = ExampleDemo2("张三", 21)
    ed1()
    ExampleDemo2("张三", 21)()


    ed3 = ExampleDemo3(1)
    for i in ed3:
        print(i)


