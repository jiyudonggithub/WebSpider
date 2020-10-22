# -*- coding: utf-8 -*-
# @Time : 2020/9/25 19:52
# @Author : Jiyudong
# @FileName: 肯德基.py
# @Software: PyCharm

import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }

    # 'http://www.kfc.com.cn/kfccda/storelist/index.aspx'
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    # 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    # city = input('请输入城市：')
    # paper = input('请输入想查看的页数：')

    param = {
        'cname': '',
        'pid': '',
        'keyword': '合肥',
        'pageIndex': '1',
        'pageSize': '10'
    }
    data = {
        'keyword': '合肥'
    }
    repost = requests.post(url=url, data=param, headers=headers)
    print(json.load(repost.text))
    print(repost)
    print('ok')
