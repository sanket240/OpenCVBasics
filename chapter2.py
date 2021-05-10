import cv2
import numpy as np
img=cv2.imread("Resource/rohit-sharma_1603803462.jpg")
kernal=np.ones((5,5),np.uint8)
imgGry=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
imgBlur=cv2.GaussianBlur(imgGry,(7,7),0)
imgCanny=cv2.Canny(img,150,100)
imgDialation=cv2.dilate(imgCanny,kernal,iterations=1)

imgEroded=cv2.erode(imgDialation,kernal,iterations=1)

cv2.imshow("Gray Image",imgGry)
cv2.imshow("Blur Image",imgBlur)
cv2.imshow("Canny Image",imgCanny)
cv2.imshow("Dialation Image",imgDialation)
cv2.imshow("Erosion Image",imgEroded)
cv2.waitKey(10000)