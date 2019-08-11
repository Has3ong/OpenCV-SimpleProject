
import cv2
import os

def ImageProcessing():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/document.jpg'
    img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)

    r = 600.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    blur = cv2.GaussianBlur(img, (7, 7), 0)

    withBlur = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)
    notBlur = cv2.adaptiveThreshold(blur, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 21, 10)

    cv2.imshow('Source', withBlur)
    cv2.imshow('Destiny', notBlur)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)


if __name__=='__main__':
    ImageProcessing()