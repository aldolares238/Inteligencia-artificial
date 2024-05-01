#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 35/59 Espacio de Estados

import matplotlib.pyplot as plt

# Definimos la clase Nodo que representa un estado en el espacio de estados
class Nodo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.conexiones = []

    def agregar_conexion(self, nodo):
        self.conexiones.append(nodo)

# Función para dibujar el grafo
def dibujar_grafo(nodos):
    for nodo in nodos:
        for conexion in nodo.conexiones:
            plt.plot([nodo.nombre, conexion.nombre], [0, 1], 'bo-')  # Dibujamos una conexión entre nodos
            plt.text(nodo.nombre, 0, nodo.nombre, fontsize=12, ha='center')  # Añadimos etiquetas a los nodos
            plt.text(conexion.nombre, 1, conexion.nombre, fontsize=12, ha='center')

    plt.title("Espacio de Estados")
    plt.xlabel("Nodos")
    plt.ylabel("Profundidad")
    plt.yticks([])  # Eliminamos los ticks del eje y para una mejor visualización
    plt.show()

# Creamos los nodos del grafo
nodo_A = Nodo('A')
nodo_B = Nodo('B')
nodo_C = Nodo('C')
nodo_D = Nodo('D')

# Establecemos las conexiones entre los nodos
nodo_A.agregar_conexion(nodo_B)
nodo_A.agregar_conexion(nodo_C)
nodo_B.agregar_conexion(nodo_D)
nodo_C.agregar_conexion(nodo_D)

# Creamos una lista de nodos
nodos = [nodo_A, nodo_B, nodo_C, nodo_D]

# Dibujamos el grafo
dibujar_grafo(nodos)
