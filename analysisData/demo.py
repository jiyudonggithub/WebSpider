# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:02
# @Author : Jiyudong
# @FileName: demo.py
# @Software: PyCharm

import re
import requests
from lxml import etree
import functools

def getdata(url):
    print('正在爬取 ', url, ' 的数据')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    page = requests.get(url=url, headers=headers)
    page_text = page.text
    tree = etree.HTML(page_text)
    tree_p = tree.xpath('//p')
    data = []
    print('爬取 ', url, ' 结束')
    for p in tree_p:
        cont = p.xpath('./text()')
        if len(cont) != 0:
            cont = p.xpath('./text()')[0].strip()
            if page.encoding == 'iso-8859-1':
                cont = cont.encode('iso-8859-1').decode('gbk')
            cont = re.sub(r'[^\u4e00-\u9fa50-9a-zA-Z]', '', cont)
            if len(cont) > 20:
                data.append(cont)
    data = [x for x in data if len(x) != 0]
    return data, page_text


if __name__ == '__main__':
    url = 'http://sn.people.com.cn/n2/2020/1029/c378288-34381381.html'
    url1 = 'https://blog.csdn.net/a419240016/article/details/109324389?spm=1000.2115.3001.4373'
    data, page_text = getdata(url=url)
    data_all = [data]
    res = re.findall(r'href="(.*?)".+', page_text)
    res = [x for x in res if not x.endswith('.png')]
    res = [x for x in res if not x.endswith('.css')]
    res = [x for x in res if not x.endswith('.ico')]
    res = [x for x in res if 'download' not in x]
    res = [x for x in res if 'https://' in x]
    print("len res ", len(res))
    if len(res) != 0:
        print("正在处理数据.......")
        for i in res:
            su, su_text = getdata(i)
            data_all.append(su)
        data_all = list(functools.reduce(lambda x, y: x + y, data_all))
    print(data_all)
