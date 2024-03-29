#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 28/37 MDP Parcialmente Observable (POMDP)

import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo vacío
G = nx.Graph()

#Agregamos nodos al grafo
G.add_nodes_from([1, 2, 3, 4, 5])

#Agregamos aristas al grafo
G.add_edges_from([(1, 2), (1, 3), (2, 4), (3, 5)])

#Asignamos observaciones a los nodos
observed_nodes = {2, 3}

#Definimos la función de transición de estado
def transition(current_state, action):
    #En este caso, simplemente cambiamos al siguiente nodo
    return list(G.neighbors(current_state))[0]

#Definimos la función de observación
def observation(current_state):
    #Simulamos una observación parcialmente observable
    return current_state in observed_nodes

#Definimos el estado inicial
current_state = 1

#Definimos la secuencia de acciones a tomar
actions = [None, None, None]  #Por simplicidad, no tomamos acciones

#Ejecutamos el algoritmo POMDP
for action in actions:
    # bservamos el estado actual
    current_observation = observation(current_state)
    print("Observation:", current_observation)

    #Tomamos una acción y cambiamos de estado
    current_state = transition(current_state, action)
    print("New State:", current_state)

#Visualizamos el grafo
pos = nx.spring_layout(G)  #Posiciones de los nodos
nx.draw(G, pos, with_labels=True, node_size=1000, node_color="skyblue")
plt.show()
