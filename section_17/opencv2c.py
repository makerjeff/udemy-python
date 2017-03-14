#Face Detection 2c, lets get face, then find eyes inside face.

import cv2

# load files and convert to BW
face_cascade = cv2.CascadeClassifier('cascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('cascades/haarcascade_eye.xml')
img = cv2.imread('images/family.jpg')
gr = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  #try others, see what it ends up looking like.

# do face detection
faces = face_cascade.detectMultiScale(gr, scaleFactor=1.2, minNeighbors=5)
# can also be (gr, 1.2, 5)

print faces
print 'faces detected: '
print len(faces)

for (x,y,w,h) in faces:
    img = cv2.rectangle(img, (x,y), (x+w, y+h), (0,255,0), 4)

    # array splicing: [start:end, start:end] = essentially creates block of ROI pixels.
    # also goes rows, then columns (essentially flipped x and y for CV2.
    roi_gr = gr[y: y+h, x: x+w]
    roi_color = img[y: y+h, x: x+w]

    eyes = eye_cascade.detectMultiScale(roi_gr, 1.05, 5)

    print eyes
    print 'eyes detected: '
    print len(eyes)

    for (ex, ey, ew, eh) in eyes:
        cv2.rectangle(roi_color, (ex, ey), (ex+ew, ey+eh), (0,0,255), 2)



cv2.imshow('faces', img)
cv2.waitKey(0)
cv2.destroyAllWindows()


