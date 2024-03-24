#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 3/37  Búsqueda en Profundidad

import networkx as nx
import matplotlib.pyplot as plt

def dfs(graph, start, visited=None): # Definimos una funcion para busqueda en profundidad, con parametros del grafo, start y nodos visitados
    if visited is None: # Si no hay nodos visitados definimos el conjutno visited como vacio
        visited = set()
    visited.add(start) # Agregamos el nodo inicial al conjunto de nodos visitados para iniciar el proceso
    print(start)  # Imprime el nodo actual, en este caso el inicial
    for neighbor in graph[start]: #Hacemos la iteracion para los nodos vecinos al nodo actual
        if neighbor not in visited: # Verificamos que el nodo vecino no haya sido visitado
            dfs(graph, neighbor, visited) # En caso de que no sea visitado, llamamos a la funcion para visitarlo

# Definimos el grafo general para nuestro ejemplo aleatorio
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Creamos un grafo de NetworkX a partir del grafo inicial para poder mostrarlo
G = nx.Graph(graph)

# Realizamos el recorrido DFS y almacenamos los nodos visitados
visited_nodes = set() #Aqui almacenaremos los nodos visitados durante el recorrido
dfs(G, 'A', visited_nodes) # Realizamos la busqueda en profundidad con los parametros establecidos

# Creamos una lista de colores para los nodos visitados
node_colors = ['red' if node in visited_nodes else 'blue' for node in G.nodes()]

# Dibujamos el grafo con los nodos visitados resaltados
nx.draw(G, with_labels=True, node_color=node_colors)
plt.show()

