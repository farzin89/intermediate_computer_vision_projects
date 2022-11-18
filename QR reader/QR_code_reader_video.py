import os
import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()

    cv2.imshow('webcam',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()