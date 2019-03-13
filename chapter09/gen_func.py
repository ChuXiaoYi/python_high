# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 下午12:08
#       @Author  : cxy =.= 
#       @File    : gen_func.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
def gen_func():
    yield 1

def func():
    return 1

def fib(index):
    if index <= 2:
        return 1
    else:
        fib(index - 2) + fib(index - 1)

def fib2(index):
    re_list = []
    n, a, b = 0, 0, 1
    while n < index:
        re_list.append(b)
        a, b = b, a+b
        n += 1
    return re_list

def gen_fib(index):
    n, a, b = 0, 0, 1
    while n < index:
        yield b
        a, b = b, a+b
        n += 1


if __name__ == '__main__':
    # gen = gen_func()
    # re = func()
    # print(fib2(10))
    for data in gen_fib(10):
        print(data)