# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 上午11:31
#       @Author  : cxy =.= 
#       @File    : instance_type.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class A:
    pass

class B(A):
    pass

b = B()

print(isinstance(b, B)) # True
print(isinstance(b, A)) # True

print(type(b) is B) # True
print(type(b) is A) # False