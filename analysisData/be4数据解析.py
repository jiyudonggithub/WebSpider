# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:38
# @Author : Jiyudong
# @FileName: be4数据解析.py
# @Software: PyCharm

import requests
import bs4
import lxml
import time
if __name__ == '__main__':
    url = 'https://www.shicimingju.com/book/sanguoyanyi.html'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    text = requests.get(url=url, headers=headers).text
    soup = bs4.BeautifulSoup(text, 'lxml')
    soup_select = soup.select('.book-mulu a')
    with open('./sanguoyanyi.txt', 'w', encoding='utf-8') as f:
        for aTage in soup_select:
            title = aTage.string
            srl = 'https://www.shicimingju.com' + aTage['href']
            # time.sleep(3)
            title__text = requests.get(url=srl, headers=headers).text
            title_soup = bs4.BeautifulSoup(title__text, 'lxml')
            find = title_soup.find('div', class_='chapter_content')
            detile = find.text
            f.write(title + ':' + detile + '\n')
            print(title + '爬取成功')

    print('ok')
