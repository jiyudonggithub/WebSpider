# -*- coding: utf-8 -*-
# @Time : 2020/9/28 10:54
# @Author : Jiyudong
# @FileName: 协程4.py
# @Software: PyCharm
import asyncio
import aiohttp


async def fecth(seesion, url):
    print('开始爬取', url)
    async with seesion.get(url) as resonse:
        text = await resonse.text()
        print(text)


async def man():
    async with aiohttp.ClientSession() as session:
        url_list = [
            'https://www.baidu.com'
            'https://www.pythonav.com'
            'https://www.bilibili.com/video/BV1Yh411o7Sz?p=99'
        ]

        task = [asyncio.create_task(fecth(session, url)) for url in url_list]
        dong, pending = await asyncio.wait(task)


if __name__ == '__main__':
    asyncio.run(man())
