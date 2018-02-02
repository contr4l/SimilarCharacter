# 此模块用于爬取汉字结构字典

import requests
from bs4 import BeautifulSoup
import re
from tqdm import tqdm
import time
import sys


def get_url():
    key_word_lst = ['左右结构','上下结构','左中右结构','上中下结构','全包围结构']
    for no,key_word in enumerate(key_word_lst):
        yield no,'http://zd.xieso.net/jg/'+key_word+'/'

def get_page():
    for no,url1 in get_url():
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}
        res1 = requests.get(url1, headers=header)
        res1.encoding ='gb18030'
        #print(res1.text)
        soup1 = BeautifulSoup(res1.text, 'html.parser')
        pattern = re.compile('.尾页')
        end_number = soup1.find_all('a',text='尾页')
        if len(end_number) > 0:
            end_number = end_number[0].get('href').split('/')[-2]
        else:
            end_number = 1
        print("\n第 %d 种结构写入中..." % (no + 1))
        for page in tqdm(range(int(end_number))):
            yield no,page,requests.get(url1 + str(page) + '/')

def get_structure():
    for no,page,res2 in get_page():
        res2.encoding = 'gb18030'
        soup2 = BeautifulSoup(res2.text,'html.parser')
        tag1 = soup2.find('div',class_='chali chazi')
        symbol_lst = tag1.find_all('li')
        f = open('D:/py/StructureDict.txt', 'a', encoding='utf-8')
        for symbol in symbol_lst:
            f.write("'{0}':'{1}',\n".format(symbol.get_text(),no+1))

        f.close()

f = open('D:/py/StructureDict.txt', 'w', encoding='utf-8')
f.truncate()
f.close()
get_structure()
