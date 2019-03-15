# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午2:35
#       @Author  : cxy =.= 
#       @File    : thread_sync.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import threading
from threading import Lock, RLock

total = 0
# lock = Lock()
lock = RLock()

def add():
    global total
    global lock

    for i in range(100000):
        lock.acquire()
        lock.acquire()
        total += 1
        print(f"{threading.current_thread()}当前total：{total}")
        lock.release()
        lock.release()




def desc():
    global total
    global lock

    for i in range(100000):
        lock.acquire()
        total -= 1
        print(f"{threading.current_thread()}当前total：{total}")
        lock.release()


t1 = threading.Thread(target=add)
t2 = threading.Thread(target=desc)

t1.start()
t2.start()
