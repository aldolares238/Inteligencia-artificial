#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 8/37 Heurísticas

"""El objetivo de este programa es resolver un problema tipo TSP, conocido como problema
del viajante, con la meta de encontrar la ruta mas corta que visite cada ciudad una vez,
haciendo uso del algoritmo Heuristico"""

import networkx as nx
import matplotlib.pyplot as plt

# Función para calcular la distancia entre dos nodos
def distancia_entre_nodos(G, nodo1, nodo2): # Obtiene parametros para el grafo y cada nodo
    return G[nodo1][nodo2]['weight'] # Retorna el peso de la arista entre esos nodos

# Función de heurística para elegir el próximo nodo a visitar
def siguiente_nodo(G, actual, no_visitados): # Obiene parametro del grafo, nodo actual y no visitado
    mejor_nodo = None # Definimos un mejor nodo como nulo
    mejor_distancia = float('inf') # La distancia inicialmente en infinito
    for nodo in no_visitados: # Iteramos para un nodo dentro de los nodos no visitados
        distancia = distancia_entre_nodos(G, actual, nodo) # Actualizamos el valor de la distancia
        if distancia < mejor_distancia: # Si la distancia actual es menor que la menor distancia...
            mejor_nodo = nodo # Declaramos a nuestro nodo actual como el mejor nodo
            mejor_distancia = distancia # Al igual que con las distancias
    return mejor_nodo # Retornamos el valor del mejor nodo para seguir iterando

# Función para resolver el TSP utilizando heurísticas
def resolver_tsp_heuristico(G, inicio): # Declaramos nuestra funcion que incluye el grafo y el inicio
    recorrido = [inicio] # El recorrido comienza en el nodo de inicio
    no_visitados = set(G.nodes()) - {inicio} # Declaramos todos los nodos como no visitados menos inicio

    while no_visitados: # Mientras haya nodos no visitados se itera
        siguiente = siguiente_nodo(G, recorrido[-1], no_visitados) # Se elige el siguiente nodo a visitar
        recorrido.append(siguiente) # Se agrega el nodo elegido al recorrido
        no_visitados.remove(siguiente) # Eliminmos el nodo elegido de los no visitados

    return recorrido

# Crear un grafo de ejemplo
G = nx.Graph()
G.add_weighted_edges_from([(0, 1, 10), (0, 2, 15), (0, 3, 20), (1, 2, 35), (1, 3, 25), (2, 3, 30)])

# Resolver el TSP heurístico desde el nodo 0, este sera nuestro nodo inicial
recorrido = resolver_tsp_heuristico(G, 2)
print("Recorrido del TSP:", recorrido) # Imprimimos el recorrido obtenido

# Visualizar el grafo y el recorrido de manera grafica para el usuario
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_color='skyblue')
nx.draw_networkx_edges(G, pos, edgelist=[(recorrido[i], recorrido[i+1]) for i in range(len(recorrido)-1)], edge_color='r', width=2)
nx.draw_networkx_edges(G, pos, edgelist=[(recorrido[-1], recorrido[0])], edge_color='r', width=2)  # Para conectar el último nodo con el primero
plt.show()

