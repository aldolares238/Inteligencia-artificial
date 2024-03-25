#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 4/37  Búsqueda en Profundidad limitada

import networkx as nx
import matplotlib.pyplot as plt

# Implementación de Búsqueda en Profundidad Limitada (DLS)

def dls(graph, start, goal, depth_limit): # Definimos una nueva funcion para la busqueda en profundidad limitada, con los parametros grafo, inicio, meta y limite de profundidad
    def recursive_dls(node, depth): # Para esta funcion se toma un nodo y nivel de profundidad como parametros
        if depth == 0 and node == goal: # Si la profundida es 0 y el nodo es la meta asignada se devuelve un True
            return True
        elif depth > 0: # Si la profundidad es mayor a cero se recorren los vecinos del nodo en cuestion
            for neighbor in graph.get(node, []):
                if recursive_dls(neighbor, depth - 1):#Si la condicion se cumple, devuelve un true
                    return True
        return False #Si ninguna de las llamadas devuelve verdadero, la funcion devuelve falso

    return recursive_dls(start, depth_limit) #Se regresan los resultados de la funcion

# Defininimos el grafo con el que vamos a trabajar
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}

# Nodo de inicio y nodo objetivo
start_node = 'A' #Este seria el nodo de inicio de la busqueda necesaria
goal_node = 'F' #Este es el nodo meta para la busqueda

# Límite de profundidad para la búsqueda
depth_limit = 3

# Realizar la búsqueda en profundidad limitada y con los parametros planteados
found = dls(graph, start_node, goal_node, depth_limit)

# Imprimir el resultado de la búsqueda
if found: #Si se devuelve un valor acorde a la funcion de busqueda nos entrega el siguiente mensaje con los parametros añadidos
    print(f"Se encontró un camino desde {start_node} hacia {goal_node} dentro del límite de profundidad {depth_limit}.")
else: #Caso contrario nos indicaria que no se encontró el camino dentro del rango especificado
    print(f"No se encontró un camino desde {start_node} hacia {goal_node} dentro del límite de profundidad {depth_limit}.")

# Crear un grafo dirigido desde el diccionario de listas de adyacencia
G = nx.DiGraph(graph)

# Colorear el camino encontrado para una mejor visualización del usuario
path_nodes = nx.shortest_path(G, source=start_node, target=goal_node) #Aqui almacenamos nuestro camino mas corto encontrado en la busqueda
edge_labels = {tuple(path_nodes[i:i+2]): i+1 for i in range(len(path_nodes) - 1)} #Asignamos etiquetas a las aristas para mejor muestra
node_colors = ['red' if node in path_nodes else 'blue' for node in G.nodes()] #Añadimos colores a los nodos depende si se visitaron o no

# Dibujar el grafo con las siguientes especificaciones
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color=node_colors, arrows=True)
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Mostrar el grafo
plt.title("Búsqueda en Profundidad Limitada")
plt.show()


