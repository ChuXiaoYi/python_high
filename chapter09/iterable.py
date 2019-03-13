# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 上午11:27
#       @Author  : cxy =.= 
#       @File    : iterable.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
from collections.abc import Iterable, Iterator
a = [1, 2, 3]
iter_rater = iter(a)
print(isinstance(a, Iterable))
print(isinstance(iter_rater, Iterator))