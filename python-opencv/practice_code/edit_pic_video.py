import cv2;

# reading images
# lena=cv2.imread("IMG_9497.JPG")
# cv2.imshow("image", lena)
# cv2.waitKey(0)

# reaing videos
# capture = cv2.VideoCapture('./Image_Video/IMG_9525.MOV')

# while True:
#     isTrue, frame = capture.read()
#     cv2.imshow('Video', frame)
    
#     if cv2.waitKey(20) & 0xFF == ord('d'):
#         break
    
# capture.release()
# cv2.destroyAllWindows()
    
# writing image
# cv2.namedWindow('img', cv2.WINDOW_NORMAL)
# cv2.resizeWindow('img', 640, 800)

# img = cv2.imread('IMG_9497.JPG')

# while True:
#     cv2.imshow('img', img)
#     key = cv2.waitKey(0)
    
#     if key == ord('q'):
#         break
#     # rewrite till machine.jpg
#     elif key == ord('s'):
#         cv2.imwrite('./machine.jpg', img)
#     else:
#         print(key)
        
# cv2.destroyAllWindows()

# open Camera
cv2.namedWindow('video', cv2.WINDOW_NORMAL)
cv2.resizeWindow('video', 640, 480)

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    
    cv2.imshow('video', frame)
    
    key = cv2.waitKey(10)
    if key == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()