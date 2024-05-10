import cv2 as cv
import numpy as np


def auto_canny(image):
    """
    Finds optimal thresholds based on median image pixel intensity.

    :param image: input image as numpy array
    """
    blurred_img = cv.blur(image, ksize=(5, 5))
    med_val = np.median(blurred_img)
    lower = int(max(0, med_val))
    upper = int(min(255, med_val))
    edges = cv.Canny(image=image, threshold1=lower, threshold2=upper)
    return edges
