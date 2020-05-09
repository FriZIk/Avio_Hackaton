import cv2 as cv
import numpy as np

window_name = ('Sobel Demo - Simple Edge Detector')
scale = 1 
delta = 0 
ddepth = cv.CV_16S

img = cv.imread('Default_Images/test.png', 1) 
cv.imshow("Original image",img) 
clahe = cv.createCLAHE(clipLimit=3., tileGridSize=(8,8)) 
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB) # convert from BGR to LAB color space 
l, a, b = cv.split(lab) # split on 3 different channels 
l2 = clahe.apply(l) # apply CLAHE to the L-channel 
lab = cv.merge((l2,a,b)) # merge channels 
img2 = cv.cvtColor(lab, cv.COLOR_LAB2BGR) # convert from LAB to BGR 
cv.imwrite('sunset_modified.jpg', img2)

# Sobel operator test
src = img2
src = cv.GaussianBlur(src, (3, 3), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv.imwrite('Ready_Images/Rezult_Sobel.png',grad)

ret, thresh = cv.threshold(gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(gray, contours, -1, (0,255,0), 3)

for cnt in contours:
    rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    box = np.int0(box) # округление координат
    cv.drawContours(gray,[box],0,(255,0,0),2) # рисуем прямоугольник

cv.imwrite('Ready_Images/Countours_Test.png',gray);
#cv.imshow(window_name, grad)