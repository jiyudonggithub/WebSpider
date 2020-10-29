#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   acioDemo.py    

@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/29 21:09   yudong      1.0         None
'''

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
            print(text)
            if text == 200:
                return url
    except:
        print('该网址不可访问')
        return None


async def creatPingTesk(url_list):
    async with aiohttp.ClientSession() as session:
        tesk = [asyncio.create_task(grab_url(session, url)) for url in url_list]
        dong, pending = await asyncio.wait(tesk)
    return dong


if __name__ == '__main__':

    url = 'https://www.runoob.com/python3/python3-set.html'

    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    res = re.findall(r'href="(.*?)".+', page_text)
    res = [x for x in res if not x.endswith('.png')]
    res = [x for x in res if not x.endswith('.css')]
    res = [x for x in res if not x.endswith('.ico')]
    res = [x for x in res if 'https://' in x]
    print("len res ",len(res))
    dong = asyncio.run(creatPingTesk(res))
    data = []
    for i in dong:
        print(i.result())
        data.append(i.result())
    data = [x for x in data if x != None]
    data = list(set(data))
    print(data)
    print(len(data))
