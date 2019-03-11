# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/11 下午3:18
#       @Author  : cxy =.= 
#       @File    : type_object_class.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
a = 1
b = 'abc'



print(type(1))
print(type(int))
print(type(b))
print(type(str))
# ------------------
# <class 'int'>
# <class 'type'>
# <class 'str'>
# <class 'type'>
# ------------------

# type -> int -> 1
# type -> class -> obj

class Student:
    pass

class Teacher(object):
    pass

class MyStudent(Student):
    pass

stu = Student()
print(type(stu))            # <class '__main__.Student'>
print(type(Student))        # <class 'type'>
print(type(MyStudent))      # <class 'type'>
print(type(object))         # <class 'type'>

# object类是最顶层的基类
# type本身也是一个类，同时type也是一个对象

print(int.__bases__)        # (<class 'object'>,)
print(str.__bases__)        # (<class 'object'>,)
print(MyStudent.__bases__)  # (<class '__main__.Student'>,)
print(Student.__bases__)    # (<class 'object'>,)
print(object.__bases__)     # ()
print(type.__bases__)       # (<class 'object'>,)