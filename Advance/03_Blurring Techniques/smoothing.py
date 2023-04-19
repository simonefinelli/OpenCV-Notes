import cv2 as cv


img_path = '../../assets/images/parrot.jpg'
img = cv.imread(img_path)  # 3 channel image (BGR)
cv.imshow('Parrot', img)


# AVERAGING - Each pixel of the image is replaced (convolution) by the average
# of all the pixels surrounding the center of the kernel area.
kernel = (5, 5)
avg = cv.blur(img, kernel)
cv.imshow('Average Blur', avg)

# GAUSSIAN - Like averaging but the average is computing on the products of the
# surrounding pixel weights in the kernel.
# Gaussian Blur is more natural than Averaging Blur.
kernel = (5, 5)
sigma_x = 0 # standard deviation in the x direction
gauss = cv.blur(img, kernel, sigma_x)
cv.imshow('Gaussian Blur', gauss)

# MEDIAN - Each pixel of the image is replaced (convolution) by the median
# of all the pixels surrounding the center of the kernel area.
# Used a lot when we have to delete salt and pepper noise.
kernel = 5
median = cv.medianBlur(img, kernel)
cv.imshow('Median Blur', median)

# BILATERAL - Apply blurring retaining the edges in the image.
# The most effective algorithm. Indeed, It is used to remove noise.
diameter = 10  # diameter of pixel neighborhood
sigma_color = 40  # larger values means that are more colors in the neighborhood that will be considered when the blur is computed.
sigma_space = 25  # larger values means that pixels further out from the central pixel will influence the blurring calculation.
bilateral = cv.bilateralFilter(img, diameter, sigma_color, sigma_space)
cv.imshow('Bilateral Blur', bilateral)


# DE-NOISING (Non-Local Means De-noising)
# There are 4 types:
# - cv.fastNlMeansDenoising() - for single grayscale images
# - cv.fastNlMeansDenoisingColored() - for color images
# - cv.fastNlMeansDenoisingMulti() - for grayscale image sequence
# - cv.fastNlMeansDenoisingColored() - for color image sequence
template_window_size = 7  #  size in pixel of the template patch that is used to compute weights. 7 is a good default.
search_windows_size = 21  # size in pixel to compute the wighted average for given pixel. Should be odd.
h = 10 # parameter deciding filter strength. Higher h value removes noise better, but removes details of image also. (10 is ok)
h_color = 8  # same as h, but for color images only. (normally same as h)
denoise_img = cv.fastNlMeansDenoisingColored(bilateral, None, h, h_color,
                                             search_windows_size)
cv.imshow('Denoised', denoise_img)

cv.waitKey(0)
