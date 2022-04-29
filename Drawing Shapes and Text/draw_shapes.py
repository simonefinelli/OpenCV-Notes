import cv2 as cv
import numpy as np

# Black image
blank = np.zeros((500,500,3), dtype='uint8')  # uint8 -> 8-bit unsigned (0-255)
cv.imshow('Blank', blank)

# Paint the whole image
blank[:] = 0, 255, 0  # green - in cv2 channels are swapped (BGR)
cv.imshow('Green', blank)

# Square
blank = np.zeros((500,500,3), dtype='uint8')
blank[100:200, 300:400] = 255, 255, 255  # white
cv.imshow('Square', blank)

# Rectangle
img = np.zeros((500,500,3), dtype='uint8')
pt1 = (0,0)  # origin
pt2 = (500, 250)
color = (255, 0, 0)  # Blue - in cv2 channels are swapped (BGR)
thickness = 2
cv.rectangle(img, pt1, pt2, color, thickness=thickness)
cv.imshow('Rectangle', img)

# Filled Rectangle
img = np.zeros((500,500,3), dtype='uint8')
pt1 = (0,0)  # origin
pt2 = (250, 250)
color = (0, 0, 255)  # Blue - in cv2 channels are swapped (BGR)
cv.rectangle(img, pt1, pt2, color, thickness=cv.FILLED)  # or thickness=-1
cv.imshow('Filled Rectangle', img)

# Circle
img = np.zeros((500,500,3), dtype='uint8')
center = (img.shape[1]//2, img.shape[0]//2)  # (x,y) -> width (shape[1]), height (shape[0])
radius = 100  # pixels
color = (0, 125, 255)
thickness = 10
cv.circle(img, center, radius, color, thickness=thickness)
cv.imshow('Circle', img)

# Line
img = np.zeros((500,500,3), dtype='uint8')
pt1 = (100, 250)  # origin
pt2 = (400, 250)
color = (255, 255, 0)
cv.line(img, pt1, pt2, color, thickness=5)
cv.imshow('Line', img)

cv.waitKey(0)