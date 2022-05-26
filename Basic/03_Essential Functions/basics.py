import cv2 as cv

path_to_img = '../assets/images/cat.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Cat', img)

# Grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

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

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)  # ignoring the aspect-ratio
cv.imshow('Resized', resized)

# Cropping
cropped = img[100:300, 100:300]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
