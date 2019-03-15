# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午4:20
#       @Author  : cxy =.= 
#       @File    : concurrent_futures.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
from concurrent.futures import ThreadPoolExecutor, as_completed, wait

import time

def get_html(times):
    time.sleep(times)
    print(f'get page {times} success')
    return times

exector = ThreadPoolExecutor(max_workers=2)

# 通过submit提交执行的函数到线程池中
# task1 = exector.submit(get_html, (3))
# task2 = exector.submit(get_html, (2))

# 获取已经成功的task的返回
urls = [2, 3, 4]
all_task = [exector.submit(get_html, (url)) for url in urls]
wait(all_task)  # 等待所有完成（默认是ALL_COMPLETED）
for future in as_completed(all_task):
    data = future.result()
    print(f'get {data} page success')

# 通过executor获取已经完成的task
# for data in exector.map(get_html, urls):
#     print(f'get {data} page ')


# 用于判定某个任务是否完成, 非阻塞
# print(task1.done())
# print(task2.done())

# 获取task的执行结果，
# print(task1.result)
# print(task2.result)