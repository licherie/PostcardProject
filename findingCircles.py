import cv2
import numpy as np
for i in range(666,667):
    myPATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(i) + "Back.jpg"
    img = cv2.imread(myPATH,0)
    if img is not None:
        img = cv2.medianBlur(img,5)
        height, width = img.shape
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        #strategy: first set most generous parameters, try to find circles. If not circles found return none. If 1-4 circles found, return this.
        #If more than 4 circles found, make parameters more restrictive
        minDist = 200
        minimumRadius = 100
        maximumRadius = 300
        parameter2 = 80
        parameter1 = 100
        initialGuess = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
        maxRadius = maximumRadius)
        #we want to start with the most restrictive and decrease until we have circles
        #or no improvement in number of circles
        #first we check that it is not none or one of the errors
        if initialGuess is not None and (np.size(initialGuess) != 4 and initialGuess[0][0][0] != 0):
                #if some circles were found, then we will start with largest distance between circle centers,
                #keeping in mind our goal is to find the minimum number of circles that isn't 0
                bestDist = 700
                #set minimum so far to the current number of circles found
                bestCircles = np.shape(initialGuess)[1]
                circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,bestDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
            maxRadius = maximumRadius)
                #if circles is None, we want to run loop until distance is decreased enough until there appears some circle
                #also, if when circles are found, this is not less than bestCircles, then we just want to stop the loop as this means decreasing is no use
                while((circles is None or np.size(circles) == 4  or circles[0][0][0] == 0 ) and bestDist > 50):
                    bestDist = bestDist / 2
                    circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,bestDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
            maxRadius = maximumRadius)
                    #following line will exit loop if the number is greater than the number of circles already found
                    if np.shape(circles)[1] >= bestCircles:
                        bestDist = 50
                print(bestDist)
        else:
            circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
                                    maxRadius = maximumRadius)
            while parameter1 >= 60 and (circles is None or np.size(circles) == 4 or circles[0][0][0] == 0):
                while parameter2 >= 60:
                   parameter2 = parameter2 - 10
                   minimumRadius = 40
                   while minimumRadius <= 100:
                        maximumRadius = minimumRadius + 100
                        circles = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,1,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
                                    maxRadius = maximumRadius)
                        minimumRadius = minimumRadius + 10
                parameter2 = 80
                parameter1 = parameter1 - 10

                
        if circles is not None:
            for j in circles[0,:]:
            # draw the outer circle
                cv2.circle(cimg,(j[0],j[1]),j[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(cimg,(j[0],j[1]),2,(0,0,255),3)
            cv2.imshow('detected circles',cimg)
            print(str(i))
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            mySavePATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(i) + "BackChecked.jpg"
            cv2.imwrite(mySavePATH,cimg)
