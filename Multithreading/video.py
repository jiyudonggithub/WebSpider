# -*- coding: utf-8 -*-
# @Time : 2020/9/27 22:21
# @Author : Jiyudong
# @FileName: video.py
# @Software: PyCharm
import requests
from multiprocessing.dummy import Pool
from lxml import etree
import execjs
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://www.pearvideo.com/category_5'

    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    li_list = tree.xpath('//*[@id="listvideoListUl"]/li')
    for li in li_list:
        src = li.xpath('.//a/@href')[0]
        name = li.xpath('.//div[@class="vervideo-title"]/text()')[0].strip()
        vedio = src.split('_')[1]
        vido_url = 'https://www.pearvideo.com/videoStatus.jsp'

        params = {
            'contId': vedio,
            'mrd': js,
        }
        print(params['mrd'])
        vido = requests.get(url=vido_url, params=params,
                            headers=headers).json()
        vedio_url = vido
        print(vido)
        print(name)
