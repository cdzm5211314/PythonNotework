# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-12 9:39

## 什么是线程: 线程也是一种多任务编程方法，可以利用计算机多核资源完成程序的并发执行。线程又被称为轻量级的进程。

## 线程特征:
# * 线程计算机多核分配的最小单位
# * 一个进程可以包含多个线程
# * 线程也是一个运行的过程，消耗计算机资源，多个线程共享进程的资源和空间
# * 线程的创建删除消耗的资源都要远远小于进程
# * 多个线程之间执行互不干扰
# * 线程也有自己的特有属性，比如指令集 ID


## 创建线程对象: threading.Thread()
# 参数说明:
# name    线程名称,默认 Thread-1
# target  线程函数
# args    元组  给线程函数位置传参
# kwargs  字典  给线程函数键值传参


# threading模块提供了哪些函数:
# threading.current_thread():    返回当前的线程变量
# threading.enumerate():         返回一个包含正在运行的线程的list.正在运行指线程启动后、结束前，不包括启动前和终止后的线程
# threading.active_count():      返回正在运行的线程数量，与len(threading.enumerate())有相同的结果

# Thread类提供了哪些方法:
# run():            用以表示线程活动的方法。
# start():          启动线程,自动运行线程函数
# join([time]):     等待至线程中止.这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# isAlive():        返回线程是否活动的
# getName():        返回线程名
# setName():        设置线程名


##################################################################################################################
import threading
import time


### 创建线程的两种方式:
## 第一种方式:
def test(num):
    print("线程: " + num)
    time.sleep(2)

# Thread(): target参数表示线程目标,即线程函数
# Thread(): args参数是一个元组
# 创建线程
t1 = threading.Thread(target=test, args=("001",))
t2 = threading.Thread(target=test, kwargs={"num": "002"})
# 启动线程
t1.start()
t2.start()


## 第二种方式:
# 1.继承Thread
class MyThread(threading.Thread):
    def __init__(self, num):
        # 2.加载Thread父类中的__init__方法
        super(MyThread, self).__init__()
        self.num = num

    # 3.重写父类的run方法
    def run(self):
        print("线程: " + self.num)
        time.sleep(2)


# 创建线程
mt1 = MyThread("003")
mt2 = MyThread("004")
# 开启线程
mt1.start()
mt2.start()
