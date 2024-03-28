#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10/37 Búsquedas A*

import matplotlib.pyplot as plt
import networkx as nx

def a_star(graph, start, goal): # Definimos la funcion de nuestra busqueda A*, con parametro de nodo, inicio y meta
    open_set = {start}  # Conjunto de nodos a explorar a partir del inicio especificado
    came_from = {}  # Diccionario para reconstruir el camino óptimo
    g_score = {start: 0}  # Costo real desde el nodo inicial hasta el nodo actual
    f_score = {start: heuristic(start, goal)}  # Estimación del costo total desde el inicio hasta el objetivo

    while open_set: # Mientras haya nodos sin explorar iteramos
        current = min(open_set, key=lambda node: f_score[node])  # Seleccionar el nodo con menor f_score

        if current == goal:  # Si hemos alcanzado el objetivo, reconstruir el camino y retornar nuestro resultaod
            return reconstruct_path(came_from, current)

        open_set.remove(current)  # Remover el nodo actual del conjunto de nodos a explorar ya que ha sido visitado
        for neighbor in graph[current]:  # Explorar los nodos vecinos del nodo actual
            tentative_g_score = g_score[current] + graph[current][neighbor]['weight']  # Calcular el costo tentativo desde el inicio hasta el vecino
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]: # Si el vecino no ha sido visitado o el nuevo costo es menor que el anterior
                # actualizar los registros y agregar el vecino al conjunto de nodos a explorar
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = g_score[neighbor] + heuristic(neighbor, goal)
                if neighbor not in open_set: # Si el vecino ya hasido explorado lo guardamos
                    open_set.add(neighbor)

    return None  # Si no se encuentra un camino, retornar None

def reconstruct_path(came_from, current):
    path = [current]  # Iniciar el camino con el nodo actual
    while current in came_from:  # Reconstruir el camino retrocediendo a través de los nodos visitados
        current = came_from[current] # Obtenemos el nodo precedente en el camino optimo
        path.append(current) # Agregamos al final de la lista el camino optimo encontrado
    return path[::-1]  # Invertir el camino para obtener la secuencia correcta

def heuristic(node, goal): # Definimos una busqueda heuristica
    return abs(node[0] - goal[0]) + abs(node[1] - goal[1])  # Heurística de distancia Manhattan util para busqueda de rutas

# Crear un grafo de ejemplo
graph = {
    (0, 0): {(0, 1): {'weight': 1}, (1, 0): {'weight': 1}},
    (0, 1): {(0, 0): {'weight': 1}, (1, 1): {'weight': 1}},
    (1, 0): {(0, 0): {'weight': 1}, (2, 0): {'weight': 1}},
    (1, 1): {(0, 1): {'weight': 1}, (1, 2): {'weight': 1}, (2, 1): {'weight': 1}},
    (2, 0): {(1, 0): {'weight': 1}, (2, 1): {'weight': 1}},
    (2, 1): {(1, 1): {'weight': 1}, (2, 2): {'weight': 1}},
    (1, 2): {(1, 1): {'weight': 1}, (2, 2): {'weight': 1}},
    (2, 2): {(1, 2): {'weight': 1}, (2, 1): {'weight': 1}}
}

# Ejecutar el algoritmo A*
start = (0, 0)
goal = (2, 2)
path = a_star(graph, start, goal)

# Visualizar el resultado
G = nx.Graph(graph)
pos = {(x, y): (y, -x) for x, y in G.nodes()}  # Posiciones de los nodos para la visualización
nx.draw(G, pos, with_labels=True, node_size=700, node_color='lightblue')  # Dibujar el grafo base
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=700)  # Resaltar nodos en el camino óptimo
nx.draw_networkx_edges(G, pos, edgelist=[(path[i], path[i+1]) for i in range(len(path)-1)], edge_color='red', width=2)  # Dibujar aristas del camino óptimo
plt.axis('equal')
plt.show()

print("El camino encontrado por el algoritmo A* es:", path)
