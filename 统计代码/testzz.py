# -*- coding: utf-8 -*-
"""
Created on Thu Mar 25 22:54:49 2021

@author: LF
"""
import os
from PIL import Image
#灰色泥质粉砂岩，黑色煤，深灰色泥岩，深灰色粉砂质泥岩，灰黑色泥岩，灰色细砂岩，浅灰色细砂岩
file_path = r"F:\B题全部数据\Rock\浅灰色细砂岩"
file_save = r'F:\B题全部数据\Pic\LightGrayGineSandstone'
for FileName in os.listdir(file_path):
    if FileName.endswith('.jpg'):
        break
    else:
        
        img = Image.open(file_path +'\\'+ FileName)
        x,y = img.size
        print(FileName)

        Pic_1 = img.crop((x*0, y*0, x*1/2, y*1/2))  # (left, upper, right, lower)
        FileName_1 = FileName[0:FileName.find(".")]+'_1.jpg'
        Pic_1.save(file_save+'\\'+ FileName_1)
        Pic_2 = img.crop((x*1/2, y*0, x, y*1/2))  # (left, upper, right, lower)
        FileName_2 = FileName[0:FileName.find(".")]+'_2.jpg'
        Pic_2.save(file_save+'\\'+ FileName_2)
        Pic_3 = img.crop((x*0, y*1/2, x*1/2, y))  # (left, upper, right, lower)
        FileName_3 = FileName[0:FileName.find(".")]+'_3.jpg'
        Pic_3.save(file_save+'\\'+ FileName_3)
        Pic_4 = img.crop((x*1/2, y*1/2, x, y))  # (left, upper, right, lower)
        FileName_4 = FileName[0:FileName.find(".")]+'_4.jpg'
        Pic_4.save(file_save+'\\'+ FileName_4)



