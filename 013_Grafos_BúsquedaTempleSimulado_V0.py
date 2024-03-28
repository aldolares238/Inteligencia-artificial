#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 13/37 Busqueda de temple simulado

import random
import matplotlib.pyplot as plt

# Definición de la clase Grafo
class Grafo:
    def __init__(self, vertices): # Iniciamos los valores del grafo y lo creamos
        self.V = vertices
        self.grafo = [[0 for columna in range(vertices)] for fila in range(vertices)]

    # Función para añadir una arista al grafo
    def añadir_arista(self, u, v, w):
        self.grafo[u][v] = w

    # Función para encontrar el vértice con la mínima distancia
    # entre los vértices aún no incluidos en el árbol de expansión
    def minima_distancia(self, distancia, incluido): 
        min_distancia = float('inf')
        for v in range(self.V): # Para cada nodo, verificamos si la distancia es menor que la minima conocida
            if distancia[v] < min_distancia and incluido[v] == False:
                min_distancia = distancia[v]
                min_indice = v
        return min_indice

    # Función para imprimir el árbol de expansión
    def imprimir_solucion(self, padre):
        print("Arista \t\tPeso")
        for i in range(1, self.V):
            print(padre[i], "-", i, "\t\t", self.grafo[i][padre[i]])

    # Función que implementa el algoritmo de temple simulado para encontrar el árbol de expansión mínima
    def temple_simulado(self):
        # Solución inicial
        solucion_actual = [0] * self.V
        # Temperatura inicial
        temperatura = 1000
        # Factor de enfriamiento
        factor_enfriamiento = 0.95
        # Iteraciones máximas
        iteraciones_maximas = 1000

        while temperatura > 1:
            # Generar una solución vecina
            vecino = list(solucion_actual)
            i = random.randint(0, self.V - 1)
            j = random.randint(0, self.V - 1)
            vecino[i], vecino[j] = vecino[j], vecino[i]

            # Calcular la energía (en este caso, la suma de los pesos de las aristas)
            energia_actual = sum(self.grafo[i][vecino[i]] for i in range(1, self.V))
            energia_vecino = sum(self.grafo[i][vecino[i]] for i in range(1, self.V))

            # Si la solución vecina es mejor, aceptarla
            if energia_vecino < energia_actual:
                solucion_actual = list(vecino)
            # Si la solución vecina es peor, aceptarla con cierta probabilidad
            else:
                probabilidad_aceptacion = random.random()
                if probabilidad_aceptacion < self.probabilidad_aceptacion(energia_actual, energia_vecino, temperatura):
                    solucion_actual = list(vecino)

            # Reducir la temperatura
            temperatura *= factor_enfriamiento

        return solucion_actual

    # Función para calcular la probabilidad de aceptar una solución peor
    def probabilidad_aceptacion(self, energia_actual, energia_vecino, temperatura):
        if temperatura == 0:
            return 0
        return pow(2.71828, -abs(energia_vecino - energia_actual) / temperatura)

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

    # Encontrar el árbol de expansión mínima usando temple simulado
    solucion = grafo.temple_simulado()

    # Imprimir la solución
    print("La solución encontrada es:")
    grafo.imprimir_solucion(solucion)

    # Mostrar el grafo
    plt.imshow(grafo.grafo, cmap='hot', interpolation='nearest')
    plt.colorbar()
    plt.show()
