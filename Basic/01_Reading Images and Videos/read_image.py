import cv2 as cv

path_to_img = '../assets/images/red_panda.jpg'

# read an image from folder
img = cv.imread(path_to_img)  # the image is read as numpy array

# display the image in a new window
cv.imshow('Lesser Panda', img)  # name of window and matrix image
cv.waitKey(0)  # to prevent the window closing
               # 0 - indefinite waiting
               # otherwise the windows is going to close after N milliseconds