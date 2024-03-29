#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 34/37 Aprendizaje por Refuerzo Activo

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Creamos un grafo dirigido
G = nx.DiGraph()

#Agregamos nodos al grafo
G.add_nodes_from([1, 2, 3, 4])

#Agregamos bordes (aristas) con pesos
G.add_edge(1, 2, weight=1)
G.add_edge(1, 3, weight=2)
G.add_edge(2, 3, weight=2)
G.add_edge(2, 4, weight=3)
G.add_edge(3, 4, weight=1)

#Inicializamos la matriz de recompensas
R = np.array([
    [-1, -1, -1, -1],
    [-1, -1, -1, 100],
    [-1, -1, -1, 100],
    [-1, -1, -1, -1]
])

#Inicializamos la matriz Q
Q = np.zeros_like(R)

#Definimos la tasa de aprendizaje
learning_rate = 0.8

#Definimos el factor de descuento
discount_factor = 0.9

#Definimos el número de episodios de entrenamiento
num_episodes = 1000

#Algoritmo de Q-Learning
for _ in range(num_episodes):
    #Seleccionamos un estado inicial aleatorio
    current_state = np.random.randint(0, 4)
    
    #Mientras no lleguemos al estado objetivo
    while current_state != 3:
        #Verificamos si hay acciones posibles desde el estado actual
        possible_actions = np.where(R[current_state] >= 0)[0]
        if len(possible_actions) == 0:
            break
        
        #Seleccionamos una acción aleatoria
        action = np.random.choice(possible_actions)
        
        #Obtenemos el máximo valor Q del próximo estado
        next_state = action
        future_rewards = Q[next_state, :]
        max_future_reward = np.max(future_rewards)
        
        #Calculamos el nuevo valor de Q
        reward = R[current_state, action]
        Q[current_state, action] = (1 - learning_rate) * Q[current_state, action] + \
                                   learning_rate * (reward + discount_factor * max_future_reward)
        
        #Pasamos al próximo estado
        current_state = next_state

#Mostramos la matriz Q
print("Matriz Q después del entrenamiento:")
print(Q)

#Dibujamos el grafo
plt.figure(figsize=(8, 6))
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500, arrows=True)

#Agregamos etiquetas de peso a los bordes
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#Mostramos el grafo
plt.show()
