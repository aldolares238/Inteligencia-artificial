#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 15/37 Algoritmos Genéticos

import networkx as nx
import random
import matplotlib.pyplot as plt

# Función para inicializar una población de rutas aleatorias
def inicializar_poblacion(tamano_poblacion, grafo):
    poblacion = []
    for _ in range(tamano_poblacion): # Iteramos sobre el tamaño de la poblacion 
        ruta = list(grafo.nodes()) # Definimos la ruta a seguir
        random.shuffle(ruta) 
        poblacion.append(ruta)
    return poblacion

# Función para calcular la distancia total de una ruta en el grafo
def calcular_distancia_total(ruta, grafo):
    distancia_total = 0 # Iniciamos la distancia en cero
    for i in range(len(ruta) - 1):
        distancia_total += grafo[ruta[i]][ruta[i+1]]['weight'] # Actualozamos el valor de la distancia
    return distancia_total

# Función de selección de padres utilizando torneo
def seleccion_de_padres(poblacion, grafo):
    padre1 = random.choice(poblacion) # Hacemos una seleccion random dentro de la poblacion
    padre2 = random.choice(poblacion)
    if calcular_distancia_total(padre1, grafo) < calcular_distancia_total(padre2, grafo):
        return padre1
    else:
        return padre2

# Función de cruce utilizando el operador de cruce en un punto
def cruce(padre1, padre2):
    punto_de_cruce = random.randint(0, len(padre1)-1)
    hijo = padre1[:punto_de_cruce] + [gen for gen in padre2 if gen not in padre1[:punto_de_cruce]]
    return hijo

# Función de mutación utilizando el intercambio de genes
def mutacion(individuo):
    indice1, indice2 = random.sample(range(len(individuo)), 2)
    individuo[indice1], individuo[indice2] = individuo[indice2], individuo[indice1]
    return individuo

# Función principal del algoritmo genético
def algoritmo_genetico(grafo, tamano_poblacion, generaciones): # Añadimos los parametros para el algoritmo
    poblacion = inicializar_poblacion(tamano_poblacion, grafo)
    mejor_ruta = None
    mejor_distancia = float('inf')

    for _ in range(generaciones): # Iteramos sobre las generaciones
        nueva_poblacion = []
        for _ in range(tamano_poblacion): # Para el tamaño de la poblacion
            padre1 = seleccion_de_padres(poblacion, grafo)
            padre2 = seleccion_de_padres(poblacion, grafo)
            hijo = cruce(padre1, padre2)
            if random.random() < 0.1:  # Probabilidad de mutación del 10%
                hijo = mutacion(hijo)
            nueva_poblacion.append(hijo)

            # Actualizar la mejor ruta encontrada
            distancia_hijo = calcular_distancia_total(hijo, grafo)
            if distancia_hijo < mejor_distancia:
                mejor_ruta = hijo
                mejor_distancia = distancia_hijo

        poblacion = nueva_poblacion

    return mejor_ruta, mejor_distancia

# Crear un grafo de ejemplo
grafo = nx.complete_graph(6)
for (u, v, w) in grafo.edges(data=True):
    w['weight'] = random.randint(1, 10)

# Ejecutar el algoritmo genético para encontrar la ruta más corta
mejor_ruta, mejor_distancia = algoritmo_genetico(grafo, 100, 100)

# Mostrar el grafo y la mejor ruta encontrada
pos = nx.spring_layout(grafo)
nx.draw(grafo, pos, with_labels=True)
nx.draw_networkx_edges(grafo, pos, edgelist=[(mejor_ruta[i], mejor_ruta[i+1]) for i in range(len(mejor_ruta)-1)], edge_color='r', width=2)
plt.title(f'Mejor Ruta: {mejor_ruta}, Distancia: {mejor_distancia}')
plt.show()
