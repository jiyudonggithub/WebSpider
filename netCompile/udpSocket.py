#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   udpSocket.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 10:40   yudong      1.0         None
'''

import socket

if __name__ == '__main__':
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    udp_socket.bind(('', 7788))
    recv_data = udp_socket.recvfrom(1024)
    print(recv_data[0].decode('utf-8'))
    data = input('请输入要发送的数据: ')
    udp_socket.sendto(data.encode('utf-8'), ('192.168.1.113', 8080))

    udp_socket.close()
