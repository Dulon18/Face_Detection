# pip install opencv-python

import cv2
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

img=cv2.imread('image.png')

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#Detect faces
faces=face_cascade.detectMultiScale(gray,1.1,4)

# draw rectangle in face
for(x,y,w,h) in faces:
       cv2.rectangle(img,(x,y),(x+w ,y+h),(55,50,255),2)
    
#display image
cv2.imshow('Face Detection',img)
cv2.waitKey()
