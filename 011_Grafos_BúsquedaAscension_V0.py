#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 11/37 Búsqueda de Ascensión de Colinas


import networkx as nx
import matplotlib.pyplot as plt
import random

def hill_climbing(graph, start_node, max_iterations): # Definimos nuestra funcion general de busqueda
    # Inicialización de variables
    current_node = start_node  # Nodo de inicio determinado para la busqueda
    current_score = evaluate_node(graph, current_node)  # Evaluación del nodo de inicio
    iteration = 0 # Numero de iteracion 
    scores = [current_score]  # Para visualizar la mejora en la gráfica
    
    # Ciclo principal del algoritmo
    while iteration < max_iterations: # Mientras no lleguemos al maximo de iteraciones
        # Obtener vecinos del nodo actual, empezando con el inicial
        neighbor_nodes = list(graph.neighbors(current_node))
        # Seleccionar un vecino aleatorio
        neighbor_node = random.choice(neighbor_nodes)
        # Evaluar el vecino seleccionado anteriormente
        neighbor_score = evaluate_node(graph, neighbor_node)
        
        # Comparar la puntuación del vecino con la puntuación actual
        if neighbor_score > current_score:
            # Si la puntuación del vecino es mejor, actualizar el nodo actual y la puntuación
            current_node = neighbor_node
            current_score = neighbor_score
            scores.append(current_score)  # Agregar la puntuación de la nueva solución
        else:
            # Si no se encuentra una mejora, terminar la búsqueda
            break
        
        iteration += 1 # Actualizamos el numero de iteracion
    
    return current_node, scores # Retornamos el resultado

def evaluate_node(graph, node):
    # Función de evaluación
    return graph.nodes[node]['score']

# Crear un grafo aleatorio para el ejemplo
graph = nx.erdos_renyi_graph(10, 0.3, seed=42)
for node in graph.nodes:
    # Asignar una puntuación aleatoria a cada nodo del grafo
    graph.nodes[node]['score'] = random.randint(0, 100)

# Seleccionar un nodo de inicio aleatorio
start_node = random.choice(list(graph.nodes))

# Ejecutar el algoritmo de búsqueda de ascensión de colinas
solution, scores = hill_climbing(graph, start_node, 100)

# Mostrar resultados
print("Nodo encontrado:", solution)
print("Puntuación del nodo encontrado:", evaluate_node(graph, solution))

# Visualizar la mejora de la puntuación a lo largo de las iteraciones
plt.plot(scores)
plt.xlabel('Iteración')
plt.ylabel('Puntuación')
plt.title('Mejora de la Puntuación en la Búsqueda de Ascensión de Colinas')
plt.show()
