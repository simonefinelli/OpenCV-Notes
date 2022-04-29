import cv2 as cv
import numpy as np

# Text
blank = np.zeros((500,500,3), dtype='uint8')
text = 'Hello World!'
position = (150, 250)
font = cv.FONT_HERSHEY_TRIPLEX
font_scale = 1.0
color = (125, 0, 255)
cv.putText(blank, text, position, font, font_scale, color, thickness=2)

cv.imshow('Text', blank)

cv.waitKey(0)