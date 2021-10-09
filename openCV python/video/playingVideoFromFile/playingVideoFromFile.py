import numpy as np
import cv2 as cv

#cap = cv.VideoCapture('testNS.mp4')  #this line doesn't work. I think it may be path problem
cap = cv.VideoCapture('E:/MyPractiseZone/openCV/openCV python/video/video_file/testNS.mp4')

#Below commented code are not work . It cause isOpened() function always return false.
#if not cap.isOpened():
    #print("Cannot open camera")
    #exit()

#while(cap.isOpened):
    #isTrue,frame = cap.read()
    #cv.imshow('Video', frame)

    #if cv.waitKey(25) & 0xFF==ord('d'):
        #break

while True:
    isTrue,frame = cap.read()
    cv.imshow('Video', frame)

    if cv.waitKey(25) & 0xFF==ord('d'):
        break

cap.release()
cv.destroyAllWindows()