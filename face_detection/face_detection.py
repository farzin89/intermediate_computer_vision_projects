
import cv2
import matplotlib.pyplot as plt
import os

cap = cv2.VideoCapture(0)
model=cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while True:

    ret,frame = cap.read()


    cv2.imshow('frame',frame)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllwindows()
