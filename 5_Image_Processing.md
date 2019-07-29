# Image_Processing

#### Scan Effect
```
> Section5-1.py

import numpy as np
import cv2
import os

def null(x):
    pass

def ImageProcessing():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/BusinessCard.jpg'
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
```

<img width=500 src="https://user-images.githubusercontent.com/44635266/62021504-7be82180-b202-11e9-892c-90a3dc7bcc20.png">

#### Gaussian Blur

<img width=500 src="https://user-images.githubusercontent.com/44635266/62019380-8ce06500-b1f9-11e9-8e62-b04dfb59105e.png">

```
> Section5-2.py

import cv2
import os

def ImageProcessing():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imgsrc = BASE_DIR + '/BusinessCard.jpg'
    img = cv2.imread(imgsrc, cv2.IMREAD_GRAYSCALE)

    r = 600.0 / img.shape[0]
    dim = (int(img.shape[1] * r), 600)
    img = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

    blur = cv2.GaussianBlur(img, (5, 5), 0)

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
```

* Results


<img width="500" src="https://user-images.githubusercontent.com/44635266/62021447-45120b80-b202-11e9-9c62-37671b09c283.png">

<img width="500" src="https://user-images.githubusercontent.com/44635266/62021449-46dbcf00-b202-11e9-8554-ef7c91643e8f.png">


