import cv2 as cv
import numpy as np
import time

path_to_img = '../../assets/images/flowers.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Flowers', img)

# with thresholding, we can binarize the image (pixel can only have 2 values: 0 - 255)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)  # 1 channel

#######################
# Simple Thresholding #
#######################
threshold_value = 127
max_value = 255  # the maximum value assigned to a pixel if pixel > threshold_value
threshold_type = cv.THRESH_BINARY
threshold, img_thresh = cv.threshold(  # threshold has the same value of threshold_value
    gray,
    threshold_value,
    max_value,
    threshold_type
)
cv.imshow(f'Simple Threshold ({threshold})', img_thresh)

# inverse
threshold_type = cv.THRESH_BINARY_INV
threshold, img_thresh_inv = cv.threshold(
    gray,
    threshold_value,
    max_value,
    threshold_type
)
cv.imshow(f'Simple Inverse Threshold ({threshold})', img_thresh_inv)


#########################
# Adaptive Thresholding # the algorithm find the optimum threshold by itself
#########################
# The adaptive thresholding use convolution (and kernel) and compute the mean (ADAPTIVE_THRESH_MEAN_C) of
# neighborhood pixels in the kernel and find the optimal threshold for that area
adaptive_method = cv.ADAPTIVE_THRESH_GAUSSIAN_C
threshold_type = cv.THRESH_BINARY  # cv.THRESH_BINARY
block_size = 15  # neighborhood size considered (kernel size)
C = 3 # int subtracted from the mean to fine tune the threshold
adaptive_thresh = cv.adaptiveThreshold(
    gray,
    max_value,
    adaptive_method,
    threshold_type,
    block_size,
    C
)
cv.imshow(f'Adaptive Threshold)', adaptive_thresh)

# instead of cv.ADAPTIVE_THRESH_MEAN_C we can use cv.ADAPTIVE_THRESH_GAUSSIAN_C
# that add weights at each pixel value in the kernel and then computes the mean
# across the pixels



cv.waitKey(0)
