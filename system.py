import cv2
import numpy as np
import pytesseract
from PIL import Image
import LPR

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

cap = cv2.VideoCapture(0) 

lpr = LPR.LPR()

while True:
    ret, frame = cap.read()

    if not ret:
        print("Error al capturar video")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)

    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for contour in contours:
        area = cv2.contourArea(contour)
        if area > 1000:
            x, y, w, h = cv2.boundingRect(contour)
            aspect_ratio = w / float(h)
            if 2.5 < aspect_ratio < 4.0:
                cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

                plate_region = gray[y:y + h, x:x + w]
                plate_text = pytesseract.image_to_string(plate_region, config='--psm 7')
                print("Texto de la placa:", plate_text)

    cv2.imshow('Reconocimiento de placas', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
