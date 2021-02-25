import cv2
import numpy as np

m1=cv2.imread("images/h2.png",1)

m1[:, : ,2]=cv2.subtract(m1[:, : ,2],m1[:, : ,1])
m1[:, : ,2]=cv2.subtract(m1[:, : ,2],m1[:, : ,0])

m2=np.full(m1.shape, (0,0,255), np.uint8)
m5=np.full(m1.shape, (255,255,255), np.uint8)
m3=cv2.subtract(m2,m1)
m6=cv2.multiply(m3,m5)


m6=m6[:, : ,2]

# cv2.imshow("M1",m1)
# cv2.imshow("M2",m2)
# cv2.imshow("M3",m3)
# cv2.imshow("M4",m4)
# cv2.imshow("M5",m5)
cv2.imshow("M6",m6)
# cv2.imshow("M7",m7)
cv2.waitKey(0)
cv2.destroyAllWindows()