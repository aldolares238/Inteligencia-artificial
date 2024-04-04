#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 27/60 Modelos de Markov Ocultos

import numpy as np
import matplotlib.pyplot as plt

#Definimos los estados ocultos y las observaciones generales
hidden_states = ['soleado', 'lluvioso']
observations = ['paraguas', 'sin paraguas']

#Definimos las Probabilidades iniciales de los estados ocultos
initial_probabilities = np.array([0.6, 0.4])

#Agregamos la Matriz de transición entre estados ocultos
transition_probabilities = np.array([[0.7, 0.3],
                                     [0.4, 0.6]])

#Definimos la Matriz de emisión de observaciones dadas los estados ocultos
emission_probabilities = np.array([[0.9, 0.1],
                                   [0.2, 0.8]])

#Declaramos una Función para generar una secuencia de observaciones y estados ocultos
def generate_sequence(length):
    hidden_states_sequence = [np.random.choice(len(hidden_states), p=initial_probabilities)]
    observations_sequence = [np.random.choice(len(observations), p=emission_probabilities[hidden_states_sequence[0]])]
    
    for _ in range(1, length):
        hidden_state = np.random.choice(len(hidden_states), p=transition_probabilities[hidden_states_sequence[-1]])
        observation = np.random.choice(len(observations), p=emission_probabilities[hidden_state])
        hidden_states_sequence.append(hidden_state)
        observations_sequence.append(observation)
    
    return hidden_states_sequence, observations_sequence

#Generamos una secuencia de observaciones y estados ocultos
sequence_length = 5
hidden_states_sequence, observations_sequence = generate_sequence(sequence_length)

#Imprimimos y mostramos la secuencia de observaciones y los estados ocultos correspondientes
print("Secuencia de observaciones generada:", [observations[i] for i in observations_sequence])
print("Estados ocultos correspondientes:", [hidden_states[i] for i in hidden_states_sequence])

#Graficamos los estados ocultos generados para el usuario
plt.figure(figsize=(10, 6))
plt.plot(hidden_states_sequence, marker='o', linestyle='', markersize=10)
plt.yticks([0, 1], hidden_states)
plt.title("Secuencia de estados ocultos generados")
plt.xlabel("Tiempo")
plt.ylabel("Estado oculto")
plt.grid(True)
plt.show()
