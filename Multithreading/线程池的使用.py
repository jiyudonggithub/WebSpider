#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   线程池的使用.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/29 19:59   yudong      1.0         None
'''
from multiprocessing.dummy import Pool
import time


def get_page(str):
    print('正在下载', str)
    time.sleep(10)
    print('下载完成')
    return str + '5'


strat_time = time.time()
name_list = ['aa', 'bb', 'cc', 'dd', 'ee', 'ff']
# 实例化线程池对象
pool = Pool(4)
pool_map = pool.map(get_page, name_list)
end_time = time.time()
print(end_time - strat_time)
print(pool_map)
