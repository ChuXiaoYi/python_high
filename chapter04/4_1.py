# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 上午9:44
#       @Author  : cxy =.= 
#       @File    : 4_1.py
#       @Software: PyCharm
#       @Desc    : 鸭子类型
# ---------------------------------------------
class Cat(object):
    def say(self):
        print('i am a cat')

class Dog(object):
    def say(self):
        print('i am a dog')

class Duck(object):
    def say(self):
        print('i am a duck')

animal = Cat()
animal.say()

class Animal(object):
    def say(self):
        print('i am a animal')

class Cat(Animal):
    def say(self):
        print('i am a cat')