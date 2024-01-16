import cv2 
import random
i= cv2.imread("OPEN_CV_PRAC/Blue.jpg",1)
'''print(i[0][5])'''
print(i.shape)
for n in range(i.shape[0]):
    for j in range(100):
        i[n,j]=[random.randint(110,150),random.randint(100,200),random.randint(0,0)]
for r in range(i.shape[0]):
    for z in range(100,200):
        i[r,z]=[random.randint(0,150),random.randint(0,100),random.randint(0,10)]
cv2.imshow("Modified Image",i)
cv2.waitKey(0)
cv2.destroyAllWindows