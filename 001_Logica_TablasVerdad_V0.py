#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 1/59 Sintaxis y Semántica: Tablas de Verdad

import numpy as np
import matplotlib.pyplot as plt
import itertools

#Definimos una función que calcula y muestra la tabla de verdad de manera gráfica para una expresión lógica simple
def tabla_verdad():
    #Declaramos la Expresión lógica: A or B
    expresion = "A or B"
    
    #Definimos los valores posibles de A y B
    valores = [False, True]
    etiquetas = ['F', 'T']
    
    #Generamos todas las combinaciones de valores booleanos para A y B
    combinaciones = np.array(list(itertools.product(valores, valores)))
    
    #Evaluamos la expresión para cada combinación de valores y almacenamos los resultados
    resultados = np.array([eval(expresion) for A, B in combinaciones])
    
    # onfiguramos el gráfico para mostrarlo al usuario
    plt.figure(figsize=(8, 6))
    plt.title("Tabla de Verdad para la expresión: " + expresion)
    plt.xticks(range(len(valores)), etiquetas)
    plt.yticks([0, 1], ['F', 'T'])
    plt.xlabel('A')
    plt.ylabel('B')
    
    #Creamos el gráfico de barras para representar los resultados
    plt.imshow(resultados.reshape(2, 2), cmap='Blues', interpolation='nearest')
    
    #Añadimos los valores en cada celda
    for i in range(len(valores)):
        for j in range(len(valores)):
            plt.text(j, i, str(resultados[i * len(valores) + j]), ha='center', va='center', color='black')
    
    #Mostramos el gráfico
    plt.colorbar(label='Resultado')
    plt.grid(False)
    plt.show()

#Llamada a la función para mostrar la tabla de verdad de manera gráfica
tabla_verdad()
