#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 10/37 Busqueda A0*

import heapq

class Node:
    def __init__(self, name): # Funcion para inicializar objetos del programa
        self.name = name
        self.neighbors = {}  # Diccionario de nodos vecinos y costos de alcanzarlos
        self.g = float('inf')  # Costo actual desde el nodo inicial
        self.h = float('inf')  # Heurística estimada al nodo final
        self.f = float('inf')  # Costo total estimado
        self.parent = None  # Nodo padre en el camino hacia el nodo actual

    def add_neighbor(self, neighbor, cost): # Agrega un vecino al n odo actual con su costo
        self.neighbors[neighbor] = cost

def ao_star_search(start, goal): # Implementamos la busqueda AO* con parametro inicial y meta
    open_list = [(start.f, start)]  # Lista de nodos abiertos ordenada por f
    start.g = 0 # Establece elcosto actual desde el nodo inicial, 0 ya que es el principio
    start.h = heuristic(start, goal) # Calcula la heuristica desde inicio hasta objetivo
    start.f = start.g + start.h # Calcula el valor total

    while open_list: # Iteramos mientras haya elementos de la lista abierta
        f, current = heapq.heappop(open_list)  # Tomar el nodo con el menor f de la lista abierta

        if current == goal: # Si se ha llegado al nodo objetivo
            # Reconstruir el camino desde el nodo objetivo hasta el nodo inicial
            path = []
            while current is not None: # Mientras el nodo actual no sea nulo
                path.append(current.name) # Actualizamos el camino con el nodo actual
                current = current.parent # Actalizamos el nodo actual al nodo padre 
            path.reverse()  # Invertir el camino para obtener la secuencia de nodos desde el inicio hasta el objetivo
            return path

        # Explorar los vecinos del nodo actual
        for neighbor, cost in current.neighbors.items():
            tentative_g = current.g + cost # Calcula el costo tenttivo para llegar a un vecino desde el nodoa actual
            if tentative_g < neighbor.g: # Si el costo tentativo es menor que el costo vecino
                # Actualizar el costo y estimaciones si se encuentra un camino mejor
                neighbor.parent = current
                neighbor.g = tentative_g
                neighbor.h = heuristic(neighbor, goal)
                neighbor.f = neighbor.g + neighbor.h
                # Agregar el nodo vecino a la lista abierta
                heapq.heappush(open_list, (neighbor.f, neighbor))

def heuristic(node, goal):
    # Heurística para estimar el costo restante (distancia euclidiana), para estimar el costo restante entre nodos
    return ((node.x - goal.x) ** 2 + (node.y - goal.y) ** 2) ** 0.5

# Crear nodos y establecer conexiones para nuestro programa
A = Node("A")
B = Node("B")
C = Node("C")
D = Node("D")

# Establecer conexiones y costos necesarios para hacer el codigo
A.add_neighbor(B, 10)
A.add_neighbor(C, 15)
B.add_neighbor(D, 20)
C.add_neighbor(D, 5)

# Definir las coordenadas de los nodos para la heurística
A.x, A.y = 0, 0
B.x, B.y = 5, 0
C.x, C.y = 0, 5
D.x, D.y = 5, 5

# Realizar la búsqueda
start = A
goal = D
path = ao_star_search(start, goal)
print("Ruta encontrada:", path)

