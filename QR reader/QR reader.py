import cv2
import os
from pyzbar.pyzbar import decode
import numpy as np
import matplotlib.pyplot as plt
input_dir = 'Capture.JPG'
img = cv2.imread(input_dir)
qr_info = decode(img)
print(qr_info)

data = qr_info.data
rect = qr_info.rect
polygon = qr_info.polygon

print(data)
print(rect)
print(polygon)
img = cv2.rectangle(img, (rect.left, rect.top), (rect.left + rect.width, rect.top + rect.height),
                            (0, 255, 0), 5)
img = cv2.polylines(img, [np.array(polygon)], True, (255, 0, 0), 5)

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.show()
