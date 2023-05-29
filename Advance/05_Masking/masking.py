import cv2 as cv
import numpy as np

path_to_img = '../../assets/images/red_panda.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Red Panda', img)

blank = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('Blank', blank)

circle = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)
cv.imshow('Circle Mask', circle)

# apply the mask on the original image
masked = cv.bitwise_and(img, img, mask=circle)
cv.imshow('Masked Image', masked)

circle_1 = cv.circle(blank.copy(), (img.shape[1]//2, img.shape[0]//2), 150, 255, -1)
rect_1 = cv.rectangle(blank.copy(), (20, 50), (200, 150), 255, -1)
cv.imshow('Circle 1 Mask', circle_1)
cv.imshow('Rectangle 1 Mask', rect_1)

weird_mask = cv.bitwise_xor(circle_1, rect_1)
cv.imshow('Weird Mask', weird_mask)

# apply the weird mask
weird_masked = cv.bitwise_and(img, img, mask=weird_mask)
cv.imshow('Final Image', weird_masked)

cv.waitKey(0)
