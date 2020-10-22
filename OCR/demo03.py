# -*- coding: utf-8 -*-
# @Time : 2020/9/27 21:33
# @Author : Jiyudong
# @FileName: demo03.py
# @Software: PyCharm
import tesserocr
from PIL import     Image
image=Image.open('imgCode.gif')
print(tesserocr.image_to_text(image))