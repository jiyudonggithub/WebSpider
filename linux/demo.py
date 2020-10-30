#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   demo.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/24 上午9:36   yudong      1.0         None
'''
import requests
from lxml import etree
import net

if __name__ == '__main__':
    server_html = net.socket(net.AF_INET, net.SOCK_STREAM)

    server_html.bind(("127.0.0.1", 8080))

    server_html.listen(128)
    conn, addr = server_html.accept()
    msg = conn.recv(1024 * 12)

    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }
    requests_get = requests.get(url=url, headers=headers)
    etree_html = etree.HTML(requests_get.text)
    xpath = etree_html.xpath('//text()')
    # with open('x.html', 'rb')as f:
    #     data = f.read()
    ss = '''
    <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>计算机</title>
</head>
<body>
     <h1>hello world !</h1>
        <h2>hello world !</h2>
        <h3>hello world !</h3>

</body>
</html>
    '''

    conn.sendall(bytes("HTTP/1.1 201 OK\r\n\r\n", "utf-8"))
    # 发送读取的内容

    conn.sendall(bytes(ss, 'utf-8'))

    conn.close()
