# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/11 下午4:59
#       @Author  : cxy =.= 
#       @File    : company.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __getitem__(self, item):
        return self.employee[item]




company = Company(['tom', 'bob', 'jane'])

company1 = company[:2]

# employee = company.employee
# for em in employee:
#     print(em)
for em in company1:
    print(em )