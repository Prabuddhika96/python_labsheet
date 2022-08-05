import cv2
import numpy as np
import matplotlib.pyplot as plt

img=cv2.imread('orion_spinelli_c1.jpg',cv2.IMREAD_COLOR)
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

img_gray=cv2.imread('orion_spinelli_c1.jpg',cv2.IMREAD_GRAYSCALE)

img_gray_blur1=cv2.medianBlur(img_gray,11)
img_gray_blur2=cv2.GaussianBlur(img_gray_blur1,(5,5),0)

##creating mask
ret,mask=cv2.threshold(img_gray_blur2,70,255,cv2.THRESH_BINARY)

##logical operation
result=cv2.bitwise_and(img,img,mask=mask)

plt.suptitle('Orion Extraction')

plt.subplot(131)
plt.imshow(img)
plt.title('Original')
plt.xticks([])
plt.yticks([])

plt.subplot(132)
plt.imshow(mask,cmap='Greys_r')
plt.title('Mask')
plt.xticks([])
plt.yticks([])

plt.subplot(133)
plt.imshow(result)
plt.title('Output')
plt.xticks([])
plt.yticks([])

plt.show()

#2)

img=cv2.imread('numbers.jpg',cv2.IMREAD_GRAYSCALE)

#global threshold value
t1=100

ret1,thresh1=cv2.threshold(img,t1,255,cv2.THRESH_BINARY)
ret2,thresh2=cv2.threshold(img,t1,255,cv2.THRESH_BINARY_INV)
ret3,thresh3=cv2.threshold(img,t1,255,cv2.THRESH_TRUNC)
ret4,thresh4=cv2.threshold(img,t1,255,cv2.THRESH_TOZERO)
ret5,thresh5=cv2.threshold(img,t1,255,cv2.THRESH_TOZERO_INV)

#adaptive thresholding
thresh6=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,21,2)
thresh7=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY_INV,21,2)
thresh8=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,21,2)
thresh9=cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY_INV,21,2)

#Otzu's Thresholding
ret10,thresh10=cv2.threshold(img,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

blur=cv2.GaussianBlur(img,(5,5),0)
ret11,thresh11=cv2.threshold(blur,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)

title=['Original','THRESH_BINARY','THRESH_BINARY_INV','THRESH_TRUNC','THRESH_TOZERO','THRESH_TOZERO_INV','ADAPTIVE_THRESH_MEAN_C+THRESH_BINARY','ADAPTIVE_THRESH_MEAN_C+THRESH_BINARY_INV','ADAPTIVE_THRESH_GAUSSIAN_C+THRESH_BINARY','ADAPTIVE_THRESH_GAUSSIAN_C+THRESH_BINARY_INV','Otzu\'s Thresholding','Otzu\'s thresholding after Gaussian filtering']

image=[img,thresh1,thresh2,thresh3,thresh4,thresh5,thresh6,thresh7,thresh8,thresh9,thresh10,thresh11]

for i in range(12):
    plt.subplot(5,3,i+1)
    plt.title(title[i],fontsize=7)
    plt.imshow(image[i],cmap='gray')
    plt.xticks([])
    plt.yticks([])


ret12, thresh12 = cv2.threshold(img,5,255,cv2.THRESH_TRUNC)
plt.subplot(5,3,14)
plt.title('all the numbers in image',fontsize=7)
plt.imshow(thresh12, cmap='Greys_r')
plt.xticks([])
plt.yticks([])

plt.show()   






























