import cv2
import ProcessWithCV2

img1 = cv2.imread("D:/py/chinese/7.png")
img2 = cv2.imread("D:/py/chinese/8.png")
a = ProcessWithCV2.dHash(img1, img2, 1)
print(a)
