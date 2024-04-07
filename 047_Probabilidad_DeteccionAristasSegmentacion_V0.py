#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 47/60 Detección de Aristas y Segmentación

import cv2
import numpy as np

#Inicializamos el objeto de captura de video
captura = cv2.VideoCapture(0)

#Declaramos el Loop para capturar imágenes continuamente desde la webcam
while True:
    #Capturamos un frame de la webcam
    ret, frame = captura.read()
    
    #Convertimos el frame a escala de grises
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    #Aplicamos un suavizado Gaussiano para reducir el ruido
    suavizado = cv2.GaussianBlur(gris, (5, 5), 0)

    #Detectamos los bordes con el algoritmo de Canny
    bordes = cv2.Canny(suavizado, 100, 200)

    #Mostramos la imagen original
    cv2.imshow('Imagen Original', frame)

    #Mostramos la imagen con los bordes detectados
    cv2.imshow('Bordes Detectados', bordes)
    
    #Esperamos a que el usuario presione 'q' para salir del loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Liberamos la captura de video y cerramos todas las ventanas
captura.release()
cv2.destroyAllWindows()
