#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 14/60 Monte Carlo para Cadenas de Markov

import numpy as np
import matplotlib.pyplot as plt

#Definimos las dimensiones de la cuadrícula
grid_size = 10

#Definimos la posición inicial del agente
initial_position = (0, 0)

#Definimos las posibles acciones: arriba, abajo, izquierda, derecha
actions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

#Definimos la función para verificar si una acción es válida
def is_valid_action(position, action):
    new_position = tuple(np.add(position, action))
    return 0 <= new_position[0] < grid_size and 0 <= new_position[1] < grid_size

#Definimos la función para obtener el siguiente estado dado un estado actual y una acción
def get_next_state(position, action):
    if is_valid_action(position, action):
        return tuple(np.add(position, action))
    else:
        return position

#Definimos la función para realizar un paso en el juego de camino aleatorio
def random_walk_step(position):
    action = actions[np.random.choice(len(actions))]
    return get_next_state(position, action)

#Definimos la función para simular múltiples pasos en el juego de camino aleatorio
def simulate_random_walk(steps):
    positions = [initial_position]
    for _ in range(steps):
        next_position = random_walk_step(positions[-1])
        positions.append(next_position)
    return positions

#Simulamos el juego de camino aleatorio
steps = 1000
positions = simulate_random_walk(steps)

#Graficamos el camino aleatorio para el ejemplo
x, y = zip(*positions)
plt.plot(x, y, marker='o', linestyle='-')
plt.title('Camino Aleatorio en una Cuadrícula 2D')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.show()
