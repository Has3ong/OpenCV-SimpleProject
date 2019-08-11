# Reading_Image

#### Image Read

```
> Section2-1.py

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
```

<img width=500 src="https://user-images.githubusercontent.com/44635266/62008457-acdc3e00-b191-11e9-9810-5b74c9ba0361.png">

#### Image Read and Save
```
> Section2-2.py

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

    cv2.imwrite('GrayDolphin.jpg', img)
    cv2.destroyAllWindows()
    cv2.waitKey(1)

if __name__=='__main__':
    readImage()
```

<img width=500 src="https://user-images.githubusercontent.com/44635266/62008381-933af680-b191-11e9-86f6-69f9b32136d6.png">