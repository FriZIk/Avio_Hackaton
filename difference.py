import cv2 as cv
import numpy as np
import os
window_name = ('Sobel Demo - Simple Edge Detector')
scale,delta = 1,0
ddepth = cv.CV_16S

#src = cv.imread('Ready_Images/Balanced.png', cv.IMREAD_COLOR)
src = cv.imread("Default_Images/.png", cv.IMREAD_COLOR)
src_backup = src
frame = src
BLUR_C,SOBEL_SIZE = 3,3

f = open("Ready_Images/iteration.txt", "r")
iterationNumber = int(f.read())
f.close()
os.makedirs("Ready_Images/{}".format(iterationNumber))
pathForToday = "Ready_Images/{}".format(iterationNumber)

src = cv.GaussianBlur(src, (BLUR_C, BLUR_C), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)

cv.imwrite('{}/GrayscaleBef.png'.format(pathForToday), gray)
weiSize,serSize,filStr = 7,7,12

gray = cv.fastNlMeansDenoising(gray, gray, weiSize, serSize, filStr)
cv.imwrite('{}/GrayscaleAftS{}F{}.png'.format(pathForToday, weiSize, filStr), gray)

lowThresh,highThresh = 100,300
note = open("{}/data.txt".format(pathForToday), "w")
note.write("Low thresh:{}\nHigh thresh:{}\n".format(lowThresh,highThresh))
note.close()

thresh = cv.Canny(gray, lowThresh, highThresh)
grad = gray
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE) # Изменить коэфициенты
cv.drawContours(grad, contours, -1, (0,255,0), 3) # Поиграться с коэфициентами

for cnt in contours:
    rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    box = np.int0(box) # округление координат
    cv.drawContours(grad,[box],0,(255,0,0),2) # Поиграться с коэфициентами

cv.imwrite('{}/Countours_TestB{}.png'.format(pathForToday, BLUR_C), grad)
f = open("Ready_Images/iteration.txt", "w")
iterationNumber += 1
f.write(str(iterationNumber))
f.close()
cv.waitKey()
cv.destroyAllWindows()
