#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 43/60  Extracción de Información

import matplotlib.pyplot as plt
import numpy as np

#Definimos una función para simular el lanzamiento de una moneda
def lanzamiento_moneda():
    return np.random.choice(['Cara', 'Sello'])

#Definimos una función para realizar múltiples lanzamientos de la moneda y contar la frecuencia de aparición de cada resultado
def simulacion_lanzamientos(num_lanzamientos):
    resultados = {'Cara': 0, 'Sello': 0}
    for _ in range(num_lanzamientos):
        resultado = lanzamiento_moneda()
        resultados[resultado] += 1
    return resultados

#Número de lanzamientos de la moneda
num_lanzamientos = 1000

#Realizamos la simulación
resultados_simulacion = simulacion_lanzamientos(num_lanzamientos)

#Graficamos los resultados para el usuario
labels = resultados_simulacion.keys()
values = resultados_simulacion.values()

plt.bar(labels, values)
plt.xlabel('Resultado')
plt.ylabel('Frecuencia')
plt.title('Simulación de lanzamiento de moneda (' + str(num_lanzamientos) + ' lanzamientos)')
plt.show()
