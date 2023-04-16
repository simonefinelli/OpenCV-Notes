# A color space is a system of representing an array of pixel colors
# Examples of color spaces:
# - RGB (additive color mixing - add color to black)
# - Gray-scale
# - CMY (subtractive color mixing - subtract color from white)

import cv2 as cv
import matplotlib.pyplot as plt

path_to_img = '../../assets/images/red_panda.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Red Panda', img)

# BGR to Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# BGR to HSV (Hue Saturation Value)
# HSV isolates color (Hue) from brightness, the Hue is less subject to
# fluctuations due to lighting conditions
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

# BGR to LAB (L*a*b* - CIELAB)
# CIELAB is designed to approximate human vision
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('Lab', lab)

# BGR to RGB
# plt.imshow(img)  # the image is plotted in RGB mode so the image looks weird (OpenCV imagaes are GBR)
# plt.show()

rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)  # remember now the channels are swapped!

# plt.imshow(rgb)  # now the image is right
# plt.show()

# some convertions are not allowed so we have to transfor img to bgr e thant apply the new color space (see below).
# HSV to Grayscale
hsv_bgr = cv.cvtColor(img, cv.COLOR_HSV2BGR)
hsv_gray = cv.cvtColor(hsv_bgr, cv.COLOR_BGR2GRAY)
cv.imshow('HSV to Gray', hsv_gray)


cv.waitKey(0)
