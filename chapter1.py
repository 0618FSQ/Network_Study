import cv2
import numpy as np

print('package imported')


# #读取图片
# img = cv2.imread('Resources/lena.png')
# #显示图片
# cv2.imshow('lena',img) #第一个参数为图片名字，第二个为读取的图像
# cv2.waitKey(0)


#########################################################################
# #读取视频
# # cap = cv2.VideoCapture('Resources/test_video.mp4')
#
# #使用笔记本摄像头
cap = cv2.VideoCapture(0)
# #设置画面大小
cap.set(3,640)
cap.set(4,480)
# #调整亮度
# cap.set(10,100)
#
while True:
    success,img = cap.read()
    cv2.imshow('Video',img)
    if cv2.waitKey(1) & 0xFF == ord('q') :
        break
############################################################################

# img = cv2.imread('Resources/lena.png')
# kernel = np.ones((5,5),dtype=np.uint8)
#
#
# #转化为灰度图
# imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
# #模糊图像
# imgBlur = cv2.GaussianBlur(imgGray,(7,7),0)
# #canny img
# imgCanny = cv2.Canny(img,100,100)
# #扩张图像
# imgDialation = cv2.dilate(imgCanny,kernel,iterations=1)
# #erod
# imgEroded = cv2.erode(imgDialation,kernel,iterations=1)
#
#
# cv2.imshow('Gray Image',imgGray)
# cv2.imshow('Blur Image',imgBlur)
# cv2.imshow('Canny Image',imgCanny)
# cv2.imshow('Dialation Image',imgDialation)
# cv2.imshow('Eroded Image',imgEroded)
# cv2.waitKey(0)


############################################################################
#调整图片


# img = cv2.imread('Resources/lambo.PNG')
#
# print(img.shape)
# #调整图片大小
# imgResize = cv2.resize(img,(300,200))    #  (宽度，高度)
# print(imgResize.shape)
# #裁剪图片
# imgCropped = img[:200,200:500]
#
#
# cv2.imshow('Image',img)
# cv2.imshow('Image Resize',imgResize)
# cv2.imshow('Image Cropped',imgCropped)
# cv2.waitKey(0)

######################################################################################
#绘制图形
#
# img = np.zeros((512,512,3),np.uint8)
# # print(img.shape)
# # img[:] = 255,0,0
#
# #画线
# cv2.line(img,(0,0),(300,300),(0,255,0),3)  #(图像，起点），终点，颜色，线宽)
# #画矩形
# cv2.rectangle(img,(0,0),(250,350),(0,0,255),3)       #(图像，左上角（高度，宽度），右下角，颜色，线宽)  线宽-1表示填充
# #画圆
# cv2.circle(img,(400,50),30,(255,255,0),3)    #(图像，圆心，半径，颜色，线宽)
# #文本框
# cv2.putText(img,'OPENCV ',(300,100),cv2.FONT_HERSHEY_SIMPLEX,1,(0,150,0),1)   #(图像，内容，位置，字体，大小，颜色，粗细)
#
#
# cv2.imshow('Image',img)
# cv2.waitKey(0)


######################################################################################

