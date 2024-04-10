#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 55/60 Generación de Mapas: SLAM

import numpy as np
import matplotlib.pyplot as plt

#Definimos el tamaño del mapa
map_size = 100

#Inicializamos el mapa vacío con probabilidad uniforme para cada celda
mapa = np.ones((map_size, map_size)) * 0.5

#Definicion de Coordenadas iniciales del robot (posición desconocida)
pos_robot = [50, 50]

#Movimientos posibles del robot (arriba, abajo, izquierda, derecha)
movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#Función para simular la observación del robot
def observar(pos_robot, mapa, distancia_max=10):
    #Generar una observación simulada de una pared a una distancia aleatoria
    distancia_real = np.random.randint(1, distancia_max + 1)
    observacion = np.zeros((map_size, map_size))
    for dx in range(-distancia_max, distancia_max + 1):
        for dy in range(-distancia_max, distancia_max + 1):
            x, y = pos_robot[0] + dx, pos_robot[1] + dy
            if 0 <= x < map_size and 0 <= y < map_size:
                #Simular la probabilidad de detección basada en la distancia
                prob_deteccion = max(0, 1 - abs(np.linalg.norm([dx, dy]) - distancia_real) / distancia_max)
                #Actualizar la probabilidad en el mapa
                observacion[x, y] = mapa[x, y] * prob_deteccion
    #Normalizar las probabilidades
    observacion /= np.sum(observacion)
    return observacion

#Función para actualizar el mapa basado en la observación
def actualizar_mapa(mapa, observacion):
    mapa_nuevo = mapa * observacion
    # Normalizar las probabilidades
    mapa_nuevo /= np.sum(mapa_nuevo)
    return mapa_nuevo

#Realizar un número de iteraciones simulando el movimiento y la observación del robot
num_iteraciones = 10
for i in range(num_iteraciones):
    # Simular el movimiento del robot
    movimiento = np.random.choice(len(movimientos))
    dx, dy = movimientos[movimiento]
    pos_robot[0] += dx
    pos_robot[1] += dy
    
    #Simular la observación del robot
    observacion = observar(pos_robot, mapa)
    
    #Actualizar el mapa basado en la observación
    mapa = actualizar_mapa(mapa, observacion)

#Visualizar el mapa resultante
plt.imshow(mapa, cmap='hot', interpolation='nearest')
plt.title('Mapa generado por SLAM')
plt.colorbar(label='Probabilidad')
plt.show()
