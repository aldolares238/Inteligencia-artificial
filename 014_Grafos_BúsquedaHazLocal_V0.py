#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 14/37 Búsqueda de Haz Local

import random
import matplotlib.pyplot as plt

# Definición de la clase Grafo
class Grafo:
    def __init__(self, vertices):
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]

    # Función para añadir una arista al grafo
    def añadir_arista(self, u, v, w):
        self.grafo[u][v] = w

    # Función para encontrar el vértice con la mínima distancia
    # entre los vértices aún no incluidos en el árbol de expansión
    def minima_distancia(self, distancia, incluido):
        min_distancia = float('inf')
        for v in range(self.V):
            if distancia[v] < min_distancia and incluido[v] == False:
                min_distancia = distancia[v]
                min_indice = v
        return min_indice

    # Función para imprimir el árbol de expansión
    def imprimir_solucion(self, padre):
        print("Arista \t\tPeso")
        for i in range(1, self.V):
            print(padre[i], "-", i, "\t\t", self.grafo[i][padre[i]])

    # Función que implementa la Búsqueda de Haz Local para encontrar el árbol de expansión mínima
    def busqueda_haz_local(self, k, iteraciones_maximas):
        # Lista para almacenar k estados iniciales aleatorios
        estados = []
        for _ in range(k):
            estado = list(range(self.V))
            random.shuffle(estado)
            estados.append(estado)

        # Bucle principal de la búsqueda
        for _ in range(iteraciones_maximas):
            # Evaluar todos los estados y ordenarlos por su función de evaluación
            estados_evaluados = [(estado, self.funcion_evaluacion(estado)) for estado in estados]
            estados_evaluados.sort(key=lambda x: x[1])

            # Seleccionar los k mejores estados para la próxima iteración
            mejores_estados = [estado for estado, _ in estados_evaluados[:k]]

            # Generar nuevos estados vecinos a partir de los mejores estados actuales
            nuevos_estados = []
            for estado in mejores_estados:
                for _ in range(k):
                    nuevo_estado = list(estado)
                    i, j = random.sample(range(self.V), 2)
                    nuevo_estado[i], nuevo_estado[j] = nuevo_estado[j], nuevo_estado[i]
                    nuevos_estados.append(nuevo_estado)

            # Actualizar los estados para la próxima iteración
            estados = nuevos_estados

        # Devolver el mejor estado encontrado
        return estados_evaluados[0][0]

    # Función de evaluación (en este ejemplo, la suma de los pesos de las aristas)
    def funcion_evaluacion(self, estado):
        return sum(self.grafo[i][estado[i + 1]] for i in range(self.V - 1))

# Ejemplo de uso
if __name__ == '__main__':
    # Crear un grafo
    grafo = Grafo(5)
    grafo.añadir_arista(0, 1, 10)
    grafo.añadir_arista(0, 2, 15)
    grafo.añadir_arista(0, 3, 20)
    grafo.añadir_arista(1, 2, 35)
    grafo.añadir_arista(1, 3, 25)
    grafo.añadir_arista(2, 3, 30)
    grafo.añadir_arista(2, 4, 12)
    grafo.añadir_arista(3, 4, 17)

    # Encontrar el árbol de expansión mínima usando Búsqueda de Haz Local
    mejor_solucion = grafo.busqueda_haz_local(k=5, iteraciones_maximas=1000)

    # Imprimir la mejor solución encontrada
    print("La mejor solución encontrada es:")
    print(mejor_solucion)
    print("Con un valor de evaluación de:", grafo.funcion_evaluacion(mejor_solucion))

    # Mostrar el grafo
    plt.imshow(grafo.grafo, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()
