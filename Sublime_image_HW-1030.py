import cv2
import numpy as np

p1=cv2.VideoCapture("images/h3.mp4")
a=p1.isOpened()

print("寬:",p1.get(3))
print("高:",p1.get(4))
print("FPS:",p1.get(5))
print("總共影格數:",p1.get(7))

while p1.isOpened()==True:
	ret, m1=p1.read()

	if ret==True:
		# print("當前的影格:",p1.get(1))
		# 變成灰階
		# m2=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
		m2=m1[:, : ,2]
		# 顏色篩選
		m2=cv2.inRange(m2, 55, 255)
		# 消除雜訊
		m2=cv2.erode(m2,np.ones((11,11)))
		m2=cv2.dilate(m2,np.ones((11,11)))
		# 反向
		m2=cv2.bitwise_not(m2)
		
		# 取得輪廓
		a,b=cv2.findContours(m2,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
		print(b)
		# m2=cv2.cvtColor(m1, cv2.COLOR_GRAY2BGR)
		# 框出輪廓	
		for i in range(0,len(a)):
			x, y, w, h =cv2.boundingRect(a[i])
			cv2.rectangle(m1, (x,y),(x+w,y+h),(0,0,255),2)




		cv2.imshow("M2", m2)
		cv2.imshow("M1", m1)
		# 設定按鍵對應值，可以隨時關閉
		if cv2.waitKey(30) != -1:
			break
	else:
		break

cv2.destroyAllWindows()