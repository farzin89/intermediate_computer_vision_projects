import cv2
import os
from pyzbar.pyzbar import decode

input_dir = 'Capture.JPG'
img = cv2.imread(input_dir)
qr_info = decode(img)
print(qr_info)


