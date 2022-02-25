# test file if you want to quickly try tesseract on a license plate image
import pytesseract
import cv2
import os
import numpy as np
import easyocr

# If you don't have tesseract executable in your PATH, include the following:
# pytesseract.pytesseract.tesseract_cmd = r'<full_path_to_your_tesseract_executable>'
# Example tesseract_cmd = r'C:\Program Files (x86)\Tesseract-OCR\tesseract'

# point to license plate image (works well with custom crop function)
gray = cv2.imread("C:/Users/lenovo/PycharmProjects/license-plate/download-1.png", 0)
gray = cv2.resize(gray, None, fx=3, fy=3, interpolation=cv2.INTER_CUBIC)
blur = cv2.GaussianBlur(gray, (5, 5), 0)
gray = cv2.medianBlur(gray, 3)
# perform otsu thresh (using binary inverse since opencv contours work better with white text)
ret, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_OTSU | cv2.THRESH_BINARY_INV)
cv2.imshow("Otsu", thresh)
cv2.waitKey(0)
rect_kern = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# apply dilation
dilation = cv2.dilate(thresh, rect_kern, iterations=1)
# cv2.imshow("dilation", dilation)
# cv2.waitKey(0)
# find contours
try:
    contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
except:
    ret_img, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

sorted_contours = sorted(contours, key=lambda ctr: cv2.boundingRect(ctr)[0])

# create copy of image
im2 = gray.copy()

plate_num = ""
# loop through contours and find letters in license plate
for cnt in sorted_contours:
        x, y, w, h = cv2.boundingRect(cnt)
        height, width = im2.shape

        # if height of box is not a quarter of total height then skip

        rect = cv2.rectangle(im2, (x, y), (x + w, y + h), (0, 255, 0), 2)
        roi = thresh[y - 5:y + h + 5, x - 5:x + w + 5]
        #roi = cv2.bitwise_not(roi)
        #roi = cv2.medianBlur(roi, 5)
        cv2.imshow("ROI", roi)
        cv2.waitKey(0)
        reader = easyocr.Reader(['en'])
        bounds = reader.readtext(roi)
        print(bounds)
        plate_num += bounds
print(plate_num)
cv2.imshow("Character's Segmented", im2)
cv2.waitKey(0)
cv2.destroyAllWindows()