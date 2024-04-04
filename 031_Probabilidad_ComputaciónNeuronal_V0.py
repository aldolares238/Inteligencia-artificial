#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 31/60 Computación Neuronal

import numpy as np
import matplotlib.pyplot as plt

#Definimos la función de activación sigmoide
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

#Definimos la función de coste (error cuadrático medio)
def cost_function(y_true, y_pred):
    return np.mean(np.square(y_true - y_pred))

#Declaramos los Datos de entrada (features)
X = np.array([[0], [1], [2], [3], [4], [5]])

#Declaramos los Datos de salida (target)
y = np.array([0, 0, 0, 1, 1, 1])

#Inicializamos los pesos y el sesgo (bias) de manera aleatoria
np.random.seed(0)  # Fijar la semilla para reproducibilidad
weights = np.random.randn(1)
bias = np.random.randn(1)

#Hiperparámetros
learning_rate = 0.1
epochs = 1000

#Entrenamiento del modelo
for epoch in range(epochs):
    #Forward pass
    z = np.dot(X, weights) + bias
    y_pred = sigmoid(z)
    
    #Cálculo del error
    loss = cost_function(y, y_pred)
    
    #Backward pass (propagación hacia atrás)
    gradient_w = np.dot(X.T, (y_pred - y)) / len(y)
    gradient_b = np.mean(y_pred - y)
    
    #Actualización de los pesos y el sesgo
    weights -= learning_rate * gradient_w
    bias -= learning_rate * gradient_b
    
    #MMostramos el progreso cada 100 epochs
    if epoch % 100 == 0:
        print(f'Epoch {epoch}: Loss {loss}')

#Predicción final
final_pred = sigmoid(np.dot(X, weights) + bias)
print("Predicciones finales:", final_pred)

#Graficamos los datos de entrada y las predicciones
plt.scatter(X, y, color='blue', label='Datos reales')
plt.plot(X, final_pred, color='red', label='Predicciones')
plt.xlabel('X')
plt.ylabel('y')
plt.title('Predicciones de la red neuronal')
plt.legend()
plt.show()
