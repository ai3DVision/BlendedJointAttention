#Cross spread implemetation

import cv2
import numpy as np
import dlib 

def process_eye(split):
	split = cv2.GaussianBlur(split,(5,5),0)
	split = cv2.adaptiveThreshold(split,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,2)
	split = cv2.dilate(split, None, iterations=1)
	return split

def filter(split):
	split = cv2.medianBlur(split,5)
	split = cv2.bilateralFilter(split,9,75,75)
	return split
# Video capture via webcam
cam = cv2.VideoCapture(-1)
cam.set(3,640)
cam.set(4,480)
video_capture = cam

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('../dlibcascades/shape_predictor_68_face_landmarks.dat')


while True:
    # Capture frame-by-frame
	ret, frame = video_capture.read()
	if ret:
		frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
		dets = detector(frame, 1)
		for k, d in enumerate(dets):
	        # Get the landmarks/parts for the face in box d.
			shape = predictor(frame, d)
	        # print(type(shape.part(1).x))
			cv2.circle(frame,(shape.part(36).x,shape.part(36).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(39).x,shape.part(39).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(42).x,shape.part(42).y),2,(0,0,255))
			cv2.circle(frame,(shape.part(45).x,shape.part(45).y),2,(0,0,255))
			x1 = shape.part(36).x-10
			y1 = shape.part(37).y-10
			x2 = shape.part(39).x+10
			y2 = shape.part(40).y+10
			split = frame[y1:y2,x1:x2]
			split = process_eye(split)
			frame[y1:y2,x1:x2]=split
			cv2.rectangle(frame,(x1,y1), (x2,y2), (0, 0, 255), 2)
			x1 = shape.part(42).x-10
			y1 = shape.part(43).y-10
			x2 = shape.part(45).x+10
			y2 = shape.part(46).y+10
			split = frame[y1:y2,x1:x2]
			split = process_eye(split)
			frame[y1:y2,x1:x2]=split
			cv2.rectangle(frame,(x1,y1), (x2,y2), (0, 0, 255), 2)
		
		# Display the resulting frame
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
# Release video capture
video_capture.release()
cv2.destroyAllWindows()