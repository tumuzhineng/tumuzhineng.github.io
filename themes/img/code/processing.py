import cv2
import numpy as np

#290 110

def pad(image):
    h,w,c = image.shape
    if h/110 > w/290:
        w_new = int(h/110*290)
        image_new = np.zeros((h,w_new,c), np.uint8)
        s = int((w_new-w)/2)
        image_new[:,s:s+w] = image
    else:
        h_new = int(w/290*110)
        image_new = np.zeros((h_new,w,c), np.uint8)
        s = int((h_new-h)/2)
        image_new[s:s+h,:] = image
    cv2.imwrite('themes/img/code/h3_1.png', image_new)
    cv2.imshow('1', image_new)
    cv2.waitKey()

def crop(image):
    h,w,c = image.shape
    if h/110 > w/290:
        h_new = int(w/290*110)
        s = int((h-h_new)/2)
        image = image[s:s+w]
    else:
        w_new = int(h/110*290)
        s = int((w-w_new)/2)
        image = image[:,s:s+w]
    cv2.imwrite('themes/img/code/h3_1.png', image)
    cv2.imshow('1', image)
    cv2.waitKey()

image = cv2.imread('themes/img/code/h3.png', cv2.IMREAD_UNCHANGED)
h,w,c = image.shape
'''
for i in range(w):
    if image[0,i,3] == 0:
        print(i)
image = image[:,6:2159]
cv2.imwrite('themes/img/code/h3_1.png', image)
cv2.imshow('1', image)
cv2.waitKey()
'''
pad(image)