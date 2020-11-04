#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   processDemo.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 14:38   yudong      1.0         None
'''
import os
from multiprocessing import Process
import time


def func1(*s):
    while True:
        print("func进程：", os.getpid())
        print("func进程的父进程：", os.getppid())
        print(s)
        time.sleep(2)


if __name__ == '__main__':
    p = Process(target=func1, args=('ffffffff', 456))
    p.start()
    while True:
        print("主进程：", os.getpid())
        print("主进程的父进程：", os.getppid())
        print('bbbb')
        time.sleep(2)
