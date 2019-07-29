from PIL import Image
import pytesseract

def TextRecognization():
    imageSource = 'Output.png'
    image = Image.open(imageSource)

    text = pytesseract.image_to_string(image)
    print(text)

if __name__ == '__main__':
    TextRecognization()