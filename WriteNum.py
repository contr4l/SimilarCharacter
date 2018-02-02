import requests
from bs4 import BeautifulSoup
import re
import Character
from tqdm import tqdm

def transutf8(symbol):
    symbol = str(symbol.encode('utf-8'))
    utf8_code = symbol[4:6]+symbol[8:10]+symbol[12:14]
    return utf8_code

def writenum(symbol):
    url_head = 'https://bihua.51240.com/'
    url_tail = '__bihuachaxun/'
    # 遍历输入汉字的utf8编码，爬取对应的笔画数
    url_mid = transutf8(symbol)

    url = url_head + url_mid + url_tail
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'lxml')
    pattern = re.compile('笔画数')
    pattern2 = re.compile('\d{1,2}')
    write_num = soup.find('td',text=pattern).parent.find('td', text=pattern2).get_text()
    return write_num

def get_dict():
    symbol_lst = Character.Symbol_lst()
    write_num_dict = {}
    for char_one in tqdm(symbol_lst):
        write_num_dict[char_one] = writenum(char_one)
    return write_num_dict


def main():
    with open("D:/py/write_num.txt", 'w') as f:
        for i,j in get_dict().items():
            f.write(i+' '+j)
        f.close()


if __name__ == '__main__':
    main()