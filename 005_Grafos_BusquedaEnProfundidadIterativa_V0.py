#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 5/37  Búsqueda en Profundidad Iterativa

import networkx as nx
import matplotlib.pyplot as plt

class Graph: #Creamos una clase para el grafo que vamos a utilizar
    def __init__(self): #Metodo constructor, inicializamos el grafo como un diccionario vacio
        self.graph = {}

    def add_edge(self, node, neighbor): # Añade una arista al grafo entre un nodo y su vecino
        if node not in self.graph: #Si el nodo no esta en el grafo se añade el vecino al nodo correspondiente
            self.graph[node] = []
        self.graph[node].append(neighbor)

    def depth_limited_search(self, start, goal, depth_limit): # Realiza una búsqueda en profundidad limitada hasta cierta profundidad
        for depth in range(depth_limit):
            visited = set()  # Conjunto que mantiene los nodos visitados en esta iteracion
            stack = [(start, 0)]  # Pila para realizar la búsqueda en profundidad
            print(f"Iteration {depth + 1}:")  # Muestra la iteración actual
            while stack:
                current, current_depth = stack.pop()  # Extrae un nodo de la pila
                if current_depth <= depth:  # Verifica si se ha alcanzado la profundidad límite especificada
                    if current == goal: #Si se encuentra el nodo objetivo...
                        print("Path found from", start, "to", goal, "within depth limit.") #Muetra el mensaje y retorna un true
                        return True
                    if current not in visited: # Su en nono no ha sido visitado...
                        print("Visiting node:", current) # Imprime el mensaje y lo añade a los nodos visitados
                        visited.add(current)
                        # Añade los vecinos del nodo actual a la pila para su exploración
                        for neighbor in self.graph.get(current, []):
                            stack.append((neighbor, current_depth + 1))
            # Si no se encuentra la solución en esta iteración, muestra un mensaje
            print("No solution found within depth limit.")
        return False

# Creamos el grafo con el que vamos a trabajar, añadiendo sus conexiones
graph = Graph()
graph.add_edge('A', 'B')
graph.add_edge('A', 'C')
graph.add_edge('B', 'D')
graph.add_edge('B', 'E')
graph.add_edge('C', 'F')

# Ejecutar la búsqueda en profundidad iterativa
start_node = 'A' # Definimos el nodo de inicio
goal_node = 'D' # Definimos el nodo destino
depth_limit = 3 # Definimos profundidad

path_found = graph.depth_limited_search(start_node, goal_node, depth_limit)

# Aqui procedemos a crear el objeto para mostrar nuestro grafo
G = nx.Graph(graph.graph)
pos = nx.spring_layout(G)

plt.figure(figsize=(8, 6))

# Dibujar los nodos del grafo
nx.draw_networkx_nodes(G, pos, node_size=700, node_color='skyblue')

# Dibujar las aristas
nx.draw_networkx_edges(G, pos, width=2, alpha=0.5, edge_color='b')

# Dibujar etiquetas de nodos
nx.draw_networkx_labels(G, pos, font_size=20, font_family='sans-serif')

# Imprimir resultado de la búsqueda acorde a las caracteristicas especificadas
if path_found:
    path = nx.shortest_path(G, start_node, goal_node)
    edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
    nx.draw_networkx_edges(G, pos, edgelist=edges, width=2, edge_color='r')
    print("Path:", "->".join(path))
else:
    print("Path not found from", start_node, "to", goal_node, "within depth limit.")

plt.title('Grafo y búsqueda en profundidad iterativa')
plt.axis('off')
plt.show()




