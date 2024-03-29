import cv2 as cv

video_path = '../../assets/videos/swiss.mp4'

# read video
capture = cv.VideoCapture(video_path)  # the method can take integer arg to select the video streaming from a source
                                        # in most cases 0 references to the main camera on the pc

# we have to read the video (or streaming) frame by frame
while True:
    is_read, frame = capture.read()  # is_read says if the frame has been correctly read or not

    if not is_read:  # frames are finished
        break

    # display the frame
    cv.imshow('Video', frame)
    cv.waitKey(30)  # changing the milliseconds we can manipulate the speed of the showed frames

# release the capture pointer
capture.release()
cv.destroyAllWindows()
