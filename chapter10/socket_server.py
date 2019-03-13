# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午4:32
#       @Author  : cxy =.= 
#       @File    : socket_server.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('0.0.0.0', 8000))
server.listen()
sock, addr = server.accept()

# 获取从客户端发送的数据
# 一次获取1k的数据
data = server.recv(1024)
print(data.decode('utf8'))
sock.send(f"服务端接收到了{data}".encode('utf8'))
server.close()