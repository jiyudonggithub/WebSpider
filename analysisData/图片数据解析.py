# -*- coding: utf-8 -*-
# @Time : 2020/9/26 9:26
# @Author : Jiyudong
# @FileName: 图片数据解析.py
# @Software: PyCharm
import re
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://pic.qiushibaike.com/system/pictures/12353/123532781/medium/96N1WS3R16BKQ3UW.jpg'
    # content获得图片的二进制数据
    img_data = requests.get(url=url, headers=headers).content
    with open('./qiutu.jpg', 'wb') as f:
        f.write(img_data)

    pass
