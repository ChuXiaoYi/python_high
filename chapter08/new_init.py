# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午3:56
#       @Author  : cxy =.= 
#       @File    : new_init.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class User(object):
    def __new__(cls, *args, **kwargs):
        print('in new')
        return super(User, cls).__new__(cls)

    def __init__(self, name):
        print('in init')
        self.name = name

if __name__ == '__main__':
    user = User(name='aaa')
