#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 18/60 Algoritmo Hacia Delante-Atrás


import numpy as np

#Definimos los parámetros del modelo
#Probabilidades de transición entre estados
transition_probabilities = np.array([
    [0.7, 0.3],  #Probabilidades de pasar de S0 a S0 y S1 respectivamente
    [0.4, 0.6]   #Probabilidades de pasar de S1 a S0 y S1 respectivamente
])

#Definimos las Probabilidades de emisión de las observaciones dadas los estados
emission_probabilities = np.array([
    [0.9, 0.1],  #Probabilidad de observar O1 dado S0 y S1 respectivamente
    [0.2, 0.8]   #Probabilidad de observar O2 dado S0 y S1 respectivamente
])

#Definimos la Lista de observaciones
observations = [0, 1]  #0 representa O1 y 1 representa O2

#Realizamos una funcion con el Algoritmo Forward-Backward
def forward_backward(observations, transition_probabilities, emission_probabilities):
    num_states = transition_probabilities.shape[0]
    num_observations = len(observations)
    
    #Forward pass
    forward = np.zeros((num_observations, num_states))
    forward[0] = np.array([1, 1])  # Inicialización
    
    for t in range(1, num_observations):
        for j in range(num_states):
            forward[t, j] = sum(forward[t-1, i] * transition_probabilities[i, j] * emission_probabilities[j, observations[t]] for i in range(num_states))
    
    #Backward pass
    backward = np.zeros((num_observations, num_states))
    backward[-1] = np.array([1, 1])  # Inicialización
    
    for t in range(num_observations - 2, -1, -1):
        for i in range(num_states):
            backward[t, i] = sum(transition_probabilities[i, j] * emission_probabilities[j, observations[t+1]] * backward[t+1, j] for j in range(num_states))
    
    #Calculamos la probabilidad conjunta de las observaciones
    joint_probabilities = forward * backward
    total_probability = joint_probabilities[-1].sum()
    
    #Calculamos las probabilidades marginales de los estados
    state_probabilities = joint_probabilities / total_probability
    
    return state_probabilities

#Ejecutamos el algoritmo
state_probs = forward_backward(observations, transition_probabilities, emission_probabilities)
print("Probabilidades marginales de los estados dadas las observaciones:")
print(state_probs)

#Gráficamente representamos las probabilidades marginales de los estados para el usuario
import matplotlib.pyplot as plt

states = ['S0', 'S1']
plt.bar(states, state_probs[-1])
plt.title('Probabilidades marginales de los estados')
plt.xlabel('Estados')
plt.ylabel('Probabilidad')
plt.show()
