# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 19:55:37 2018

@author: Murali
"""

import cv2
import numpy as np
img = cv2.imread("c:\\temp\\0.7483.png",0)
laplacian = cv2.Laplacian(img,cv2.CV_8UC1) # Laplacian Edge Detection
minLineLength = 900
maxLineGap = 100
lines = cv2.HoughLinesP(laplacian,1,np.pi/180,100,minLineLength,maxLineGap)
for line in lines:
    for x1,y1,x2,y2 in line:
        cv2.line(img,(x1,y1),(x2,y2),(255,255,255),1)
cv2.imwrite('Written_Back_Results.jpg',img)