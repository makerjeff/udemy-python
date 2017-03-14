#Face Detection

import cv2

face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
img = cv2.imread('images/news.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# do the face detection
faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors = 5)

print type(faces)
print faces
print len(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 5)

resized = cv2.resize(img, (img.shape[1]/3, img.shape[0]/3))

# END PLATE
cv2.imshow('resized face image', resized)
cv2.waitKey(0)
cv2.destroyAllWindows()