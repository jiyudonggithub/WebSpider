#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo01.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/30 20:57   yudong      1.0         None
'''

import re

# match 从头匹配
print(re.match(r'^w{3}', 'www.baidu.com'))
print(re.match(r'bai', 'www.baidu.com'))
# 匹配第一个，则返回
print(re.search(r'w', 'www.baidu.com'))

print(re.findall(r'w', 'wwW.baidu.com', flags=re.I))

print(re.findall(r'\D', 'wwW.bai846 5du.co5416m'))

print(re.findall(r'\W', 'wwW.bai846 5du.c""o5416m'))

print(re.findall(r'a.*?d', 'sAasmdjnijkimdjknjhvjvjdnl'))
