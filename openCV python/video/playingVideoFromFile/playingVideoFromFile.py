import numpy as np
import cv2 as cv

cap = cv.VideoCapture("E:\\MyPractiseZone\\openCV\\openCV python\\video\\playingVideoFromFile\\testNS.mp4")

if (cap.isOpened() == False):
    print("Error opening video file")


while (cap.isOpened()):
    ret,frame = cap.read()

    #if frame is read correctly ret is True
    if not ret:
        print("Can't receive frame (stream end?). Exiting...")
        break

    if ret == True:
        cv.imshow('Frame', frame)

    
    if cv.waitKey(0) & ord('q'):
        break
    else:
        break
cap.release()
cv.destroyAllWindows()