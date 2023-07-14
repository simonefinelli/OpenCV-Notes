# Face detection is the ability of an algorith to locate a face on an image

# The principal method developed in this filed uses the Haar Cascades
# There are a lots of Haar Cascades, and we can find those on
# https://github.com/opencv/opencv/tree/4.x/data/haarcascades

# A better method is local binary pattern (LBP)


import cv2 as cv

path_to_img = '../assets/images/people.jpg'
img = cv.imread(path_to_img)  # 3 channel image (BGR)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

# load haar cascades kernels
haar_cascade = cv.CascadeClassifier('./haarcascade_frontalface_default.xml')
faces_rect = haar_cascade.detectMultiScale(
    gray,
    scaleFactor=1.2,
    minNeighbors=5  # the number of neighborhoods rectangles should have to be called a face
)

# faces found
print(f'Number of faces found: {len(faces_rect)}')

# draw faces found
for x, y, w, h in faces_rect:
    cv.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKeyEx(0)
