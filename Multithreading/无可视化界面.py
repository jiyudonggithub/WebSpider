# -*- coding: utf-8 -*-
# @Time : 2020/9/28 16:48
# @Author : Jiyudong
# @FileName: 无可视化界面.py
# @Software: PyCharm

from selenium import webdriver
import time
# from selenium.webdriver.chrome.options import Options

# 无可视化界面操作
chorme_options = webdriver.ChromeOptions()
chorme_options.add_argument('--start-maximized')
# chorme_options.add_argument('--headless')
# chorme_options.add_argument('--disable-gpu')
# 实现selenium 不被服务器检测到
chorme_options.add_experimental_option('excludeSwitches', ['enable-automation'])

bro = webdriver.Chrome(executable_path='./chromedriver', options=chorme_options)

bro.get('https://qzone.qq.com/')

print(bro.page_source)
time.sleep(15)

bro.quit()
