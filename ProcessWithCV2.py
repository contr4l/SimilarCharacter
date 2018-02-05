# coding=gbk
import cv2
import Character
from tqdm import tqdm

# 根据灰度比较生成图片的hash代码
def dHash(img1,img2):
    img1 = cv2.resize(img1, (12,12), interpolation=cv2.INTER_CUBIC)
    img2 = cv2.resize(img2, (12,12), interpolation=cv2.INTER_CUBIC)
    gray1 = cv2.cvtColor(img1,cv2.COLOR_BGR2GRAY)
    gray2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)
    similarity = 0
    for i in range(12):
        for j in range(12):
            if gray1[i,j] == gray2[i,j]:
                similarity += 1
            else:
                pass
    return similarity/144

def main():
    file1 = open('D:/py/Shape_CV2.txt', 'w')

    word_pic_path = 'D:/py/chinese/'
    for index1,word1 in tqdm(enumerate(Character.Symbol_lst())):
        # print(index1,word1)
        # print(word_pic_path + str(index1) + '.png')
        word_pic1 = cv2.imread(word_pic_path + str(index1) + '.png')
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
                similar_index = dHash(word_pic1,word_pic2)
                if similar_index > 0.85:
                    print(similar_index, word1, word2)
                    file1.write(word2)
    file1.close()



# 2018-02-05下步工作打算备忘
# 判断整体匹配度，若超过0.8，则录入，否则进入分支：
# 区分汉字结构，若为左右结构，进入模式1：若右侧匹配度超过0.9或者整体匹配度超过0.8，则录入
# 若为上下结构，进入模式2：若下部匹配度超过0.9或整体匹配度超过0.8，则录入
# 若为独体字结构，进入模式3：若整体匹配度超过0.75，则录入

