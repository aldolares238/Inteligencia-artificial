#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 49/59 Espacio de Versiones y AQ

import numpy as np
import matplotlib.pyplot as plt

# Creamos datos de ejemplo para clasificación binaria
X = np.array([[1, 2], [2, 3], [3, 1], [6, 5], [7, 7], [8, 6]])
y = np.array([0, 0, 0, 1, 1, 1])

# Inicializamos el espacio de versiones
V = []

# Iteramos sobre cada ejemplo de entrenamiento
for i in range(len(X)):
    x_i = X[i]
    y_i = y[i]

    # Si el ejemplo es negativo, agregamos su versión negativa al espacio de versiones
    if y_i == 0:
        V.append([-x_i[0], -x_i[1]])

    # Agregamos la versión positiva del ejemplo al espacio de versiones
    V.append(x_i)

# Convertimos el espacio de versiones en un arreglo numpy
V = np.array(V)

# Graficamos los datos y las versiones en el espacio de características
plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.coolwarm, label='Datos de entrenamiento')
plt.scatter(V[:, 0], V[:, 1], marker='x', color='red', label='Espacio de Versiones')

# Configuramos la leyenda y mostramos la gráfica
plt.legend()
plt.title('Espacio de Versiones y AQ para clasificación binaria')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')
plt.grid(True)
plt.show()
