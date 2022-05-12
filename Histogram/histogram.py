import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

# Histograms allow you to visualize the distribution of pixels intensity
# in an image.

path_to_img = '../assets/images/parrot.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)
# cv.imshow('Flowers', img)  # conflict with plt
plt.figure()
plt.imshow(cv.cvtColor(img, cv.COLOR_BGR2RGB))

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('Gray', gray)  # conflict with plt
plt.figure()
plt.imshow(cv.cvtColor(gray, cv.COLOR_BGR2RGB))

#######################
# Grayscale Histogram #
#######################
imgs_list = [gray]
n_channels_list = [0]
hist_size_list = [255]
mask = None  # to calculate histogram only on a portion of the image
ranges_list = [0, 255]
gray_hist = cv.calcHist(
    imgs_list,
    n_channels_list,
    mask,
    hist_size_list,
    ranges_list
)

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')  # represent the interval of pixels intensity
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim(0, 256)

# Mask

blank = np.zeros(img.shape[:2], dtype='uint8')
mask_circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)
img_masked = cv.bitwise_and(gray, gray, mask=mask_circle)
plt.figure()
plt.title('Masked Grayscale Image')
plt.imshow(cv.cvtColor(img_masked, cv.COLOR_BGR2RGB))

# Grayscale Histogram
imgs_list = [gray]
n_channels_list = [0]
hist_size_list = [255]
mask = mask_circle  # to calculate histogram only on a portion of the image
ranges_list = [0, 255]
gray_with_mask_hist = cv.calcHist(
    imgs_list,
    n_channels_list,
    mask,
    hist_size_list,
    ranges_list
)

plt.figure()
plt.title('Grayscale with Mask')
plt.xlabel('Bins')  # represent the interval of pixels intensity
plt.ylabel('# of pixels')
plt.plot(gray_with_mask_hist)
plt.xlim(0, 256)


####################
# Colour Histogram #
####################

blank = np.zeros(img.shape[:2], dtype='uint8')
mask_circle = cv.circle(blank, (img.shape[1]//2, img.shape[0]//2), 250, 255, -1)
img_masked = cv.bitwise_and(img, img, mask=mask_circle)
plt.figure()
plt.title('Masked Colour Image')
plt.imshow(cv.cvtColor(img_masked, cv.COLOR_BGR2RGB))

# Color Histogram
colors = ('r', 'g', 'b')
plt.figure()
plt.title('Color with Mask')
plt.xlabel('Bins')  # represent the interval of pixels intensity
plt.ylabel('# of pixels')
for i, c in enumerate(colors):
    imgs_list = [img]
    n_channels_list = [i]
    hist_size_list = [255]
    mask = mask_circle  # to calculate histogram only on a portion of the image
    ranges_list = [0, 255]
    color_with_mask_hist = cv.calcHist(
        imgs_list,
        n_channels_list,
        mask,
        hist_size_list,
        ranges_list
    )


    plt.plot(color_with_mask_hist, color=c)
    plt.xlim(0, 256)



plt.show()
cv.waitKeyEx(0)
