import cv2
import numpy as np
import matplotlib.pyplot as plt

## q1)

##read image
img=cv2.imread('fire.jpg',cv2.IMREAD_COLOR)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#split to hsv
h,s,v=cv2.split(cv2.cvtColor(img,cv2.COLOR_RGB2HSV))
eq_v=cv2.equalizeHist(v)

##merge
eq_img=cv2.merge([h,s,eq_v])
eq_img=cv2.cvtColor(eq_img,cv2.COLOR_HSV2RGB)

##threshold
ret,thresh=cv2.threshold(eq_img,205,255,cv2.THRESH_BINARY_INV)

##mask
mask=cv2.inRange(thresh,(0,0,255),(0,255,255))

##applying a mask to the image
result=cv2.bitwise_and(eq_img,eq_img,mask=mask)

plt.subplot(1,3,1)
plt.title('Original')
plt.imshow(img)
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,2)
plt.title('Mask')
plt.imshow(mask,cmap='Greys_r')
plt.xticks([])
plt.yticks([])

plt.subplot(1,3,3)
plt.title('Result')
plt.imshow(result)
plt.xticks([])
plt.yticks([])

plt.show()



## q2)
img=cv2.imread('1.jpg',cv2.IMREAD_GRAYSCALE)

#global
hist_eq_img=cv2.equalizeHist(img)

#creating a CLAHE object with clipLimit 2.0
clahe1=cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))
gray_img_clahe_1=clahe1.apply(img)

#creating a CLAHE object with clipLimit 5.0
clahe2=cv2.createCLAHE(clipLimit=5.0, tileGridSize=(8,8))
gray_img_clahe_2=clahe2.apply(img)

#creating a CLAHE object with clipLimit 10.0
clahe3=cv2.createCLAHE(clipLimit=10.0, tileGridSize=(8,8))
gray_img_clahe_3=clahe3.apply(img)

#creating a CLAHE object with clipLimit 20.0
clahe4=cv2.createCLAHE(clipLimit=20.0, tileGridSize=(8,8))
gray_img_clahe_4=clahe4.apply(img)

array=[gray_img_clahe_1,gray_img_clahe_2,gray_img_clahe_3,gray_img_clahe_4]
title=['clipLimit = 2.0', 'clipLimit = 5.0', 'clipLimit = 10.0', 'clipLimit = 20.0']

for i in range(0,4):
    plt.subplot(2,2,i+1)
    plt.title(title[i])
    plt.imshow(array[i], cmap='Greys_r')
    plt.xticks([])
    plt.yticks([])

plt.show()

































