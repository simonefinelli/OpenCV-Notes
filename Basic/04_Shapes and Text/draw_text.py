import cv2 as cv
import numpy as np

# image
blank = np.zeros((500, 500, 3), dtype='uint8')

# text settings
text = 'Hello World!'
position = (150, 250)
# the font can we use are:
# - FONT_HERSHEY_SIMPLEX, FONT_HERSHEY_PLAIN
# - FONT_HERSHEY_DUPLEX, FONT_HERSHEY_COMPLEX
# - FONT_HERSHEY_TRIPLEX, FONT_HERSHEY_COMPLEX_SMALL
# - FONT_HERSHEY_SCRIPT_SIMPLEX, FONT_HERSHEY_SCRIPT_COMPLEX
font = cv.FONT_HERSHEY_DUPLEX
font_scale = 1.0
color = (0, 125, 255)

# apply text
cv.putText(blank, text, position, font, font_scale, color, thickness=2)

# show image
cv.imshow('Custom Text', blank)

cv.waitKey(0)