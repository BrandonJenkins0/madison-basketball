# Importing modules
import cv2
import math
import matplotlib.pyplot as plt
import pandas as pd
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input, VGG16
import numpy as np
from keras.utils import np_utils
from skimage.transform import resize
from sklearn.model_selection import train_test_split
from keras.models import Sequential
from keras.layers import Dense, InputLayer, Dropout

# Saving videos as pictures
count = 0
videoFile = 'data/thunderridge_at_madison.mp4'
cap = cv2.VideoCapture(videoFile)
frameRate = cap.get(5)
x = 1

while cap.isOpened():
    frameId = cap.get(1)
    ret, frame = cap.read()
    if ret == False:
        break
    if frameId % math.floor(frameRate) == 0:
        filename = 'photos/frame{}.jpg'.format(count)
        count += 1
        cv2.imwrite(filename, frame)
cap.release()
print("Done baby!")

# Did it work
img = cv2.imread('photos/frame290.jpg')
plt.imshow(img)
plt.show()

