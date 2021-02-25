import cv2
import numpy as np

# m1=cv2.imread("images/1.jpg",1)
# m2=cv2.imread("images/62.jpg",1)
# m2=np.full(m1.shape, (30,30,30), np.uint8)

# m3=cv2.add(m1,m2)
# m3=cv2.subtract(m1,m2)
 
# m3=cv2.absdiff(m1,m2)
# m3=cv2.multiply(m1,m2)
# m3=cv2.divide(m1,m2)

# m2=cv2.bitwise_not(m1)

# 超過255就會改變型態，不是uint8
# m3=m1+5000
# print(m3)
# m3=m1-m2
# m3=m1*m2
# m3=m1/m2

# 調整照片大小
# w=300
# h=int((w/m1.shape[1])*m1.shape[0])
# h=700
# w=int((h/m1.shape[0])*m1.shape[1])
# m2=cv2.resize(m1,(w,h))

# 翻轉照片
# 0==左右翻轉，1==上下翻轉, -1==上下左右翻轉
# m2=cv2.flip(m1,-1)


# 變換矩陣=cv2.getRotationMatrix2D(旋轉中心, 角度, 縮放比率)
# 結果圖像=cv2.warpAffine(圖像變數, 變換矩陣, 輸出的圖像大小)
# w=cv2.getRotationMatrix2D((300,200), 45, 1)
# m2=cv2.warpAffine(m1, w, (980,800))


#圖像變數[Y軸範圍起始:Y軸範圍結束, X軸範圍起始: X軸範圍結束]
# m2[100:400,100:400]=m1[150:450,270:570]
# m2[100:400,100:400]=[0,0,255]

# m2[0:250:1,425:700:1]=m1[100:350:1,375:650:1]
# print(m2.shape)


# m1=cv2.imread("images/1.jpg",0)
# 要做出複製才能執行彩色版，下面不會被覆蓋
# m2=m1.copy()
# 變數一, 變數二=cv2.threshold(圖像變數, 門檻值, 最大值, 方法)

# G
# th,m2[:,:,0]=cv2.threshold(m1[:,:,0], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# # B
# th,m2[:,:,1]=cv2.threshold(m1[:,:,1], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
# # R
# th,m2[:,:,2]=cv2.threshold(m1[:,:,2], 127, 255, cv2.THRESH_BINARY|cv2.THRESH_OTSU)
# print(th)
#-------------------------------------------------------------------------------------------
# 結果圖像=cv2.adaptiveThreshold(圖像變數,最大值,方法一,方法二,區塊大小,微調值)
# 區塊大小只能是單數
# m2=cv2.adaptiveThreshold(m1,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,51,0)

# 影像邊緣偵測-----------------------------------------
# 結果圖像=cv2.Canny(圖像變數,門檻值1,門檻值2)
# m2=cv2.Canny(m1,30,200)


# 影像模糊化--------------------------------------------

# 平均值模糊法
# 範圍大小是寬跟高
# 結果圖像=cv2.blur(圖像變數,範圍大小)
# m2=cv2.blur(m1,(30,30))

# 中值模糊法
# 處理數量，純數值，必須是單數
# 結果圖像=cv2.medianBlur(圖像變數,處理數量)
# m2=cv2.medianBlur(m1,11)

# 影像銳利化--------------------------------------------------

# 直方圖均衡化法
# 結果圖像=cv2.equalizeHist(圖像變數)
m1=cv2.imread("images/h2.png",1)
# 要做出複製才能執行彩色版，下面不會被覆蓋
# m2=m1.copy()
# m2[:,:,0]=cv2.equalizeHist(m1[:,:,0])
# m2[:,:,1]=cv2.equalizeHist(m1[:,:,1])
# m2[:,:,2]=cv2.equalizeHist(m1[:,:,2])

# 侵蝕蝕(色彩值低的會侵蝕色彩值高的)
# 結果圖像=cv2.erode(圖像變數, 結構陣列)
# m2=cv2.erode(m1,np.ones((100,60)))

# 結構陣列(np.ones((高,寬)))

# 膨脹(色彩值高的會侵蝕色彩值低的)
# 結果圖像=cv2.dilate(圖像變數, 結構陣列)
# m3=cv2.dilate(m1,np.ones((100,10)))


# 結果圖像=cv2.morphologyEx(圖像變數, 方法, 結構陣列)
# m2=cv2.morphologyEx(m1,cv2.MORPH_GRADIENT ,np.ones((3,3)))

# 判斷圖像裡的各項素是否在指定色彩範圍內
# 結果圖像=cv2.inRange(圖像變數, 顏色下限, 顏色上限)
m2=cv2.inRange(m1,(0,0,0),(255,255,254))










# cv2.imshow("M1",m1)
cv2.imshow("M2",m2)
# cv2.imshow("M3",m3)

cv2.waitKey(0)
cv2.destroyAllWindows()