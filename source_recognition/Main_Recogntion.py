import cv2 as cv
import numpy as np
window_name = ('Sobel Demo - Simple Edge Detector')
scale = 1 
delta = 0 
ddepth = cv.CV_16S

src = cv.imread("Default_Images/test.png", cv.IMREAD_COLOR)
src_backup = src


# Sobel operator test
src = cv.GaussianBlur(src, (3, 3), 0)
gray = cv.cvtColor(src, cv.COLOR_BGR2GRAY)
grad_x = cv.Sobel(gray, ddepth, 1, 0, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
grad_y = cv.Sobel(gray, ddepth, 0, 1, ksize=3, scale=scale, delta=delta, borderType=cv.BORDER_DEFAULT)
abs_grad_x = cv.convertScaleAbs(grad_x)
abs_grad_y = cv.convertScaleAbs(grad_y)
grad = cv.addWeighted(abs_grad_x, 0.5, abs_grad_y, 0.5, 0)
cv.imwrite('Ready_Images/Rezult_Sobel.png',grad)

ret, thresh = cv.threshold(gray, 127, 255, 0)
contours, hierarchy = cv.findContours(thresh, cv.RETR_TREE, cv.CHAIN_APPROX_NONE)

cv.drawContours(gray, contours, -1, (0,255,0), 3)

# Remove noise




for cnt in contours:
    rect = cv.minAreaRect(cnt) # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect) # поиск четырех вершин прямоугольника
    box = np.int0(box) # округление координат
    cv.drawContours(gray,[box],0,(255,0,0),2) # рисуем прямоугольник


cv.imwrite('Ready_Images/Countours_Test.png',gray);
#cv.imshow(window_name, grad)


# Laplasian operator test
kernel_size = 3
src_backup = cv.GaussianBlur(src_backup, (3, 3), 0)
src_gray = cv.cvtColor(src_backup, cv.COLOR_BGR2GRAY)
cv.namedWindow(window_name, cv.WINDOW_AUTOSIZE)
dst = cv.Laplacian(src_gray, ddepth, ksize=kernel_size)
abs_dst = cv.convertScaleAbs(dst)
cv.imwrite('Ready_Images/Rezult_Laplacian.png',abs_dst)

cv.destroyAllWindows()