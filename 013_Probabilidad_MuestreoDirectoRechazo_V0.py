#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 13/60 Ponderación de Verosimilitud

import numpy as np
import matplotlib.pyplot as plt

#Definimos la probabilidad inicial de un evento (por ejemplo, lanzar una moneda)
probabilidad_evento = 0.5

#Definimos las observaciones (0 para cara, 1 para cruz)
observaciones = [0, 1, 0, 0, 1, 1, 0, 1, 1, 1]

#Inicializamos la lista para almacenar las probabilidades actualizadas
probabilidades_actualizadas = []

#Iteramos sobre las observaciones y actualizar la probabilidad
for observacion in observaciones:
    if observacion == 0:
        #Si la observación es cara, actualizar la probabilidad multiplicándola por 0.6
        probabilidad_evento *= 0.6
    else:
        #Si la observación es cruz, actualizar la probabilidad multiplicándola por 0.4
        probabilidad_evento *= 0.4
    probabilidades_actualizadas.append(probabilidad_evento)

#Creamos un array de números para representar los pasos
pasos = np.arange(1, len(observaciones) + 1)

#Graficamos la evolución de la probabilidad
plt.plot(pasos, probabilidades_actualizadas, marker='o')
plt.xlabel('Número de observaciones')
plt.ylabel('Probabilidad')
plt.title('Evolución de la probabilidad usando ponderación de verosimilitud')
plt.grid(True)
plt.show()

#Mostramos la probabilidad final
print("La probabilidad final del evento después de todas las observaciones es:", probabilidad_evento)


