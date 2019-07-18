import cv2
import numpy as np
myPATH = "C://Users//SEAB//Desktop//postcardImages//" + "postcard" + str(17) + "Back.jpg"
img = cv2.imread(myPATH,0)
img = cv2.medianBlur(img,5)
cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
#strategy: first set most generous parameters, try to find circles. If not circles found return none. If 1-4 circles found, return this.
#If more than 4 circles found, make parameters tigether.
minDist = 50
minimumRadius = 40
maximumRadius = 300
parameter2 = 90
parameter1 = 100
circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
maxRadius = maximumRadius)
if circles is not None and (np.size(circles) != 4 and circles[0][0][0] != 0):
    bestDist = 700
    bestCircles = np.shape(circles)[1]
    maxDist = bestDist
    while((np.shape(circles)[1] > 2 or circles is None) and (maxDist >= 25)):
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
        maxRadius = maximumRadius)
        print(circles, maxDist)
        if np.shape(circles)[1] < bestCircles:
            bestDist = maxDist
            bestCircles = np.shape(circles)[1]
        maxDist = maxDist/2

if circles is not None: 
    for j in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(j[0],j[1]),j[2],(0,255,0),2)
    # draw the center of the circle
        cv2.circle(cimg,(j[0],j[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
