import cv2
import numpy as np
def findCircles(number):
    myPATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(number) + "Back.jpg"
    img = cv2.imread(myPATH,0)
    if img is not None:
        img = cv2.medianBlur(img,5)
        height, width = img.shape
        cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
        #strategy: first set most generous parameters, try to find circles. If not circles found return none. If 1-4 circles found, return this.
        #If more than 4 circles found, make parameters more restrictive
        minDist = 700
        maximumRadius  = 200
        minimumRadius = maximumRadius - 20
        parameter2 = 100
        parameter1 = 100
        dp = 1
        numberFound1 = []
        initialGuess1 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
        maxRadius = maximumRadius)
        while (dp <= 2):
            maximumRadius  = 200
            minimumRadius = maximumRadius - 20
            parameter2 = 100
            while ((initialGuess1 is None or np.size(initialGuess1) == 4 or initialGuess1[0][0][0] != 0) and maximumRadius >= 130):
                   maximumRadius = maximumRadius - 50
                   minimumRadius = maximumRadius - 30
                   parameter2 = parameter2 - 10
                   print(parameter1, parameter2, minimumRadius, maximumRadius, dp, minDist)
                   initialGuess1 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
                            maxRadius = maximumRadius)
                   if initialGuess1 is not None:
                       numberFound1.append(initialGuess1[0][0])
                       print(initialGuess1)
            dp = dp + 1
        minDist = 700
        minimumRadius = 30
        maximumRadius = minimumRadius + 20
        parameter2 = 100 
        parameter1 = 100
        dp = 2
        initialGuess2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
        maxRadius = maximumRadius)
        print("number2 starts here")
        numberFound2 = []
        while dp >= 1:
            minimumRadius = 40
            maximumRadius = minimumRadius + 20
            while ((initialGuess2 is None or np.size(initialGuess2) == 4 or initialGuess2[0][0][0] != 0) and dp >= 1 and minimumRadius <= 130):
                   print(minimumRadius)
                   minimumRadius = minimumRadius  + 50
                   print(minimumRadius)
                   maximumRadius = minimumRadius + 30
                   parameter2 = parameter2 - 10
                   print(parameter1, parameter2, minimumRadius, maximumRadius, dp, minDist)
                   initialGuess2 = cv2.HoughCircles(img,cv2.HOUGH_GRADIENT,dp,minDist, param1 = parameter1, param2= parameter2, minRadius = minimumRadius,
                maxRadius = maximumRadius)
                   if initialGuess2 is not None:
                       numberFound2.append(initialGuess2[0][0])
                       print(initialGuess2)
            dp = dp - 1
        if numberFound1 is not None:
            for circle in numberFound1:
            # draw the outer circle
                cv2.circle(cimg,(circle[0],circle[1]),circle[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(cimg,(circle[0],circle[1]),2,(0,0,255),3)
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            mySavePATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(number) + "BackChecked.jpg"
            cv2.imwrite(mySavePATH,cimg)
        if numberFound2 is not None:
            cimg = cv2.cvtColor(img,cv2.COLOR_GRAY2BGR)
            for circle in numberFound2:
            # draw the outer circle
                cv2.circle(cimg,(circle[0],circle[1]),circle[2],(0,255,0),2)
            # draw the center of the circle
                cv2.circle(cimg,(circle[0],circle[1]),2,(0,0,255),3)
            cv2.imshow('detected circles',cimg)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            mySavePATH2 = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(number) + "BackChecked2.jpg"
            cv2.imwrite(mySavePATH2,cimg)
        return numberFound1,numberFound2
