import cv2
import numpy as np
img = cv2.imread('/home/wargun/Pictures/spiderman2.jpg')


kernel = np.ones((5,5),np.uint8)
imGrey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imBlur = cv2.GaussianBlur(imGrey,(11,11),0)
imCanny = cv2.Canny(img, 150, 200)
imDialation = cv2.dilate(imCanny, kernel, iterations=1)
imEroded = cv2.erode(imDialation, kernel, iterations=1)



cv2.imshow('Gray image', imGrey)
cv2.imshow('Blur image', imBlur)
cv2.imshow('Canny image', imCanny)
cv2.imshow('Dilation image', imDialation)
cv2.imshow('Eroded image', imEroded)
cv2.waitKey(0)
