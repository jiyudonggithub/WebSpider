# -*- coding: utf-8 -*-
# @Time : 2020/9/26 11:34
# @Author : Jiyudong
# @FileName: xpath数据解析.py
# @Software: PyCharm
import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    url = 'https://xa.58.com/ershoufang/'

    page_text = requests.get(url=url, headers=headers).text

    tree = etree.HTML(page_text)
    tree_xpath = tree.xpath('//ul[@class="house-list-wrap"]/li')
    for tx in tree_xpath:
        # 局部解析要加上’.‘
        text_ = tx.xpath('.//h2/a/text()')[0]
        print(text_)
