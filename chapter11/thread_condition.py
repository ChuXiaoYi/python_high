# -*- coding: utf-8 -*-
# ---------------------------------------------
#       @Time    : 2019/3/14 下午3:05
#       @Author  : cxy =.= 
#       @File    : thread_condition.py
#       @Software: PyCharm
#       @Desc    : 
# ---------------------------------------------
import threading
from threading import Condition

class XiaoAi(threading.Thread):
    def __init__(self, cond):
        super(XiaoAi, self).__init__(name="小爱")
        self.cond = cond

    def run(self):
        with self.cond:
            self.cond.wait()
            print(f'{self.name}: 在')
            self.cond.notify()

            self.cond.wait()
            print(f'{self.name}: 好啊！')
            self.cond.notify()

class TianMao(threading.Thread):
    def __init__(self, cond):
        super(TianMao, self).__init__(name="天猫")
        self.cond = cond

    def run(self):
        with self.cond:
            print(f'{self.name}: 小爱同学')
            self.cond.notify()
            self.cond.wait()

            print(f'{self.name}: 我们来对古诗吧！')
            self.cond.notify()
            self.cond.wait()


if __name__ == '__main__':
    lock = threading.Condition()
    xiaoai = XiaoAi(lock)
    tianmao = TianMao(lock)

    # 注意这里的顺序
    xiaoai.start()
    tianmao.start()
