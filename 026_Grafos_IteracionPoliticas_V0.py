#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 26/37 Iteración de Políticas

import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo dirigido
G = nx.DiGraph()

#Añadimos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D'])

#Añadimos arcos ponderados al grafo
G.add_weighted_edges_from([('A', 'B', 1), ('A', 'C', 2), ('B', 'D', 3), ('C', 'D', 2)])

#Dibujamos el grafo
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=15, arrows=True)
plt.title('Grafo Original')
plt.show()

#Implementación del algoritmo de Iteración de Políticas
#Definimos las políticas iniciales
policy = {'A': 'B', 'B': 'D', 'C': 'D', 'D': None}

# Definimos la función de actualización de políticas
def policy_iteration(G, policy):
    for node in G.nodes:
        if node != 'D':  # Ignoramos el nodo final D
            max_value = float('-inf')
            best_action = None
            for successor in G.successors(node):
                # Manejamos el caso de política None
                if policy[successor] is not None:
                    if G[node][successor]['weight'] + int(policy[successor]) > max_value:
                        max_value = G[node][successor]['weight'] + int(policy[successor])
                        best_action = successor
            policy[node] = best_action

# Iteramos para mejorar las políticas
for i in range(5):  # Realizamos 5 iteraciones
    policy_iteration(G, policy)

# Mostramos las políticas resultantes
print("Políticas después de la iteración:")
print(policy)

# Dibujamos el grafo actualizado con las nuevas políticas
nx.draw(G, with_labels=True, node_color='lightblue', node_size=1500, font_size=15, arrows=True)
plt.title('Grafo con Políticas Actualizadas')
plt.show()
