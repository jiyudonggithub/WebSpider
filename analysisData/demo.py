# -*- coding: utf-8 -*-
# @Time : 2020/9/26 10:02
# @Author : Jiyudong
# @FileName: demo.py
# @Software: PyCharm

import re

if __name__ == '__main__':
    # test = '//pic.qiushibaike.com/system/pictures/12342/123424058/medium/JPVO5AAE1XA6I8GX.jpg'
    #
    # re_search = re.search(r'(.*)/(.*)\.jpg', test)

    # print(re_search.group(0))
    # print(re_search.group(1))
    # print(re_search.group(2))
    # url = 'https://www.qiushibaike.com/imgrank/page/%d/'
    # pageNum = 3
    # print(format(url % pageNum))
    city = [
        '', '', '阿坝州', '', '', '', '安康', '', '', '', '阿克苏地区', '', '', '', '阿里地区', '', '', '', '阿拉善盟', '', '', '',
        '阿勒泰地区', '', '', '', '安庆', '', '', '', '安顺', '', '', '', '鞍山', '', '', '', '克孜勒苏州', '', '', '', '安阳', '', '']
    new_city = []
    for ct in city:
        if len(ct) != 0:
            new_city.append(ct)
    print(new_city)
