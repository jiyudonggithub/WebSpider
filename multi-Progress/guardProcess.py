#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   guardProcess.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 14:54   yudong      1.0         None
'''

from multiprocessing import Process
import time, os, random


def func1(*s):
    # print("func进程：", os.getpid())
    # print("func进程的父进程：", os.getppid())
    print('子进程开始')
    time.sleep(5)
    print('子进程结束')


if __name__ == '__main__':
    p = Process(target=func1, args=('ffffffff', 456))
    p.daemon = True
    p.start()
    print('父进程开始')
    time.sleep(4)
    print('父进程结束')
