# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/17 6:35 PM
#       @Author  : cxy =.= 
#       @File    : loop_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
# import asyncio
# import time
#
#
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()  # 完成了前面的selector
#
#     tasks = [get_html("http://www.imooc.com") for i in range(100)]
#
#     loop.run_until_complete(asyncio.wait(tasks))
#     print(f'{time.time() - start_time} done!')


# 获取协程的返回值
# import asyncio
# import time
#
# from functools import partial
#
#
# async def get_html(url):
#     print("start get url")
#     await asyncio.sleep(2)
#     print("end get url")
#     return 'cxy'
#
#
# def callback(url, future):
#     print(url)
#     print("send email to cxy!")
#
#
# if __name__ == '__main__':
#     start_time = time.time()
#     loop = asyncio.get_event_loop()  # 完成了前面的selector
#
#     task = loop.create_task(get_html('http://www.imooc.com'))
#     task.add_done_callback(partial(callback, "callback args"))
#     loop.run_until_complete(task)
#     print(task.result())
#     print(f'{time.time() - start_time} done!')

# wait 和 gather
import asyncio
import time


async def get_html(url):
    print("start get url")
    await asyncio.sleep(2)
    print(f"end get url {url}")

if __name__ == '__main__':
    start_time = time.time()
    loop = asyncio.get_event_loop()  # 完成了前面的selector

    group1 = [get_html("http://www.imooc.com") for i in range(2)]
    group2 = [get_html("http://www.baidu.com") for i in range(2)]

    group1 = asyncio.gather(*group1)
    group2 = asyncio.gather(*group2)

    group2.cancel()

    loop.run_until_complete(asyncio.gather(group1, group2))
    print(f'{time.time() - start_time} done!')


