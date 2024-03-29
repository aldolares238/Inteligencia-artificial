#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 24/37  Valor de la Información

import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo dirigido para trabajar el ejemplo
G = nx.DiGraph()

#Añadimos nodos al grafo que nos ayudaran al proceso
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

#Añadimos aristas con sus respectivos pesos
G.add_edge('A', 'B', weight=0.6)
G.add_edge('A', 'C', weight=0.2)
G.add_edge('B', 'D', weight=0.3)
G.add_edge('B', 'E', weight=0.1)
G.add_edge('C', 'E', weight=0.4)
G.add_edge('C', 'F', weight=0.7)
G.add_edge('D', 'E', weight=0.9)
G.add_edge('E', 'F', weight=0.5)

#Calculamos el valor de información para cada nodo
node_values = {node: sum(G[u][v]['weight'] for u, v in G.in_edges(node)) + #Sumamos los pesos de las aristas que entran en el nodo y los pesos de las aristas que salen del nodo
                      sum(G[u][v]['weight'] for u, v in G.out_edges(node)) for node in G.nodes}

#Dibujamos el grafo con los valores de información como etiquetas de los nodos
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=2000, node_color='skyblue', font_size=12, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f"{G[u][v]['weight']:.1f}" for u, v in G.edges}, font_color='red')
nx.draw_networkx_labels(G, pos, labels=node_values, font_color='green')
plt.title("Grafo con Valor de Información")
plt.show()

#Mostramos los valores de información calculados para cada nodo
print("Valor de Información de cada nodo:")
for node, value in node_values.items():
    print(f"Nodo {node}: {value:.2f}")
