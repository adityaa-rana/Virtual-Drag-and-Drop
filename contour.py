import cv2 as cv
img=cv.imread('./cat.webp')

grayimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
cv.imshow("Gray",grayimg)
cannyimg=cv.Canny(img,125,175 )
cv.imshow("Canny",cannyimg)

contours,heirarchies=cv.findContours(cannyimg,cv.RETR_LIST,cv.CHAIN_APPROX_NONE)