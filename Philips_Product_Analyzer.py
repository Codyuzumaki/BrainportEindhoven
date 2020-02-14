# -*- coding: utf-8 -*-
"""Philips_Item_Detection
Algorithm to clasify several Philips product images related to Brainport Eindhoven competition.

The images can be of any size, buy the algorithm was optimized to work with 4032x3024 images

This algorithm needs the file "Philips_model_v.3.7.h5" in the same folder, where the trained convolutional net is stored

The images to be clasified must be stored to a folder called "New_Images"

Victor Ramos Vicedo - 2020 © 
victorramos7@gmail.com
"""
# IMPORTS

import sys
import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import time
import cv2
from tensorflow.keras import models
import matplotlib.image as mpimg
import numpy as np

# IMAGE READING FUNCTION DEFINITION
def readImage( path , width , height ):
        img = mpimg.imread(path)
        if ((width!=0) & (height != 0)):
          img = cv2.resize(img, ( width , height ))
        return img

# IMAGE LISTING
path="/home/Philips/New_Images/"
listImages=os.listdir(path)
print(' ')
print('---------------------------------------')
print(' ')
print('Loading ' + str(len(listImages)) + ' images')
sys.stdout.flush()
time.sleep(.2)

# IMAGE READING
X = []
for im in listImages:
    X.append(readImage(path + im , 224 , 224 ))
X= np.array(X)
Xn=(X.astype(float)/255)
Xn=Xn-0.5
print(' ')
print('---------------------------------------')
print(' ')
print(str(len(listImages)) + ' images loaded')
print(' ')
print('---------------------------------------')
print(' ')
print('Analyzing...')
sys.stdout.flush()
time.sleep(.2)

# PRODUCT NAMES
Dict = {
  0: "shaver",
  1: "smart-baby-bottle",
  2: "wake-up-light",
  3: "toothbrush"
}

# MODEL LOAD
model=models.load_model("/home/Philips/Philips_model_v.3.7.h5", compile=False)

# PREDICTION
Res=model.predict(Xn)
Resultado=Res.argmax(1)

#RESULT
print(' ')
print('---------------------------------------')
print(' ')
print('IMAGE \t\t-\t RESULT')
print(' ')
for i in range(Xn.shape[0]):
  im=listImages[i]
  print(im[:-4] + '\t-\t' + Dict.get(Resultado[i]))

print(' ')
print('---------------------------------------')
print(' ')
print('Analysis completed')
print(' ')
print('---------------------------------------')
print(' ')