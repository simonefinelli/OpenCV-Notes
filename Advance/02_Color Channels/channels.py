import cv2 as cv
import numpy as np


path_to_img = '../../assets/images/flowers.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Flowers', img)

# split the image in three channels
b, g, r = cv.split(img)

cv.imshow('Blue Channel', b)  # white areas -> color channel - because if we get one dimension the maximun value is 255 (white)
cv.imshow('Green Channel', g)  # white areas -> color channel
cv.imshow('Red Channel', r)  # white areas -> color channel

# merge the channels
merged = cv.merge([b, g, r])
cv.imshow('Merged', merged)

# isolate one channel on three dimensions
blank = np.zeros(img.shape[:2], dtype='uint8')
blue = cv.merge([b, blank, blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank, blank, r])

cv.imshow('Blue Channel on 3 channels', blue)
cv.imshow('Green Channel on 3 channels', green)
cv.imshow('Red Channel on 3 channels', red)

cv.waitKey(0)
