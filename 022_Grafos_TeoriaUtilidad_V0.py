#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 22/37 Teoría de la Utilidad: Función de Utilidad

import networkx as nx
import matplotlib.pyplot as plt

#Definimos una función de utilidad que retorna la distancia entre dos nodos
def utilidad(nodo_inicial, nodo_destino):
    return abs(ord(nodo_destino) - ord(nodo_inicial))

#Definimos el grafo de ejemplo como un diccionario de nodos y sus vecinos
grafo = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

#creamos una Función para encontrar el camino más corto desde el nodo inicial al nodo destino
def encontrar_camino_mas_corto(grafo, nodo_inicial, nodo_destino):
    #Creamos un grafo dirigido para visualización 
    G = nx.Graph()

    #Agregamos los nodos al grafo
    for nodo in grafo:
        G.add_node(nodo)

    #Agregamos las aristas al grafo
    for nodo, vecinos in grafo.items():
        for vecino in vecinos:
            G.add_edge(nodo, vecino)

    #Mostramos el grafo
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue', font_size=15)
    plt.title("Grafo")

    #Calculamos la distancia entre el nodo inicial y el destino
    distancia = utilidad(nodo_inicial, nodo_destino)

    #Mostramos la utilidad al usuario
    print(f"Utilidad desde {nodo_inicial} hasta {nodo_destino}: {distancia}")

    #Calculamos el camino más corto
    camino_mas_corto = nx.shortest_path(G, source=nodo_inicial, target=nodo_destino)

    #Mostramos el camino más corto
    print(f"Camino más corto desde {nodo_inicial} hasta {nodo_destino}: {camino_mas_corto}")

    #Dibujamos el camino más corto
    nx.draw_networkx_nodes(G, pos, nodelist=camino_mas_corto, node_color='red', node_size=1000)
    nx.draw_networkx_edges(G, pos, edgelist=[(camino_mas_corto[i], camino_mas_corto[i + 1]) for i in range(len(camino_mas_corto) - 1)], edge_color='red', width=2)
    plt.title("Camino más corto")
    
    #Mostramos el grafo y el camino más corto
    plt.show()

#Llamamos a la función para encontrar el camino más corto y poder mostrar resultado
encontrar_camino_mas_corto(grafo, 'A', 'F')
