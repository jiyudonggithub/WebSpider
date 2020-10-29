# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:02
# @Author : Jiyudong
# @FileName: demo.py
# @Software: PyCharm

import re
import requests
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://accounts.douban.com/passport/login?redir=https%3A%2F%2Fmovie.douban.com%2F'
    page_text = requests.get(url=url, headers=headers).text
    print(page_text)

