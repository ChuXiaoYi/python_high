# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/12 上午10:38
#       @Author  : cxy =.= 
#       @File    : abc_test.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------

# 检查某个类是否有某种方法
class Company(object):
    def __init__(self, employee_list):
        self.employee = employee_list

    def __len__(self):
        return len(self.employee)

com = Company(['a', 'b'])
print(hasattr(com, '__len__'))




# 在某些情况之下希望判定某个对象的类型
from collections import Sized
print(isinstance(com, Sized))




# 模拟一个抽象基类
import abc
class CacheBase(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def get(self, key):
        pass

    @abc.abstractmethod
    def set(self, key ,value):
        pass

class RedisCache(CacheBase):
    def set(self, key ,value):
        print(f'{key}: {value}')

    def get(self, key):
        print(f'{key}')

redis_cache = RedisCache()
redis_cache.set('k', 'v')