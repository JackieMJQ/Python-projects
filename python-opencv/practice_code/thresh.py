import cv2 as cv


img = cv.imread('python-opencv/Image_Video/pingpong.JPG')
cv.imshow('pingpong', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# simple thresholding
threshold, thresh = cv.threshold(gray, 100, 255, cv.THRESH_BINARY)
cv.imshow('Simple Tresholded', thresh)

threshold, thresh_inv = cv.threshold(gray, 100, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Tresholded Inverse', thresh_inv)

# adaptive thresholding
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 1)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break