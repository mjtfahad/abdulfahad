import cv2
import pytesseract
from PIL import Image
def main():
    path = input()

    image = cv2.imread(path)

    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    temp = input("Do you want to pre-process the image ?nThreshold : 1nGrey : 2nNone : 0nEnter your choice : ").strip()

    if temp == "1":
         gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    elif temp == "2":
         gray = cv2.medianBlur(gray, 3)

    filename = "{}.png".format("temp")
    cv2.imwrite(filename, gray)

    text = pytesseract.image_to_string(Image.open(filename))
    print(text)
 
try: 
    main()
except Exception as e:
     print(e.args)