# -*- coding: utf-8 -*-
# @Time : 2020/9/27 11:02
# @Author : Jiyudong
# @FileName: 验证码识别.py
# @Software: PyCharm

import requests
from lxml import etree
from OCR.CRecognition import CRecongnition
import imghdr
import io
import PIL.Image

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36'
    }
    url = 'https://so.gushiwen.cn/user/login.aspx?from=http://so.gushiwen.cn/user/collect.aspx'

    page_text = requests.get(url=url, headers=headers).text
    tree = etree.HTML(page_text)
    img_src = tree.xpath('//img[@id="imgCode"]/@src')[0].strip()
    URL = 'https://so.gushiwen.cn' + img_src
    img_content = requests.get(url=URL, headers=headers).content
    imghdr_what = imghdr.what(None, img_content)
    img_path = './imgCode.%s' % imghdr_what

    with open(img_path, 'wb') as f:
        f.write(img_content)
    CRe = CRecongnition()
    picture_type = CRe.changePictureType(img_content)

    ocr = CRe.getContentOCR(content=picture_type, OCR_type='WebOCR')
    print(ocr)
