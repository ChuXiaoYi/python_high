# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午2:33
#       @Author  : cxy =.= 
#       @File    : super_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class A(object):
    def __init__(self):
        print("A")

class B(A):
    def __init__(self):
        print("B")
        super().__init__()

class C(A):
    def __init__(self):
        print('C')
        super(C, self).__init__()

class D(B, C):
    def __init__(self):
        print('D')
        super(D, self).__init__()

if __name__ == '__main__':
    d = D()
