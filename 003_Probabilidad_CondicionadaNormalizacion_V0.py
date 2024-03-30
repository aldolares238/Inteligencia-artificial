#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 3/60 Probabilidad Condicionada y Normalización

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función para simular el lanzamiento de un dado
def lanzar_dado():
    return np.random.randint(1, 7)

#Número de lanzamientos
num_lanzamientos = 10000

#Lanzamos los dados
dado1 = np.array([lanzar_dado() for _ in range(num_lanzamientos)])
dado2 = np.array([lanzar_dado() for _ in range(num_lanzamientos)])

#Calculamos la probabilidad condicionada P(D2 > 7 | D1 > 3)
condicion = (dado1 > 3)
evento = (dado1 + dado2 > 7)
probabilidad_condicionada = np.sum(evento & condicion) / np.sum(condicion)

#Visualización de los resultados
plt.figure(figsize=(8, 6))

#Histograma de la suma de los dados
plt.hist(dado1 + dado2, bins=11, density=True, color='skyblue', alpha=0.7, label='Suma de dados')

#Línea vertical para resaltar el valor 7
plt.axvline(x=7, color='red', linestyle='--', linewidth=1, label='Suma deseada (7)')

#Configuración del gráfico
plt.title('Histograma de la suma de dos dados')
plt.xlabel('Suma de los dados')
plt.ylabel('Densidad de probabilidad')
plt.legend()
plt.grid(True)

# Mostrar la probabilidad condicionada
plt.text(9, 0.06, f'P(D2 > 7 | D1 > 3) = {probabilidad_condicionada:.2f}', fontsize=12, color='green')

# Mostrar el gráfico
plt.show()
