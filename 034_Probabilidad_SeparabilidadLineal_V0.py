#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 34/60 Separabilidad Lineal

import numpy as np
import matplotlib.pyplot as plt

#Generamos datos de dos clases ficticias
np.random.seed(0)
class1 = np.random.randn(50, 2) + [2, 2]  #Clase 1 centrada en (2, 2)
class2 = np.random.randn(50, 2) + [-2, -2]  #Clase 2 centrada en (-2, -2)

#Visualizamos los datos generados
plt.scatter(class1[:, 0], class1[:, 1], color='blue', label='Clase 1')
plt.scatter(class2[:, 0], class2[:, 1], color='red', label='Clase 2')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Datos Generados')
plt.legend()
plt.grid(True)
plt.show()

#Concatenamos los datos de las dos clases
X = np.vstack((class1, class2))

#Asignamos etiquetas a las clases (0 para la clase 1, 1 para la clase 2)
y = np.hstack((np.zeros(50), np.ones(50)))

#Definimos la función de activación (sigmoid en este caso)
def sigmoid(z):
    return 1 / (1 + np.exp(-z))

#Inicializamos pesos aleatorios para las características y el sesgo
weights = np.random.randn(3)

#Agregamos una columna de unos para el término de sesgo (bias)
X_with_bias = np.column_stack([np.ones((X.shape[0], 1)), X])

#Calculamos el producto punto de los pesos y las características
z = np.dot(X_with_bias, weights)

#Aplicamos la función de activación para obtener las probabilidades
probabilities = sigmoid(z)

#Clasificamos las muestras basadas en las probabilidades
predictions = (probabilities >= 0.5).astype(int)

#Visualizamos los resultados
plt.scatter(X[:, 0], X[:, 1], c=predictions, cmap='coolwarm', edgecolors='k')
plt.xlabel('Característica 1')
plt.ylabel('Característica 2')
plt.title('Clasificación de las Muestras')
plt.grid(True)
plt.show()
