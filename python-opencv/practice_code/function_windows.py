import cv2 as cv

# create windows
# its not allowed to change the size for window_autosize
cv.namedWindow('window', cv.WINDOW_NORMAL)

cv.resizeWindow('window', 800, 600)
cv.imshow('machine', 0)

# waitKey return ascii value
# key is int value, at least 16 bits, but ascii is 8-bit
key = cv.waitKey(0)
if key & 0xFF == ord('q'):
    print('destory window')
    cv.destroyAllWindows()