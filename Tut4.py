import numpy as n
import cv2 
cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    w=int(cap.get(3))
    h=int(cap.get(4))
    i= cv2.line(frame,(0,0),(w,h),(200,0,100),10)
    i=cv2.line(frame,(w,0),(0,h),(170,100,200),10)
    cv2.imshow("Frame",i)
    if cv2.waitKey(1)==ord("q"):
        break
cap.release()
cv2.destroyAllWindows