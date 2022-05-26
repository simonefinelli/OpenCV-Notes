import cv2 as cv
import numpy as np


def translate(img, x, y):
    """
    Translating the image
    :param img: np array
    :param x: -x >> left, x >> right
    :param y: -y >> up, y >> down
    :return: np array
    """
    trans_mat = np.float32([[1,0,x], [0,1,y]])
    dimensions = (img.shape[1], img.shape[0])  # width, height
    return cv.warpAffine(img, trans_mat, dimensions)


def rotate(img, angle, rotation_point=None):
    """
    Rotate the image
    :param img: np array
    :param angle: -angle -> clockwise, +angle -> counterclockwise
    :param rotation_point: pixel tuple
    :return: np image
    """
    height, width, _ = img.shape

    if rotation_point is None:
        rotation_point = (width//2, height//2)

    r_mat = cv.getRotationMatrix2D(rotation_point, angle, scale=1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, r_mat, dimensions)