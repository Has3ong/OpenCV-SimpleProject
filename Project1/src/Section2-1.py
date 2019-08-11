import cv2
import os

def readImage():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Dolphin.jpg'
    img = cv2.imread(imgsrc, cv2.IMREAD_COLOR)

    cv2.imshow('Image', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

if __name__=='__main__':
    readImage()