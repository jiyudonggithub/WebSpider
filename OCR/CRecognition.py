# -*- coding: utf-8 -*-
# @Time : 2020/9/27 10:04
# @Author : Jiyudong
# @FileName: CRecognition.py
# @Software: PyCharm
# encoding:utf-8
import requests

import base64
import imghdr
import io
import PIL.Image


class CRecongnition:

    def __init__(self):
        self.API_Key = 'blCljWQzt2xYHvG1384q7z9O'
        self.Secret_Key = 'NY9KDcPkM6gg5vPUMIu3gUS7i6eFgNer'
        self.wordOCR = 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic'
        self.WebOCR = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'
        self.NumOCR = 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'

    def getAccessToken(self):
        # client_id 为官网获取的AK， client_secret 为官网获取的SK
        host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'

        url = host % (self.API_Key, self.Secret_Key)

        response = requests.get(url)
        if response:
            return response.json()['access_token']
        else:
            return None

    def getImgOCR(self, img_path, OCR_type='WebOCR'):
        '''
        网络图片文字识别
        '''
        url_type = {
            'wordOCR': self.wordOCR,
            'NumOCR': self.NumOCR,
            'WebOCR': self.WebOCR
        }
        # 二进制方式打开图片文件
        img_content = ''
        with  open(img_path, 'rb') as f:
            img_content = f.read()
        img = base64.b64encode(img_content)
        params = {"image": img}
        access_token = self.getAccessToken()
        request_url = url_type[OCR_type] + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()['words_result'][0]['words']
        else:
            return None

    def changePictureType(self,img_content):
        '''
        改变图片的的格式，如果不是jpg或png则将其转成png
        :param img_content: 输入图片的二进制
        :return: 输出图片的二进制
        '''
        imghdr_what = imghdr.what(None, img_content)
        if imghdr_what not in ['jpg', 'png']:
            byte_stream = io.BytesIO(img_content)
            pil_image_open = PIL.Image.open(byte_stream)
            bytes_io = io.BytesIO()
            pil_image_open.save(bytes_io, format='png')
            img_content = bytes_io.getvalue()
        return img_content

    def getContentOCR(self, content, OCR_type='WebOCR'):
        '''
        网络图片文字识别
        '''
        url_type = {
            'wordOCR': self.wordOCR,
            'NumOCR': self.NumOCR,
            'WebOCR': self.WebOCR
        }
        # 二进制方式打开图片文件
        img = base64.b64encode(content)
        params = {"image": img}
        access_token = self.getAccessToken()
        request_url = url_type[OCR_type] + "?access_token=" + access_token
        headers = {'content-type': 'application/x-www-form-urlencoded'}
        response = requests.post(request_url, data=params, headers=headers)
        if response:
            return response.json()['words_result'][0]['words']
        else:
            return None
