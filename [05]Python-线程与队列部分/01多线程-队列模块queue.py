# -*- coding:utf-8 -*-
# @Desc : 
# @Author : Administrator
# @Date : 2019-07-12 9:29

## Python提供了一个队列操作:模块queue ---> 类Queue
# Queue: FIFO先入先出
# LifoQueue: FIFO后入先出
# PriorityQueue: 优先级


## 队列对象方法: Queue(maxsize) - 创建一个先进先出的队列
# Queue.qsize()                                 返回队列的大小
# Queue.empty()                                 判断队列是否为空,队列为空返回True
# Queue.full()                                  判断队列是否满了,队列满了返回True
# Queue.get(item, block=True, timeout=None)     从队列里取数据
# Queue.put(item, block=True, timeout=None)     往队列里放数据
# Queue.join()                                  一直阻塞,直到队列中的所有元素都被取出和执行
# Queue.put_nowait(item)                        往队列里存放元素，不等待
# Queue.get_nowait(item)                        从队列里取元素，不等待
# Queue.task_done()                             清除任务:从queue中取出一个任务,然后清除一下任务


