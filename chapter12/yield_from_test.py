# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/17 12:12 PM
#       @Author  : cxy =.= 
#       @File    : yield_from_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
from itertools import chain

my_list = [1, 2, 3]
my_dict = {'a': 'http://projectsedu.com', 'b': 'http://www.imooc.com'}


# def g1(iterable):
#     yield iterable
#
#
# def g2(iterable):
#     yield from iterable
#
#
# for value in g1(range(10)):
#     print(value)
#
# for value in g2(range(10)):
#     print(value)

# def my_chain(*args, **kwargs):
#     for my_iterable in args:
#         # for value in my_iterable:
#         #     yield value
#         yield from my_iterable
#
# for value in my_chain(my_list, my_dict, range(5,10)):
#     print(value)


