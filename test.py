import pytesseract
import cv2
import os
import glob
import re
import easyocr
import numpy as np

def show_result(path):

    pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
    result = {}
    result['detections'] = []
    for file in glob.glob(path):
        print(file)
        img = cv2.imread(file)

                        #cv2.imshow('Result', img)
                        #cv2.waitKey(0)
                        #boxes = pytesseract.image_to_boxes(img)

        cv2.imshow('img', img)
        cv2.waitKey(0)

        img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

                        #text = pytesseract.image_to_string(img,lang = 'eng')
                        #clean_text = re.sub('[\W_]+','',text)
        reader  = easyocr.Reader(['en'])
        bounds = reader.readtext(img1)
        result['detections'].append(bounds[0][1])

    return result






















