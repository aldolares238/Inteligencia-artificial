#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 24/59 - Lógica Difusa:Fuzzy CLIPS

# Importamos la biblioteca necesaria

import numpy as np
import matplotlib.pyplot as plt

# Función de membresía para la temperatura
def membresia_temperatura(x):
    # Definimos las funciones de membresía para "fría", "templada" y "caliente"
    fria = np.maximum(0, 1 - abs((x - 20) / 20))
    templada = np.maximum(0, np.minimum((x - 10) / 10, (40 - x) / 10))
    caliente = np.maximum(0, 1 - abs((x - 40) / 20))
    return fria, templada, caliente

# Función de membresía para la velocidad del ventilador
def membresia_ventilador(x):
    # Definimos las funciones de membresía para "baja", "media" y "alta"
    baja = np.maximum(0, 1 - x / 50)
    media = np.maximum(0, np.minimum(x / 50, (100 - x) / 50))
    alta = np.maximum(0, (x - 50) / 50)
    return baja, media, alta

# Definimos el rango de valores para la temperatura y la velocidad del ventilador
temperatura_range = np.arange(0, 41, 1)
ventilador_range = np.arange(0, 101, 1)

# Calculamos las funciones de membresía para cada valor en el rango de temperatura
fria, templada, caliente = membresia_temperatura(temperatura_range)
# Calculamos las funciones de membresía para cada valor en el rango de velocidad del ventilador
baja, media, alta = membresia_ventilador(ventilador_range)

# Visualizamos las funciones de membresía
plt.figure(figsize=(10, 6))

plt.subplot(2, 1, 1)
plt.plot(temperatura_range, fria, label='Fría')
plt.plot(temperatura_range, templada, label='Templada')
plt.plot(temperatura_range, caliente, label='Caliente')
plt.title('Funciones de Membresía para la Temperatura')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Grado de Membresía')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(ventilador_range, baja, label='Baja')
plt.plot(ventilador_range, media, label='Media')
plt.plot(ventilador_range, alta, label='Alta')
plt.title('Funciones de Membresía para la Velocidad del Ventilador')
plt.xlabel('Velocidad del Ventilador (%)')
plt.ylabel('Grado de Membresía')
plt.legend()

plt.tight_layout()
plt.show()
