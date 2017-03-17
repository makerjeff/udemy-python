# http://docs.opencv.org/3.0-beta/doc/py_tutorials/py_feature2d/py_features_harris/py_features_harris.html#harris-corners

import cv2
import numpy as np

filename = 'checkerboard.jpg'
img = cv2.imread(filename)
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = np.float32(gray)
dst = cv2.cornerHarris(gray, 2, 3, 0.04)

# result is dialated for marking the corners (not important)
dst = cv2.dilate(dst, None)

# thresholding image for optimal value, depends on the image
img[dst > 0.01 * dst.max()] = [0,0,255]

cv2.imshow('dst', img)

if cv2.waitKey(0) & 0xff == 27:
    cv2.destroyAllWindows()