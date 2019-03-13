# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午2:43
#       @Author  : cxy =.= 
#       @File    : how_gen_work.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
def foo():
    bar()

def bar():
    pass


import dis
# print(dis.dis(foo))

def  gen_func():
    yield 1
    name = 'a'
    yield 2
    age = 30
    return "imooc"

gen = gen_func()
# print(dis.dis(gen))
print(gen.gi_frame.f_lasti)
print(gen.gi_frame.f_locals)

from collections import UserList