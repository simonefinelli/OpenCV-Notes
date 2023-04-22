import cv2 as cv
import numpy as np

from utilities.utility import imshow

img_path = '../../assets/images/red_panda.jpg'

# read an image from folder
img = cv.imread(img_path)  # the image is read as numpy array

# check the image shape
shape = img.shape  # height, width, depth
print(f'Height of the image: {shape[0]}')
print(f'Width of the image: {shape[1]}')
print(f'Depth of the image: {shape[2]}')

# the cv image is a numpy array, so we can use np to performs operations
print(np.shape(img))  # same result as above

# display the image in a new window
cv.imshow('Lesser Panda', img)  # name of window and matrix image
cv.waitKey(0)  # to prevent the window closing
               # 0 - indefinite waiting
               # otherwise the windows is going to close after N milliseconds

# we can also use pyplot to show the image (check the utility function)
imshow('Lesser Panda', img)
