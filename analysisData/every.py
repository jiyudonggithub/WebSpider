#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   every.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/29 17:27   yudong      1.0         None
'''
import functools
from gzip import GzipFile

import requests
from lxml import etree
import re
import asyncio
import aiohttp
import chardet

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
}


# , headers=headers

async def grab_url(seesion, url):
    print('正在爬取 ', url, ' 的数据')
    try:
        async with seesion.get(url, headers=headers, timeout=60) as responses:
            code = responses.status
            # print("状态码：", code)
            red = await responses.read()
            if chardet.detect(red)['encoding'].lower() == 'gb2312':
                page_text = await responses.text(encoding='gbk')
            else:
                page_text = await responses.text(encoding='utf-8')
            if code == 200:
                tree = etree.HTML(page_text)
                tree_p = tree.xpath('//p')
                data = []
                if len(tree_p) != 0:
                    for p in tree_p:
                        cont = p.xpath('./text()')
                        if len(cont) != 0:
                            cont = cont[0].strip()
                            cont = re.sub(r'[^\u4e00-\u9fa50-9]', '', cont)
                            data.append(cont)
                    data = [x for x in data if len(x) != 0]
                print('爬取 ', url, ' 结束')
                return data

    except BaseException as e:
        print('该网址不可访问', e)
        return None


async def creatTesk(url_list):
    cookies = {'my_cookie': "my_value"}
    conn = aiohttp.TCPConnector(limit=8)  # 默认100，0表示无限
    async with aiohttp.ClientSession(cookies=cookies, connector=conn) as session:
        tesk = [asyncio.create_task(grab_url(session, url)) for url in url_list]
        dong, pending = await asyncio.wait(tesk)
    return dong


def getdata(url):
    print('正在爬取 ', url, ' 的数据')
    page = requests.get(url=url, headers=headers)
    page_text = page.text
    if page.encoding.lower() == 'iso-8859-1':
        page_text = page_text.encode('iso-8859-1').decode('gbk')
    tree = etree.HTML(page_text)
    tree_p = tree.xpath('//p')
    data = []
    print('爬取 ', url, ' 结束')
    for p in tree_p:
        cont = p.xpath('./text()')
        if len(cont) != 0:
            cont = p.xpath('./text()')[0].strip()
            cont = re.sub(r'[^\u4e00-\u9fa50-9a-zA-Z]', '', cont)
            data.append(cont)
    data = [x for x in data if len(x) != 0]
    return data, page_text


if __name__ == '__main__':
    url = input('请输入网址：')
    data, page_text = getdata(url=url)
    data_all = [data]
    res = re.findall(r'href="(.*?)".+', page_text)
    res = [x for x in res if not x.endswith('.png')]
    res = [x for x in res if not x.endswith('.css')]
    res = [x for x in res if not x.endswith('.ico')]
    res = [x for x in res if 'download' not in x]
    res = [x for x in res if 'https://' in x]
    # res = [url]
    print("len res ", len(res))
    if len(res) != 0:
        dong = asyncio.run(creatTesk(res))
        print("正在处理数据.......")
        for i in dong:
            if i.result() is not None:
                data_all.append(i.result())
        data_all = list(functools.reduce(lambda x, y: x + y, data_all))
    else:
        data_all = data_all[0]
    print(data_all)
