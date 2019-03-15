# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午12:20
#       @Author  : cxy =.= 
#       @File    : thread_queue_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import time
import threading
from queue import Queue

def get_detail_html(queue):
    while True:
        url = queue.get()
        print("get detail html started")
        time.sleep(2)
        print("get detail html end")

def get_detail_url(queue):
    """
    爬去文章列表页
    :param queue:
    :return:
    """
    print("get detail url started")
    time.sleep(4)
    for i in range(20):
        queue.put(f"http://projectsedu.com/{i}")
    print("get detail url end")

if __name__ == '__main__':
    detail_url_queue = Queue(maxsize=1000)
    thread_detail_url = threading.Thread(target=get_detail_url , args=(detail_url_queue,))
    for i in range(10):
        thread_detail_html = threading.Thread(target=get_detail_html, args=(detail_url_queue,))
        thread_detail_html.start()
    start = time.time()

    detail_url_queue.join()
    print(f"last time: {time.time()-start}")