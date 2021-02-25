import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image


x=0
a=0
while True:
	m1 = np.full((400,600,3),(255,255,255),np.uint8)
	cv2.rectangle(m1, (x,150), (x+100,250), (255,0,0), -1)
	cv2.imshow("M1", m1)
	x+=a
	if x==0:
		a=1
	elif x==500:
		a=-1
	if cv2.waitKey(2) != -1:
 			break
 	x+=a

cv2.waitKey(0)
cv2.destroyAllWindows()