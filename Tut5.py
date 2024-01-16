import numpy as n 
import cv2
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    w= int(cap.get(3))
    h=int(cap.get(4))
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    l_blue=n.array([90,50,50])
    h_blue=n.array([255,100,100])
    mask=cv2.inRange(hsv,l_blue,h_blue)
    result=cv2.bitwise_and(frame,frame,mask=mask)

    cv2.imshow("Frame",result)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release
cv2.destroyAllWindows()
