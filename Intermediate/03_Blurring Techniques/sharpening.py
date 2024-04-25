import cv2 as cv
import numpy as np


img_path = '../../assets/images/parrot.jpg'
img = cv.imread(img_path)
cv.imshow('Parrot', img)

# sharpening kernel has sum one
kernel = np.array([[-1, -1, -1],
                   [-1,  9, -1],
                   [-1, -1, -1]])

sharpened = cv.filter2D(img, -1, kernel)

cv.imshow('Sharpened', sharpened)

cv.waitKey(0)
