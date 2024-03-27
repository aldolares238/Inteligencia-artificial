#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 6/37  Búsqueda bidireccional

import networkx as nx
import matplotlib.pyplot as plt
from collections import defaultdict, deque

class Graph: # Creamos una clase para nuestro grafo general e inicializamos el diccionario vacio
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v): # Aqui agregamos las aristar necesarias al grafo acorde lo especifica
        self.graph[u].append(v)

    def bidirectional_search(self, start, goal): #Creamos la funcion encargada de la busqueda bidireccional
        # Le damos los parametros del grafo, inciio y objetivo
        visited_start = {start: None} # Definimos los nodos visitados a partir del inicio
        visited_goal = {goal: None} # Nos ayuda a hacer seguimiento a los nodos visitados para la meta

        
        # Colas para la búsqueda desde el inicio y desde el objetivo
        queue_start = deque([start])
        queue_goal = deque([goal])

        while queue_start and queue_goal: # Verificamos que las colas no esten vacias para trabajar con ellas
            # Búsqueda desde el inicio
            current_start = queue_start.popleft()
            for neighbor in self.graph[current_start]: # Iteramos para la busqueda en nodos vecinos
                if neighbor not in visited_start: # Si el nodo vecino no ha sido visitado registramos su recorrido
                    visited_start[neighbor] = current_start
                    queue_start.append(neighbor) # Esto sirve para iniciar la siguiente busqueda en el ultimo nodo vecino visitado
                    
            # Verificar intersección entre los nodos vistados desde el inicio y los del objetivo
            for node in visited_start: # Itera sobre los nodos visitados desde el inicio
                if node in visited_goal: # Verifica si el noodo actual ha sido visitado tambien desde objetivo
                    path = self._merge_paths(visited_start, visited_goal, node) # Si intersectann combinamos los caminos
                    return path
            
            # Búsqueda desde el objetivo
            current_goal = queue_goal.popleft() #Extrae el primer nodo de la cola para explorar desde objetivo
            for neighbor in self.graph[current_goal]: # Itera sobre todos los nodos vecinos del actual
                if neighbor not in visited_goal: # Verifica si el nodo vecino no ha sido visitdo desde objetivo
                    visited_goal[neighbor] = current_goal # Mantenemos un registro del camino recorrido
                    queue_goal.append(neighbor) # Añadimos el nodo vecino como visitado para seguir buscando
                    
            # Verificar intersección
            for node in visited_goal: # Iteramos para los nodos visitados desde objetivo
                if node in visited_start:# Verificamos si el nodo fue visitado desde inicio
                    path = self._merge_paths(visited_start, visited_goal, node) # En caso de que si, se combinan caminos
                    return path # Devuelve el camino guardado
        
        return None

    def _merge_paths(self, visited_start, visited_goal, intersection): # Este metodo nos ayuda a combinar caminos encontrados
        path_start = self._reconstruct_path(visited_start, intersection) # Reconstruye el camino de inicio a inteseccion
        path_goal = self._reconstruct_path(visited_goal, intersection) # Reconstruye le camino de objetivo a interseccion
        path_goal.reverse() # Invierte el orden del camino de objetivo ya que es inverso al de inicio
        return path_start + path_goal

    def _reconstruct_path(self, visited, node): # Metodo para reconstruir el camino
        path = []  #Iniciamos una lista vacia para almacenar el camino reconstruido
        while node is not None: # Mientrsa el nodo actual no sea none, que no se ha alcanzado el nodo
            path.append(node) # Agrega el nodo actual al camino reconstruido
            node = visited[node] # Actualiza el nodo actual al visitado para retrodceder en el camino
        path.reverse() # Invierte el orden del camino ya que los nodos agregados quedan inversos
        return path # Devuelve el camino reconstruido

# Ejemplo de uso de est tema
if __name__ == "__main__":
    # Crear un grafo de ejemplo
    g = Graph()
    g.add_edge('A', 'B')
    g.add_edge('B', 'C')
    g.add_edge('C', 'D')
    g.add_edge('D', 'E')
    g.add_edge('B', 'F')
    g.add_edge('F', 'G')
    g.add_edge('G', 'E')

    start_node = 'A'
    goal_node = 'F'
    
    # Realizar la búsqueda bidireccional
    path = g.bidirectional_search(start_node, goal_node)

    # Imprimir el resultado
    if path:
        print("El camino encontrado es:", path)
    else:
        print("No se encontró camino entre", start_node, "y", goal_node)

    # Visualizar el grafo y el camino encontrado de manera grafica para el usuario
    G = nx.DiGraph()
    for u, neighbors in g.graph.items(): # Añadimos las caracteristicas y dibujamos el grafo
        for v in neighbors:
            G.add_edge(u, v)
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True, arrows=True)
    if path:
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color='r', width=2)
    plt.show()

