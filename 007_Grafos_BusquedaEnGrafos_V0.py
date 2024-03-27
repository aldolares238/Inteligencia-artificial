#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 7/37  Búsqueda en Grafos

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido con el que vamos a trabajar
G = nx.DiGraph()

# Agregamos nodos al grafo
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

# Agregamos aristas ponderadas al grafo para su busqueda
G.add_weighted_edges_from([
    ("A", "B", 1),
    ("A", "C", 1),
    ("B", "D", 1),
    ("B", "E", 1),
    ("C", "E", 1),
    ("D", "F", 1),
    ("E", "F", 1)
])

# Función de búsqueda en grafos
def bfs(graph, start):
    visited = set()  # Conjunto para almacenar nodos visitados
    queue = [start]  # Cola para almacenar nodos por visitar

    while queue: # Mientras la cola contenga datos
        node = queue.pop(0)  # Tomamos el primer nodo de la cola
        if node not in visited: # Si el nodo actual no ha sido visitado...
            print(node)  # Mostramos el nodo visitado actual
            visited.add(node)  # Marcamos el nodo como visitado
            neighbors = graph.neighbors(node)  # Obtenemos los vecinos del nodo
            queue.extend(neighbors)  # Agregamos los vecinos a la cola

# Ejecutamos la búsqueda en el grafo comenzando desde el nodo "A"
bfs(G, "A")

# Dibujamos el grafo
nx.draw(G, with_labels=True, node_size=1000, node_color="lightblue", font_size=12, font_weight="bold")
plt.show()
