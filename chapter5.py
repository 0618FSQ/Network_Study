import cv2
import numpy as np



img = cv2.imread('Resources/cards.jpg')
print(img.shape)
width ,height = 250 ,350

#需要截取的区域顶点
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])

#新的图像顶点
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])

#图片转换
matrix = cv2.getPerspectiveTransform(pts1,pts2)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

cv2.imshow('Image',img)
cv2.imshow('Outputs',imgOutput)
cv2.waitKey(0)

