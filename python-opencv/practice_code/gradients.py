import cv2 as cv
import numpy as np

img = cv.imread('python-opencv/Image_Video/pingpong.JPG')
cv.imshow('pingpong', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('SObel x', sobelx)
cv.imshow('Sobel y', sobely)
cv.imshow('Combined sobel', combined_sobel)

Canny = cv.Canny(gray, 150, 175)
cv.imshow('Canny', Canny)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break