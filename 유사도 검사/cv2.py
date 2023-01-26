import numpy as np
import cv2
from matplotlib import pyplot as plt
import glob
import os


img_list = glob.glob('/Users/admin/Desktop/최종 프로젝트/이미지/삐삐/*.jpg')
# dir_img_list = glob.glob('/home/john/PycharmProjects/MOT_test/person_frame/*.jpg')

for i in range(len(img_list)):
    img1 = cv2.imread(f'{img_list[0]}',0)          # queryImage
    img2 = cv2.imread(f'{img_list[1]}',0) # trainImage

    sift = cv2.xfeatures2d.SIFT_create()
    kp1, des1 = sift.detectAndCompute(img1,None)
    kp2, des2 = sift.detectAndCompute(img2,None)
    bf = cv2.BFMatcher()

    matches = bf.knnMatch(des1,des2, k=2)
    good = []

    for m,n in matches:
        # if m.distance < 0.3*n.distance:
        if m.distance < n.distance:

            good.append([m])
    print('same_good', good)
    img3 = cv2.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=2)
    plt.imshow(img3),plt.show()
    cv2.imshow("comapre", img3)
    cv2.waitKey(1)