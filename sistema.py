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

    #Extracción de ancho y alto de fotogramas
    al, an, c = frame.shape

    #Tomar el centro de la imagen
    #En x:
    x1 = int(an / 3) #Tomando el 1/3 de la imagen
    x2 = int(x1 * 2) #Hasta el inicio del 3/3 de la imagen

    #En y:
    y1 = int(al / 3)
    y2 = int(y1 * 2)

    #Dibujo del rectángulo que contiene el Texto "Procesando placa"
    cv2.rectangle(frame, (x1 + 160, y1 + 500), (1120, 940), (0, 0, 0), cv2.FILLED)
    cv2.putText(frame, 'Procesando placa', (x1 + 180, y1 + 550), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)



