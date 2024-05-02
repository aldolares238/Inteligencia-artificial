#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 51/59 Explicaciones e Información Relevante

import numpy as np
import matplotlib.pyplot as plt

# Creamos datos de ejemplo
X = np.array([[2, 3], [3, 4], [4, 5], [5, 6], [6, 7]])
y = np.array([0, 0, 1, 1, 1])

# Separamos los datos por clase
clase_0 = X[y == 0]
clase_1 = X[y == 1]

# Calculamos la media de cada clase
media_clase_0 = np.mean(clase_0, axis=0)
media_clase_1 = np.mean(clase_1, axis=0)

# Calculamos la distancia entre las medias de las clases
distancia_medias = np.linalg.norm(media_clase_0 - media_clase_1)

# Visualizamos los datos y las medias de cada clase
plt.scatter(clase_0[:, 0], clase_0[:, 1], color='blue', label='Clase 0')
plt.scatter(clase_1[:, 0], clase_1[:, 1], color='red', label='Clase 1')
plt.scatter(media_clase_0[0], media_clase_0[1], color='black', marker='x', s=100, label='Media Clase 0')
plt.scatter(media_clase_1[0], media_clase_1[1], color='green', marker='x', s=100, label='Media Clase 1')
plt.legend()
plt.title('Explicaciones e Información Relevante')
plt.xlabel('Feature 1')
plt.ylabel('Feature 2')

# Añadimos una línea que representa la distancia entre las medias de las clases
plt.plot([media_clase_0[0], media_clase_1[0]], [media_clase_0[1], media_clase_1[1]], linestyle='--', color='gray')

# Añadimos texto que muestra la distancia entre las medias
plt.text((media_clase_0[0] + media_clase_1[0]) / 2, (media_clase_0[1] + media_clase_1[1]) / 2,
         f'Distancia: {distancia_medias:.2f}', ha='center', va='center')

plt.grid(True)
plt.show()
