import cv2
import numpy as np

# m3=cv2.imread("images/58.jpg",1)
# m1=cv2.cvtColor(m3, cv2.COLOR_BGR2GRAY)
# # m2=np.full((m1.shape[0],m1.shape[1],3),255,np.uint8)



# m1=cv2.inRange(m1,180,255)
# m1=cv2.erode(m1, np.ones((2,2)))
# m1=cv2.dilate(m1, np.ones((2,2)))



# a,b=cv2.findContours(m1,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
# print(b)
# cv2.imshow("M1",m1)
# for i in range(0,len(a)):
# 	m2=m3.copy()
# 	x,y,w,h=cv2.boundingRect(a[i])
# 	cv2.imwrite("20201030/"+str()+".png", m3[y:y+h,x:x+w])
# 	cv2.rectangle(m2, (x,y),(x+w,y+h),(0,0,255),2)
# 	cv2.imshow("M2",m2)
# 	cv2.waitKey(0)

	# if b[0][i][3]==1:
		# m2=cv2.cvtColor(m1, cv2.COLOR_GRAY2BGR)
		# m2=m3.copy()
		# # cv2.drawContours(m2,a,i,(0,0,255),1)
		# x, y, w, h =cv2.boundingRect(a[i])
		# cv2.imwrite("20201030/"+str()+".png", m3[y:y+h,x:x+w])
		# cv2.rectangle(m2, (x,y),(x+w,y+h),(0,0,255),2)
		










# cv2.imshow("M1",m1)
# cv2.imshow("M2",m2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 文字辨識
import pytesseract as pt



# m1=cv2.imread("images/101.png",1)
# # 辨識結果=pt.image_to_string(圖片變數, 語言包名稱, 設定值)
# text=pt.image_to_string(m1,"my","")
# print(text)
# cv2.imshow("M1",m1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 條碼辨識
# from pyzbar import pyzbar

# m1=cv2.imread("images/103.png",1)
# # 辨識方式
# # 結果變數=pyzbar.decode(圖像變數)
# ret=pyzbar.decode(m1)
# # 印出 LIST
# for d in ret:
# 	print("類型:",d.type)
# 	# 有些中文顯示不出來，編碼成日文在編碼成utf8
# 	# 能顯示，不能顯示，兩種都包含
# 	try:
# 		print("資料:",d.data.decode("utf-8").encode("sjis").decode("utf-8"))
# 	except:

# 		print("資料:",d.data.decode("utf-8"))

# 	# print("包覆他的矩形:",d.rect)
# 	x,y,h,w=d.rect
# 	# 標示出辨識到哪一個

# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# 	cv2.imshow("M1",m1)
# 	cv2.waitKey(0)
# 	print("===============================")

# # cv2.imshow("M1",m1)

# # cv2.waitKey(0)
# cv2.destroyAllWindows()


# 辨識
# 分類器：
# 控制變數=cv2.CascadeClassifier(分類器文件)
# 辨識目標：
# 結果變數=控制變數.detectMultiScale(圖像變數,minNeighbors=檢測門檻數,minSize=最小尺寸)

# 辨識人臉
# m1=cv2.imread("images/62.jpg",1)
# p1=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
# ret=p1.detectMultiScale(m1,minNeighbors=15,minSize=(10,10))
# for x,y,w,h in ret:
# 	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# cv2.imshow("M1",m1)

# cv2.waitKey(0)
# cv2.destroyAllWindows()


# 加入攝影機辨識人臉
# p1=cv2.VideoCapture(0)
# p2=cv2.CascadeClassifier("cascade/haarcascade_frontalface_default.xml")
# while p1.isOpened()==True:
# 	ret,m1=p1.read()
# 	if ret==True:
# 		ret=p2.detectMultiScale(m1,minNeighbors=3,minSize=(10,10))
# 		for x,y,w,h in ret:
# 			cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
# 		cv2.imshow("M1",m1)
# 		if cv2.waitKey(42)!=-1:
# 			break
# 	else:
# 		break

# cv2.destroyAllWindows()



m1=cv2.imread("classifier_training/Data/image.jpg",1)
p1=cv2.CascadeClassifier("classifier_training/xml/cascade.xml")
ret=p1.detectMultiScale(m1,minNeighbors=5,minSize=(10,10))
for x,y,w,h in ret:
	cv2.rectangle(m1,(x,y),(x+w,y+h),(0,0,255),2)
cv2.imshow("M1",m1)

cv2.waitKey(0)
cv2.destroyAllWindows()
