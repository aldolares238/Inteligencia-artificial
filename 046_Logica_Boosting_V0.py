#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 46/59 Conjuntos de Hipótesis: Boosting

import numpy as np
import matplotlib.pyplot as plt

# Creamos datos de ejemplo
np.random.seed(0)
X = np.random.rand(100, 2) * 2 - 1  # 100 puntos en un cuadrado [-1,1]x[-1,1]
y = np.sign(X[:, 0]**2 + X[:, 1]**2 - 0.5)  # Clasificación basada en círculo

# Definimos la función de clasificación débil (hipótesis débil)
def weak_classifier(X, threshold=0):
    """
    Clasificador débil basado en umbral.
    """
    return np.where(X[:, 0] + X[:, 1] <= threshold, -1, 1)

# Inicializamos pesos para el conjunto de datos
weights = np.ones(len(X)) / len(X)

# Definimos el número de iteraciones
num_iterations = 5

# Lista para almacenar los clasificadores débiles
weak_classifiers = []

# Iteramos para construir los clasificadores débiles
for _ in range(num_iterations):
    # Entrenamos un clasificador débil
    h = weak_classifier(X)
    
    # Calculamos el error ponderado
    weighted_error = np.sum(weights * (h != y))
    
    # Calculamos el coeficiente de importancia del clasificador débil
    alpha = 0.5 * np.log((1 - weighted_error) / weighted_error)
    
    # Actualizamos los pesos
    weights *= np.exp(-alpha * y * h)
    weights /= np.sum(weights)
    
    # Añadimos el clasificador débil a la lista
    weak_classifiers.append((alpha, h))

# Clasificación final utilizando el conjunto de clasificadores débiles
def predict(X):
    """
    Realiza la clasificación final utilizando el conjunto de clasificadores débiles.
    """
    predictions = np.zeros(len(X))
    for alpha, h in weak_classifiers:
        predictions += alpha * h(X)
    return np.sign(predictions)

# Visualización de la clasificación final
def plot_final_classification():
    """
    Visualiza la clasificación final.
    """
    xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))
    Z = predict(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title('Clasificación final')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# Visualización de la clasificación en cada iteración
def plot_iteration(i):
    """
    Visualiza la clasificación en la iteración i.
    """
    alpha, h = weak_classifiers[i]
    xx, yy = np.meshgrid(np.linspace(-1.5, 1.5, 100), np.linspace(-1.5, 1.5, 100))
    Z = alpha * h(np.c_[xx.ravel(), yy.ravel()])
    Z = Z.reshape(xx.shape)
    plt.contourf(xx, yy, Z, alpha=0.3)
    plt.scatter(X[:, 0], X[:, 1], c=y, cmap=plt.cm.Paired)
    plt.xlim(-1.5, 1.5)
    plt.ylim(-1.5, 1.5)
    plt.title(f'Clasificación en la iteración {i+1}')
    plt.xlabel('X1')
    plt.ylabel('X2')
    plt.show()

# Visualización de la clasificación final
plot_final_classification()

# Visualización de la clasificación en cada iteración
for i in range(num_iterations):
    plot_iteration(i)
