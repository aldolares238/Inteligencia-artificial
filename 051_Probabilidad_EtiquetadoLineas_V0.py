#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 51/60 Etiquetados de Líneas

import numpy as np
import matplotlib.pyplot as plt

#Definimos las etiquetas disponibles
etiquetas = ['Sustantivo', 'Verbo', 'Adjetivo']

#Definimos las probabilidades iniciales de transición
#La matriz de transición representa las probabilidades de cambiar de una etiqueta a otra
#En este caso, una matriz de 3x3 donde cada fila representa la probabilidad de cambiar desde una etiqueta a otra
transiciones = np.array([[0.4, 0.3, 0.3],
                         [0.2, 0.5, 0.3],
                         [0.3, 0.4, 0.3]])

#Definimos las probabilidades iniciales de emisión
#La matriz de emisión representa las probabilidades de observar una palabra dada una etiqueta
#En este caso, una matriz de 3x3 donde cada fila representa la probabilidad de observar una palabra dada una etiqueta
emisiones = np.array([[0.3, 0.4, 0.3],
                      [0.2, 0.3, 0.5],
                      [0.4, 0.3, 0.3]])

#Declaramos una Función para simular una secuencia de etiquetas
def simular_secuencia(longitud):
    secuencia = []
    estado_actual = np.random.choice(len(etiquetas))  # Elegimos un estado inicial aleatorio
    for _ in range(longitud):
        secuencia.append(estado_actual)
        estado_actual = np.random.choice(len(etiquetas), p=transiciones[estado_actual])
    return secuencia

#Declramos una Función para mostrar la secuencia generada
def mostrar_secuencia(secuencia):
    palabras = [etiquetas[i] for i in secuencia]
    print("Secuencia de etiquetas generada:", palabras)

#Generamos una secuencia de etiquetas de longitud 10
secuencia_generada = simular_secuencia(10)
mostrar_secuencia(secuencia_generada)

#Graficamos la secuencia generada
plt.figure(figsize=(10, 5))
plt.plot(secuencia_generada, marker='o', linestyle='-', color='b')
plt.xticks(range(10), ['Palabra{}'.format(i) for i in range(1, 11)])
plt.yticks(range(len(etiquetas)), etiquetas)
plt.title('Secuencia de Etiquetas Generada')
plt.xlabel('Palabras')
plt.ylabel('Etiquetas')
plt.grid(True)
plt.show()
