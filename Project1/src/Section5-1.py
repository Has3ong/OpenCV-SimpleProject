import numpy as np
import cv2
import os

def null(x):
    pass

def ImageProcessing():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/document.jpg'
    img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)

    r = 600.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    window = 'Window'
    TrackBar = 'TrackBar'
    cv2.namedWindow(window)
    cv2.createTrackbar(TrackBar, window, 127, 255, null)
    Threshold = np.zeros(img.shape, np.uint8)

    while 1:
        TrackBarPos = cv2.getTrackbarPos(TrackBar, window)
        cv2.threshold(img, TrackBarPos, 255, cv2.THRESH_BINARY, Threshold)
        cv2.imshow(window, Threshold)

        k = cv2.waitKey(0)
        if k == 27:
            cv2.destroyAllWindows()
            cv2.waitKey(1)
            break
    return

if __name__=='__main__':
    ImageProcessing()