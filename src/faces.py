import numpy as np
import cv2

face_cascade = cv2.CascadeClassifier('cascades/data/haarcascade_frontalface_alt2.xml')
#This cascade works only with gray images, so we need to turn the image gray.
cap = cv2.VideoCapture(0)

while(True):
	#Capture frame-by-frame
	ret, frame = cap.read()
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = face_cascade.detectMultiScale(gray)
	#print(faces)
	for (x,y,w,h) in faces:
		print(x, y, w, h)
		roi_gray = gray[y:y+h, x:x+w]
		#Basically, x is where the face begins and w how much to go in right.
		#Same for vertical axis, y is where the face begins and h how much to go below.
		roi_color = frame[y:y+h, x:x+w]

		#Here's the part for recognition.

		img_item = 'my_image.png'
		cv2.imwrite(img_item,roi_color)

		color = (125, 255, 200) #BGR - Blue - Green - Red
		stroke = 2
		show = cv2.rectangle(frame, (x,y), (x+w, y+h), color, stroke)
	#Displaying the resulting frame
	cv2.imshow('frame', frame)

	if cv2.waitKey(20) & 0xFF == ord('q'):
		break

cap.release()
cap.destroyAllWindows()

