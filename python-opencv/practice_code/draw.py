import cv2 as cv
import numpy as np

blank = np.zeros((500, 500, 3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. paint the image a certain color
# blank[200:300, 300:400] = 0,255,0
# cv.imshow('Green', blank)
# img = cv.imread('Image_Video/IMG_9497.JPG')
# cv.imshow(img)

# 2. draw a rectangle 
cv.rectangle(blank, (0,0), (250, 500), (0, 255, 0), thickness=cv.FILLED)
cv.imshow('Rectangle', blank)

# 3. Draw circle
cv.circle(blank, (250, 250), 40, (0,0,255), thickness=2)
cv.imshow('circle', blank)

# 4. Draw a line
cv.line(blank, (0, 0), (250, 250), (0,0,255), thickness=2)
cv.imshow('line', blank)

# 5. Write text
cv.putText(blank, 'Hello, my name is Jackie', (255, 255), cv.FONT_HERSHEY_TRIPLEX, 1.0, (0, 255, 0), thickness=2)
cv.imshow('Text', blank)


cv.waitKey(0)
