# vee dee oh, in a while loop.
import cv2
import time

video = cv2.VideoCapture(0)     # [#] for webcam number, or a pass in a file name to play a video
current_frame = 1


while True:

    current_frame += 1
    check, frame = video.read()     # video is a stream of data so it needs to be 'read' // check = boolean, frame = object

    print check
    print frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Video frame ', gray)

    #1000/frame rate: 30fps = 33ms wait, 60fps = 16.67ms wait.
    key = cv2.waitKey(1000/15)

    if key == ord('q'):
        break   # releases us from the while loop.

print 'Number of frames iterated through: ' + str(current_frame)
cv2.destroyAllWindows()
video.release()     # release the camera at the endq
