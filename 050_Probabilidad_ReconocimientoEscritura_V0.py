#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 50/60 Reconocimiento de Escritura

import numpy as np
import matplotlib.pyplot as plt

#Definimos una función para generar datos de escritura simulados
def generar_muestra_aleatoria():
    #Creamos una matriz de 28x28 para simular una imagen de escritura
    muestra = np.random.rand(28, 28)
    return muestra
#Definimos una función para calcular la similitud entre dos muestras de escritura
def calcular_similitud(muestra_1, muestra_2):
    #Calculamos la diferencia cuadrada entre las dos muestras
    diferencia_cuadrada = np.square(muestra_1 - muestra_2)
    #Sumamos los cuadrados de las diferencias y calculamos la similitud como la inversa de esa suma
    similitud = 1 / (1 + np.sum(diferencia_cuadrada))
    return similitud

#Generamos una muestra de escritura para comparar
muestra_referencia = generar_muestra_aleatoria()

#Creamos una lista para almacenar las similitudes calculadas
similitudes = []

#Generamos y comparamos muestras aleatorias para simular un conjunto de datos de referencia
for _ in range(10):
    muestra_comparacion = generar_muestra_aleatoria()
    similitud = calcular_similitud(muestra_referencia, muestra_comparacion)
    similitudes.append(similitud)

#Visualizamos los resultados
plt.figure(figsize=(10, 5))
plt.bar(range(10), similitudes, color='skyblue')
plt.xlabel('Muestra de escritura')
plt.ylabel('Similitud')
plt.title('Similitud de muestras de escritura con la muestra de referencia')
plt.xticks(range(10))
plt.ylim(0, 1)  #Establecemos el límite del eje y entre 0 y 1
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()
