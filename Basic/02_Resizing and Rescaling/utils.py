import cv2 as cv


def rescale_img(img, scale=0.75):
    height, width, _ = img.shape  # shape[0] -> height, shape[1] -> width

    width = int(width * scale)
    height = int(height * scale)
    scaling_dimensions = (width, height)  # width and height are swapped

    resized = cv.resize(img, scaling_dimensions, interpolation=cv.INTER_LANCZOS4)

    return resized
