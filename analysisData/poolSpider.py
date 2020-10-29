#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   poolSpider.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/29 21:34   yudong      1.0         None
'''
import functools

import requests
from lxml import etree
import re
from multiprocessing.dummy import Pool


def getdata(url, num=0):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    print('正在爬取 ', url, ' 的数据')
    try:
        page_text = requests.get(url=url, headers=headers).text
        tree = etree.HTML(page_text)
        tree_p = tree.xpath('//p')
        data = []
        print('爬取 ', url, ' 结束')

        for p in tree_p:
            cont = p.xpath('./text()')
            if len(cont) != 0:
                cont = cont[0].strip()
                cont = re.sub(r'[^\u4e00-\u9fa50-9]', '', cont)
                # cont = cont.encode('iso-8859-1').decode('gbk')
                data.append(cont)
        data = [x for x in data if len(x) != 0]
        if num == 1:
            return data, page_text
        else:
            return data
    except BaseException:
        print('不可下载')


def ping_net(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    try:
        res = requests.get(url=url, headers=headers)
        code = res.status_code
        print(code)
        if code == 200:
            return url
    except BaseException:
        print('捕获到异常')


if __name__ == '__main__':
    pool = Pool(12)
    url = 'https://movie.douban.com/'
    data, page_text = getdata(url=url, num=1)
    data_all = [data]
    res = re.findall(r'href="(.*?)".+', page_text)
    res = [x for x in res if not x.endswith('.png')]
    res = [x for x in res if not x.endswith('.css')]
    res = [x for x in res if not x.endswith('.ico')]
    res = [x for x in res if 'https://' in x]
    url_list = []

    pool_net = pool.map(ping_net, url_list)
    pool_data = pool.map(getdata, url_list)
