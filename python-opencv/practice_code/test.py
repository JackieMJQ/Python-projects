# Import library
import numpy as np
import cv2 as cv
import time

# Video Capture
cap = cv.VideoCapture('python-opencv/Image_Video/Video_Tracking.mp4')
# cap = cv.VideoCapture('Table Tennis Ball.mp4')
if not cap.isOpened():
    print("Cannot open camera")
    exit()

# Set up colors for bounding box and Text
red = (0,0,255)
blue = (255,0,0)
green = (0,255,0)
yellow = (0,255,255)

# Setup object tracking or object detection mode
detection_mode = 1

# Set up max tracking frame
max_tracking_frame  = 20
count_tracking_frame  = 0

# Set up fps
fps = 30
prev = 0

# Set up HSV
# low_thres = (0, 0, 200)
# high_thres = (11,100,141)
# high_thres = (180, 50, 255)

# yellow ball
low_thres = (11, 60,141)
high_thres = (30,255,255)

# Create function to draw bounding box and put label
def boundingBox_putText(input_frame, box_color, index, first_point, second_point):
    # Draw bounding box and put label
    cv.rectangle(input_frame, first_point, second_point, box_color, 2)
    cv.putText(input_frame,'B ' + str(index+1), first_point, cv.FONT_HERSHEY_COMPLEX_SMALL, 1, green, 1)

# Create function to process hsv 
def hsv_processing(input_frame, low_thres, high_thres):
    # Gaussian filter
    gauss_filter = cv.GaussianBlur(input_frame, (3,3), 0)
    # Convert bgr to hsv
    hsv = cv.cvtColor(gauss_filter, cv.COLOR_BGR2HSV)
    # Binarize the img using HSV color space
    hsv_binary = cv.inRange(hsv, low_thres, high_thres)
    
    return hsv_binary

# Create function to process noise
def noise_processing(input_frame):
    # Create kernel
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(5,5))
    # Remove noise
    out = cv.morphologyEx(input_frame, cv.MORPH_OPEN, kernel, iterations=2)
    # Fill Small Hold Noise
    out = cv.morphologyEx(out, cv.MORPH_CLOSE, kernel, iterations=4)
    
    return out

# Create a function to find contours
def findContours_processing(input_frame, ball_rois_list):
    contour, hierachy = cv.findContours(input_frame, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    # detect circle
    min_radius = 15
    max_radius = 42
    for index, cnt in enumerate(contour):  
        # Find radius
        (x,y),radius = cv.minEnclosingCircle(cnt)
        radius = int(radius)
        if (radius > min_radius) and (radius < max_radius):
            ball = cv.boundingRect(cnt)
            # Get x,y,w,h
            first_point = (int(ball[0]), int(ball[1]))
            second_point = (int(ball[0]+ball[2]), int(ball[1]+ball[3]))
            # Add x,y,w,h contour to list
            ball_rois_list.append(ball)
            # Draw bounding box = red color and Text = green color
            boundingBox_putText(frame, red, index, first_point, second_point)

    return ball_rois_list

while True:
    timeElapsed = time.time() - prev
    if timeElapsed > 1./fps:
        prev = time.time()
        # Capture frame-by-frame
        ret, frame = cap.read()
        ball_rois_list = []
        
        if detection_mode == 1: # Turn on detect
            # Process hsv color
            hsv_work = hsv_processing(frame, low_thres, high_thres)
            
            # Process noise
            noise_rmv = noise_processing(hsv_work)
            
            # Find contour area
            ball_detection = findContours_processing(noise_rmv,ball_rois_list)  
            
            # Create multi tracker
            multi_trackers = cv.legacy.MultiTracker_create()
            
            # Initialize tracker
            for ball_roi in ball_detection:
                multi_trackers.add(cv.legacy.TrackerCSRT_create(), frame, ball_roi)

            # Turn off object detection and turn on object tracking
            detection_mode = 0
                
        else: # Turn on tracking
            # Set max number of tracking frame
            if count_tracking_frame == max_tracking_frame:
                detection_mode = 1
                count_tracking_frame = 0
            
            # Update tracker
            ret, objs = multi_trackers.update(frame)
            if ret:
                for index, obj in enumerate(objs):
                    # Check the size of w and h if they are not equal, back to detection mode
                    if((float(obj[2])/float(obj[3])) < 0.93 or (float(obj[2])/float(obj[3])) > 1.36):
                        # print('tracking fail')
                        detection_mode = 1
                    else:
                        # Get x,y,w,h
                        first_point = (int(obj[0]), int(obj[1]))
                        second_point = (int(obj[0]+obj[2]), int(obj[1]+obj[3]))
                        # Draw bounding box and put label
                        boundingBox_putText(frame, blue, index, first_point, second_point)
                
            else:
                # print('tracking fail')
                detection_mode = 1
            
            # Count tracking frame
            count_tracking_frame += 1
        
        # Note on the corner of the screen
        cv.putText(frame,'Blue: Tracking ', (700,20), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, blue, 1)
        cv.putText(frame,'Red:  Detection ', (700,45), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, red, 1)
        cv.putText(frame,f'Tracking_Frame: {max_tracking_frame}', (700,70), cv.FONT_HERSHEY_COMPLEX_SMALL, 1, yellow, 1)
        
        
        # Display the resulting frame
        cv.imshow('Table Tennis Ball Tracking', frame)
        if cv.waitKey(1) == ord('q'):
            break
        
# When everything done, release the capture
cap.release()
cv.destroyAllWindows()