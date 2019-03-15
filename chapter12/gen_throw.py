# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/15 下午6:15
#       @Author  : cxy =.= 
#       @File    : gen_throw.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
def gen_func():
    try:
        yield 1
    except Exception as e:
        pass

    # print(html)
    yield 2
    yield 3
    return 'cxy'

if __name__ == '__main__':
    gen = gen_func()
    print(next(gen))
    gen.throw(Exception, 'download error')
    print(next(gen))
