# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/15 下午4:14
#       @Author  : cxy =.= 
#       @File    : coroutine_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
# def get_url(url):
#     # do something 1
#     html = get_html(html)   # 此处应该暂停，切换到另一个函数执行
#     # parse html
#     urls = parse_url(html)
#
# def get_url2():
#     pass

def gen_func():
    html = yield 1
    print(html)
    yield 2
    yield 3
    return 'cxy'

if __name__ == '__main__':
    gen = gen_func()
    url = next(gen)
    html = 'send'
    print(gen.send(html))
    print(next(gen))
    # print(next(gen))
    # print(next(gen))