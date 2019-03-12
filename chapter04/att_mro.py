# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 上午11:55
#       @Author  : cxy =.= 
#       @File    : att_mro.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
# class A:
#     name = "类属性"
#     def __init__(self):
#         self.name = "实例属性"
#
# a = A()
# print(a.name)

# class D:
#     pass
#
# class C(D):
#     pass
#
# class B(D):
#     pass
#
# class A(B, C):
#     pass
#
# print(A.__mro__)    # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.D'>, <class 'object'>)
class E:
    pass

class D:
    pass

class C(E):
    pass

class B(D):
    pass

class A(B, C):
    pass

print(A.__mro__)    # (<class '__main__.A'>, <class '__main__.B'>, <class '__main__.D'>, <class '__main__.C'>, <class '__main__.E'>, <class 'object'>)


