# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/15 下午2:56
#       @Author  : cxy =.= 
#       @File    : select_http.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import socket
from selectors import DefaultSelector, EVENT_WRITE, EVENT_READ
from urllib.parse import urlparse


#使用select完成http请求

selector = DefaultSelector()

urls = []
stop = False

class Fetcher(object):
    def get_url(self, url):
        self.spider_url = url
        # 通过socket请求html
        url = urlparse(url)
        self.host = url.netloc
        self.path = url.path
        self.data = b''
        if self.path == "":
            self.path = "/"

        # 建立socket连接
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.client.setblocking(False)

        try:
            self.client.connect((self.host, 80))  # 阻塞不会消耗cpu
        except BlockingIOError as e:
            pass

        # 注册
        selector.register(self.client.fileno(), EVENT_WRITE, self.connected)

    # 回调函数
    def connected(self, key):
        selector.unregister(key.fd)
        self.client.send("GET {} HTTP/1.1\r\nHost:{}\r\nConnection:close\r\n\r\n".format(self.path, self.host).encode("utf8"))
        selector.register(self.client.fileno(), EVENT_READ, self.readable)

    def readable(self, key):

        d = self.client.recv(1024)

        if d:
            self.data += d
        else:
            selector.unregister(key.fd)

            data = self.data.decode("utf8")
            html_data = data.split("\r\n\r\n")[1]
            print(html_data)
            self.client.close()

            urls.remove(self.spider_url)
            if not urls:
                global stop
                stop = True

def loop():
    """
    回调+时间循环+select
    :return:
    """
    while True:
        ready = selector.select()
        for key, mask in ready:
            call_back = key.data
            call_back(key)

if __name__ == "__main__":
    # fetcher = Fetcher()
    #
    # fetcher.get_url("http://www.baidu.com")
    # loop()
    fetcher = Fetcher()
    import time

    start_time = time.time()
    for url in range(20):
        url = "http://shop.projectsedu.com/goods/{}/".format(url)
        urls.append(url)
        fetcher = Fetcher()
        fetcher.get_url(url)
    loop()
    print(time.time() - start_time)
