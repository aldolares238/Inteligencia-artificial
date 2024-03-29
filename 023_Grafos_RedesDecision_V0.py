#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 23/37 Redes de decisión

import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo dirigido para el ejemplo
G = nx.DiGraph()

#Añadimos nodos al grafo que vamos a utilizar
G.add_nodes_from(["Inicio", "Decisión 1", "Decisión 2", "Fin"])

#Añadimos aristas ponderadas entre los nodos
G.add_weighted_edges_from([("Inicio", "Decisión 1", 0.5), 
                            ("Inicio", "Decisión 2", 0.5), 
                            ("Decisión 1", "Fin", 0.8), 
                            ("Decisión 2", "Fin", 0.2)])

#Creamos un layout para la visualización de ayida al usuario
pos = nx.spring_layout(G)

#Dibujamos el grafo
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="lightblue", font_size=10, font_weight="bold")

#Añadimos etiquetas de peso a las aristas
labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#Mostramos el grafo
plt.title("Red de Decisión Simple")
plt.show()


