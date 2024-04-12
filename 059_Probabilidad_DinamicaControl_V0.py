#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 59/60 Dinámica y Control

import numpy as np
import matplotlib.pyplot as plt

#Definimos la Función que simula el lanzamiento de un dado
def lanzar_dado():
    return np.random.randint(1, 7)  #Generamos un número aleatorio entre 1 y 6

#Declaramos la Función que simula múltiples lanzamientos de un dado y registra la frecuencia de cada resultado
def simulacion_lanzamiento_dado(n_lanzamientos):
    resultados = np.zeros(6)  #Inicializamos un arreglo para almacenar la frecuencia de cada resultado del dado
    for _ in range(n_lanzamientos):
        resultado = lanzar_dado()  #Lanzamos el dado
        resultados[resultado - 1] += 1  #Incrementamos la frecuencia del resultado obtenido
    probabilidades = resultados / n_lanzamientos  #Calculamos las probabilidades dividiendo por el número total de lanzamientos
    return probabilidades

#Realizamos la simulación con 1000 lanzamientos
n_lanzamientos = 1000
probabilidades = simulacion_lanzamiento_dado(n_lanzamientos)

#Creamos un gráfico de barras para visualizar las probabilidades
valores_dado = np.arange(1, 7)  # Valores posibles del dado (1 al 6)
plt.bar(valores_dado, probabilidades, tick_label=valores_dado, color='skyblue')
plt.title('Probabilidades de lanzamiento de un dado')
plt.xlabel('Resultado del dado')
plt.ylabel('Probabilidad')
plt.show()  #Mostrar el gráfico
