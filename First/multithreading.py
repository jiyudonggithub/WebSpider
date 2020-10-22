# -*- coding: utf-8 -*-
# @Time : 2020/9/24 19:53
# @Author : Jiyudong
# @FileName: multithreading.py
# @Software: PyCharm
import time
import threading

tasks = ['move1', 'move2', 'move3', 'move4', 'move5', 'move6', 'move7', 'move8', 'move9', 'move10']


def download(move):
    print(f'start downloading {move}')
    time.sleep(2)
    print(f'finish download {move}\n')

if __name__ == '__main__':
    for task in tasks:
        thread = threading.Thread(target=download, args=(task,))
        thread.start()
