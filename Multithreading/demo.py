# -*- coding: utf-8 -*-
# @Time : 2020/9/28 9:39
# @Author : Jiyudong
# @FileName: demo.py
# @Software: PyCharm

import random
import execjs
import time
import math
# print(time.localtime())
# print(time.time())
# print(math.random())
js = execjs.eval('Math.random()')
print(js)