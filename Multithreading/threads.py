# -*- coding: utf-8 -*-
# @Time : 2020/9/27 22:11
# @Author : Jiyudong
# @FileName: threads.py
# @Software: PyCharm

# 进程池
import time
from multiprocessing.dummy import Pool

name_list = ['aa', 'bb', 'cc', 'dd']

start_time = time.time()


def get_page(str):
    print('正在下载：', str)
    time.sleep(2)
    print('下载完成：', str)


pool = Pool(4)
pool.map(get_page, name_list)

end_time = time.time()

print('%d second' % (end_time - start_time))
