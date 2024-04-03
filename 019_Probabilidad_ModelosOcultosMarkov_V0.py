    #Nombre: Aldo Emiliano Chavez Lares
    #Registro: 21310238
    #Grupo: 6E1
    #Practica: 19/60 Modelos Ocultos de Markov

import numpy as np
import matplotlib.pyplot as plt

#Definimos el modelo HMM con 2 estados ocultos y 2 observaciones posibles
#Creamos la Matriz de transición entre estados
transition_matrix = np.array([[0.7, 0.3], [0.4, 0.6]])

#Definiomos las Probabilidades iniciales de los estados
initial_probabilities = np.array([0.6, 0.4])

#Definimos las Probabilidades de emisión de cada estado
emission_probabilities = np.array([[0.2, 0.8], [0.6, 0.4]])

#Declaramos una Función para generar una secuencia de observaciones y estados ocultos
def generate_sequence(num_steps):
    # Inicializar la secuencia de estados y observaciones
    states = []
    observations = []

    #Elegimos el estado inicial
    current_state = np.random.choice(range(2), p=initial_probabilities)
    states.append(current_state)

    #Generamos observaciones y estados ocultos para cada paso de tiempo
    for _ in range(num_steps):
        #Generamos la observación actual
        observation = np.random.choice(range(2), p=emission_probabilities[current_state])
        observations.append(observation)

        #Actualizamos el estado actual
        current_state = np.random.choice(range(2), p=transition_matrix[current_state])
        states.append(current_state)

    return states, observations

#Generamos una secuencia de observaciones y estados ocultos
np.random.seed(42)
states, observations = generate_sequence(100)

#Graficamos la secuencia de estados ocultos y de observaciones
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(states, 'r-', label='Estado Real')
plt.title('Secuencia de Estados Ocultos')
plt.xlabel('Tiempo')
plt.ylabel('Estado')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(observations, 'g-')
plt.title('Secuencia de Observaciones')
plt.xlabel('Tiempo')
plt.ylabel('Observación')
#Mostramos los resultados con sus respectivas caracteristicas al usuario
plt.tight_layout()
plt.show()


