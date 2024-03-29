#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 25/37 Iteración de Valores

import networkx as nx
import matplotlib.pyplot as plt

#Se crea un grafo dirigido
G = nx.DiGraph()

#Añade nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

#Se añaden arcos al grafo con pesos
G.add_edge('A', 'B', weight=3)
G.add_edge('A', 'C', weight=5)
G.add_edge('B', 'C', weight=2)
G.add_edge('B', 'D', weight=6)
G.add_edge('C', 'D', weight=4)
G.add_edge('C', 'E', weight=7)
G.add_edge('D', 'E', weight=8)

#Diccionario que representa las asignaciones de valores iniciales para cada nodo
values = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0}

#Función que realiza una iteración del algoritmo de Iteración de Valores para el ejemplo
def value_iteration_step(graph, values):
    new_values = {}
    for node in graph.nodes:
        if node == 'E':  #El nodo 'E' tiene un valor fijo de 100
            new_values[node] = 100
        else:
            #Se calcula el nuevo valor del nodo como el máximo valor de sus sucesores más el peso del arco
            new_values[node] = max(
                values[successor] + graph[node][successor]['weight'] for successor in graph.successors(node))
    return new_values

#Realizamos 5 iteraciones del algoritmo
for i in range(5):
    values = value_iteration_step(G, values)
    print(f"Iteración {i+1}: {values}") #Imprimimos el resultado de la funcion

# Dibujamos el grafo con sus respectivos colores y tamaños de forma
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='lightblue', font_size=12, font_weight='bold')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title('Grafo con Iteración de Valores')
plt.show()
