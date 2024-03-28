#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 12/37 Búsqueda Tabú

import networkx as nx
import random
import matplotlib.pyplot as plt

# Función para crear el grafo de ejemplo
def create_graph():
    G = nx.Graph()
    G.add_nodes_from(range(1, 6))  # Creamos 5 ciudades numeradas del 1 al 5
    edges = [(1, 2, 7), (1, 3, 9), (1, 4, 14), (2, 3, 10), (2, 5, 15), (3, 4, 11), (3, 5, 2), (4, 5, 9)]
    G.add_weighted_edges_from(edges)  # Añadimos rutas con costos asociados
    return G

# Función para calcular el costo total de un camino en el grafo
def objective_function(graph, path):
    cost = 0
    for i in range(len(path) - 1): # Iteramos sobre los nodos del camino especificados
        cost += graph[path[i]][path[i+1]]['weight']  # Sumamos el costo de cada arista en el camino
    return cost

# Función de Búsqueda Tabú para encontrar el camino óptimo en el grafo
def tabu_search(graph, starting_node, max_iter, tabu_size): # Parametros especificados
    current_node = starting_node # El primer nodo es el nodo de inicio
    tabu_list = [] # Definimos la lista tabu inicial
    best_path = [current_node] # Iniciamos nuestro mejor ccamino

    for _ in range(max_iter): # Iteraomos con un maximo de iteraciones
        neighbors = list(graph.neighbors(current_node))  # Obtener los nodos vecinos del nodo actual
        neighbors = [n for n in neighbors if n not in tabu_list]  # Filtrar los vecinos que no están en la lista tabú

        if not neighbors:
            break
        
        next_node = random.choice(neighbors)  # Elegir aleatoriamente un vecino como siguiente nodo
        tabu_list.append(next_node)  # Agregar el siguiente nodo a la lista tabú
        if len(tabu_list) > tabu_size:
            tabu_list.pop(0)  # Mantener el tamaño de la lista tabú

        current_node = next_node
        best_path.append(current_node)  # Agregar el siguiente nodo al camino

        # Actualizar el mejor camino si se encuentra un camino más corto
        if objective_function(graph, best_path) < objective_function(graph, tabu_list):
            best_path = tabu_list.copy()

    return best_path

# Crear el grafo
graph = create_graph()

# Parámetros de búsqueda
starting_node = 1  # Nodo de inicio
max_iter = 50  # Número máximo de iteraciones
tabu_size = 3  # Tamaño de la lista tabú

# Ejecutar búsqueda tabú
best_path = tabu_search(graph, starting_node, max_iter, tabu_size)

# Imprimir resultado
print("El camino óptimo encontrado es:", best_path)
print("El costo del camino óptimo es:", objective_function(graph, best_path))

# Visualización del grafo y el camino encontrado
pos = nx.spring_layout(graph)  # Posiciones de los nodos para graficar
nx.draw(graph, pos, with_labels=True, node_color='lightblue')
nx.draw_networkx_edges(graph, pos, edgelist=[(best_path[i], best_path[i+1]) for i in range(len(best_path)-1)], edge_color='red', width=2)  # Dibujar el camino óptimo en rojo
plt.title('Búsqueda Tabú en Grafo - Ejemplo básico')
plt.show()
