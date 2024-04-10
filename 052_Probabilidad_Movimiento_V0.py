#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 52/60 Movimiento

import numpy as np
import matplotlib.pyplot as plt

#Definimos una función para simular el movimiento basado en probabilidad
def movimiento_probabilistico(posicion_actual):
    #Definimos las probabilidades de moverse hacia la izquierda, derecha, arriba y abajo
    probabilidades = {'izquierda': 0.25, 'derecha': 0.25, 'arriba': 0.25, 'abajo': 0.25}
    
    #Elegimos aleatoriamente una dirección basada en las probabilidades para nuestro ejemplo
    direccion = np.random.choice(list(probabilidades.keys()), p=list(probabilidades.values()))
    
    #Movemos la posición en la dirección elegida
    if direccion == 'izquierda':
        posicion_actual[0] -= 1
    elif direccion == 'derecha':
        posicion_actual[0] += 1
    elif direccion == 'arriba':
        posicion_actual[1] += 1
    elif direccion == 'abajo':
        posicion_actual[1] -= 1
    
    return posicion_actual

#Definimos la posición inicial
posicion_actual = [0, 0]

#Realizamos el movimiento varias veces y almacenamos las posiciones
num_movimientos = 100
posiciones_x = [posicion_actual[0]]
posiciones_y = [posicion_actual[1]]
for _ in range(num_movimientos):
    posicion_actual = movimiento_probabilistico(posicion_actual)
    posiciones_x.append(posicion_actual[0])
    posiciones_y.append(posicion_actual[1])

#Graficamos el movimiento para mostrarlo al usuario añadiendo nombres y posiciones
plt.figure(figsize=(8, 6))
plt.plot(posiciones_x, posiciones_y, marker='o', linestyle='-', color='b')
plt.title('Movimiento Probabilístico')
plt.xlabel('Posición X')
plt.ylabel('Posición Y')
plt.grid(True)
plt.show()

