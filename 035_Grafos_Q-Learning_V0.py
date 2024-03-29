#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 35/37 Q-Learning

import networkx as nx
import matplotlib.pyplot as plt
import random

#Creamos un grafo dirigido
G = nx.DiGraph()

#Añadimos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D'])

#Añadimos aristas con un peso aleatorio entre 1 y 10
G.add_edge('A', 'B', weight=random.randint(1, 10))
G.add_edge('A', 'C', weight=random.randint(1, 10))
G.add_edge('B', 'D', weight=random.randint(1, 10))
G.add_edge('C', 'D', weight=random.randint(1, 10))

#Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color="skyblue", font_size=20, font_weight="bold", arrowsize=20)
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.show()

#Implementación básica del algoritmo Q-Learning

#Inicializamos la matriz Q con ceros
Q = {}
for node in G.nodes:
    for neighbor in G.neighbors(node):
        Q[(node, neighbor)] = 0

#Definimos el factor de aprendizaje y el factor de descuento
alpha = 0.1  # Factor de aprendizaje
gamma = 0.6  # Factor de descuento

#Definimos la función para elegir una acción basada en la matriz Q (exploración vs explotación)
def choose_action(state):
    possible_actions = [action for action in G.neighbors(state)]
    return random.choice(possible_actions)

#Ejecutamos el algoritmo de Q-Learning
epochs = 1000
for _ in range(epochs):
    current_state = random.choice(list(G.nodes))
    while current_state != 'D':  #Hasta que alcancemos el nodo objetivo 'D'
        action = choose_action(current_state)
        next_state = action
        max_reward = max([Q[(next_state, neighbor)] for neighbor in G.neighbors(next_state)])
        Q[(current_state, action)] = (1 - alpha) * Q[(current_state, action)] + alpha * (G[current_state][action]['weight'] + gamma * max_reward)
        current_state = next_state

#Mostramos la matriz Q resultante
print("Matriz Q:")
for key, value in Q.items():
    print(key, value)
