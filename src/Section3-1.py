import cv2
import os

def EdgeDetection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Ryan.png'
    img = cv2.imread(imgsrc)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(image, 50, 220)
    dst, contours, hierarchy = cv2.findContours(edge, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    cv2.imshow('Edge', edge)
    cv2.drawContours(img, contours, -1, (0, 255, 0), 1)
    cv2.imshow('Contour', img)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
if __name__=='__main__':
    EdgeDetection()