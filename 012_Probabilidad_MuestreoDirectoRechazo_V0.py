#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 12/60 Muestreo Directo y Por Rechazo

import numpy as np
import matplotlib.pyplot as plt

#Creamos la Función objetivo que queremos muestrear
def target_distribution(x):
    return np.sin(x) * np.exp(-0.1 * x)

#Creamos la funcion de envoltura que envuelve nuestra función objetivo
def envelope_distribution(x):
    return 0.3 * np.exp(-0.05 * x)

#Esrte es el Rango en el que generaremos muestras
x = np.linspace(0, 20, 1000)

#Generamos muestras utilizando el método de aceptación-rechazo
samples = []
for _ in range(1000):
    x_proposal = np.random.uniform(0, 20)  #Generamos una propuesta aleatoria dentro del rango
    p_target = target_distribution(x_proposal)
    p_envelope = envelope_distribution(x_proposal)
    if np.random.uniform(0, 1) < p_target / p_envelope:
        samples.append(x_proposal)

#Visualización de la distribución objetivo y las muestras generadas
plt.figure(figsize=(10, 6))
plt.plot(x, target_distribution(x), label='Distribución Objetivo')
plt.plot(x, envelope_distribution(x), label='Distribución de Envoltura')
plt.hist(samples, bins=30, density=True, alpha=0.5, label='Muestras Generadas')
plt.xlabel('x')
plt.ylabel('Densidad de Probabilidad')
plt.title('Muestreo Directo y Por Rechazo')
plt.legend()
plt.grid(True)
plt.show()
