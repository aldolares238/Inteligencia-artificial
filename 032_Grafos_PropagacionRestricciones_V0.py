#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 32/37 - Propagación de Restricciones


import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo dirigido
G = nx.DiGraph()

#Agregamos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D'])

#Agregamos aristas al grafo (con restricciones)
G.add_edges_from([('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')])

#Inicializamos el dominio de cada variable
domain = {'A': [1, 2, 3], 'B': [2, 3, 4], 'C': [1, 3, 4], 'D': [2, 4, 5]}

#Mostramos el grafo antes de la propagación de restricciones
nx.draw(G, with_labels=True, font_weight='bold')
plt.title("Grafo inicial")
plt.show()

#Función para propagar restricciones
def propagate_constraints(graph, domains):
    for node in graph.nodes():
        neighbors = list(graph.successors(node))  #Obtenemos los sucesores (vecinos) del nodo
        for neighbor in neighbors:
            for value in domains[node][:]:  #Iteramos sobre el dominio actual del nodo
                if value not in domains[neighbor]:  #Si el valor no es válido para el vecino
                    domains[node].remove(value)  #Eliminamos el valor del dominio del nodo

#Propagamos restricciones
propagate_constraints(G, domain)

#Mostramos el grafo después de la propagación de restricciones
nx.draw(G, with_labels=True, font_weight='bold')
plt.title("Grafo después de propagación de restricciones")
plt.show()

#Mostramos los dominios finales de cada variable
print("Dominios finales después de la propagación de restricciones:")
for node, values in domain.items():
    print(f"{node}: {values}")
