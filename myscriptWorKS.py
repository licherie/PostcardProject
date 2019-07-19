import cv2
import numpy as np
myPATH = "C://Users//SEAB//Desktop//postcardImages//" + "postcard" + str(2) + "Back.jpg"
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
#we want to start with the most restrictive and drop it down liKE it's HOT like it's HOT lmao until we have none circles
#or no improvement
#first we check that it is not none or one of the errors 
if circles is not None and (np.size(circles) != 4 and circles[0][0][0] != 0):
    #if some circles were found, then we will start with largest distance between circle centers,
    #keeping in mind our goal is to find the minimum number of circles that isn't 0 
    bestDist = 700
    #set minimum so far to the current number of circles found
    bestCircles = np.shape(circles)[1]
    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,bestDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
maxRadius = maximumRadius)
    #if circles is None, we want to run loop until distance is decreased enough until there appears some circle
    #also, if when circles are found, this is not less than bestCircles, then we just want to stop the loop as this means decreasing is no use
    while((circles is None or np.size(circles) == 4  or circles[0][0][0] == 0 ) and bestDist > 50):
        bestDist = bestDist / 2
        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,bestDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
maxRadius = maximumRadius)
        if np.shape(circles)[1] >= bestCircles:
            bestDist = 50
    #when while loop ends, this means that either 
if circles is not None: 
    for j in circles[0,:]:
    # draw the outer circle
        cv2.circle(cimg,(j[0],j[1]),j[2],(0,255,0),2)
    # draw the center of the circle
        cv2.circle(cimg,(j[0],j[1]),2,(0,0,255),3)
    cv2.imshow('detected circles',cimg)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
