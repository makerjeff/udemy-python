#Face Detection 2b, experimentation: get eyes

import cv2
import numpy as np

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')

# lets find eyes first
img = cv2.imread('images/news.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.2, minNeighbors = 5)

print type(eyes)
print eyes
print len(eyes)

for (x,y,w,h) in eyes:
    cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 2)

cv2.imshow('eyes in picture', img)
cv2.waitKey(0)
cv2.destroyAllWindows()

