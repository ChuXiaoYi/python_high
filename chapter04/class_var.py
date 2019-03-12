# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 上午11:36
#       @Author  : cxy =.= 
#       @File    : class_var.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class A:
    aa = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

a = A(2, 3)
A.aa = 11
a.aa = 100  # 这一步是对当前这个实例新建一个变量aa，赋值为100
print(a.x, a.y, a.aa)
print(A.aa)


