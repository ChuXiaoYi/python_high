# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午3:34
#       @Author  : cxy =.= 
#       @File    : read_file.py
#       @Software: PyCharm
#       @Desc    : 读取500G文件
# ---------------------------------------------
def myreadlines(f, newline):
    buf = ""
    while True:
        while newline in buf:
            pos = buf.index(newline)
            yield buf[:pos]
            buf = buf[pos+len(newline):]
        chunk = f.read(4096)

        if not chunk:
            yield buf
            break
        buf += chunk

