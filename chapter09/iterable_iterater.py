# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/13 上午11:36
#       @Author  : cxy =.= 
#       @File    : iterable_iterater.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]

if __name__ == '__main__':
    company = Company(['a', 'b', 'c'])
