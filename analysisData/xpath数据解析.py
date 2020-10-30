# -*- coding: utf-8 -*-
# @Time : 2020/9/26 11:34
# @Author : Jiyudong
# @FileName: xpath数据解析.py
# @Software: PyCharm
import functools

import requests
from lxml import etree
import re


def getdata(page_text):
    tree = etree.HTML(page_text)
    tree_xpath = tree.xpath('//div[@class="fl text_con_left"]//p')
    data = []
    for tx in tree_xpath:
        text_ = tx.xpath('./text()')[0].encode('iso-8859-1').decode('gbk').strip()
        line = re.sub(r'[^\u4e00-\u9fa50-9]', ' ', text_).strip()
        line = line.split(' ')
        line = [x for x in line if len(x) != 0]
        if len(line) != 0:
            data.append(line)

    data = list(functools.reduce(lambda x, y: x + y, data))
    return data


if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'
    }

    url = 'http://opinion.people.com.cn/n1/2020/1027/c1003-31906837.html'
    URL = 'http://opinion.people.com.cn'
    page_text = requests.get(url=url, headers=headers).text
    data = getdata(page_text)
    tree = etree.HTML(page_text)
    tree_xpath = tree.xpath('//div[@id="rwb_rdtj"]//li')
    sum_data = [data]
    for x in tree_xpath:
        url = URL + x.xpath('./a/@href')[0]
        page_text = requests.get(url=url, headers=headers).text
        sum_data.append(getdata(page_text))
    print(sum_data)
    print(len(sum_data))
