#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 45/59 Árboles de Regresión: M5

# Importar las bibliotecas necesarias
import numpy as np
import matplotlib.pyplot as plt
from sklearn.tree import DecisionTreeRegressor
from sklearn.model_selection import train_test_split

# Generar datos de ejemplo
np.random.seed(0)
X = np.sort(5 * np.random.rand(80, 1), axis=0)
y = np.sin(X).ravel() + np.random.normal(0, 0.1, X.shape[0])

# Dividir los datos en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Crear el modelo de Árbol de Regresión M5
tree = DecisionTreeRegressor(max_depth=5)

# Entrenar el modelo
tree.fit(X_train, y_train)

# Predecir en el conjunto de prueba
y_pred = tree.predict(X_test)

# Graficar los resultados
plt.figure()
plt.scatter(X_test, y_test, s=20, edgecolor="black", c="darkorange", label="data")
plt.plot(X_test, y_pred, color="cornflowerblue", label="prediction", linewidth=2)
plt.xlabel("data")
plt.ylabel("target")
plt.title("Árbol de Regresión M5")
plt.legend()
plt.show()
