# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/15 上午10:34
#       @Author  : cxy =.= 
#       @File    : progress_queue.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
# from multiprocessing import Process, Queue

import time

# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == '__main__':
#     queue = Queue(10)
#     my_producer = Process(target=producer, args=(queue, ))
#     my_consumer = Process(target=consumer, args=(queue, ))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()

# manager
# from multiprocessing import pool, Manager
#
# def producer(queue):
#     queue.put("a")
#     time.sleep(2)
#
# def consumer(queue):
#     time.sleep(2)
#     data = queue.get()
#     print(data)
#
# if __name__ == '__main__':
#     p = pool.Pool(2)
#     queue = Manager().Queue(10)
#     p.apply_async(producer, args=(queue, ))
#     p.apply_async(consumer, args=(queue, ))
#     p.close()
#     p.join()

# Pipe
# from multiprocessing import pool, Pipe, Process
#
# def producer(send_pipe):
#     send_pipe.send("2")
#     time.sleep(2)
#
# def consumer(receive_pipe):
#     time.sleep(2)
#     data = receive_pipe.recv()
#     print(data)
#
# if __name__ == '__main__':
#     receive_pipe, send_pipe = Pipe()
#
#     my_producer = Process(target=producer, args=(send_pipe, ))
#     my_consumer = Process(target=consumer, args=(receive_pipe, ))
#
#     my_producer.start()
#     my_consumer.start()
#
#     my_producer.join()
#     my_consumer.join()


from multiprocessing import Manager, Process

def add_data(p_dict, key, value):
    p_dict[key] = value

if __name__ == '__main__':
    progress_dict = Manager().dict()
    first_progress = Process(target=add_data, args=(progress_dict, 'k1', 'v1'))
    second_progress = Process(target=add_data, args=(progress_dict, 'k2', 'v2'))

    first_progress.start()
    second_progress.start()
    first_progress.join()
    second_progress.join()

    print(progress_dict)