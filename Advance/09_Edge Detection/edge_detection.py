import cv2 as cv

"""
 Canny is a specific edge detector (and it uses sobel in one of his stages).
 Canny accepts three args:
  - The first argument is our input image.
  - The second and third arguments are our minVal and maxVal respectively.
  - The forth argument is aperture_size. It is the size of Sobel kernel used for find image gradients.
    By default it is 3.

 The threshold1 and threshold2 in Canny Edge Detector are the gradient values (see ).
 In particular any gradient value larger than threshold2 is considered to be an edge, instead, any value below 
 threshold1 is considered not to be an edge. Values in between threshold1 and threshold2 are either classiﬁed as 
 edges or non-edges based on how their intensities are “connected”.
"""

path_to_img = '../../assets/images/parrot.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
# cv.imshow('Parrot', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# Blur
kernel_size = (5, 5)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
# cv.imshow('Blur', blur)

# Edge Cascade (edge detector)
threshold_1 = 100
threshold_2 = 210
canny = cv.Canny(blur, threshold_1, threshold_2)  # passing a blurred image the detector will work better
cv.imshow('Canny', canny)

cv.waitKey(0)
