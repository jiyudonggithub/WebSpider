# -*- coding: utf-8 -*-
# @Time : 2020/9/27 15:14
# @Author : Jiyudong
# @FileName: demo.py
# @Software: PyCharm
import requests
import base64
from PIL import Image
# encoding:utf-8
API_Key = 'blCljWQzt2xYHvG1384q7z9O'
Secret_Key = 'NY9KDcPkM6gg5vPUMIu3gUS7i6eFgNer'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=%s&client_secret=%s'

url = host % (API_Key, Secret_Key)

response = requests.get(url)
if response:
    access_token = response.json()['access_token']
    print(access_token)
# with  open('./cord.jpg', 'rb') as f:
#     img_content = f.read()
f = open('./a.png', 'rb')
img = base64.b64encode(f.read())
params = {"image": img}
url_type = {
    'wordOCR': 'https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic',
    'WebOCR': 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage',
    'NumOCR': 'https://aip.baidubce.com/rest/2.0/ocr/v1/numbers'
}
request_url = 'https://aip.baidubce.com/rest/2.0/ocr/v1/webimage'
# request_url = url_type['WebOCR'] + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
request_url = request_url + "?access_token=" + access_token
response = requests.post(request_url, data=params, headers=headers)
if response:
    print(response.json())
