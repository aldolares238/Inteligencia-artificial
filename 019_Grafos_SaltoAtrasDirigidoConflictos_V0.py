#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 19/37 Salto Atrás Dirigido por Conflictos

import networkx as nx
import matplotlib.pyplot as plt

#Crearemos un grafo dirigido con el que vamos a trabajar
G = nx.DiGraph()

#Agregamos nodos al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

#Agregamos aristas al grafo
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 4), (4, 5)])

#Función para realizar la búsqueda utilizando Backjumping como lo solicita el programa
def backjumping(graph, start, goal, path=[]):
    # Agregamos el nodo actual al camino, asi iniciamos el proceso
    path = path + [start]
    #Si el nodo actual es el objetivo, retornamos el camino indicando que se terminó
    if start == goal:
        return path
    #Si el nodo actual no está en el grafo, retornamos None por algun error
    if not graph.has_node(start):
        return None
    #Iteramos sobre los sucesores del nodo actual para seguir la busqueda
    for node in graph.successors(start):
        #Si el nodo ya está en el camino, continuamos con el siguiente sucesor
        if node in path:
            continue
        #Realizamos la búsqueda recursiva
        new_path = backjumping(graph, node, goal, path)
        #Si se encuentra un camino válido, lo regresamos como un resultado
        if new_path:
            return new_path
    #Si ningún sucesor lleva a una solución, retrocedemos y realizamos un salto atrás
    return None

#Realizamos la búsqueda desde el nodo 1 al nodo 5 del grafo creado
result = backjumping(G, 1, 5)

# Mostramos el camino encontrado de manera grafica para el usuario
if result:
    print("Camino encontrado:", result)
    #Dibujamos el grafo con el camino resaltado para el usuario
    pos = nx.spring_layout(G)  # Posición de los nodos
    nx.draw(G, pos, with_labels=True, arrows=True)
    nx.draw_networkx_nodes(G, pos, nodelist=result, node_color='r')  #Resaltamos el camino en rojo
    plt.show()
else:
    print("No se encontró un camino desde el nodo inicial al nodo objetivo.")

