#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 37/59 Grafos de Planificación: GRAPHPLAN

import matplotlib.pyplot as plt

# Definición de la clase para representar el grafo
class Graph:
    def __init__(self):
        self.graph = {}

    # Método para agregar una arista al grafo
    def add_edge(self, node1, node2):
        if node1 in self.graph:
            self.graph[node1].append(node2)
        else:
            self.graph[node1] = [node2]

    # Método para dibujar el grafo utilizando matplotlib
    def draw_graph(self):
        for node, edges in self.graph.items():
            for edge in edges:
                plt.plot([node[0], edge[0]], [node[1], edge[1]], marker='o', color='b')
        plt.show()

# Creamos una instancia del grafo
graph = Graph()

# Agregamos nodos y aristas al grafo
graph.add_edge((0, 0), (1, 1))
graph.add_edge((1, 1), (2, 2))
graph.add_edge((1, 1), (3, 3))

# Dibujamos el grafo
graph.draw_graph()
