import cv2 as cv

img = cv.imread('Image_Video/IMG_9497.JPG')
cv.imshow('machine', img)

# converting to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
blur = cv.GaussianBlur(img, (7, 7), cv.BORDER_DEFAULT)
cv.imshow('blur', blur)

# Edge Cascade
cany = cv.Canny(blur, 125, 175)
cv.imshow('Canny', cany)

# Dilating the image
dilated = cv.dilate(cany, (3,3), iterations = 1)
cv.imshow('Dilate', dilated)

# Eroding
# eroded = cv.erode(dilated, (3,3), iterations=1)

# resize
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)