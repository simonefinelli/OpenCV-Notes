import cv2 as cv

from utilities.utility import translate, rotate

path_to_img = '../../assets/images/forest.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Waterfall', img)

# translation
translated = translate(img, 100, 150)
cv.imshow('Translated', translated)

translated = translate(img, -100, -150)
cv.imshow('Translated 2', translated)

# rotation
rotated = rotate(img, 180)
cv.imshow('Rotated', rotated)

rotation_point = (100, 300)
rotated = rotate(img, -20, rotation_point)
cv.imshow('Rotated 2', rotated)

# flipping
flip_code = 1  # 0, 1, -1 -> vertically (x axis), horizontally (y axis), both
flipped = cv.flip(img, flip_code)
cv.imshow('Flipped', flipped)

flip_code = -1
flipped = cv.flip(img, flip_code)
cv.imshow('Flipped 2', flipped)

# transposing
transposed = cv.transpose(img)
cv.imshow('Transposed', transposed)  # applying the transpose function twice,
                                     # the original image is restored

cv.waitKey(0)
