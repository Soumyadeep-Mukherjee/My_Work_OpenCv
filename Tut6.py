import numpy as n
import cv2
c= cv2.imread("OPEN_CV_PRAC/Blue square.png")
c=cv2.resize(c,(0,0),fx=0.5,fy=0.5)
L=cv2.cvtColor(c,cv2.COLOR_BGR2GRAY)
corners= cv2.goodFeaturesToTrack(L,4,0.01,5)
print(corners)
corners=n.int0(corners)
for co in corners:
    x,y=co.ravel() #ravel removes the inner matric ie [[[4,5,6]]]-->[4,5,6]
    cv2.circle(c,(x,y),10,(0,0,255),5)
cv2.imshow("frame",c)
cv2.waitKey(0)
cv2.destroyAllWindows()