#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   server.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/31 10:10   yudong      1.0         None
'''
import socket

sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定ip端口
sk.bind(('localhost', 8080))
# 监听
sk.listen(5)
# 等待连接
print('服务器启动成功......')
clientSocket, clientAdress = sk.accept()
print('{} -- {} 连接成功'.format(str(clientSocket), str(clientAdress)))

while True:
    data = clientSocket.recv(1024)
    print('收到数据')
    data = data.decode('utf-8')
    print(data)
    clientSocket.send('你好'.encode('utf-8'))
