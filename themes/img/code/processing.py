import cv2
import numpy as np

image = cv2.imread('themes/img/code/h2.png', cv2.IMREAD_UNCHANGED)

h,w,c = image.shape

#290 110

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
cv2.imwrite('themes/img/code/h2_1.png', image_new)
cv2.imshow('1', image_new)
cv2.waitKey()
