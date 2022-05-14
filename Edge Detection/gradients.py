import cv2 as cv
import numpy as np

# We could think of gradients as regions that are present in an image
# gradients and edge are completely different things (mathematically), but in
# we can use them like edges.

path_to_img = '../assets/images/parrot.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Laplacian
lap = cv.Laplacian(gray, cv.CV_64F)
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

# Sobel  # computes the gradients in two directions: x and y.
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Sobel', combined_sobel)

cv.waitKey(0)