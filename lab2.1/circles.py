import matplotlib.image as mpimg 
import matplotlib.pyplot as plt 
import numpy as np
import imgaug.augmenters as iaa
import cv2
import statistics
import pandas as pd
import math

dic = "circles"
files = [str(dic + "/" + x) for x in ["circles.png", "circles_blur.png", "circles_diff.png", "circles_noise.png", "circles_elipsa.png", "circles_scale.png", "circles_cross.png"]]

img = cv2.imread('circles.png',0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)

circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,20,
                            param1=100,param2=100,minRadius=0,maxRadius=0)

circles = np.uint16(np.around(circles))
for i in circles[0,:]:
    # draw the outer circle
    cv2.circle(cimg,(i[0],i[1]),i[2],(0,255,0),2)
    # draw the center of the circle
    cv2.circle(cimg,(i[0],i[1]),2,(0,0,255),3)

cv2.imshow('detected circles',cimg)
cv2.waitKey(0)
cv2.destroyAllWindows()