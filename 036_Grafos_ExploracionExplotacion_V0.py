#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 36/37  Exploración vs. Explotación


import networkx as nx
import matplotlib.pyplot as plt
import random

#Creamos un grafo dirigido
G = nx.DiGraph()

#Añadimos nodos al grafo
G.add_nodes_from(range(1, 11))

#Añadimos conexiones entre nodos (aristas)
edges = [(1, 2), (1, 3), (2, 4), (2, 5), (3, 6), (3, 7), (4, 8), (5, 9), (6, 10)]
G.add_edges_from(edges)

#Creamos una función para visualizar el grafo
def visualize_graph(G):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
    plt.show()

#Visualizamos el grafo
visualize_graph(G)

#Definimos la función de exploración vs. explotación
def exploration_exploitation(G, start_node, num_iterations):
    current_node = start_node
    path = [current_node]

    for _ in range(num_iterations):
        neighbors = list(G.successors(current_node))
        if random.random() < 0.5 and len(neighbors) > 0:
            next_node = random.choice(neighbors)
            path.append(next_node)
            current_node = next_node
        else:
            path.append(start_node)  #Exploración: volvemos al nodo inicial
            current_node = start_node

    return path

#Ejecutamos el algoritmo
path = exploration_exploitation(G, 1, 20)
print("Camino obtenido:", path)

#Visualizamos el camino en el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='skyblue', font_size=12, font_weight='bold', arrowsize=20)
nx.draw_networkx_nodes(G, pos, nodelist=path, node_color='red', node_size=1000)
plt.show()
