import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

# m1=cv2.imread("images/1.jpg", 1)
# print(m1)
# print("高:",m1.shape[0])
# print("寬:",m1.shape[1])
# print("色彩空間通道數:",m1.shape[2])
# m1=cv2.cvtColor(m1,cv2.COLOR_BGR2GRAY)
# # print(m1.shape)
# m1=cv2.cvtColor(m1,cv2.COLOR_GRAY2BGR)
# print(m1.shape)
# cv2.COLOR_BGR2HSV
# cv2.COLOR_BGR2GRAY
# cv2.COLOR_HSV2BGR
# cv2.COLOR_GRAY2BGR

# cv2.imwrite("images/0.jpg",m1,[cv2.IMWRITE_JPEG_QUALITY, 100])
# p1=cv2.VideoCapture(0)
# print("寬:",p1.get(3))
# print("高:",p1.get(4))
# print("FPS:",p1.get(5))
# # print("總共影格數:",p1.get(7))

# # p1.set(1,4500)
# w=int(p1.get(3))
# h=int(p1.get(4))
# p2=cv2.VideoWriter("20201021.mp4",cv2.VideoWriter_fourcc(*'MP4V'),24,(w,h))
# while p1.isOpened()==True:
# 	ret, m1=p1.read()
# 	if ret==True:
# 		# print("當前的影格:",p1.get(1))
# 		p2.write(m1)
# 		cv2.imshow("M1", m1)
# 		# 設定按鍵對應值，可以隨時關閉
# 		if cv2.waitKey(30) != -1:
# 			break
# 	else:
# 		break
# p2.release()
# cv2.destroyAllWindows()


# 建立一張圖片
# ((長寬高)(顏色))
m1 = np.full((300,600,3),(255,255,255),np.uint8)
# # 畫線
# cv2.line(m1, (10,250), (300,250), (0,0,255), 6)
# cv2.line(m1, (300,250), (0,0), (0,255,255), 6)
# # 畫矩形，最後-1為實心
# cv2.rectangle(m1, (200,100), (300,200), (255,0,0), 6)
# # cv2.rectangle(m1, 矩形左上點, 矩形右下點, 顏色, 線粗細)
# # 畫圓型，最後-1為實心
# cv2.circle(m1, (300,150), 50, (0,255,0), 6)

m1=Image.fromarray(m1)
ImageDraw.Draw(m1).text((150,120), "維尼吃大便", (0,0,255), ImageFont.truetype("kaiu.ttf",50))
m1=np.array(m1)

cv2.imshow("M1", m1)

cv2.waitKey(0)
cv2.destroyAllWindows()




