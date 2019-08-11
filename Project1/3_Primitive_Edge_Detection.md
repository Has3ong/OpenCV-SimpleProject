# Primitive_Edge_Detection

#### RGB, HSV Color Space

<img width=600 src="https://user-images.githubusercontent.com/44635266/62008827-aa2e1880-b192-11e9-83c2-42c23ffc68f5.png">

#### Canny Algorithm

<img width=600 src="https://user-images.githubusercontent.com/44635266/62008863-dd70a780-b192-11e9-98bc-55b8c1c18478.png">

```
> Section3-1.py

import cv2
import os

def EdgeDetection():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/Ryan.png'
    img = cv2.imread(imgsrc)
    image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    edge = cv2.Canny(image, 100, 200)
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
```

#### Results

* edge = cv2.Canny(image, 100, 200)

<img width=500 src="https://user-images.githubusercontent.com/44635266/62009092-18280f00-b196-11e9-9a9f-a2536e1ea91c.png">

* edge = cv2.Canny(image, 50, 220)

<img width=500 src="https://user-images.githubusercontent.com/44635266/62009112-6806d600-b196-11e9-81a0-c5afb845afc3.png">

#### Source
<img width=500 src="https://user-images.githubusercontent.com/44635266/62009093-19593c00-b196-11e9-9c57-d007c403e57e.png">

