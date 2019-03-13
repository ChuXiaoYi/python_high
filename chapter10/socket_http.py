# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午5:40
#       @Author  : cxy =.= 
#       @File    : socket_http.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import socket
import urllib.parse

def get_url(url):
    # 通过socket请求html
    url = urllib.parse.urlparse(url)
    host = url.netloc
    path = url.path
    if path == "":
        path = "/"

    # 建立socket连接
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect((host, 80))

    client.send(f"GET {path}\r\nHost:{host}\r\nConnection:close\r\n\r\n".encode('utf8'))

    data = b""
    while True:
        d = client.recv(1024)
        if d:
            data += d
        else:
            break

    data = data.decode('utf8')
    print(data)
    client.close()

if __name__ == '__main__':
    get_url('http://www.baidu.com')
