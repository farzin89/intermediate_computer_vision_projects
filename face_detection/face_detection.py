
import cv2
import matplotlib.pyplot as plt
import os

cap = cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret,frame = cap.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = model.detectMultiScale(gray,scaleFactor = 1.5,minNeighbors = 5)

    for face in faces:
        x,y,w,h = face
        img = cv2.rectangle(frame,(x,y),(x + w, y + h),(0,255,0),10)

        cv2.putText(frame,'face',(x,y-15),cv2.FONT_HERSHEY_COMPLEX,1,(150,150,50),2)







    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllwindows()
