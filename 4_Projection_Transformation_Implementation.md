# Projection_Transformation_Implementation

<img width = 400 src="https://user-images.githubusercontent.com/44635266/62017611-49cec380-b1f2-11e9-90e8-8025a4db91bd.png">

#### warpAffine Example

```
> Section4-1.py

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

```

* Results

<img width = 400 src="https://user-images.githubusercontent.com/44635266/62018371-63bdd580-b1f5-11e9-9278-665ade518c4b.png">

<img width = 400 src="https://user-images.githubusercontent.com/44635266/62018373-65879900-b1f5-11e9-84a3-449175c7224b.png">

#### warpPerspective Example

```
> Section4-2.py

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
```

* Results

<img width=400 src="https://user-images.githubusercontent.com/44635266/62018375-67e9f300-b1f5-11e9-9793-c3cde5cf059d.png">

<img width=400 src="https://user-images.githubusercontent.com/44635266/62018378-69b3b680-b1f5-11e9-9d98-136174f7eaba.png">