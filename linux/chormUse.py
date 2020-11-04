#!/usr/bin/env python
# -*- encoding: utf-8 -*-
'''
@File    :   chormUse.py    
@Contact :   yudong.j@icloud.com


@Modify Time      @Author    @Version    @Desciption
------------      -------    --------    -----------
2020/10/27 下午9:54   yudong      1.0         None
'''

from selenium import webdriver
import time
from PIL import Image
from Multithreading.chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains

if __name__ == '__main__':
    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument('--start-maximized')

    bro = webdriver.Chrome(executable_path='/home/yudong/chromedriver', options=chorme_options)

    bro.get('https://login.taobao.com/')
    bro.switch_to.frame('login-form')
    sigin = bro.find_element_by_class_name('fm-button fm-submit password-login')
    sigin.click()
    # action = ActionChains(bro)
    # for i in range(5):
    #     action.move_by_offset(17, 0).perform()
    # action.release()
    time.sleep(5)
    bro.quit()
