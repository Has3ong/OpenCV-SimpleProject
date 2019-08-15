from PIL import Image
import pytesseract
import os

def TextRecognization():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    imageSource = BASE_DIR + '/Output.png'

    image = Image.open(imageSource)
    text = pytesseract.image_to_string(image)

    print(text)

if __name__ == '__main__':
    TextRecognization()