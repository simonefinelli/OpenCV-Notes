import cv2 as cv
import numpy as np

# Canny is a specific edge detector (and it uses sobel in one of his stages)

path_to_img = '../../assets/images/parrot.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
# cv.imshow('Parrot', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
kernel_size = (5,5)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade (edge detector)
threshold_1 = 100
threshold_2 = 210
canny = cv.Canny(blur, threshold_1, threshold_2)  # passing a blurred image the detector will work better
cv.imshow('Canny', canny)

cv.waitKey(0)
