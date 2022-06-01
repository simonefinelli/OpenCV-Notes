import cv2 as cv
from utils import rescale_img

"""
Interpolation Methods:
- cv2.INTER_AREA - Good for shrinking or down sampling
- cv2.INTER_NEAREST - Fastest
- cv2.INTER_LINEAR - Good for zooming or up sampling (default)
- cv2.INTER_CUBIC - Good to enlarge an image (slower than linear)
- cv2.INTER_LANCZOS4 - Best
"""

path_to_img = '../../assets/images/forest.jpg'
img = cv.imread(path_to_img)
cv.imshow('Forest', img)

# simple resizing
new_dim = (500, 500)
img_resized = cv.resize(img, new_dim, interpolation=cv.INTER_LANCZOS4)
cv.imshow('Simple Resize', img_resized)

# rescaling (keep aspect ratio)
img_rescaled = cv.resize(img, None, fx=0.75, fy=0.75, interpolation=cv.INTER_LANCZOS4)
cv.imshow('Rescaled Forest', img_rescaled)

# rescaling with custom method
img_rescaled_c = rescale_img(img)
cv.imshow('Rescaled Forest Custom', img_rescaled_c)


cv.waitKey(0)