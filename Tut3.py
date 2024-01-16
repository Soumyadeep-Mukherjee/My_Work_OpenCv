import numpy as n
import cv2 
cap= cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    width=int(cap.get(3))
    height= int(cap.get(4))
    i=n.zeros(frame.shape,n.uint8)
    s_frame=cv2.resize(frame,(0,0),fx=0.5,fy=0.5) 
    i[:height//2,:width//2]=cv2.rotate(s_frame,cv2.ROTATE_180)
    i[:height//2,width//2:]=s_frame
    i[height//2:,width//2:]=s_frame
    i[height//2:,:width//2]=cv2.rotate(s_frame,cv2.ROTATE_180)
    cv2.imshow("Image",i)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows