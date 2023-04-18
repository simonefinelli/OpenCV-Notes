import cv2 as cv
import numpy as np

path_to_img = '../../assets/images/cat.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Cat', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # only 1 channel is used
cv.imshow('Gray', gray)
print(gray.shape)

# Grayscale
gray = cv.imread(path_to_img, 0)
cv.imshow('Gray 2', gray)
print(gray.shape)

# Blur
kernel_size = (5,5)
blur = cv.GaussianBlur(img, kernel_size, cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# Edge Cascade (edge detector)
threshold_1 = 100
threshold_2 = 210
canny = cv.Canny(blur, threshold_1, threshold_2)  # passing a blurred image the detector will work better
cv.imshow('Canny', canny)

# Dilating the Image
kernel_size = (3,3)
dilated = cv.dilate(canny, kernel_size, iterations=3)
cv.imshow('Dilated', dilated)

# Eroding
kernel_size = (3,3)
eroded = cv.erode(dilated, kernel_size, iterations=3)  # we went back almost like to the canny
cv.imshow('Eroded', eroded)

# Cropping
img = cv.imread(path_to_img)
start_row, start_col = int(img.shape[0] * 0.25), int(img.shape[1] * 0.25)  # height and width
end_row, end_col = int(img.shape[0] * 0.65), int(img.shape[1] * 0.65)
cropped = img[start_row:end_row, start_col:end_col]
cv.imshow('Cropped', cropped)

# Brightness increasing/decreasing
b_m = np.ones(gray.shape, dtype='uint8') * 100
gray_bright = cv.add(gray, b_m)  # increase the brightness by 100
cv.imshow('Brightness +', gray_bright)

b_m = np.ones(gray.shape, dtype='uint8') * 100
gray_bright = cv.subtract(gray, b_m)  # increase the brightness by 100
cv.imshow('Brightness -', gray_bright)


cv.waitKey(0)
