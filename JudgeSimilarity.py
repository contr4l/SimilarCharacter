# coding=gbk
from Dict import TrAngle as dict1 # 四码字典
import Character # 包含所有汉字的列表
from tqdm import tqdm # 进度条
from writenumDict import write_num_dict as dict2 # 笔画数字典
from Dict import structure_dict as dict3 # 结构字典
from Pronunciation import pronunciation_index

lst = Character.Symbol_lst()

file1 = open('D:/py/Shape.txt', 'w')

def get_similar(char1,char2): # char1,char2为汉字
    # 获取四码和汉字笔画数
    code1 = dict1[char1]
    code2 = dict1[char2]
    write_num1 = int(dict2[char1])
    write_num2 = int(dict2[char2])
    structure1 = dict3.setdefault(char1,None)
    structure2 = dict3.setdefault(char2,None)

    # 定义结构相似度
    if structure1 and structure2 and structure1 == structure2:
        structure_index = 1
    else:
        structure_index = 0

    # 定义四码相似度
    code_index = 0
    # 四码分为四位计算，若相同则指数+1，不同为0,总权数除以4再加权
    for _i in range(4):
        if code1[_i] == code2[_i]:
            code_index += 1
    code_index /= 4

    # 添加发音相似度
    voice_index = pronunciation_index(char1,char2)



    # 笔画数利用相对偏差的方式进行计算
    write_num_index = 1- abs((write_num1 - write_num2)/max(write_num1,write_num2))
    # 四码权重、笔画权重和结构权重分别为为 0.4 0.3 0.3
    similarity_index_ = (code_index * 0.4 + write_num_index * 0.3 + structure_index * 0.3) * 0.5 + voice_index * 0.5

    return similarity_index_

print('形近字判断写入中...')
for i in tqdm(lst):
    file1.write(i+' ')
    for j in lst:
        if i == j:
            pass
        else:
            # 设计一个加权音字形相似度算法，根据笔画数和四码相近程度来判断，若大于某一个阈值，则写入相近字文件
            similarity_index = get_similar(i,j)
            if similarity_index > 0.9:
                file1.write(j)
    file1.write('\n')
file1.close()