# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/11 下午3:10
#       @Author  : cxy =.= 
#       @File    : all_is_project.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
def ask(name='cxy'):
    print(name)

class Person(object):
    def __init__(self):
        print('cxy')


def decorator_func():
    print('decorator start')
    return ask

my_ask = decorator_func()
my_ask('tom')


# obj_list = []
# obj_list.append(ask)
# obj_list.append(Person)


# my_func = ask
# my_func('aaa')

# my_class = Person
# my_class()

# for item in obj_list:
#     print(item())
