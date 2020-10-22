# -*- coding: utf-8 -*-
# @Time : 2020/9/25 16:09
# @Author : Jiyudong
# @FileName: deamo0.py
# @Software: PyCharm
import requests
import json

if __name__ == '__main__':
    # 需求 1 爬取指定词条的搜索结果

    URL = "http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx'
    param = {
        'cname': '',
        'keyword': '合肥',
        'pageIndex': '1',
        'pageSize': '10',
        'pid': ''
    }
    params = {
        'cname': '合肥',
        'pageSize': 10
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    html = requests.post(url=url, data=params, headers=headers)
    info = json.loads(html.text)
    print(info)
