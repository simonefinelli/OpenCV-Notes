import cv2 as cv

img_path = '../../assets/images/red_panda.jpg'
out_path = '../../assets/images/red_panda.jpg'

# read an image from folder
img = cv.imread(img_path)

# make some modifications (e.g. flipping)
flipped = cv.flip(img, 0)

# save image
cv.imwrite('./out/output.jpg', flipped)
