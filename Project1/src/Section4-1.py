import numpy as np
import cv2
import os

def TransformationImplementation():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Transform.png'
    img = cv2.imread(imgsrc)

    point1 = np.float32([[50, 50], [200, 50], [20, 200]])
    point2 = np.float32([[70, 100], [220, 50], [150, 250]])

    trans = cv2.getAffineTransform(point1, point2)
    result = cv2.warpAffine(img, trans, (350, 300))

    cv2.imshow('Source', img)
    cv2.imshow('Destiny', result)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)
if __name__=='__main__':
    TransformationImplementation()