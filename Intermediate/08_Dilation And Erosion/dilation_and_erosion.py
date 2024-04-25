"""
    Dilation – Adds pixels to the boundaries of objects in an image
    Erosion – Removes pixels at the boundaries of objects in an image
    Opening - Erosion followed by dilation
    Closing - Dilation followed by erosion
"""

import cv2 as cv
import numpy as np

image = cv.imread('../../assets/images/faces_b.jpg', 0)  # read image as gray-scale
cv.imshow('Original', image)

# Let's define our kernel size
kernel = np.ones((5, 5), np.uint8)

# Now we erode
erosion = cv.erode(image, kernel, iterations=1)
cv.imshow('Erosion', erosion)

# Dilate here
dilation = cv.dilate(image, kernel, iterations=1)
cv.imshow('Dilation', dilation)

# Opening - Good for removing noise
opening = cv.morphologyEx(image, cv.MORPH_OPEN, kernel)
cv.imshow('Opening', opening)

# Closing - Good for removing noise
closing = cv.morphologyEx(image, cv.MORPH_CLOSE, kernel)
cv.imshow('Closing', closing)

cv.waitKey(0)
