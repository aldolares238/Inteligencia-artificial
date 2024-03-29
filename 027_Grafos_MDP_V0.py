#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 27/37 Proceso de Decisión de Markov (MDP)

import networkx as nx
import matplotlib.pyplot as plt
import numpy as np

#Creamos un grafo dirigido para el ejemplo
G = nx.DiGraph()

#Añadimos nodos al grafo
G.add_nodes_from(['A', 'B', 'C', 'D'])

#Añadimos aristas ponderadas al grafo
G.add_weighted_edges_from([('A', 'B', 0.5), ('A', 'C', 0.5), ('B', 'D', 1), ('C', 'D', 1)])

#Definimos las recompensas de cada estado
recompensas = {'A': 0, 'B': 1, 'C': -1, 'D': 0}

#Definimos la tasa de descuento
gamma = 0.8

#Definimos el diccionario de políticas
politicas = {'A': 'B', 'B': 'D', 'C': 'D', 'D': None}

#Definimos la función de utilidad para actualizar el valor de los estados
def calcular_utilidad(estado, politicas, recompensas, gamma):
    if politicas[estado] is None:
        return recompensas[estado]
    prox_estado = politicas[estado]
    return recompensas[estado] + gamma * calcular_utilidad(prox_estado, politicas, recompensas, gamma)

# Actualizamos las políticas de acuerdo a la utilidad
nuevas_politicas = {}
for estado in G.nodes:
    posibles_acciones = list(G.successors(estado))
    if not posibles_acciones:  # Verificar si no hay acciones posibles desde el estado
        nuevas_politicas[estado] = None
    else:
        valores_utilidad = [calcular_utilidad(accion, politicas, recompensas, gamma) for accion in posibles_acciones]
        mejor_accion_idx = np.argmax(valores_utilidad)
        nuevas_politicas[estado] = posibles_acciones[mejor_accion_idx]

politicas = nuevas_politicas

#Mostramos las políticas resultantes
print("Políticas optimizadas:")
for estado, accion in politicas.items():
    print(f"Estado: {estado}, Acción: {accion}")

#Visualizamos el grafo con las políticas
pos = nx.spring_layout(G)  # Layout del grafo
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='skyblue')
nx.draw_networkx_edge_labels(G, pos, edge_labels={(u, v): f'{G[u][v]["weight"]}' for u, v in G.edges()}, font_color='red')
plt.show()
