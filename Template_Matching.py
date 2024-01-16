import numpy as n 
import cv2
i = cv2.imread("OPEN_CV_PRAC/Football_with_Maradona.jpg",0)
i_resize=cv2.resize(i,(0,0),fx=0.5,fy=0.5)
ti= cv2.imread("OPEN_CV_PRAC/Football.jpg",0)
ti_resize=cv2.resize(ti,(0,0),fx=0.5,fy=0.5)
h,w=ti.shape
methods = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR,
            cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
for m in methods:
    i2=i_resize.copy()
    res=cv2.matchTemplate(i2,ti_resize,m)
    min_val,max_val,min_loc,max_loc=cv2.minMaxLoc(res)
    if m in [cv2.TM_SQDIFF,cv2.TM_SQDIFF_NORMED]:
        location=min_loc
    else:
        location= max_loc
bottom_right=[location[0]+w,location[1]+h]
cv2.rectangle(i2,location,bottom_right,255,5)
cv2.imshow("Match",i2)
cv2.waitKey(0)
cv2.destroyAllWindows()