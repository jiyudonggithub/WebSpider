# -*- coding: utf-8 -*-
# @Time : 2020/9/10 19:40
# @Author : Jiyudong
# @FileName: Demo01.py
# @Software: PyCharm
import multiprocessing
import time
import os


def funcA(num):
    print('funca', os.getpid())
    for i in range(num):
        print('任务A')
        time.sleep(2)
    return None


def funcB(num, name):
    print('funca', os.getpid())
    for i in range(num):
        print('任务B', name)
        time.sleep(1)
    return None


if __name__ == '__main__':
    funcB_process = multiprocessing.Process(target=funcB, args=(5, 'xiaoming'))
    funcA_process = multiprocessing.Process(target=funcA, kwargs={"num": 3})
    funcA_process.daemon = True
    funcB_process.start()
    funcA_process.start()
    time.sleep(4)
    print('主进程执行结束')
