# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

## 什么是程序: 例如xxx.py这是程序,是一个静态的
## 什么是进程: 正在运行的应用程序就是一个进程;进程是资源分配的基本单元

## 进程的状态:
# 工作中,任务数往往大于CPU的核数,即一定有一些任务正在执行,而另外一些任务在等待CPU进行执行,因此导致了有了不同的状态
# 就绪态: 运行的条件都已经满足,正在等待CPU执行
# 执行态: CPU正在执行其功能
# 等待态: 等待某些条件满足,例如一个程序sleep了,此时就处于等待态


## 创建进程对象: multiprocessing.Process()
# 参数说明:
# target  如果传递了函数的引用,子进程就执行这里面的内容
# name    进程设定名称,默认为Process-N,N为从1开始递增的整数
# args    元组,给target指定的函数传递的参数,以元组的方式传递
# kwargs  字典,给target指定的函数传递的参数,以关键字方式传递

## multiprocessing.Process进程类提供了哪些属性:
# pid: 当前进程的pid(进程号)

## multiprocessing.Process进程类提供了哪些方法:
# start():          启动子进程实例(创建子进程)
# is_alive():       判断进程子进程是否还在活着
# join([timeout]):  是否等待子进程执行结束,或等待多少秒
# terminate():      不管任务是否完成,立即终止子进程

## 线程与进程的区别:
# 进程: 能够完成多任务,如: 一台电脑上能够同时运行多个多个QQ
# 线程: 能够完成多任务,如: 一个QQ中得多个聊天窗口


##############################################################################################

import multiprocessing
import time

def test1():
    """ 子进程要执行的代码 """
    while True:
        print(" --- test1 --- ")
        time.sleep(1)

def test2():
    """ 子进程要执行的代码 """
    while True:
        print(" --- test2 --- ")
        time.sleep(1)

# def main():
#
#     p1 = multiprocessing.Process(target=test1)
#     p2 = multiprocessing.Process(target=test2)
#     p1.start()
#     p2.start()


#############################################################################################

## 通过队列完成多进程之间通信

def download_from_web(q):
    """ 下载数据 """
    # 模拟从网上下载数据
    data = [11,22,33,44,55]
    # 向队列中写数据
    for temp in data:
        q.put(temp)
    print("下载器已经下载完了数据,并已存入队列中...")

def analysis_data(q):
    """ 数据处理 """
    waitting_analysis_data = list()
    # 从队列中取数据
    while True:
        data = q.get()
        waitting_analysis_data.append(data)
        if q.empty():  # 如果队列为空,退出循环
            break
    print(waitting_analysis_data)

# def main():
#     # 创建一个队列
#     q = multiprocessing.Queue()
#
#     # 创建多个进程,将队列的引用当做实参进行传递到里面
#     p1 = multiprocessing.Process(target=download_from_web, args=(q,))
#     p2 = multiprocessing.Process(target=analysis_data, args=(q,))
#     p1.start()
#     p2.start()


#############################################################################################

## 进程池: 可以指定最大进程数

# from multiprocessing import Pool
import random, os

def worker(msg):
    t_start = time.time()
    print("%s开始执行,进程号为%d" %(msg, os.getpid()))
    # random.random() 随机生成0~1之间的浮点数
    time.sleep(random.random()*2)
    t_stop = time.time()
    print(msg,"执行完毕,耗时%0.2f" % (t_stop - t_start))

pool = multiprocessing.Pool(3)  # 定义一个进程池,最大进程数3
for i in range(10):
    # Pool.apply_async(要调用的目标函数,(传递给目标函数的参数元组,))
    # 每次循环将会用空闲出来的子进程去调用目标
    pool.apply_async(worker, args=(i,))

print(" --- 开始 --- ")
pool.close()  # 关闭进程池,关闭后po不在接受新的请求
pool.join()  # 等待po中所有子进程执行完成,必须放在close语句之后
print(" --- 结束 --- ")



if __name__ == '__main__':
    # main()
    pass


