# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-12 9:39


## 多任务的原理:
# 1.并发: 假的多任务,指的是任务数大于CPU核数,经过时间片的轮转,快速的交替运行任务
# 2.并行: 真的多任务,指的是任务数小于等于CPU核数,即任务真的是一起执行

## 实现多任务的三种方式: 线程,进程,协程

## 什么是线程: 线程也是一种多任务编程方法,可以利用计算机多核资源完成程序的并发执行;线程又被称为轻量级的进程
# 注: 程序运行起来,就给它创建了一个主线程,等待子线程结束后再结束


## 创建线程对象: threading.Thread()
# 参数说明:
# target  目标线程函数名(即指定线程去哪个函数执行代码)
# name    线程名称,默认Thread-1
# args    元组,给线程函数位置传参(即线程调用函数时传递什么数据过去)
# kwargs  字典,给线程函数键值传参(即线程调用函数时传递什么数据过去)

# threading.Thread线程类提供了哪些方法:
# start():          启动线程,让目标线程函数开始执行
# run():            用以表示线程活动的方法
# join([time]):     等待至线程中止.这阻塞调用线程直至线程的join() 方法被调用中止-正常退出或者抛出未处理的异常-或者是可选的超时发生
# isAlive():        返回线程是否活动的
# getName():        返回线程名
# setName():        设置线程名

# threading线程模块提供了哪些函数:
# threading.current_thread():    返回当前的线程变量
# threading.enumerate():         返回当前运行的线程列表(列表中存放的是主线程和每一个子线程的信息)
# 注: 如果主线程挂了,子线程立即结束运行;当子线程运行结束,不会影响主线程的运行
# threading.active_count():      返回正在运行的线程数量,与len(threading.enumerate())有相同的结果


##################################################################################################################

import threading
import time

### 创建线程的两种方式:
## 第一种创建线程方式:
def test():
    for i in range(1,6):
        print("线程执行: %s" % i)
        # time.sleep(1)

# 创建线程
t1 = threading.Thread(target=test)
t2 = threading.Thread(target=test)
# t1 = threading.Thread(target=test, args=("001",))
# t2 = threading.Thread(target=test, kwargs={"num": "002"})
# 启动线程
t1.start()
t2.start()

## 总结:
# 使用Thread创建子线程对象的时候,并不会创建线程
# 当子线程对象调用start()方法的时候,才开始创建子线程,并且线程开始运行


## 第二种创建线程方式:
# 1.继承Thread类
class MyThread(threading.Thread):

    # 2.重写run方法,run方法是该线程要执行的动作
    def run(self):
        for i in range(1, 6):
            print("线程执行: %s" % i)
            # time.sleep(1)

    # def __init__(self, num):
    #     # 2.加载Thread父类中的__init__方法
    #     super(MyThread, self).__init__()
    #     self.num = num

# 创建线程
mt1 = MyThread()
mt2 = MyThread()
# mt1 = MyThread("001")
# mt2 = MyThread("002")
# 开启线程
mt1.start()
mt2.start()


#############################################################################################

## 全局变量总结:
# 在一个函数中对全局变量进行修改的时候,到底是否需要使用global进行说明???要看是否对全局变量的执行指向进行了修改???
# 如果修改了指向,即让全局变量变量指向了一个新的地方,那么必须使用global
# 如果仅仅是修改了指向空间中的数据,此时不需要使用global


