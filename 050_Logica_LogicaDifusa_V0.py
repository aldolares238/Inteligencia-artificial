#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 50/59 Logica Difusa

import numpy as np
import matplotlib.pyplot as plt

# Definimos las funciones de membresía triangulares
def triangular(x, a, b, c):
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Definimos las variables de entrada y salida
calidad = np.arange(0, 11, 1)
servicio = np.arange(0, 11, 1)
propina = np.arange(0, 26, 1)

# Definimos las funciones de membresía para la calidad
calidad_baja = triangular(calidad, 0, 0, 5)
calidad_media = triangular(calidad, 0, 5, 10)
calidad_alta = triangular(calidad, 5, 10, 10)

# Definimos las funciones de membresía para el servicio
servicio_bajo = triangular(servicio, 0, 0, 5)
servicio_medio = triangular(servicio, 0, 5, 10)
servicio_alto = triangular(servicio, 5, 10, 10)

# Definimos las funciones de membresía para la propina
propina_baja = triangular(propina, 0, 0, 13)
propina_media = triangular(propina, 0, 13, 25)
propina_alta = triangular(propina, 13, 25, 25)

# Visualizamos las funciones de membresía
plt.figure()

plt.plot(calidad, calidad_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(calidad, calidad_media, 'g', linewidth=1.5, label='Media')
plt.plot(calidad, calidad_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Calidad de la comida')
plt.legend()

plt.figure()

plt.plot(servicio, servicio_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(servicio, servicio_medio, 'g', linewidth=1.5, label='Medio')
plt.plot(servicio, servicio_alto, 'r', linewidth=1.5, label='Alto')
plt.title('Calidad del servicio')
plt.legend()

plt.figure()

plt.plot(propina, propina_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(propina, propina_media, 'g', linewidth=1.5, label='Media')
plt.plot(propina, propina_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Propina')
plt.legend()

plt.show()
