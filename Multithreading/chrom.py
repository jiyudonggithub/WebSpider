# -*- coding: utf-8 -*-
# @Time : 2020/9/28 15:32
# @Author : Jiyudong
# @FileName: chrom.py
# @Software: PyCharm
from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://www.taobao.com/')
search_input = bro.find_element_by_id('q')
search_input.send_keys('macpro')
btn = bro.find_element_by_class_name('btn-search')
btn.click()
time.sleep(5)
bro.quit()
