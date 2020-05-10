import cv2 as cv
import numpy as np
import os
window_name = ('Sobel Demo - Simple Edge Detector')
scale = 1
delta = 0
ddepth = cv.CV_16S


#src = cv.imread('Ready_Images/Balanced.png', cv.IMREAD_COLOR)
src = cv.imread("Default_Images/test.png", cv.IMREAD_COLOR)
src_backup = src
frame = src
BLUR_C = 3
SOBEL_SIZE = 3

f = open("Ready_Images/iteration.txt", "r")
iterationNumber = int(f.read())
f.close()
os.makedirs("Ready_Images/{}".format(iterationNumber))
pathForToday = "Ready_Images/{}".format(iterationNumber)


# Sobel operator test
#src = cv.GaussianBlur(src, (BLUR_C, BLUR_C), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imwrite('{}/GrayscaleBef.png'.format(pathForToday), gray)
weiSize = 1
serSize = 1
filStr = 0
gray = cv.fastNlMeansDenoising(gray, gray, weiSize, serSize, filStr)
cv.imwrite('{}/GrayscaleAftS{}F{}.png'.format(pathForToday, weiSize, filStr), gray)

lowThresh = 250
highThresh = 350
note = open("{}/data.txt".format(pathForToday), "w")
note.write("Low thresh:{}\nHigh thresh:{}\n".format(lowThresh,highThresh))
note.close()

thresh = cv.Canny(gray, lowThresh, highThresh)
cv.imwrite('{}/Canny.png'.format(pathForToday), thresh)
grad = gray
""""" sobel transformation
grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=SOBEL_SIZE,  scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=SOBEL_SIZE, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv.imwrite('{}/Rezult_Sobel.png'.format(pathForToday),grad)

#grad = cv.cvtColor(grad, cv.COLOR_BGR2GRAY)


ret, thresh = cv.threshold(grad, 127, 255, 0)
#thresh = cv.adaptiveThreshold(grad, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 2) Adaptive didn't work out great
"""""
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)
cv.drawContours(grad, contours, -1, (0,255,0), 3)


for cnt in contours:
    rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    box = np.int0(box) # округление координат
    cv.drawContours(grad,[box],0,(255,0,0),2) # рисуем прямоугольник

cv.imwrite('{}/Countours_TestB{}.png'.format(pathForToday, BLUR_C), grad)
#cv.imshow(window_name, grad)


# Laplasian operator test
kernel_size = 3
src_backup = cv.GaussianBlur(src_backup, (BLUR_C, BLUR_C), 0)
src_gray = cv.cvtColor(src_backup, cv.COLOR_BGR2GRAY)
#src_gray = src_backup

cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
abs_dst = cv.convertScaleAbs(dst)
cv.imwrite('{}/Rezult_Laplacian.png'.format(pathForToday),abs_dst)


"""""
ret, thresh = cv.threshold(abs_dst, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
cv.drawContours(abs_dst, contours, -1, (0,255,0), 3)


for cnt in contours:
    rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    box = np.int0(box) # округление координат
    cv.drawContours(abs_dst,[box],0,(255,0,0),2) # рисуем прямоугольник

cv.imwrite('Ready_Images/Countours2_Test.png',abs_dst);

"""""
f = open("Ready_Images/iteration.txt", "w")
iterationNumber += 1
f.write(str(iterationNumber))
f.close()
cv.waitKey()
cv.destroyAllWindows()
