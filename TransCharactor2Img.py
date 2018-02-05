# coding=utf-8
import os
import pygame
import Character


# 此程序用于将汉字转图片输出，以便利用opencv进行相似度识别
chinese_dir = 'D:/py/chinese/'
if not os.path.exists(chinese_dir):
    os.mkdir( chinese_dir)

pygame.init()
for i,word in enumerate(Character.Symbol_lst()):
    font = pygame.font.Font("C:\Windows\Fonts\msyh.ttf", 100)  # 当前目录下要有微软雅黑的字体文件msyh.ttc,或者去c:\Windows\Fonts目录下找
    rtext = font.render(word, True, (0, 0, 0), (255, 255, 255))
    pygame.image.save(rtext, os.path.join(chinese_dir+ str(i) + ".png"))

