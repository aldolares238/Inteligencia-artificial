#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 56/60 Movimiento: Espacio de Configuración

import numpy as np
import matplotlib.pyplot as plt

#Definimos las dimensiones de la cuadrícula
grid_size = 10

#Creamos una matriz para representar la cuadrícula con todas las celdas inicialmente vacías
grid = np.zeros((grid_size, grid_size))

#Posición inicial de la partícula
particle_pos = [0, 0]

#Función para mostrar la cuadrícula con la partícula
def visualize(grid, particle_pos):
    plt.imshow(grid, cmap='Blues', origin='lower')
    plt.scatter(particle_pos[1], particle_pos[0], color='red', marker='o', s=100)
    plt.title("Movimiento de la partícula en la cuadrícula")
    plt.xlabel("Columna")
    plt.ylabel("Fila")
    plt.grid(True)
    plt.show()

#Mostramos la cuadrícula inicial con la partícula en su posición inicial
visualize(grid, particle_pos)

#Definimos las posibles direcciones de movimiento (arriba, abajo, izquierda, derecha)
movements = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#Probabilidades de elegir cada dirección de movimiento (inicialmente todas iguales)
probabilities = [0.25, 0.25, 0.25, 0.25]

#Realizamos un número de pasos definido
num_steps = 3
for step in range(num_steps):
    #Elegimos la dirección de movimiento según las probabilidades definidas
    direction = np.random.choice(range(len(movements)), p=probabilities)
    #Movemos la partícula en la dirección elegida
    movement = movements[direction]
    particle_pos[0] = (particle_pos[0] + movement[0]) % grid_size  # Controlamos el movimiento dentro de los límites de la cuadrícula
    particle_pos[1] = (particle_pos[1] + movement[1]) % grid_size
    #Mostramos la cuadrícula con la nueva posición de la partícula
    visualize(grid, particle_pos)

