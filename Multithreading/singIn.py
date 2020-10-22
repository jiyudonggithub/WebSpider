# -*- coding: utf-8 -*-
# @Time : 2020/9/28 16:03
# @Author : Jiyudong
# @FileName: singIn.py
# @Software: PyCharm
from selenium import webdriver
import time

bro = webdriver.Chrome(executable_path='./chromedriver')

bro.get('https://qzone.qq.com/')
bro.switch_to.frame('login_frame')
passSign = bro.find_element_by_id('switcher_plogin')
passSign.click()

name = bro.find_element_by_css_selector('#u')
password = bro.find_element_by_css_selector('#p')
name.send_keys('1942705644')
time.sleep(1)
password.send_keys('10281103love')
time.sleep(1)
submit = bro.find_element_by_css_selector('#login_button')

submit.click()
time.sleep(5)
bro.execute_script('window.scrollTo(0,document.body.scrollHeight)')

time.sleep(10)

bro.quit()
