import cv2
import time

video = cv2.VideoCapture(0)

current_frame = 0

while True:
    current_frame += 1

    check, frame = video.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('Capturing', gray)
    print gray

    if cv2.waitKey(1000/15) & 0xFF == ord('q'):
        break

print current_frame

video.release()
cv2.destroyAllWindows()