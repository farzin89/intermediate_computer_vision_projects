import os
import cv2
import numpy as np
from keras.models import model_from_json
from keras_preprocessing import image

# load model
model = model_from_json(open("fer.json","r").read())
#load weight
model.load_weights('fer.h5')
# load face detection model
face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

