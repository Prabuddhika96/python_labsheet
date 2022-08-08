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
img=cv2.imread('1.jpg',cv2.IMREAD_COLOR)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

#split & applying CLAHE
def apply_clahe(img,limit):
    h,s,v=cv2.split(cv2.cvtColor(img,cv2.COLOR_RGB2HSV))
    clahe=cv2.createCLAHE(clipLimit=limit, tileGridSize=(8,8))
    new_v=clahe.apply(v)

    result=cv2.merge([h,s,new_v])
    result=cv2.cvtColor(result,cv2.COLOR_HSV2RGB)

    return result

#creating a CLAHE object with clipLimit 2.0
img_clahe_2=apply_clahe(img,2.0)

#creating a CLAHE object with clipLimit 5.0
img_clahe_5=apply_clahe(img,5.0)

#creating a CLAHE object with clipLimit 10.0
img_clahe_10=apply_clahe(img,10.0)

#creating a CLAHE object with clipLimit 20.0
img_clahe_20=apply_clahe(img,20.0)

array=[img,img_clahe_2,img_clahe_5,img_clahe_10,img_clahe_20]
title=['Original','clipLimit = 2.0', 'clipLimit = 5.0', 'clipLimit = 10.0', 'clipLimit = 20.0']

#print plots
for i in range(0,5):
    plt.subplot(2,3,i+1)
    plt.title(title[i])
    plt.imshow(array[i])
    plt.xticks([])
    plt.yticks([])

plt.show()

































