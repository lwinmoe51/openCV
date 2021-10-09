import numpy as np
import cv2 as cv

cap = cv.VideoCapture('E:/MyPractiseZone/openCV/openCV python/video/video_file/testNS.mp4')

while True:
    isTrue,frame = cap.read()
    cv.imshow('Video', frame)

    if cv.waitKey(25) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()