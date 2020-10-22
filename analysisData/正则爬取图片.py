# -*- coding: utf-8 -*-
# @Time : 2020/9/26 9:36
# @Author : Jiyudong
# @FileName: 正则爬取图片.py
# @Software: PyCharm

import re
import requests
import os

if __name__ == '__main__':

    if not os.path.exists('./src'):
        os.mkdir('./src')
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    img_src_all = []
    for pageNum in range(5, 13):
        newUrl = format(url % pageNum)
        get__text = requests.get(url=newUrl, headers=headers).text
        ex = '<div class="thumb">.*?<img src="(.*?)" alt.*?</div>'
        img_src_list = re.findall(ex, get__text, re.S)
        img_src_all.append(img_src_list)

    for img_src in img_src_all:
        for src in img_src:
            srl = 'https:' + src
            content = requests.get(url=srl, headers=headers).content
            re_search = re.search(r'(.*)/(.*)\.jpg', src)
            path = './src/' + re_search.group(2) + '.jpg'
            # if os.path.exists(path):
            #     os.remove(path=path)
            with open(path, 'wb') as f:
                print(re_search.group(2) + '.jpg', '正在爬取...........')
                f.write(content)
                print(re_search.group(2) + '.jpg', '已爬取成功')
    print('ok')
