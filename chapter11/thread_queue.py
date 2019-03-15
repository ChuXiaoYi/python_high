# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 上午10:55
#       @Author  : cxy =.= 
#       @File    : thread_queue.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import time
import threading

detail_url_list = []

def get_detail_html(detail_url_list):
    while True:
        if len(detail_url_list):
            url = detail_url_list.pop()
            print("get detail html started")
            time.sleep(2)
            print("get detail html end")

def get_detail_url(detail_url_list):
    print("get detail url started")
    time.sleep(4)
    for i in range(20):
        detail_url_list.apped(f"http://projectsedu.com/{i}")
    print("get detail url end")

# 1.线程间的通信方式 —— 共享变量
if __name__ == '__main__':
    thread_detail_url = threading.Thread(target=get_detail_url, args=(detail_url_list, ))
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_list, ))
        thread_detail_html.start()
    start = time.time()


