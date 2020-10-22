# -*- coding: utf-8 -*-
# @Time : 2020/9/26 16:40
# @Author : Jiyudong
# @FileName: 解析所有城市.py
# @Software: PyCharm
import requests
from lxml import etree

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://www.aqistudy.cn/historydata/'
    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    city = {}
    title = tree.xpath('//div[@class="hot"]/div[1]/text()')[0].strip()
    city[title] = tree.xpath('//div[@class="hot"]/div[2]//a/text()')
    allcity = tree.xpath('//div[@class="all"]/div[1]/text()')[0].strip()
    ul_list = tree.xpath('//div[@class="all"]/div[2]/ul')
    all_city = {}
    for tr in ul_list:
        tag_title = tr.xpath('./div[1]//text()')[0].strip()
        print(tag_title)
        tag_city = tr.xpath('./div[2]//text()')
        new_cty = []
        for tagc in tag_city:
            tagc = tagc.strip()
            if len(tagc) != 0:
                new_cty.append(tagc)
        all_city[tag_title] = new_cty
        print(new_cty)
    city[allcity] = all_city

pass
