# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午3:12
#       @Author  : cxy =.= 
#       @File    : getattr.py
#       @Software: PyCharm
#       @Desc    : __getattr__和__getattribute__
# ---------------------------------------------


from datetime import date


class User(object):
    def __init__(self, name, birthday, info={}):
        self.name = name
        self.birthday = birthday
        self.info = info

    def __getattr__(self, item):
        """
        __getattr__是查找不到属性的时候调用
        :param item:
        :return:
        """
        # return "not find attr"
        return self.info[item]

    def __getattribute__(self, item):
        """
        任何时候只要访问属性，就会调用这个
        :param item:
        :return:
        """
        return '__getattribute__'

if __name__ == '__main__':
    user = User('cxy', date(year=1987, month=1, day=1), info={'company_name': 'aaaa'})
    print(user.company_name)