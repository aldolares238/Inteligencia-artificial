#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 31/37 Búsqueda de Vuelta Atrás


import networkx as nx
import matplotlib.pyplot as plt

def backtracking_search(graph, start, goal):
    #Función principal que ejecuta la búsqueda de vuelta atrás
    
    #Inicializar una lista para rastrear los nodos visitados
    visited = []
    
    #Llamamos a la función de búsqueda de vuelta atrás recursiva
    path = backtrack(graph, start, goal, visited)
    
    if path:
        print("¡Se encontró un camino!")
        print("Camino encontrado:", path)
        return path
    else:
        print("No se encontró ningún camino desde", start, "a", goal)
        return None

def backtrack(graph, current, goal, visited):
    #Función recursiva para realizar la búsqueda de vuelta atrás
    
    #Marcamos el nodo actual como visitado
    visited.append(current)
    
    #Si el nodo actual es el nodo objetivo, retornar el camino
    if current == goal:
        return [current]
    
    #Recorremos los vecinos del nodo actual
    for neighbor in graph.neighbors(current):
        #Si el vecino no ha sido visitado, explorarlo recursivamente
        if neighbor not in visited:
            path = backtrack(graph, neighbor, goal, visited)
            #Si se encuentra un camino, agregar el nodo actual al camino y retornarlo
            if path:
                return [current] + path
    
    #Si no se encuentra ningún camino desde el nodo actual, retroceder
    return None

#Creamos un grafo de ejemplo
G = nx.Graph()
G.add_edges_from([(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (4, 7), (5, 8), (6, 9), (7, 10), (8, 9), (9, 10)])

#Mostramos el grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1000, font_size=12, font_weight='bold')
plt.title('Grafo de ejemplo')
plt.show()

#Ejecutamos la búsqueda de vuelta atrás en el grafo
start_node = 1
goal_node = 10
backtracking_search(G, start_node, goal_node)
