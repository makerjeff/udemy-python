# vee dee oh
import cv2
import time

video = cv2.VideoCapture(1)     # [#] for webcam number, or a pass in a file name to play a video
check, frame = video.read()     # video is a stream of data so it needs to be 'read' // check = boolean, frame = object

print check
print frame


time.sleep(3)
gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

cv2.imshow('Video frame ', gray)

cv2.waitKey(0)
cv2.destroyAllWindows()
video.release()     # release the camera at the endq
