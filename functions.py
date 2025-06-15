#converting image to grayscale
import cv2 as cv
img=cv.imread('./cat.webp')
# cv.imshow('CAT',img)

grayimg=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
# cv.imshow("Gray",grayimg)
# cv.waitKey(0)

#bluring the image
blurimg=cv.GaussianBlur(img,(9,9 ),cv.BORDER_DEFAULT)

#increasee the odd number tuple value to increase the blur in the image
# cv.imshow("Blurred",blurimg)
# cv.waitKey(0)

# finding the edges of the objects in the image
# borderedimg=cv.Canny(img,125,175 )
# cv.imshow("borders",borderedimg)
# cv.waitKey(0)

# resizing image 
# resized=cv.resize(img,(800,500),interpolation=cv.INTER_AREA)
# cv.imshow("resized",resized)

# cropped=img[50:200 ,200:400]
# cv.imshow("cropped",cropped)
# cv.waitKey(0)


