# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午6:02
#       @Author  : cxy =.= 
#       @File    : multiprocessing_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import os
import time

# pid = os.fork()
# print("cxy")
#
# if pid == 0:
#
#     print(f'我是子进程：{os.getpid()}，我的父进程：{os.getppid()}')
# else:
#     print(f'我是父进程：{pid}')

from concurrent.futures import ProcessPoolExecutor
import multiprocessing

def get_html(n):
    time.sleep(n)
    print("sub_progress success")
    return n



if __name__ == '__main__':
    # progress = multiprocessing.Process(target=get_html, args=(2,))
    # progress.start()
    # progress.join()
    # print("main progress end")


    pool = multiprocessing.Pool()
    # result = pool.apply_async(func=get_html, args=(2,))
    # pool.close()
    # pool.join()
    # print(result.get())
    # print("main progress end")

    for result in pool.imap_unordered(get_html, [1, 5, 3]):
        print(f'{result} sleep success')
    pool.close()
    pool.join()

