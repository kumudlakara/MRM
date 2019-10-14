import cv2 as cv
import numpy as np
import math

img=cv.imread("hand2.jpg")

krnl=np.ones((3,3),np.uint8)

hsv=cv.cvtColor(img,cv.COLOR_BGR2HSV)

lowers = np.array([0,20,70], dtype=np.uint8)
uppers= np.array([20,255,255], dtype=np.uint8)

mask=cv.inRange(hsv,lowers,uppers)

mask=cv.dilate(mask,krnl,iterations=4)

mask=cv.GaussianBlur(mask,(5,5),0)

contours,hierarchy= cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

cntr=max(contours,key=lambda x:cv.contourArea(x))

epsilon=0.0005*cv.arcLength(cntr,True)
approx=cv.approxPolyDP(cntr,epsilon,True)

hull=cv.convexHull(approx, returnPoints=False)
defects=cv.convexityDefects(approx,hull)
l=0
for i in range(defects.shape[0]):
	s,e,f,d=defects[i,0]
	start=tuple(approx[s][0])
	end=tuple(approx[e][0])
	far=tuple(approx[f][0])

	a=((end[0]-start[0])**2+(end[1]-start[1])**2)**0.5
	b=((far[0]-start[0])**2+(far[1]-start[1])**2)**0.5
	c=((end[0]-far[0])**2+(end[1]-far[1])**2)**0.5



	angle=math.acos(((b**2 + c**2 - a**2)/(2*b*c))) * 57
	if angle<=90:
		l+=1
		cv.circle(img,far,3,[255,0,0],-1)

	cv.line(img,start,end,[0,255,0],2)
l+=1

if l==1:
	print("1")
elif l==2:
	print("2")
elif l==3:
	print("3")
elif l==4:
	print("4")
elif l==5:
	print("5")

cv.imshow("img",img)
cv.imshow("mask",mask)
cv.waitKey(5000)
cv.destroyAllWindows()
