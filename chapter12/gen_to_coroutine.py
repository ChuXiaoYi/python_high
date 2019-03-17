# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/17 5:54 PM
#       @Author  : cxy =.= 
#       @File    : gen_to_coroutine.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import inspect


def gen_func():
    value = yield 1
    return 'cxy'


def downloader(url):
    pass


def download_html(html):
    html = yield from downloader(html)


if __name__ == '__main__':
    gen = gen_func()
    print(inspect.getgeneratorstate(gen))
    print(next(gen))
    print(inspect.getgeneratorstate(gen))
