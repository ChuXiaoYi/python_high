# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午6:37
#       @Author  : cxy =.= 
#       @File    : python_thread.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
# 1 通过Thread类实例化
import time
import threading

def get_detail_html(url):
    print("get detail html started")
    time.sleep(2)
    print("get detail html end")

def get_detail_url(url):
    print("get detail url started")
    time.sleep(4)
    print("get detail url end")

if __name__ == '__main__':
    thread1 = threading.Thread(target=get_detail_html, args=("", ))
    thread2 = threading.Thread(target=get_detail_url, args=("", ))
    start_time = time.time()
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()

    print(f"last time {time.time()-start_time}")


