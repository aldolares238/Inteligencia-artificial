#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 29/59 Reglas, Redes Semánticas y Lógica Descriptiva

import networkx as nx
import matplotlib.pyplot as plt

# Creamos un grafo dirigido
G = nx.DiGraph()

# Agregamos nodos y aristas con sus respectivas etiquetas
G.add_node("Humano")  # Nodo Humano
G.add_node("Mamífero")  # Nodo Mamífero
G.add_node("Gato")  # Nodo Gato

# Añadimos aristas que representan relaciones semánticas
G.add_edge("Humano", "Mamífero", relation="es_un")  # Humano es un Mamífero
G.add_edge("Mamífero", "Gato", relation="es_un")   # Mamífero es un Gato

# Dibujamos el grafo
pos = nx.spring_layout(G)  # Layout para la disposición de los nodos
nx.draw(G, pos, with_labels=True, node_size=2000, node_color="skyblue", font_size=10, font_weight="bold")

# Agregamos etiquetas a las aristas
edge_labels = nx.get_edge_attributes(G, 'relation')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# Mostramos el grafo
plt.title("Red Semántica")
plt.show()
