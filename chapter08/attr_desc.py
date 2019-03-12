 # -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午3:20
#       @Author  : cxy =.= 
#       @File    : attr_desc.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import numbers

class IntField(object):
    """
    数据描述符
    """
    def __get__(self, instance, owner):
        return self.value

    def __set__(self, instance, value):
        if isinstance(value, numbers.Integral):
            raise ValueError('int value need')
        self.value = value

    def __delete__(self, instance):
        pass

class User(object):
    age = IntField()

if __name__ == '__main__':
    user = User()
    # user.age = 10
    print(user.age)