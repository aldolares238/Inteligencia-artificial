#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 4/60 Distribución de probabilidad

import numpy as np
import matplotlib.pyplot as plt

#Definimos los datos de entrada (valores posibles)
valores = [1, 2, 3, 4, 5, 6]

#Definimos las probabilidades asociadas a cada valor
probabilidades = [0.1, 0.2, 0.3, 0.2, 0.1, 0.1]

#Verificamos que las probabilidades sumen 1
if np.sum(probabilidades) != 1:
    raise ValueError("Las probabilidades deben sumar 1")

#Creamos un gráfico de barras para visualizar la distribución de probabilidades
plt.bar(valores, probabilidades, color='skyblue')
plt.xlabel('Valores')
plt.ylabel('Probabilidad')
plt.title('Distribución de Probabilidad')
plt.xticks(valores)
plt.yticks(np.arange(0, max(probabilidades)+0.1, 0.1))
plt.grid(True)

#Mostramos el gráfico
plt.show()
