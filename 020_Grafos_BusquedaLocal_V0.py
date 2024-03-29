#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 20/37 Búsqueda Local: Mínimos-Conflictos

import networkx as nx
import random
import matplotlib.pyplot as plt

def generate_random_graph(num_nodes, num_edges): #Generamos un grafo aleatorio con el numero de nodos y aristas
    G = nx.gnm_random_graph(num_nodes, num_edges)  
    return G

def initialize_colors(graph): #Inicializamos un color aleatorio para cada nodo del grafo
    colors = {}
    #Iteramos sobre cada nodo en el grafo y asigna un color aleatorio a cada uno
    for node in graph.nodes:
        colors[node] = random.choice(['red', 'green', 'blue'])
    return colors

def count_conflicts(graph, colors): #Contamos el numero de conflictos en el grafo acorde colores
    conflicts = 0
    #Iteramos sobre cada arista en el grafo y verifica si los nodos adyacentes tienen el mismo color
    for u, v in graph.edges:
        if colors[u] == colors[v]:  
            conflicts += 1  #Incrementamos el contador de conflictos si los nodos tienen el mismo color
    return conflicts

def minimize_conflicts(graph, colors, max_iterations): #Aplicamos el algoritmo para la busqueda local
    #Iteramos hasta que se alcance el número máximo de iteraciones o no haya conflictos
    for _ in range(max_iterations):
        node = random.choice(list(graph.nodes))  #Elegimos un nodo aleatorio del grafo
        current_color = colors[node]  #Guardamos el color actual del nodo seleccionado
        min_conflicts = float('inf')  #Inicializamos el mínimo de conflictos con infinito
        best_color = None
        #Iteramos sobre cada color posible excepto el color actual del nodo
        for color in ['red', 'green', 'blue']:
            if color != current_color:
                colors[node] = color  #Le asignamos un nuevo color al nodo
                conflicts = count_conflicts(graph, colors)  #Calculamos el número de conflictos
                if conflicts < min_conflicts:
                    min_conflicts = conflicts  #Actualizamos el mínimo de conflictos si se encuentra uno menor
                    best_color = color  #Guardamos el mejor color encontrado hasta ahora
        colors[node] = best_color  #Le asignamos el mejor color al nodo seleccionado
        if min_conflicts == 0:
            break  #En caso de que no haya conflictos, termina el proceso
    return colors

def draw_graph(graph, colors):
    """Dibuja el grafo con la asignación de colores."""
    #Dibujamos el grafo con etiquetas de nodos y colores asignados a los nodos
    nx.draw(graph, with_labels=True, node_color=[colors[node] for node in graph.nodes])
    plt.show()  #Mostramos el gráfico

if __name__ == "__main__":
    num_nodes = 10  #Número de nodos en el grafo
    num_edges = 15  #Número de aristas en el grafo
    max_iterations = 1000  #Número máximo de iteraciones permitidas

    #Generamos un grafo aleatorio llamando a la funcion y sus parametros
    G = generate_random_graph(num_nodes, num_edges)

    #Inicializamos una asignación de colores aleatoria para los nodos del grafo
    colors = initialize_colors(G)

    #Aplicamos el algoritmo de Búsqueda Local: Mínimos-Conflictos
    colors = minimize_conflicts(G, colors, max_iterations)

    #Dibujamos el grafo con la asignación de colores
    draw_graph(G, colors)
