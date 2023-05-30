import cv2 as cv


img = cv.imread('python-opencv/Image_Video/pingpong.JPG')
cv.imshow('pingpong', img)

# Averaging 
average = cv.blur(img, (30,30))
cv.imshow('Average Blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (15,15), 0)
cv.imshow('gaussian', gauss)

# Median blur
median = cv.medianBlur(img, 15)
cv.imshow('Median', median)

# Bilateral blur
bilateral = cv.bilateralFilter(img, 5, 30, 30)
cv.imshow('Bilateral', bilateral)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break