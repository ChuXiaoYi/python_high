# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午3:57
#       @Author  : cxy =.= 
#       @File    : thread_semaphore.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import time
import threading

class HtmlSpider(threading.Thread):

    def __init__(self, url, sem):
        super(HtmlSpider, self).__init__()
        self.url = url
        self.sem = sem

    def run(self):
        time.sleep(2)
        print('get html success')
        self.sem.release()

class UrlProducer(threading.Thread):

    def __init__(self, sem):
        super(UrlProducer, self).__init__()
        self.sem = sem

    def run(self):
        for i in range(20):
            self.sem.acquire()
            html_thread = HtmlSpider(f'https://baidu.com/{i}', self.sem)
            html_thread.start()


if __name__ == '__main__':
    sem = threading.Semaphore(3)
    url_producer = UrlProducer(sem)
    url_producer.start()
