#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   hello_socket.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/24 上午10:48   yudong      1.0         None
'''
from socket import *

if __name__ == '__main__':
    # 创建tcp的套接字

    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.sendto(b'jiosj', ('192.168.1.111', 8080))

    # 关闭套接字
    tcp_socket.close()
