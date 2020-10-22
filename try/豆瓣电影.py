# -*- coding: utf-8 -*-
# @Time : 2020/9/25 17:19
# @Author : Jiyudong
# @FileName: 豆瓣电影.py
# @Software: PyCharm
import requests
import json

if __name__ == '__main__':
    url = 'https://movie.douban.com/j/chart/top_list'

    param = {
        'type': '24',
        'interval_id': '100:90',
        'action': '',
        'start': '10',
        'limit': '20',
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    req_get = requests.get(url=url, params=param, headers=headers)
    json1 = req_get.json()
    fb = open('./move.json', 'w', encoding='utf-8')
    json.dump(json1, fb, ensure_ascii=False)
    print('ok')
