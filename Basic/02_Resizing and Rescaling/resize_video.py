import cv2 as cv
from utils import rescale_img

path_to_vid = '../assets/videos/swiss.mp4'

# read video
capture = cv.VideoCapture(path_to_vid)
while True:
    is_read, frame = capture.read()
    if not is_read:
        break

    # display the frame
    cv.imshow('Original Video', frame)
    cv.imshow('Rescaled Video', rescale_img(frame, scale=0.25))
    cv.waitKey(30)

capture.release()
cv.destroyAllWindows()