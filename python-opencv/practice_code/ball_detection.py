import cv2 as cv
import numpy as np

videoCap = cv.VideoCapture(0)
# previous circle
prevCircle = None

# calculate the frame of circle (coordinate)
dist = lambda x1, y1, x2, y2: (x1-x2)**2+(y1-y2)**2

while True:
    ret, frame = videoCap.read()
    if not ret: break
    
    # change to gray color space
    grayFrame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    # reduce the noise (make video blur)
    blurFrame = cv.GaussianBlur(grayFrame, (17,17), 0)
    
    #  find the circle
    circles = cv.HoughCircles(blurFrame, cv.HOUGH_GRADIENT, 1.2, 50, param1=150, param2=50, minRadius=10, maxRadius=500)
    
    # check if there is circle in video and draw it 
    if circles is not None:
        circles = np.uint16(np.around(circles))
        chosen = None
        for i in circles[0, :]: 
            if chosen is None: chosen = i
            if prevCircle is not None:
                if dist(chosen[0], chosen[1], prevCircle[0], prevCircle[1]) <= dist(i[0], i[1], prevCircle[0], prevCircle[1]):
                    chosen = i
        cv.circle(frame, (chosen[0], chosen[1]), 1, (0, 100, 100), 3)
        cv.circle(frame, (chosen[0], chosen[1]), chosen[2], (255,0,255), 3)
        prevCircle = chosen
        
    cv.imshow('circles', frame)
    
    if cv.waitKey(1) & 0xFF == ord('q'): break

videoCap.release()
cv.destroyAllWindows()