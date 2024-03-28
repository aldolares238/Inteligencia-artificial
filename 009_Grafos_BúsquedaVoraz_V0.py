#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 9/37 Búsqueda Voraz Primero el Mejor

import networkx as nx
import matplotlib.pyplot as plt

# Función para realizar la búsqueda Voraz Primero el Mejor
def greedy_best_first_search(graph, start, goal): # La funcion recibe el grafo, el inicio y la meta
    visited = set()  # Conjunto de nodos visitados
    priority_queue = [(0, start)]  # Declaramos la Cola de prioridad con tuplas (heurística, nodo)
    
    while priority_queue: # Iteramos mmientras que la cola de prioridad contenga datos
        _, current_node = priority_queue.pop(0)  # Extraemos el nodo con la menor heurística
        visited.add(current_node)  # Marcar el nodo actual como nodo visitado
        
        if current_node == goal:  # Si se alcanza el nodo objetivo, terminar la búsqueda
            print("Se encontró el objetivo:", goal) # Imprimimos que hemos encontrado el objetivo
            break
        
        neighbors = graph.neighbors(current_node) # Obtenemos los nodos vecinos del nodo actual
        for neighbor in neighbors: # Iteramos mientras el nodo vecino sea actual
            if neighbor not in visited: # Verificamos si el nodo vecino no ha sido visitado
                heuristic = graph.nodes[neighbor]['heuristic']  # Obtenemos la heurística del vecino no visitado
                priority_queue.append((heuristic, neighbor))  # Agregar a la cola de prioridad
                
        priority_queue.sort(key=lambda x: x[0])  # Ordenar la cola por heurística

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_nodes_from([(1, {'heuristic': 10}), (2, {'heuristic': 7}), (3, {'heuristic': 5}), (4, {'heuristic': 3})])
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4)])

# Visualizar el grafo
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

# Ejecutar la búsqueda Voraz Primero el Mejor con los parametros seleccionados
greedy_best_first_search(G, 1, 4)
