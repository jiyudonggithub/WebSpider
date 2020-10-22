# -*- coding: utf-8 -*-
# @Time : 2020/9/24 20:59
# @Author : Jiyudong
# @FileName: p1.py
# @Software: PyCharm
import threading

count = 0
thread_task = 1000000
thread_num = 100
lock = threading.Lock()


def finishTask():
    global count;
    # print(threading.current_thread())
    for i in range(thread_task):
        lock.acquire()
        count += 1
        print(count)
        lock.release()


if __name__ == '__main__':
    threads = []

    for i in range(thread_num):
        thread = threading.Thread(target=finishTask)
        threads.append(thread)
        thread.start()

    for t in threads:
        t.join()
    print(f'应有任务数量{thread_task * thread_num}')
    print(f'实际任务数量{count}')
