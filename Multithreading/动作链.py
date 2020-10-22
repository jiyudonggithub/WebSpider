# -*- coding: utf-8 -*-
# @Time : 2020/10/9 9:35
# @Author : Jiyudong
# @FileName: 动作链.py
# @Software: PyCharm
from selenium import webdriver
import time
from PIL import Image
from Multithreading.chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument('--start-maximized')

    bro = webdriver.Chrome(executable_path='./chromedriver', options=chorme_options)
    # 浏览器最大化
    # bro.maximize_window()
    bro.get('https://login.taobao.com/')
    action = ActionChains(bro)
    for i in range(5):
        action.move_by_offset(17, 0).perform()
    action.release()
    bro.quit()
