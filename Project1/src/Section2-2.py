import cv2
import os

def readImage():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Dolphin.jpg'
    img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)

    cv2.imshow('Image', img)
    k = cv2.waitKey(0)

    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)

    cv2.imwrite('src/GrayDolphin.jpg', img)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__=='__main__':
    readImage()