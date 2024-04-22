#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 23/59 Lógica Difusa: Inferencia Difusa

import numpy as np
import matplotlib.pyplot as plt

# Funciones de membresía triangulares
def trimf(x, params):
    a, b, c = params
    return np.maximum(0, np.minimum((x - a) / (b - a), (c - x) / (c - b)))

# Definir variables de entrada y salida
calidad = np.arange(0, 11, 1)
servicio = np.arange(0, 11, 1)
propina = np.arange(0, 26, 1)

# Definir funciones de membresía para calidad
calidad_baja = trimf(calidad, [0, 0, 5])
calidad_media = trimf(calidad, [0, 5, 10])
calidad_alta = trimf(calidad, [5, 10, 10])

# Definir funciones de membresía para servicio
servicio_bajo = trimf(servicio, [0, 0, 5])
servicio_medio = trimf(servicio, [0, 5, 10])
servicio_alto = trimf(servicio, [5, 10, 10])

# Definir funciones de membresía para propina
propina_baja = trimf(propina, [0, 0, 13])
propina_media = trimf(propina, [0, 13, 25])
propina_alta = trimf(propina, [13, 25, 25])

# Visualización de las funciones de membresía
plt.figure()

plt.subplot(3, 1, 1)
plt.plot(calidad, calidad_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(calidad, calidad_media, 'g', linewidth=1.5, label='Media')
plt.plot(calidad, calidad_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Calidad')
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(servicio, servicio_bajo, 'b', linewidth=1.5, label='Bajo')
plt.plot(servicio, servicio_medio, 'g', linewidth=1.5, label='Medio')
plt.plot(servicio, servicio_alto, 'r', linewidth=1.5, label='Alto')
plt.title('Servicio')
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(propina, propina_baja, 'b', linewidth=1.5, label='Baja')
plt.plot(propina, propina_media, 'g', linewidth=1.5, label='Media')
plt.plot(propina, propina_alta, 'r', linewidth=1.5, label='Alta')
plt.title('Propina')
plt.legend()

plt.tight_layout()
plt.show()
