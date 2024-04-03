#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 16/60 Hipótesis de Markov: Procesos de Markov

import numpy as np
import matplotlib.pyplot as plt

#Definimos los estados posibles del clima: soleado, nublado, lluvioso para nuestro proceso
estados = ['Soleado', 'Nublado', 'Lluvioso']

#Definimos la matriz de transición que representa las probabilidades de cambiar de un estado a otro
#Las filas representan el estado actual, las columnas representan el estado siguiente
transiciones = np.array([
    [0.6, 0.3, 0.1],  #Probabilidades de cambiar de Soleado
    [0.2, 0.6, 0.2],  #Probabilidades de cambiar de Nublado
    [0.1, 0.4, 0.5]   #Probabilidades de cambiar de Lluvioso
])

#Estado inicial (probabilidades iniciales de estar en cada estado) asiganando valores
estado_inicial = np.array([0.4, 0.3, 0.3])  #Probabilidades de comenzar en Soleado, Nublado, Lluvioso respectivamente

#Definimos la función para simular el clima durante varios días
def simular_clima(dias):
    clima = [np.random.choice(estados, p=estado_inicial)]  #Empezamos con un estado aleatorio
    for _ in range(dias - 1):
        estado_actual = clima[-1]  #Estado actual
        siguiente_estado = np.random.choice(estados, p=transiciones[estados.index(estado_actual)])
        clima.append(siguiente_estado)
    return clima

#Simulamos el clima durante 7 días
dias_simulados = 7
resultado_simulacion = simular_clima(dias_simulados)

#Graficamos los resultados con colores y etiquetas para el usuario
plt.figure(figsize=(10, 5))
plt.plot(range(1, dias_simulados + 1), [estados.index(clima) for clima in resultado_simulacion], marker='o')
plt.xticks(range(1, dias_simulados + 1))
plt.xlabel('Día')
plt.ylabel('Estado del Clima')
plt.yticks(range(len(estados)), estados)
plt.title('Simulación del Clima con Hipótesis de Markov')
plt.grid(True)
plt.show()
#Incluimos en la consola un resumen del resultado
print("Clima simulado para", dias_simulados, "días:", resultado_simulacion)
