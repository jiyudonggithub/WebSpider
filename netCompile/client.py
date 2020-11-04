#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   client.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 10:20   yudong      1.0         None
'''
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sk.connect(('localhost', 8080))

while True:
    data = input('请输入给服务器的数据')
    sk.send(data.encode('utf-8'))
    info = sk.recv(1024)
    print('服务器说:', info.decode('utf-8'))
