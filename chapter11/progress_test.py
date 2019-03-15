# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午5:33
#       @Author  : cxy =.= 
#       @File    : progress_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from concurrent.futures import ProcessPoolExecutor


# 计算密集型，耗费cpu，用多进程
# def fib(n):
#     if n<=2:
#         return 1
#     return fib(n-1) + fib(n-2)
#
# print(fib(3))
#
# if __name__ == '__main__':
#     with ProcessPoolExecutor(3) as executor:
#         all_task = [executor.submit(fib, (num)) for num in range(25, 40)]
#         start_time = time.time()
#         for future in as_completed(all_task):
#             data = future.result()
#             print(f'exe result: {data}')
#
#         print(f'last time is {time.time()-start_time}')


def random_sleep(n):
    time.sleep(n)
    return n

if __name__ == '__main__':
    with ProcessPoolExecutor(3) as executor:
        all_task = [executor.submit(random_sleep, (num)) for num in [2]*30]
        start_time = time.time()
        for future in as_completed(all_task):
            data = future.result()
            print(f'exe result: {data}')

        print(f'last time is {time.time()-start_time}')
