# -*- coding: utf-8 -*-
# @Time : 2020/9/27 20:12
# @Author : Jiyudong
# @FileName: demo02.py
# @Software: PyCharm
import imghdr
import io

import PIL.Image

# im = PIL.Image.open('cord.gif')
# with open('./cord.gif', 'rb') as f:
#     content = f.read()
# byte_stream = io.BytesIO(content)
# # 把请求到的数据转换为Bytes字节流(这样解释不知道对不对，可以参照[廖雪峰](https://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/001431918785710e86a1a120ce04925bae155012c7fc71e000)的教程看一下)
#
# roiImg = PIL.Image.open(byte_stream)  # Image打开二进制流Byte字节流数据
#
# imgByteArr = io.BytesIO()  # 创建一个空的Bytes对象
#
# roiImg.save(imgByteArr, format='PNG')  # PNG就是图片格式，我试过换成JPG/jpg都不行
#
# imgByteArr = imgByteArr.getvalue()  # 这个就是保存的二进制流
#
# # 下面这一步只是本地测试， 可以直接把imgByteArr，当成参数上传到七牛云
# with open("./abc.png", "wb") as f:
#     f.write(imgByteArr)
im = PIL.Image.open('./cord.gif')
bytes_io = io.BytesIO()
im.save(bytes_io, format='png')
# with open('./a.png', 'rb') as f:
#     cent = f.read()
imgtype = imghdr.what(None, bytes_io.getvalue())
print(imgtype)
