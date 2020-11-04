#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   processPool.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 15:05   yudong      1.0         None
'''
import random
from multiprocessing import Pool
import time


def func1(*a):
    # print("func进程：", os.getpid())
    # print("func进程的父进程：", os.getppid())
    print('子进程{}开始'.format(a[0]))
    time.sleep(random.choice([5, 4, 3]))
    print('子进程{}结束'.format(a[0]))


if __name__ == '__main__':
    # 创建进程池 默认大小是cpu核心数
    print('父进程开始')
    pp = Pool(4)
    for x in range(10):
        pp.apply_async(func=func1, args=(x,))
    pp.close()
    pp.join()
    print('父进程结束')
