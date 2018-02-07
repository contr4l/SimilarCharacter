# coding=gbk
import cv2
import Character
from tqdm import tqdm
import Dict

# 根据灰度比较生成图片的hash代码


def dHash(img1, img2, no):
    # no值为整型，0代表泛用型比较（也包括上中下结构、独体字和全包围结构），1代表左右结构，2代表上下结构，3代表左中右结构
    img1 = cv2.resize(img1, (12, 12), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (12, 12), interpolation=cv2.INTER_CUBIC)
    gray1 = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    similarity = 0
    similarity_1 = 0
    similarity_2 = 0
    if no == 0:  # 针对独体字、上中下、左中右以及两者结构不同的情况
        for i in range(12):
            for j in range(12):
                if gray1[i, j] == gray2[i, j]:
                    similarity += 1
        return similarity/144

    elif no == 1:
        # 左右结构按照右部标准进行(右部可能占整体的0.75或者0.5，暂时按照0.75来算)
        for i in range(0, 12):
            for j in range(3, 12):
                if gray1[i, j] == gray2[i, j]:
                    similarity += 1
                else:
                    pass
        return similarity / 108

    elif no == 2:
        # 上下结构按照上部或下部标准进行
        for i in range(0, 9):
            for j in range(0, 12):
                if gray1[i, j] == gray2[i, j]:
                    similarity_1 += 1
        for i in range(3, 12):
            for j in range(12):
                if gray1[i, j] == gray2[i, j]:
                    similarity_2 += 1
        return max(similarity_1, similarity_2) / 108


def main():

    # 首先执行文件清空操作
    word_pic_path = 'D:/py/chinese/'
    file1 = open('D:/py/Shape_CV2.txt', 'w')
    file1.truncate()
    file1.close()

    # 文件判断写入
    for index1, word1 in tqdm(enumerate(Character.Symbol_lst())):
        # 每次执行一次文件打开关闭操作
        file1 = open('D:/py/Shape_CV2.txt', 'a')
        word_pic1 = cv2.imread(word_pic_path + str(index1) + '.png')
        # 写入头文字
        file1.write(word1 + ' ')
        for index2, word2 in enumerate(Character.Symbol_lst()):
            word_pic2 = cv2.imread(word_pic_path + str(index2) + '.png')
            if index1 == index2:
                continue
            else:
                # cv2.imshow('image1',word_pic1)
                # cv2.waitKey(0)
                # cv2.imshow('image2',word_pic2)
                # cv2.waitKey(0)

                # 若两字在结构字典中存在且值相同，进入局部判断分支
                if word1 in Dict.structure_dict and word2 in Dict.structure_dict and Dict.structure_dict[word1] == \
                        Dict.structure_dict[word2]:
                    # 字典值——0为独体字，1为左右结构，2为上下结构，3为左中右结构，4为上中下结构，5为右上包围结构，6为左上包围，7为左下包围
                    if Dict.structure_dict[word1] in ['1', '2']:
                        similar_index = dHash(word_pic1, word_pic2, int(Dict.structure_dict[word1]))
                    else:
                        similar_index = dHash(word_pic1, word_pic2, 0)
                # 若有一字不在字典中，进入泛用型比较
                else:
                    similar_index = dHash(word_pic1, word_pic2, 0)

                if similar_index >= 0.8:
                    file1.write(word2)

        file1.write('\n')
        file1.close()


if __name__ == '__main__':
    main()
