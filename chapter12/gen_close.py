# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/15 下午6:08
#       @Author  : cxy =.= 
#       @File    : gen_close.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
def gen_func():
    try:
        yield 1
    except GeneratorExit:
        pass
    # print(html)
    yield 2
    yield 3
    return 'cxy'

if __name__ == '__main__':
    gen = gen_func()
    next(gen)
    gen.close()
    next(gen)