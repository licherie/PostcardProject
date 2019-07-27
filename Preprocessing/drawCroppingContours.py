import cv2
import numpy as np
import math
import matplotlib.pyplot as plt

def findNumberContours(postcardNumber):
    myPATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(postcardNumber) + "Back.jpg"
    img = cv2.imread(myPATH)
    if img is not None:
        greyImg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        blur = cv2.medianBlur(greyImg, 5)
        ret,thresh1 = cv2.threshold(blur,200,255,cv2.THRESH_BINARY)
        contours, hierarchy =  cv2.findContours(thresh1,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        if contours is None or not contours:
            th3 = cv2.adaptiveThreshold(blur,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                cv2.THRESH_BINARY,11,2)
            contours, hierarchy =  cv2.findContours(th3,cv2.RETR_LIST,cv2.CHAIN_APPROX_SIMPLE)
        if contours is not None and contours:
            max_contour_area = cv2.contourArea(contours[0])
            max_index = 0
            second_largest_area = 0
            second_largest_index = 0
            for index, contour in enumerate(contours):
                #print("contour " + str(index) + " has area" +
                     # str(cv2.contourArea(contour)))
                if cv2.contourArea(contour) > max_contour_area:
                    max_contour_area = cv2.contourArea(contour)
                    max_index = index
                if cv2.contourArea(contour) > second_largest_area and cv2.contourArea(contour) < max_contour_area:
                    second_largest_area = cv2.contourArea(contour)
                    second_largest_index = index
           #rect = cv2.minAreaRect(contours[max_index])
            x,y,w,h = cv2.boundingRect(contours[max_index])
            print(max_index, len(contours), second_largest_area, second_largest_index)
            cv2.drawContours(img, contours,max_index, (0,255,0), 3)
            cv2.imshow('img', img)
            cv2.waitKey()
            cv2.destroyAllWindows()
            mySavePATH = "C://Users//SEAB//Desktop//postcardImages//newPostcardList//" + "postcard" + str(postcardNumber) + "BackCropped.png"
            crop = img[y:y+h,x:x+w]
            cv2.imwrite(mySavePATH, crop)
            return contours,hierarchy

