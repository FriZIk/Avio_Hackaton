import cv2 as cv
import numpy as np


scale = 1
delta = 0
ddepth = cv.CV_16S

src = cv.imread("Default_Images/test.png", cv.IMREAD_COLOR)
src_backup = src
frame = src
BLUR_C = 3

img = src

result = cv.cvtColor(img, cv.COLOR_BGR2LAB)
avg_a = np.average(result[:, :, 1])
avg_b = np.average(result[:, :, 2])
result[:, :, 1] = result[:, :, 1] - ((avg_a - 128) * (result[:, :, 0] / 255.0) * 1.1)
result[:, :, 2] = result[:, :, 2] - ((avg_b - 128) * (result[:, :, 0] / 255.0) * 1.1)
result = cv.cvtColor(result, cv.COLOR_LAB2BGR)

img = result
hsv_min = np.array((0, 54, 5), np.uint8)
hsv_max = np.array((187, 255, 253), np.uint8)

hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)  # меняем цветовую модель с BGR на HSV
thresh = cv.inRange(hsv, hsv_min, hsv_max)  # применяем цветовой фильтр
contours0, hierarchy = cv.findContours(thresh.copy(), cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

# перебираем все найденные контуры в цикле
for cnt in contours0:
    rect = cv.minAreaRect(cnt)  # пытаемся вписать прямоугольник
    box = cv.boxPoints(rect)  # поиск четырех вершин прямоугольника
    box = np.int0(box)  # округление координат
    cv.drawContours(img, [box], 0, (255, 0, 0), 2)  # рисуем прямоугольник

cv.imshow('contours', img)  # вывод обработанного кадра в окно

cv.waitKey()
cv.destroyAllWindows()










"""""
res = src
final = cv.cvtColor(res, cv.COLOR_BGR2LAB)

avg_a = -np.average(final[:,:,1])
avg_b = -np.average(final[:,:,2])

for x in range(final.shape[0]):
    for y in range(final.shape[1]):
        l,a,b = final[x][y]
        shift_a = avg_a * (l/100.0) * 1.1
        shift_b = avg_b * (l/100.0) * 1.1
        final[x][y][1] = a + shift_a
        final[x][y][2] = b + shift_b

final = cv.cvtColor(final, cv.COLOR_LAB2BGR)
final = np.hstack((res, final))
"""""
cv.imwrite('Ready_Images/Balanced.png', result)