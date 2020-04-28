# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator

# 安装: pip install greenlet
# 安装: pip install gevent


from greenlet import greenlet
import time

def test1():
    while True:
        print(" ---A--- ")
        gr2.switch()
        time.sleep(0.5)

def test2():
    while True:
        print(" ---B--- ")
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(test1)
gr2 = greenlet(test2)

#切换到gr1中运行
gr1.switch()


########################################################################################

import gevent
import time
from gevent import monkey

monkey.patch_all()

def f1(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

def f2(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

def f3(n):
    for i in range(n):
        print(gevent.getcurrent(), i)
        time.sleep(0.5)
        # gevent.sleep(0.5)

print("---1---")
g1 = gevent.spawn(f1, 5)
print("---2---")
g2 = gevent.spawn(f2, 5)
print("---3---")
g3 = gevent.spawn(f3, 5)
print("---4---")
g1.join()
g2.join()
g3.join()