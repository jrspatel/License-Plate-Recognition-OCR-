
import cv2
from PIL import Image as im

# getting the cropped image shapes
def Cropped_Images(outputs,img_path):
    image = cv2.imread(img_path)
    num = 1
    for axes in (outputs['detections']['labels']):
        print(axes['x'], axes['y'], axes['height'], axes['width'])
        x_min = axes['x']
        x_max = axes['x'] + axes['width']

        y_min = axes['y']
        y_max = axes['y'] + axes['height']


        ci = image[y_min:y_max, x_min:x_max]
        print(ci)
        org_image = im.fromarray(ci)

        org_image.save('C:/Users/lenovo/PycharmProjects/license-plate/cropped-image/new_{}.jpg'.format(num))
        num+=1


        '''ci = np.array_str(ci)
        img = cv2.imread(ci)
        cv2.imshow('Result', img)
        cv2.waitKey(0)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
        text = pytesseract.image_to_string(img)
        print(text)'''







