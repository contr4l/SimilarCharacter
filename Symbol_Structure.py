# -*-coding:utf-8-*-
# 此模块用于爬取汉字结构字典

import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm


def get_url():
    file1 = open('D:/py/Word_Structure_Dict.txt', 'w', encoding='utf-8')
    file1.truncate()
    file1.close()

    key_word_lst = ['danyi', 'zuoyou', 'shangxia', 'zuozhongyou', 'shangzhongxia', 'youshangbaowei', 'zuoshangbaowei', 'zuoxiabaowei']
    header = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) \
            Chrome/63.0.3239.132 Safari/537.36'}
    for index, key_word in enumerate(key_word_lst):
        file1 = open('D:/py/Word_Structure_Dict.txt', 'a', encoding='utf-8')
        url = 'http://zidian.miaochaxun.com/'+key_word+'.html'
        print(url)
        res1 = requests.get(url, headers=header)
        res1.encoding = 'utf-8'
        soup1 = BeautifulSoup(res1.text, 'html.parser')
        zi_list = soup1.find_all('p', class_='zi')
        for s in zi_list:
            [p.extract() for p in s.find_all('span')]

        for s in zi_list:
            for word in s.find_all('a'):
                # print(word.get_text())
                try:
                    file1.write("'{0}':'{1}',\n".format(word.get_text(), index))
                except TypeError:
                    pass
                continue
        file1.close()


if __name__ == '__main__':
    get_url()
