#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   客户端.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/30 21:41   yudong      1.0         None
'''

import socket
import ssl
# 创建socket对象
# 指定协议 AF_INET-ipv4,AF_INET-ipv6
# socket.SOCK_STREAM 面向流的TCP协议
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# sk = ssl.wrap_socket(socket.socket(socket.AF_INET, socket.SOCK_STREAM))
# addr = ("www.bilibili.com", 443)
# sk.connect(addr)
# b'GET / HTTP/1.1\r\nHost: www.sina.com.cn:80\r\nConnection: close\r\n\r\n'
# 建立连接
sk.connect(('www.baidu.com', 80))
# 发送数据
sk.send(b'GET / HTTP/1.1\r\n'
        b'Host: www.baidu.com\r\n'
        b'Connection: close\r\n'
        # b'Upgrade-Insecure-Requests: 1\r\n'
        b'User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36\r\n'
        # b'Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\r\n'
        # b'Accept-Encoding: gzip, deflate, br\r\n'
        # b'Accept-Language: zh-CN,zh;q=0.9\r\n'
        b'\r\n')
# 等待接收数据
data = []
while True:
    tampeData = sk.recv(1024)
    if tampeData:
        data.append(tampeData)
    else:
        break
datStr = (b''.join(data)).decode('utf-8')

sk.close()
print(datStr)
