import cv2 as cv
from utils import rescale_img

path_to_img = '../assets/images/forest.jpg'
img = cv.imread(path_to_img)
cv.imshow('Forest', img)

new_img = rescale_img(img)
cv.imshow('Rescaled Forest', new_img)

cv.waitKey(0)