# -*- coding: utf-8 -*-
# @Time : 2020/9/26 15:50
# @Author : Jiyudong
# @FileName: 爬取4k图片.py
# @Software: PyCharm

import requests
from lxml import etree
import os

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    url = 'http://pic.netbian.com/4kmeinv/'

    requests_get = requests.get(url=url, headers=headers)
    # 如果现中文乱码，可以将响应数据进行utf-8编码
    # requests_get.encoding = 'utf-8'
    page_html = requests_get.text

    html_tree = etree.HTML(page_html)
    src_list = html_tree.xpath('//ul[@class="clearfix"]//img')
    print(src_list)
    imgPath = './src/meinv/'
    if not os.path.exists(imgPath):
        os.mkdir(imgPath)

    for src in src_list:
        src_url = src.xpath('./@src')[0]
        src_Name = src.xpath('./@alt')[0]
        src_Name = src_Name.encode('iso-8859-1').decode('gbk')
        # URL = 'http://pic.netbian.com' + src_url
        # center = requests.get(url=URL, headers=headers).content
        src_url = src_url.split('/')[-1]
        # with open(imgPath + split_, 'wb') as f:
        #     f.write(center)
        print(src_url + '\t', src_Name)
    print('爬取结束')
