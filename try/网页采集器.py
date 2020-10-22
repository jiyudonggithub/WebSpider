# -*- coding: utf-8 -*-
# @Time : 2020/9/25 16:16
# @Author : Jiyudong
# @FileName: 网页采集器.py
# @Software: PyCharm
import requests

# UA伪装
# UA ：user-Agent(请求载体的身份标识)
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://www.sogou.com/web'
    # 处理url携带的参数：封装到字典
    kw = input('enter a word:')
    param = {
        'query': kw
    }
    get = requests.get(url=url, params=param, headers=headers)
    text = get.text
    print(text)
