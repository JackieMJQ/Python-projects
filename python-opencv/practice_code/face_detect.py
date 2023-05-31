import cv2 as cv

img = cv.imread('python-opencv/Image_Video/kyrie.jpg')
cv.imshow('kyrie', img)

# Convert image to Grayscale
# Haar_face.xml try to use contour to recognize if it's a face or not
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray person', gray)

# read xml
haar_cascade = cv.CascadeClassifier('python-opencv/practice_code/haar_face.xml')

# detect face
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

# grab coordinates of image and draw a rectangle
for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=3)
    
cv.imshow('Detected faces', img)

print(f'Number of faces found = {len(faces_rect)}')


while True:
    if cv.waitKey(1) & 0xFF == ord('q'):
        break