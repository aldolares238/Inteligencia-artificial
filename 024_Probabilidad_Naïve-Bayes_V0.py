#Nombre: Aldo Emiliano Chavez Lares
#Registro: 21310238
#Grupo: 6E1
#Practica: 24/60  Naïve-Bayes

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score

#Cargamos el conjunto de datos Iris
iris = datasets.load_iris()
X = iris.data
y = iris.target

#Dividimos el conjunto de datos en entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#Inicializamos el clasificador Naïve-Bayes
model = GaussianNB()

#Entrenamos el modelo
model.fit(X_train, y_train)

#Realizamos predicciones en el conjunto de prueba
y_pred = model.predict(X_test)

#Calculamos la precisión del modelo
accuracy = accuracy_score(y_test, y_pred)
print("Precisión del modelo Naïve-Bayes:", accuracy)

#Visualizamos los resultados utilizando un gráfico
plt.figure(figsize=(8, 6))

#Graficamos las clases verdaderas
for i in range(3):
    plt.scatter(X_test[y_test == i][:, 0], X_test[y_test == i][:, 1], label=f'Clase {i}', alpha=0.7)

#Graficamos las clases predichas
for i in range(3):
    plt.scatter(X_test[y_pred == i][:, 0], X_test[y_pred == i][:, 1], label=f'Predicho {i}', alpha=0.7, marker='x')

plt.title("Clasificación utilizando Naïve-Bayes")
plt.xlabel("Característica 1")
plt.ylabel("Característica 2")
plt.legend()
plt.show()
