#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 18/37 Comprobación Hacia Delante

import networkx as nx
import matplotlib.pyplot as plt

#Creamos un grafo dirigido con el que vamos a trabajar
G = nx.DiGraph()

#Agregamos nodos al grafo con los que vamos a trabajar
G.add_nodes_from(["A", "B", "C", "D", "E", "F"])

#Agregamos aristas que representan relaciones entre nodos
G.add_edges_from([("A", "B"), ("A", "C"),
                  ("B", "D"), ("C", "E"),
                  ("D", "F"), ("E", "F")])

#Función para realizar la comprobación hacia adelante
def comprobacion_hacia_delante(grafo, inicio):
    #Lista para almacenar los nodos que han sido visitados
    visitados = []
    #Pila para realizar el recorrido en profundidad
    pila = [inicio]
    
    #Mientras la pila no esté vacía
    while pila:
        #Sacamos el último nodo de la pila
        nodo = pila.pop()
        #Si el nodo no ha sido visitado
        if nodo not in visitados:
            #Lo marcamos como visitado
            visitados.append(nodo)
            #Agregamos los sucesores del nodo a la pila
            pila.extend(grafo.successors(nodo))
    
    return visitados

#Ejemplo de uso y aplicacion del tema
inicio = "A"
resultado = comprobacion_hacia_delante(G, inicio)
print("Nodos visitados:", resultado)

#Visualización del grafo para el usuario
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()



