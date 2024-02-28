import cv2
import numpy as np
import pytesseract
from PIL import Image

#Videocaptura
cap = cv2.Videocapture() #Pendiente por definir la ruta

Ctexto = ''

#While True
while True:
    #Lectura de la videocaptura
    ret, frame = cap.read()

    if ret == false:
        break

    #Dibujo del rectángulo donde se mostrarán las placas identificadas
    cv2.rectangle(frame, (870, 750), (1070, 850), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, Ctexto[0:9], (900, 810), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
