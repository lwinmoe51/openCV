import cv2 as cv
import sys

#both line work
img = cv.imread(cv.samples.findFile("lwintest.jpg"))
#img = cv.imread("lwintest.jpg")

if img is None:
    sys.exit("Could not read the image.")

cv.imshow("Display windown", img)

k = cv.waitKey(0)

if k==ord("s"):
    cv.imwrite("lwintest.jpg", img)
