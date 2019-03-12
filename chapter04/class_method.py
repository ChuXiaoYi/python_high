# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午12:10
#       @Author  : cxy =.= 
#       @File    : class_method.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
class Date(object):


    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __str__(self):
        return f"{self.year}/{self.month}/{self.day}"

    def tomorrow(self):
        self.day += 1

if __name__ == '__main__':
    new_day = Date(2019, 3, 12)
    new_day.tomorrow()
    print(new_day)