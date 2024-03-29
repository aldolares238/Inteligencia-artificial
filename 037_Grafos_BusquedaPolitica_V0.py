#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 37/37!!!!!!!!!!!!! Búsqueda de la Política


import networkx as nx
import matplotlib.pyplot as plt

#Creamos el grafo
G = nx.Graph()

#Agregamos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D', 'E', 'F'])

#Agregamos aristas al grafo
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('B', 'E'), ('C', 'F'), ('E', 'F')])

#Dibujamos el grafo
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue')

#Mostramos el grafo
plt.title('Grafo Ejemplo')
plt.show()

#Hacemos una Función de búsqueda de política
def policy_search(graph, start, goal):
    current_node = start
    path = [current_node]
    
    while current_node != goal:
        neighbors = list(graph.neighbors(current_node))
        next_node = None
        shortest_distance = float('inf')
        
        #Para Encontrar el vecino más cercano al nodo objetivo
        for neighbor in neighbors:
            if nx.shortest_path_length(graph, neighbor, goal) < shortest_distance:
                next_node = neighbor
                shortest_distance = nx.shortest_path_length(graph, neighbor, goal)
        
        #Movemos al siguiente nodo y actualizar el camino
        current_node = next_node
        path.append(current_node)
    
    return path

#Ejecutamos la búsqueda de política
start_node = 'A'
goal_node = 'F'
policy = policy_search(G, start_node, goal_node)

#Imprimimos la política encontrada
print("Política encontrada:", policy)

#Dibujamos la política sobre el grafo
plt.figure()
nx.draw(G, pos, with_labels=True, node_size=1000, node_color='lightblue')
path_edges = [(policy[i], policy[i+1]) for i in range(len(policy)-1)]
nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='red', width=2)
plt.title('Política de búsqueda')
plt.show()
