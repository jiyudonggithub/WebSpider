#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   every.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/29 17:27   yudong      1.0         None
'''
import functools

import requests
from lxml import etree
import re
import asyncio
import aiohttp

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


async def grab_url(seesion, url):
    print('正在测试 ', url)
    try:
        async with seesion.get(url, headers=headers, verify_ssl=False) as resonse:
            text = resonse.status
            if text == 200:
                return url
    except BaseException:
        print('该网址不可访问')


async def creatPingTesk(url_list):
    async with aiohttp.ClientSession() as session:
        tesk = [asyncio.create_task(grab_url(session, url)) for url in url_list]
        dong, pending = await asyncio.wait(tesk)
    return dong


async def grab(seesion, url):
    print('正在爬取 ', url, ' 的数据')
    try:
        async with seesion.get(url, headers=headers, verify_ssl=False) as resonse:
            text = await resonse.text()
            tree = etree.HTML(page_text)
            tree_p = tree.xpath('//p')
            data = []
            if len(tree_p) != 0:
                for p in tree_p:
                    cont = p.xpath('./text()')
                    if len(cont) != 0:
                        cont = cont[0].strip()
                        cont = re.sub(r'[^\u4e00-\u9fa50-9]', '', cont)
                        cont = cont.encode('iso-8859-1').decode('gbk')
                        data.append(cont)
                data = [x for x in data if len(x) != 0]
            print('爬取 ', url, ' 结束')
            return data
    except BaseException:
        print('该网址不可下载')


async def creatTesk(url_list):
    async with aiohttp.ClientSession() as session:
        tesk = [asyncio.create_task(grab(session, url)) for url in url_list]
        dong, pending = await asyncio.wait(tesk)
    return dong


def getdata(url):
    print('正在爬取 ', url, ' 的数据')
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    tree_p = tree.xpath('//p')
    data = []
    print('爬取 ', url, ' 结束')
    for p in tree_p:
        cont = p.xpath('./text()')
        if len(cont) != 0:
            cont = p.xpath('./text()')[0].strip()
            cont = re.sub(r'[^\u4e00-\u9fa50-9]', '', cont)
            data.append(cont)
    data = [x for x in data if len(x) != 0]
    return data, page_text


if __name__ == '__main__':
    url = 'https://www.csdn.net/gather_2e/MtjaMg2sMDc5LWJsb2cO0O0O.html'
    data, page_text = getdata(url=url)
    data_all = [data]
    res = re.findall(r'href="(.*?)".+', page_text)
    res = [x for x in res if not x.endswith('.png')]
    res = [x for x in res if not x.endswith('.css')]
    res = [x for x in res if not x.endswith('.ico')]
    res = [x for x in res if 'https://' in x]
    print("len res ", len(res))
    if len(res) != 0:
        dong = asyncio.run(creatPingTesk(res))
        url_list = []
        for i in dong:
            print(i.result())
            url_list.append(i.result())
        url_list = [x for x in url_list if x is not None]
        dong = asyncio.run(creatTesk(url_list))
        print("正在处理数据.......")
        for i in dong:
            data_all.append(i.result())
        data_all = [x for x in data_all if x is not None]
        data_all = list(functools.reduce(lambda x, y: x + y, data_all))
        print(data_all)
    else:
        print('没有网址可爬取')
