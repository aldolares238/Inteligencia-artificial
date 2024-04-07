#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 46/60 Preprocesado: Filtros

import numpy as np
import matplotlib.pyplot as plt

#Generamos datos de ejemplo con ruido
np.random.seed(0)
x = np.linspace(0, 10, 100)
y = np.sin(x) + np.random.normal(0, 0.1, size=x.shape)

#Mostramos los datos de ejemplo antes de aplicar el filtro
plt.figure(figsize=(10, 5))
plt.scatter(x, y, label='Datos con ruido')
plt.title('Datos de ejemplo con ruido')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()

#Definimos una función para aplicar el filtro de media
def filtro_media(datos, ventana):
    """Aplica un filtro de media a los datos."""
    resultado = np.convolve(datos, np.ones(ventana) / ventana, mode='same')
    return resultado

#Aplicamos el filtro de media a los datos con una ventana de tamaño 5
y_suavizado = filtro_media(y, ventana=5)

#Mostramos los datos suavizados después de aplicar el filtro
plt.figure(figsize=(10, 5))
plt.scatter(x, y, label='Datos con ruido')
plt.plot(x, y_suavizado, color='red', label='Datos suavizados')
plt.title('Datos suavizados después de aplicar filtro de media')
plt.xlabel('X')
plt.ylabel('Y')
plt.legend()
plt.grid(True)
plt.show()
