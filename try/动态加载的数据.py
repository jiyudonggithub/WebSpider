# -*- coding: utf-8 -*-
# @Time : 2020/9/25 21:54
# @Author : Jiyudong
# @FileName: 动态加载的数据.py
# @Software: PyCharm

import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    data = {
        'on': 'true',
        'page': '1',
        'pageSize': '15',
        'productName': '',
        'conditionType': '1',
        'applyname': '',
    }
    post = requests.post(url=url, data=data, headers=headers)
    post_json = post.json()
    id_lsit = []
    for head in post_json['list']:
        print(head["ID"])
        id_lsit.append(head["ID"])
    URL = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    for id in id_lsit:
        datas = {
            'id': id
        }
        requests_post = requests.post(url=URL, data=datas, headers=headers).json()
        print(requests_post)
