# pip install opencv-python

import cv2
face_cascade=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# capture video file ,you are also use webcam ,that time us -
# cap = cv2.VideoCapture(0) -> 0 for laptop and 1 for extra webcam

cap = cv2.VideoCapture('video.mp4')

while True:
    # read the frame
    _, vid = cap.read()
    gray=cv2.cvtColor( vid, cv2.COLOR_BGR2GRAY)
    
    # detect the faces
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)
    
    # draw rectangle on face
    for (x, y, w, h) in faces:
             cv2.rectangle(vid, (x, y), (x + w, y + h), (55, 50, 255), 2)
        
    # display video
    cv2.imshow('Face Detection', vid)
    
    # press Esc for close window
    k= cv2.waitKey(33) & 0xff
    if k==27:
     break

cap.release()
