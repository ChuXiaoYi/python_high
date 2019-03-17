# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/17 7:20 PM
#       @Author  : cxy =.= 
#       @File    : coroutine_nest.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import time
import asyncio


async def get_html(sleep_time):
    print('waiting')
    await asyncio.sleep(sleep_time)
    print(f'done after {sleep_time}s')


if __name__ == '__main__':
    task1 = get_html(2)
    task2 = get_html(3)
    task3 = get_html(4)

    tasks = [task1, task2, task3]

    loop = asyncio.get_event_loop()
    try:
        loop.run_until_complete(asyncio.wait(tasks))
    except KeyboardInterrupt as e:
        all_task = asyncio.Task.all_tasks()
        for task in all_task:
            print('cancel task')
            task.cancel()  # 在运行中的task不能被取消
        loop.stop()
        loop.run_forever()
    finally:
        loop.close()
