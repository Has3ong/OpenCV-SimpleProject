# Text_Recognization

#### Tesseract

```
> Section7-1.py

from PIL import Image
import pytesseract

def TextRecognization():
    imageSource = 'Output.png'
    image = Image.open(imageSource)

    text = pytesseract.image_to_string(image)
    print(text)

if __name__ == '__main__':
    TextRecognization()
```


* Results

```
QUEUE

COFFEE >

COFFEEQUEUE

QUEUE

/ COFFEEQUEUE
```