#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 29/37 Red Bayesiana Dinámica

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido para representar la red bayesiana
G = nx.DiGraph()

# Añadimos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D'])

# Añadimos arcos (relaciones) entre los nodos
G.add_edges_from([('A', 'B'), ('B', 'C'), ('C', 'D'), ('D', 'A')])

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Layout para la visualización
nx.draw(G, pos, with_labels=True, node_size=3000, node_color='skyblue', font_size=20, font_weight='bold', arrowsize=20)
plt.title("Red Bayesiana Dinámica")
plt.show()
