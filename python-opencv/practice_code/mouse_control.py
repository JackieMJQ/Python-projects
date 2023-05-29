# control mouse
import cv2 as cv
import numpy as np

# must have 5 variable
# flags means combination of mouse event
def mouse_callback(event, x, y, flags, userdata):
    print(event, x, y, flags, userdata)
    if event == 2:
        cv.destroyAllWindows()

# create window
cv.namedWindow('mouse', cv.WINDOW_NORMAL)
cv.resizeWindow('mouse', 640, 360)

cv.setMouseCallback('mouse', mouse_callback, '123')

img = np.zeros((360, 640, 3), np.uint8)
while True:
    cv.imshow('mouse', img)
    key = cv.waitKey(1)
    if key == ord('q'):
        break
    
cv.destroyAllWindows()
