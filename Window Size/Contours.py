import cv2
import sys
import numpy as np
from matplotlib import pyplot as plt

# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    if ret:

    	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    	frame = cv2.Canny(gray,100,90)
    	contours = cv2.findContours(frame,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
    	cv2.drawContours(frame, contours, -1, (0,255,0), 3)

		cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()
