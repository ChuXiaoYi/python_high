# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午2:57
#       @Author  : cxy =.= 
#       @File    : property_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
from datetime import date, datetime

class User(object):
    def __init__(self, name, birthday):
        self.name = name
        self.birthday = birthday
        self._age = 0

    @property
    def age(self):
        return datetime.now().year - self.birthday.year

    @age.setter
    def age(self, value):
        self._age = value

if __name__ == '__main__':
    user = User('cxy', date(year=1987, month=1, day=1))
    # print(f'in {__file__} file')
    print(user.age)
    user.age = 30
    print(user._age)