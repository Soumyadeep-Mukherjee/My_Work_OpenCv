import cv2
i=cv2.imread('OPEN_CV_PRAC/Me.jpg',1)
i=cv2.resize(i,(0,0),fx=0.7,fy=0.7)
i= cv2.rotate(i, cv2.ROTATE_90_COUNTERCLOCKWISE)

cv2.imshow("Image", i)
cv2.waitKey(0)
cv2.destroyAllWindows()