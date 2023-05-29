import cv2 as cv

# img = cv.imread('Image_Video/IMG_9497.JPG')
# cv.imshow(img)

def rescaleFrame(frame, scale=0.75):
    # work for image, video, live video
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimensions = (width, height)
    
    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

def changeRes(width, height):
    # live video
    capture.set(3, width)
    capture.set(4, height)

# reading videos
capture = cv.VideoCapture('./Image_Video/IMG_9525.MOV')

while True:
    isTrue, frame = capture.read()
    frame_resized = rescaleFrame(frame, scale=.2)
    cv.imshow('Video', frame)
    cv.imshow('video resized', frame_resized)
    
    if cv.waitKey(20) & 0xFF == ord('d'):
        break
    
capture.release()
cv.destroyAllWindows()
    
cv.waitKey(0)