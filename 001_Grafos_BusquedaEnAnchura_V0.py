#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 1/37 Busqueda en anchura

#Importamos las librerias necesarias, principalmente las necesitaremos para mostrar de manera grafica el grafo
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

# Definición del grafo como un diccionario de listas de adyacencia
grafo = {
    'A': ['B', 'C'], #El vertice A está conectado con aristas a los vertices B y C
    'B': ['D', 'E'], #El vertice B está conectado con aristas a los vertices D y E
    'C': ['F'], #El vertice C está conectado con arista al vertice F
    'D': [], #Las conexiones de este vertice ya estan previamente especificadas
    'E': ['F'], #El veertice E se encuentra conectado con el vertice F
    'F': [] #Las conexiones de este vertice ya estan previamente especificadas
}

# Declaramos la siguiente función para realizar la búsqueda en anchura
def bfs(grafo, inicio): #BFS (Breadth-First Search) se trata de nuestro algoritmo busqueda en anchura, se manda a llamar al grafo declarado
    visitados = set()  # Conjunto para almacenar los nodos explorados o visitados durante la busqueda
    cola = deque([inicio])  # Cola para mantener los nodos a visitar durante la busqueda
    
    while cola:
        nodo = cola.popleft()  # Tomamos el primer nodo de la cola para ubicar bien la secuencia
        if nodo not in visitados: #Si el nodo de la cola no se ha visitado en la busqueda:
            print(nodo)  # Imprimir el nodo visitado
            visitados.add(nodo)  # Señalamos este nodo como un nodo ya visitado
            for vecino in grafo[nodo]: #Buscamos el nodo vecino acorde al nodo seleccionado
                if vecino not in visitados: # Si el nodo vecino no se ha visitado...
                    cola.append(vecino)  # Agregar los vecinos no visitados a la cola
                    G.add_edge(nodo, vecino)  # Agregar la conexión al grafo

# Crear un gráfico vacío para mostrar los resultados de manera visible para el usuario
G = nx.Graph()

# Agregamos los nodos del grafo a nuestra grafica 
for nodo in grafo: #Utilizamos un for para añadir todos los nodos del grafo
    G.add_node(nodo)

# Ejecutar la búsqueda en anchura tomando como incio o nodo inicial el nodo A
print("Recorrido BFS:")
bfs(grafo, 'A')

# Dibujar el grafo en una grafica para el usuario
pos = nx.spring_layout(G)  # Calcular la posición de los nodos
nx.draw(G, pos, with_labels=True, node_size=700, node_color='skyblue', font_size=12, font_weight='bold') #Esta linea se encarga de dar los valores esteticos a nuestra grafica, colores, tamaños, formas, etc
plt.title('Grafo') #Titulo de la grafica
plt.show() #Mostramos el grafico


