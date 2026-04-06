import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'D:\tesseract\tesseract.exe'
import numpy
import cv2

def get_zone(img):
    top_left = (2329, 5)
    bottom_right = (2493, 22)

    zone_name_img = img[
        top_left[1]:bottom_right[1],
        top_left[0]:bottom_right[0]
    ]
    zone_name_img = cv2.cvtColor(zone_name_img, cv2.COLOR_BGR2GRAY)
    zone_name_img = cv2.threshold(zone_name_img, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)[1]

    zone = pytesseract.image_to_string(zone_name_img)


    return zone
