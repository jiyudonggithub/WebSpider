#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   进程通信.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 15:57   yudong      1.0         None
'''
import os, time
from multiprocessing import Process, Queue


def write(q):
    print('开启写进程: ', os.getpid())
    for i in ['A', 'B', 'C', 'D', 'E', 'F', 'G']:
        q.put(i)
        print("写到的数据", i)
    print('结束写进程: ', os.getpid())


def read(q):
    print('开启读进程: ', os.getpid())
    while True:
        data = q.get()
        print("读到的数据", data)
    print('结束读进程: ', os.getpid())


if __name__ == '__main__':
    print('启动父进程')
    q = Queue()
    write_process = Process(target=write, args=(q,))
    read_process = Process(target=read, args=(q,))

    write_process.start()
    read_process.start()
    write_process.join()
    #   强制结束
    read_process.terminate()
    print('结束父进程')
