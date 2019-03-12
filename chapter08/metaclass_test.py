# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 下午4:05
#       @Author  : cxy =.= 
#       @File    : metaclass_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------

# 1
def create_class(name):
    if name == 'user':
        class User:
            def __str__(self):
                return 'user'
        return User
    elif name == 'company':
        class Company:
            def __str__(self):
                return 'company'
        return Company

# 2
def say(self):
    return 'i an user'
    # return self.name

class BaseClass(object):
    def answer(self):
        return 'i am baseclass'
# type动态创建类
User = type('User', (BaseClass, ), {"name": "a", "say": say})


# 3
class MetaClass(type):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls, *args, **kwargs)

class User2(metaclass=MetaClass):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return 'user2'



if __name__ == '__main__':
    # MyClass = create_class('user')
    # my_obj = MyClass()
    # print(my_obj)
    # my_obj = User()
    my_obj = User2('aaaaa')
    print(my_obj)
    # print(my_obj.name)
    # print(my_obj.say())
    # print(my_obj.answer())