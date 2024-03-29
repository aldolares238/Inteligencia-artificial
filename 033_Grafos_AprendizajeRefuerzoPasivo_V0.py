#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 33/37 Aprendizaje por Refuerzo Pasivo

import networkx as nx
import matplotlib.pyplot as plt
import random

#Creamos un grafo dirigido
G = nx.DiGraph()

#Añadimos nodos al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

#Añadimos aristas al grafo
G.add_edge(1, 2, reward=0)  # Nodo 1 conectado con el Nodo 2 con recompensa 0
G.add_edge(1, 3, reward=0)  # Nodo 1 conectado con el Nodo 3 con recompensa 0
G.add_edge(2, 4, reward=0)  # Nodo 2 conectado con el Nodo 4 con recompensa 0
G.add_edge(3, 4, reward=100)  # Nodo 3 conectado con el Nodo 4 con recompensa 100
G.add_edge(4, 5, reward=0)  # Nodo 4 conectado con el Nodo 5 con recompensa 0

#Dibujamos el grafo con las caracteristicas necesarias para verlo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=20, font_weight="bold")
edge_labels = nx.get_edge_attributes(G, 'reward')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

#Mostramos el grafo
plt.title("Grafo con recompensas")
plt.show()

#Definimos función para que el agente tome una acción aleatoria
def take_random_action(current_node):
    neighbors = list(G.neighbors(current_node))
    return random.choice(neighbors)

#Definimos nodo inicial y nodo objetivo
current_node = 1
goal_node = 5

#Realizamos movimientos aleatorios hasta llegar al nodo objetivo
while current_node != goal_node:
    next_node = take_random_action(current_node)
    print(f"Desde el nodo {current_node} al nodo {next_node} con recompensa {G[current_node][next_node]['reward']}")
    current_node = next_node

print("¡Llegaste al nodo objetivo!")
