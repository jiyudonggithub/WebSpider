# -*- coding: utf-8 -*-
# @Time : 2020/9/25 17:05
# @Author : Jiyudong
# @FileName: 破解百度翻译.py
# @Software: PyCharm
import requests

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    post_url = 'https://fanyi.baidu.com/sug'
    kw = input('请输入单词: ')
    param = {
        'kw': kw
    }
    post = requests.post(url=post_url, data=param, headers=headers)
    json = post.json()
    print(json)
