#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 2/37 Busqueda en anchura de costo uniforme

import heapq
import networkx as nx
import matplotlib.pyplot as plt

def uniform_cost_search(graph, start, goal): # Definimos nuestra funcion para la busqueda de costo uniforme, le damos 3 parametros, el grafo, el inicio y la meta
    frontier = [(0, start)]  # En esta variable se toma como una cola de prioridad, en la que tiene valores de costo acumulado y nodo de inicio
    explored = set()  # En esta variable almacenaremos los nodos que ya han sido explorados
    parent = {}  # Diccionario para hacer un seguimiento de los padres de los nodos en el camino mínimo

    while frontier:
        cost, node = heapq.heappop(frontier)  # Esta función elimina y devuelve el elemento de menor valor, tomando valores de la tupla que contiene el costo y el nodo
        if node == goal: # Si el nodo en cuestion es el nodo meta...
            path = [node] #Al llegar al nodo meta, guargamos en la variable path el camino mas corto que se ha encontrdo
            while node != start: #Mientras el nodo enfocado no sea igual al del start
                node = parent[node] # Actualizamos el nodo actal con su nodo padre
                path.append(node) # Actualizamos el camino que se va siguiendo
            path.reverse()  # Obtenemos el camino minimo del nodo inicial al objetivo
            return cost, path  # Devuelve el costo acumulado y el camino mínimo
        explored.add(node) # Definimos que ese nodo ya ha sido explorado

        for neighbor, neighbor_cost in graph[node]: #Iteramos el bucle sobre todos los vecinos del nodo actual
            if neighbor not in explored: # Verificamos si el vecino ha sido explorado para evitar redundancias
                total_cost = cost + neighbor_cost #Actualizamos el costo total acumulado al llegar al nodo vecino
                heapq.heappush(frontier, (total_cost, neighbor))  # Agrega el vecino a la cola de prioridad
                parent[neighbor] = node # Registramos el nodo actual como padre del nodo vecino

    return float('inf'), None  # Devuelve infinito si no se encontró un camino


def draw_graph(graph, path=None): #Se crea un grafico para mostrar el resultado al usuario
    G = nx.Graph() #Creamos el obhjeto
    for node, neighbors in graph.items(): #Agregamos los nodos y vecinos en tupla 
        for neighbor, cost in neighbors: #Tambien se añade el costo de cada vecino
            G.add_edge(node, neighbor, weight=cost) 

    pos = nx.spring_layout(G)  # Layout para la disposición de los nodos en el gráfico
    nx.draw(G, pos, with_labels=True, node_color='skyblue', node_size=1500)  # Dibuja el grafo

    if path:
        edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)] # Le damos valores para el grafico
        nx.draw_networkx_edges(G, pos, edgelist=edges, edge_color='red', width=2)  # Resalta el camino mínimo

    plt.show()



# Creamos nuestro grafo, a manera de tupla, dando valor del nombre acompañado de su costo
graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2)],
    'C': [('D', 5)],
    'D': []  
}

start_node = 'A' #Iniciamos el recorrido en el nodo A
goal_node = 'D' #La meta es el nodo D

cost, path = uniform_cost_search(graph, start_node, goal_node) #Llamamos a la funcion y le damos los parametros deseaods

if path: #Verificamos que se haya encontrado un camino minimo para la meta asignada e imprimimos los resultados
    print("El costo mínimo desde {} hasta {} es: {}".format(start_node, goal_node, cost))
    print("El camino mínimo es:", path)
    draw_graph(graph, path)
else: #En caso de que no tengamos un camino en el rango establecido, nos notificara
    print("No se encontró un camino desde {} hasta {}".format(start_node, goal_node))
