import cv2 as cv
import numpy as np

path_to_img = '../assets/images/moon.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
cv.imshow('Moon', img)

# get a grayscale image
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# blurring
kernel_size = (5, 5)
blur = cv.GaussianBlur(gray, kernel_size, cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

# edge detection
canny = cv.Canny(blur, 50, 60)
cv.imshow('Canny Edges', canny)

################################
# # we can use instead of blurring + edge detection the threshold
# threshold = 125  # if a pixel < N is set to 0
# max_val = 250    # if a pixel > M is set to 255
# ret, thresh = cv.threshold(gray, threshold, max_val, cv.THRESH_BINARY)  # look at the image and trys to binaraze the image
# cv.imshow('Thresh', thresh)
#################################

# contours
contours, hierarchies = cv.findContours(  # contours is a list of all conountours finded
    canny,  # thresh or canny            # hierarchies is the hierachical rapresentation of contours (how the algorithm find that contours)
    cv.RETR_LIST,  # RETR_LIST return all counters found
    cv.CHAIN_APPROX_SIMPLE  # how we want to approximate contours
)
print(f"Found {len(contours)} contours!")

# drawing contours
blank = np.zeros(img.shape, dtype='uint8')

contour_idx = -1  # all contours
color = (0, 125, 255)
cv.drawContours(blank, contours, -1, color, thickness=1)
cv.imshow('Contours', blank)

cv.waitKey(0)
