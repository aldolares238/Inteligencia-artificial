#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 20/37 Acondicionamiento del Corte

import networkx as nx
import matplotlib.pyplot as plt

#Se crea un grafo dirigido para trabajar con el
G = nx.DiGraph()

#Le Añadimos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D', 'E'])

#Le Añadimos aristas al grafo con pesos
G.add_weighted_edges_from([('A', 'B', 3), ('A', 'C', 6),
                            ('B', 'C', 4), ('B', 'D', 2),
                            ('C', 'D', 1), ('C', 'E', 5),
                            ('D', 'E', 7)])

#Visualizamos el grafo para observar su comportamiento, añadimos colores y formas
pos = nx.spring_layout(G)  #Añadimos posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue')
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
plt.title("Grafo Original")
plt.show()

#Algoritmo de Acondicionamiento del Corte, le añadimos los parametros necesarios
cut_set = nx.minimum_edge_cut(G, 'A', 'E')

#Visualizamos el corte mínimo para compararlo con el original
H = G.copy()
H.remove_edges_from(cut_set)

pos = nx.spring_layout(H)  #Posiciones de los nodos, añadimos nombres y formas para mostrar
nx.draw(H, pos, with_labels=True, node_size=700, node_color='lightgreen')
labels = nx.get_edge_attributes(H, 'weight')
nx.draw_networkx_edge_labels(H, pos, edge_labels=labels)
plt.title("Corte Mínimo")
plt.show()

#Imprimimos el conjunto de corte mínimo
print("Conjunto de Corte Mínimo:", cut_set)
