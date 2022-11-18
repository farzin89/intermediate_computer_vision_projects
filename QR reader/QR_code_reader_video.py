import os
import cv2
from pyzbar.pyzbar import decode
import matplotlib.pyplot as plt
import numpy as np

cap = cv2.VideoCapture(0)

while True:

    ret,frame = cap.read()

    cv2.imshow('webcam',frame)

    qr_info = decode(frame)

    if len(qr_info) > 0:

        qr = qr_info[0]
        data = qr.data
        rect = qr.rect
        polygon = qr.polygon
        

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()