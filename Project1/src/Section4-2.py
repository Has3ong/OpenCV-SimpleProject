import numpy as np
import cv2
import os

def TransformationImplementation():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Transform2.png'
    img = cv2.imread(imgsrc)

    TopLeft = [99, 35]
    TopRight = [392, 23]
    BottomLeft = [70, 453]
    BottomRight = [414, 461]

    point1 = np.float32([TopLeft, TopRight, BottomRight, BottomLeft])

    w1 = abs(BottomRight[0] - BottomLeft[0])
    w2 = abs(TopRight[0] - TopLeft[0])
    h1 = abs(TopRight[1] - BottomRight[1])
    h2 = abs(TopLeft[1] - BottomLeft[1])

    width = min([w1, w2])
    height = min([h1, h2])

    point2 = np.float32([[0, 0], [width-1, 0], [width-1, height-1], [0, height-1]])

    trans = cv2.getPerspectiveTransform(point1, point2)
    result = cv2.warpPerspective(img, trans, (int(width), int(height)))

    cv2.imshow('Source', img)
    cv2.imshow('Destiny', result)

    k = cv2.waitKey(0)
    if k == 27:
        cv2.destroyAllWindows()
        cv2.waitKey(1)

if __name__=='__main__':
    TransformationImplementation()