# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午4:31
#       @Author  : cxy =.= 
#       @File    : socket_client.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('127.0.0.1', 8000))
client.send('cxy'.encode('utf8'))
data = client.recv(1024)
print(data.decode('utf8'))
client.close()