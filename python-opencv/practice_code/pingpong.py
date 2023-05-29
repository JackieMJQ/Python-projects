# import cv2
# import numpy as np

# # Initialize video capture from default camera
# cap = cv2.VideoCapture(0)

# # Define lower and upper boundaries for the ball color in HSV color space
# white_lower = np.array([0, 0, 200])  # Lower boundary for white in HSV
# white_upper = np.array([179, 50, 255])  # Upper boundary for white in HSV

# while True:
#     # Read frame from video capture
#     ret, frame = cap.read()
    
#     # Convert frame to rgb color space
#     hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    
#     # Threshold the frame to extract the ball color
#     mask = cv2.inRange(hsv, white_lower, white_upper)
    
#     # Perform morphological operations to remove noise and improve detection
#     mask = cv2.erode(mask, None, iterations=2)
#     mask = cv2.dilate(mask, None, iterations=2)
    
#     # Find contours of the ball
#     contours, _ = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Check if any contours are found
#     if len(contours) > 0:
#         # Find the largest contour (assumed to be the ball)
#         ball_contour = max(contours, key=cv2.contourArea)
        
#         # Get the bounding rectangle of the contour
#         x, y, w, h = cv2.boundingRect(ball_contour)
        
#         # Draw a rectangle around the ball
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     # Display the resulting frame
#     cv2.imshow('Ping Pong Ball Tracking', frame)
    
#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all windows
# cap.release()
# cv2.destroyAllWindows()

# import cv2
# import numpy as np

# # Initialize video capture from default camera
# cap = cv2.VideoCapture(0)

# while True:
#     # Read frame from video capture
#     ret, frame = cap.read()

#     # Convert frame to grayscale
#     gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
#     # Apply Gaussian blur to reduce noise
#     blurred = cv2.GaussianBlur(gray, (15, 15), 0)
    
#     # Apply adaptive thresholding to segment the ball
#     _, threshold = cv2.threshold(blurred, 220, 255, cv2.THRESH_BINARY)
    
#     # Perform morphological operations to remove noise
#     morphed = cv2.morphologyEx(threshold, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
#     morphed = cv2.morphologyEx(morphed, cv2.MORPH_CLOSE, np.ones((20, 20), np.uint8))
    
#     # Find contours of the ball
#     contours, _ = cv2.findContours(morphed.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
#     # Check if any contours are found
#     if len(contours) > 0:
#         # Find the largest contour (assumed to be the ball)
#         ball_contour = max(contours, key=cv2.contourArea)
        
#         # Get the bounding rectangle of the contour
#         x, y, w, h = cv2.boundingRect(ball_contour)
        
#         # Draw a rectangle around the ball
#         cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
    
#     # Display the resulting frame
#     cv2.imshow('White Ping Pong Ball Tracking', frame)
    
#     # Exit the loop if 'q' is pressed
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break

# # Release the video capture and close all windows
# cap.release()
# cv2.destroyAllWindows()
