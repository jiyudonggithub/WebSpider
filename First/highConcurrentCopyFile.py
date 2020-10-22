# -*- coding: utf-8 -*-
# @Time : 2020/9/24 19:34
# @Author : Jiyudong
# @FileName: highConcurrentCopyFile.py
# @Software: PyCharm
import os
import multiprocessing


def copyFile(soure_file, file, dest_file):
    sabPath = os.path.join(soure_file, file)
    dabPath = os.path.join(dest_file, file)
    with open(sabPath, 'rb') as sf:
        with open(dabPath, 'wb') as df:
            while True:
                data = sf.read(1024)
                if data:
                    df.write(data)
                else:
                    break


if __name__ == '__main__':
    source_file = 'D:\\虚拟机镜像'
    dest_file = 'F:\\Desktop\\test'
    try:
        os.mkdir(dest_file)
    except:
        print(dest_file, '已经存在')
    listdir = os.listdir(source_file)
    for filedir in listdir:
        process = multiprocessing.Process(target=copyFile, args=(source_file, filedir, dest_file))
        process.start()
