# -*- coding: utf-8 -*-
# @Time : 2020/9/28 19:34
# @Author : Jiyudong
# @FileName: 12306.py
# @Software: PyCharm

from selenium import webdriver
import time
from PIL import Image
from Multithreading.chaojiying import Chaojiying_Client
from selenium.webdriver import ActionChains


def localList(result):
    local_list = []
    if '|' in result:
        result_list = result.split("|")
        for re in result_list:
            split_str = splitStr(re)
            local_list.append(split_str)
    else:
        local_list.append(splitStr(result))

    return local_list


def splitStr(s):
    s_list = []
    s_split = s.split(",")
    s_list.append(int(s_split[0]))
    s_list.append(int(s_split[1]))
    return s_list


if __name__ == '__main__':
    ID = 908425
    user = '15155727229'
    password = '10281103love'

    # 浏览器最大化
    chorme_options = webdriver.ChromeOptions()
    chorme_options.add_argument('--start-maximized')

    bro = webdriver.Chrome(executable_path='./chromedriver', options=chorme_options)
    # 浏览器最大化
    # bro.maximize_window()
    bro.get('https://kyfw.12306.cn/otn/resources/login.html')
    singin = bro.find_element_by_css_selector('.login-hd-account')
    singin.click()
    time.sleep(1)
    # 将网页进行全部截屏
    bro.save_screenshot('./12306.png')
    # 裁剪区域的确定
    img_ele = bro.find_element_by_css_selector('#J-loginImg')
    # 验证码图片左上角的图片
    location = img_ele.location
    # print(location)
    # 验证码图片的长和宽
    size = img_ele.size
    # print(size)
    coordinate = (
        int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    # print(coordinate)
    image_open = Image.open('./12306.png')
    frame = image_open.crop(coordinate)
    frame.save('./code.png')
    chaojiying = Chaojiying_Client(username=user, password=password, soft_id=ID)
    im = open('./code.png', 'rb').read()
    pic_str_result = chaojiying.PostPic(im, 9004)['pic_str']
    local_list = localList(pic_str_result)
    print(local_list)
    for local in local_list:
        x = local[0]
        y = local[1]
        ActionChains(bro).move_to_element_with_offset(img_ele, xoffset=x, yoffset=y).click().perform()
        time.sleep(0.5)

    bro.quit()
