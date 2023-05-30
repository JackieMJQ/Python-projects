import cv2 as cv
import numpy as np

img = cv.imread('python-opencv/Image_Video/pingpong.JPG')
cv.imshow('pingpong', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank image', blank)

mask = cv.circle(blank, (img.shape[1]//2 + 45, img.shape[0]//2 + 150), 400,255,-1)
cv.imshow('Mask', mask)

masked = cv.bitwise_and(img, img, mask=mask)
cv.imshow('Masked', masked)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break