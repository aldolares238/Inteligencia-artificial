#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 17/37 Problemas de Satisfacción de Restricciones

import networkx as nx
import matplotlib.pyplot as plt

# Definimos el grafo que representa el mapa
G = nx.Graph()
# Agregamos los nodos al grafo
G.add_nodes_from(["A", "B", "C", "D", "E", "F", "G"])
# Agregamos las aristas que representan las conexiones entre las regiones del mapa
G.add_edges_from([("A", "B"), ("A", "C"), ("B", "C"), ("B", "D"), ("C", "D"), ("C", "E"), ("D", "F"), ("E", "F"), ("E", "G"), ("F", "G")])

#Función para verificar si una asignación es válida o no
def is_valid(graph, coloring):
    for node in graph.nodes:
        for neighbor in graph.neighbors(node):
            #Verificamos si dos nodos adyacentes tienen el mismo color 
            if coloring[node] == coloring[neighbor]:
                return False
    return True

#Algoritmo de backtracking para colorear el mapa
def backtrack(graph, colors, assignment):
    #Verificamos si se ha alcanzado una asignación completa
    if len(assignment) == len(graph.nodes):
        return assignment
    
    #Seleccionamos un nodo que aún no ha sido asignado
    node = None
    for n in graph.nodes:
        if n not in assignment:
            node = n
            break
    
    #Probamos cada color disponible para el nodo seleccionado
    for color in colors:
        assignment[node] = color
        #Verificamos si la asignación actual es válida
        if is_valid(graph, assignment):
            #Si es válida, continuamos con la búsqueda recursiva
            result = backtrack(graph, colors, assignment)
            if result is not None:
                return result
        #Si la asignación no es válida, retroceder y probar otro color
        assignment.pop(node)
    
    #Si ninguna asignación válida fue encontrada, retornar None
    return None

#Colores disponibles para colorear el mapa
colors = ["red", "green", "blue"]

#Llamada al algoritmo de backtracking para colorear el mapa
color_assignment = backtrack(G, colors, {})

#Dibujar el mapa coloreado
pos = nx.spring_layout(G)
#Dibujar el grafo con etiquetas de nodos y colores asignados
nx.draw(G, pos, with_labels=True, node_color=[color_assignment[node] for node in G.nodes])
plt.show()
